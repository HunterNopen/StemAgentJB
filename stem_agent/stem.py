from __future__ import annotations

import os
import csv
import json
import shutil
import subprocess
import time
from dataclasses import asdict
from pathlib import Path
from typing import Optional
from collections import Counter

import yaml
from openai import OpenAI

from .naive import run_cosmic_ray, filter_passing_tests
from .StemRunResult import StemRunResult
from .IterationRecord import IterationRecord
from .static import (MAX_ITER, SATURATION_THRESHOLD, PLATEAU_THRESHOLD, 
                    RESEARCH_SYSTEM, GENERATE_SYSTEM,
                    RESEARCH_USER_TEMPLATE, GENERATE_USER_TEMPLATE, FEEDBACK_BLOCK_TEMPLATE)

from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

def _strip_markdown_fences(text: str) -> str:
    """Clean the invalid LLM output forcefully - prevent hallucination risk"""

    text = text.strip()
    if text.startswith("```"):
        text = text.split("```", 2)[1] if text.count("```") >= 2 else text
        for tag in ("python", "json"):
          if text.startswith(tag):
              text = text[len(tag):]
              break
        text = text.strip()
        if text.endswith("```"):
            text = text[:-3].strip()

    return text


def _validate_research_dict(research_dict: dict) -> None:
    """Check JSON for valid keys and columns"""

    required_keys = {"category", "rationale", "test_patterns", "concerns"}
    missing = required_keys.difference(research_dict)
    if missing:
        raise ValueError(f"Research response missing keys: {sorted(missing)}")
    
    if not isinstance(research_dict["test_patterns"], list):
        raise ValueError("Research response key 'test_patterns' must be a list")
    
    if not isinstance(research_dict["concerns"], list):
        raise ValueError("Research response key 'concerns' must be a list")

def research(client: OpenAI, model: str, 
             function_name: str, spec: str, source: str) -> tuple[dict, int, int]:
    """
    RESEARCH Phase:
    - Craft SYSTEM prompt
    - Craft RESEARCH_USER_TEMPLATE with function_name, spec, source
    - Call LLM
    - Strip markdown fences from response
    - Parse JSON, validate keys
    """

    response = client.chat.completions.create(
        model=model,
        temperature=0,
        messages=[
            {"role": "system", "content": RESEARCH_SYSTEM},
            {"role": "user", "content": RESEARCH_USER_TEMPLATE.format(
                function_name=function_name,
                spec=spec,
                source=source,
            )},
        ],
    )

    content = response.choices[0].message.content or ""
    content = _strip_markdown_fences(content)
    research_dict = json.loads(content)
    if not isinstance(research_dict, dict):
        raise ValueError("Research response must be a JSON object")
    _validate_research_dict(research_dict)
    return research_dict, response.usage.prompt_tokens, response.usage.completion_tokens


def generate_tests(
    client: OpenAI, model: str, function_name: str, spec: str, source: str,
    research_dict: dict, feedback: Optional[dict] = None,
) -> tuple[str, int, int]:
    """
    GENERATE Phase:
    - Craft SYSTEM prompt
    - Craft GENERATE_USER_TEMPLATE with function_name, spec, source, research_dict and feedback
    - Call LLM
    - Strip markdown fences from response
    """

    patterns_list = ", ".join(
        pattern.get("name", "") for pattern in research_dict.get("test_patterns", [])
        if isinstance(pattern, dict)
    )
    concerns = "; ".join(str(concern) for concern in research_dict.get("concerns", []))

    if feedback is None:
        feedback_block = ""
    else:
        feedback_block = FEEDBACK_BLOCK_TEMPLATE.format(
            previous_score=feedback["previous_score"],
            previous_test_code=feedback["previous_test_code"],
            surviving_summary=feedback["surviving_summary"],
            dropped_summary=feedback["dropped_summary"],
        )

    user_msg = GENERATE_USER_TEMPLATE.format(
        function_name=function_name,
        spec=spec,
        source=source,
        category=research_dict["category"],
        rationale=research_dict["rationale"],
        patterns_list=patterns_list,
        concerns=concerns,
        feedback_block=feedback_block,
    )

    response = client.chat.completions.create(
        model=model,
        temperature=0,
        messages=[
            {"role": "system", "content": GENERATE_SYSTEM},
            {"role": "user", "content": user_msg},
        ],
    )

    code = _strip_markdown_fences(response.choices[0].message.content or "")
    return code, response.usage.prompt_tokens, response.usage.completion_tokens


def summarize_surviving_mutants(workdir: Path) -> str:
    """
    Given the workdir of the current iteration, parse the Cosmic Ray session data
    """

    session = workdir / "session.sqlite"
    if not session.exists():
        return "(no session data)"

    try:
        result = subprocess.run(
            ["cr-report", str(session)],
            capture_output=True,
            text=True,
            timeout=60,
        )
    except Exception as e:
        return f"(error: {e})"
    
    survivor_counts: Counter[str] = Counter()
    blocks = result.stdout.split("[job-id]")[1:]

    for block in blocks:
        if "test outcome: survived" not in block:
            continue

        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if not lines:
            continue

        mutator_line = lines[1] if len(lines) >= 2 else ""
        parts = mutator_line.split("core/")
        if len(parts) < 2:
            continue

        mutator = parts[1].split()[0]
        survivor_counts[mutator] += 1

    if not survivor_counts:
        return "(no surviving mutants)"

    total = sum(survivor_counts.values())
    summary_lines = [f"- {mutator}: {count} surviving" for mutator, count in survivor_counts.most_common(10)]
    return f"Total surviving mutants: {total}\nTop categories:\n" + "\n".join(summary_lines)


def summarize_dropped_tests(test_file: Path, dropped_names: list[str]) -> str:
    """Given the test file and list of dropped test names, produce a summary string."""

    if not dropped_names:
        return "(no tests dropped)"
    
    return f"{len(dropped_names)} tests dropped: {', '.join(dropped_names)}"

def should_stop(history: list[IterationRecord]) -> tuple[bool, str]:
    """Return whether the refinement loop should stop and why"""

    if not history:
        return False, ""
        
    last = history[-1]
    if last.mutation_score >= SATURATION_THRESHOLD:
        return True, "saturation"
    
    if len(history) >= 2:
        prev = history[-2]
        delta = last.mutation_score - prev.mutation_score
        if 0 <= delta < PLATEAU_THRESHOLD:
            return True, "plateau"
        
    if len(history) >= MAX_ITER:
        return True, "iteration_cap"
    
    return False, ""

def run_one_function_stem(
    client: OpenAI, model: str, fn_dir: Path,
    run_index: int, workdir_root: Path,
) -> tuple[StemRunResult, list[IterationRecord], dict]:
    """
    Run the STEM agent on one function, returning the final result, iteration history and research dict
    """

    function_name = fn_dir.name
    axis = "unknown"
    complexity = "unknown"
    history: list[IterationRecord] = []
    research_dict: dict = {}
    stopped_because = "error"
    total_tokens_in = 0
    total_tokens_out = 0
    timer_start: Optional[float] = None
    total_seconds = 0.0

    try:
        source_path = fn_dir / "source.py"
        spec_path = fn_dir / "spec.md"
        meta_path = fn_dir / "meta.yaml"

        source = source_path.read_text(encoding="utf-8")
        spec = spec_path.read_text(encoding="utf-8")
        meta = yaml.safe_load(meta_path.read_text(encoding="utf-8")) or {}

        function_name = str(meta.get("name", fn_dir.name))
        axis = str(meta.get("axis", "unknown"))
        complexity = str(meta.get("complexity", "unknown"))

        run_tag = f"{function_name}_run{run_index}_{time.time_ns()}"
        workdir = workdir_root / run_tag
        workdir.mkdir(parents=True, exist_ok=False)

        research_dict, r_in, r_out = research(
            client=client,
            model=model,
            function_name=function_name,
            spec=spec,
            source=source,
        )
        total_tokens_in += r_in
        total_tokens_out += r_out

        feedback: Optional[dict] = None
        timer_start = time.perf_counter()

        for iteration in range(MAX_ITER):
            iter_dir = workdir / f"iter_{iteration}"
            tests_dir = iter_dir / "tests"
            tests_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_path, iter_dir / "source.py")

            test_code, g_in, g_out = generate_tests(
                client=client,
                model=model,
                function_name=function_name,
                spec=spec,
                source=source,
                research_dict=research_dict,
                feedback=feedback,
            )
            total_tokens_in += g_in
            total_tokens_out += g_out

            test_file = tests_dir / "test_stem.py"
            test_file.write_text(test_code, encoding="utf-8")
            (tests_dir / "conftest.py").write_text(
                "import sys\n"
                "from pathlib import Path\n"
                "sys.path.insert(0, str(Path(__file__).parent.parent))\n",
                encoding="utf-8",
            )

            filter_result = filter_passing_tests(iter_dir, test_file)
            n_generated, n_kept, dropped_names = filter_result

            mutants_total, mutants_killed, mutation_score = run_cosmic_ray(
                workdir=iter_dir,
                source_filename="source.py",
            )

            history.append(
                IterationRecord(
                    iteration=iteration,
                    tests_generated=n_generated,
                    tests_kept=n_kept,
                    mutation_score=mutation_score,
                    mutants_total=mutants_total,
                    mutants_killed=mutants_killed,
                    tokens_in=g_in,
                    tokens_out=g_out,
                )
            )

            should_end, reason = should_stop(history)
            if should_end:
                stopped_because = reason
                break

            previous_test_code = test_file.read_text(encoding="utf-8")

            feedback = {
                "previous_score": mutation_score,
                "previous_test_code": previous_test_code,
                "surviving_summary": summarize_surviving_mutants(iter_dir),
                "dropped_summary": summarize_dropped_tests(test_file, dropped_names),
            }

        if timer_start is not None:
            total_seconds = time.perf_counter() - timer_start

        if history:
            final = history[-1]
            result = StemRunResult(
                function_name=function_name,
                axis=axis,
                complexity=complexity,
                run_index=run_index,
                model=model,
                n_iterations=len(history),
                stopped_because=stopped_because,
                final_mutation_score=final.mutation_score,
                final_mutants_total=final.mutants_total,
                final_mutants_killed=final.mutants_killed,
                final_tests_generated=final.tests_generated,
                final_tests_kept=final.tests_kept,
                research_category=str(research_dict.get("category", "unknown")),
                total_tokens_in=total_tokens_in,
                total_tokens_out=total_tokens_out,
                total_seconds=total_seconds,
                error=None,
            )
        else:
            result = StemRunResult(
                function_name=function_name,
                axis=axis,
                complexity=complexity,
                run_index=run_index,
                model=model,
                n_iterations=0,
                stopped_because="error",
                final_mutation_score=0.0,
                final_mutants_total=0,
                final_mutants_killed=0,
                final_tests_generated=0,
                final_tests_kept=0,
                research_category=str(research_dict.get("category", "unknown")),
                total_tokens_in=total_tokens_in,
                total_tokens_out=total_tokens_out,
                total_seconds=total_seconds,
                error="No successful iteration recorded",
            )

        specialization_record = {
            "function_name": function_name,
            "run_index": run_index,
            "research": research_dict,
            "iterations": [asdict(item) for item in history],
            "result": asdict(result),
        }
        (workdir / "specialization_record.yaml").write_text(
            yaml.safe_dump(specialization_record, sort_keys=False),
            encoding="utf-8",
        )

        return result, history, research_dict

    except Exception as e:
        if timer_start is not None:
            total_seconds = time.perf_counter() - timer_start

        result = StemRunResult(
            function_name=function_name,
            axis=axis,
            complexity=complexity,
            run_index=run_index,
            model=model,
            n_iterations=len(history),
            stopped_because="error",
            final_mutation_score=0.0,
            final_mutants_total=0,
            final_mutants_killed=0,
            final_tests_generated=history[-1].tests_generated if history else 0,
            final_tests_kept=history[-1].tests_kept if history else 0,
            research_category=str(research_dict.get("category", "unknown")),
            total_tokens_in=total_tokens_in,
            total_tokens_out=total_tokens_out,
            total_seconds=total_seconds,
            error=str(e),
        )
        return result, history, research_dict


def main():
    """
    Main orchestration function:
    - Define model and parameters
    - Prepare directories and CSV output
    - Discover function directories in benchmark
    - Loop over functions and runs
    """
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")

    model = "gpt-4o-mini"
    n_runs_per_function = 3
    client = OpenAI(api_key=api_key)

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    run_dir = Path("results") / "runs" / timestamp
    workdir_root = run_dir / "workdir"
    records_dir = run_dir / "records"
    run_dir.mkdir(parents=True, exist_ok=True)
    workdir_root.mkdir(parents=True, exist_ok=True)
    records_dir.mkdir(parents=True, exist_ok=True)

    csv_path = run_dir / "stem_baseline.csv"
    benchmark_root = Path("benchmark")
    function_dirs: list[Path] = []

    SKIP_FN = {"apply_discount", "queue1", "can_access_resource", "stack1"}

    for group in ["internal", "external"]:
        group_dir = benchmark_root / group
        if not group_dir.is_dir():
            continue
        for fn_dir in sorted(group_dir.iterdir()):
            if fn_dir.is_dir() and fn_dir.name not in SKIP_FN:
                function_dirs.append(fn_dir)

    fieldnames = list(StemRunResult.__dataclass_fields__.keys())
    all_results: list[StemRunResult] = []

    # function_dirs = [d for d in function_dirs if d.name == "linkedList1"]
    # n_runs_per_function = 1

    print(f"Running {len(function_dirs)} functions, {n_runs_per_function} runs each = {len(function_dirs) * n_runs_per_function} total runs")
    for fn_dir in function_dirs:
        print(f"  - {fn_dir.name}")

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for fn_dir in function_dirs:
            for run_index in range(n_runs_per_function):
                result, history, research_dict = run_one_function_stem(
                    client=client,
                    model=model,
                    fn_dir=fn_dir,
                    run_index=run_index,
                    workdir_root=workdir_root,
                )
                all_results.append(result)
                writer.writerow(asdict(result))
                f.flush()

                record_payload = {
                    "function_dir": str(fn_dir),
                    "result": asdict(result),
                    "research": research_dict,
                    "iterations": [asdict(item) for item in history],
                }
                record_path = records_dir / f"{result.function_name}_run{run_index}.yaml"
                record_path.write_text(
                    yaml.safe_dump(record_payload, sort_keys=False),
                    encoding="utf-8",
                )

    manifest = {
        "timestamp": timestamp,
        "model": model,
        "n_runs_per_function": n_runs_per_function,
    }
    (run_dir / "manifest.yaml").write_text(
        yaml.safe_dump(manifest, sort_keys=False),
        encoding="utf-8",
    )

    by_function: dict[str, list[float]] = {}
    for result in all_results:
        by_function.setdefault(result.function_name, []).append(result.final_mutation_score)

    print("\nPer-function summary (final mutation score):")
    for fn_name in sorted(by_function):
        vals = by_function[fn_name]
        mean = sum(vals) / len(vals)
        std = 0.0
        if len(vals) > 1:
            variance = sum((v - mean) ** 2 for v in vals) / (len(vals) - 1)
            std = variance ** 0.5
        print(f"{fn_name}: mean={mean:.2f}, std={std:.2f}")


if __name__ == "__main__":
    main()