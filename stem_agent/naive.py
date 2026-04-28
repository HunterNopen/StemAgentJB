from __future__ import annotations
import os
import csv
import ast
import shutil
import subprocess
import time
from dataclasses import asdict
from pathlib import Path
from typing import Optional

import yaml
from openai import OpenAI

from .static import NAIVE_SYSTEM, NAIVE_USER_TEMPLATE, PYTEST_RESULT_RE, IS_DEMO_MODE, DEMO_FUNCTION, DEMO_FUNCTION_TIER
from .RunResult import RunResult

from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

def run_cosmic_ray(workdir: Path, source_filename: str) -> tuple[int, int, float]:
    """
    Returns (mutants_total, mutants_killed, mutation_score_percent)
    Raises RuntimeError on baseline failure or exec failure

    Workdir MUST contain:
    - source.py
    - tests/
    Creates: cr.toml, session.sqlite
    """

    cr_toml = workdir / "cr.toml"
    session = workdir / "session.sqlite"
    if session.exists():
        session.unlink()

    cr_toml.write_text(f"""[cosmic-ray]
module-path = "{source_filename}"
timeout = 60.0
excluded-modules = []
test-command = "pytest -x --tb=no tests/"

[cosmic-ray.distributor]
name = "local"
""")

    bl = subprocess.run(
        ["cosmic-ray", "--verbosity=INFO", "baseline", "cr.toml"],
        cwd=workdir, capture_output=True, text=True, timeout=120,
    )
    if "Baseline passed" not in bl.stdout + bl.stderr:
        raise RuntimeError(f"baseline failed: {bl.stdout}\n{bl.stderr}")

    subprocess.run(["cosmic-ray", "init", "cr.toml", "session.sqlite"],
                   cwd=workdir, check=True, timeout=60)
    subprocess.run(["cosmic-ray", "exec", "cr.toml", "session.sqlite"],
                   cwd=workdir, check=True, timeout=1800)

    rate = subprocess.run(["cr-rate", "session.sqlite"],
                          cwd=workdir, capture_output=True, text=True, check=True)

    rep = subprocess.run(["cr-report", "session.sqlite"],
                         cwd=workdir, capture_output=True, text=True, check=True)
    total = rep.stdout.count("[job-id]")
    killed = rep.stdout.count("test outcome: killed")

    score = 100.0 * killed / total if total > 0 else 0.0
    return total, killed, score


def generate_tests_naive(client: OpenAI, model: str, function_name: str, spec: str, source: str) -> tuple[str, int, int]:
    """
    Returns (test_code, tokens_in, tokens_out)
    Strips forcefully unintended markdown artifacts
    """
    response = client.chat.completions.create(
        model=model,
        temperature=0,
        messages=[
            {"role": "system", "content": NAIVE_SYSTEM},
            {"role": "user", "content": NAIVE_USER_TEMPLATE.format(function_name=function_name, spec=spec, source=source)},
        ],
    )
    code = response.choices[0].message.content

    if code.startswith("```"):
        code = code.split("```")[1]
        if code.startswith("python"):
            code = code[len("python"):]
        code = code.strip()

    return code, response.usage.prompt_tokens, response.usage.completion_tokens


def run_one_function(
    client: OpenAI, model: str, fn_dir: Path, 
    run_index: int, workdir_root: Path) -> RunResult:
    """
    Run Cosmic-ray mutation testing per case
    """

    function_name = fn_dir.name
    axis = "unknown"
    complexity = "unknown"
    tokens_in = 0
    tokens_out = 0
    timer_start: Optional[float] = None

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

        shutil.copy2(source_path, workdir / "source.py")
        tests_dir = workdir / "tests"
        tests_dir.mkdir(parents=True, exist_ok=True)

        test_code, tokens_in, tokens_out = generate_tests_naive(
            client=client,
            model=model,
            function_name=function_name,
            spec=spec,
            source=source,
        )
        (tests_dir / "test_naive.py").write_text(test_code, encoding="utf-8")
        (tests_dir / "conftest.py").write_text(
            "import sys\n"
            "from pathlib import Path\n"
            "sys.path.insert(0, str(Path(__file__).parent.parent))\n",
            encoding="utf-8",
        )

        n_generated, n_kept, _ = filter_passing_tests(workdir, tests_dir / "test_naive.py")

        timer_start = time.perf_counter()
        mutants_total, mutants_killed, mutation_score = run_cosmic_ray(
            workdir=workdir,
            source_filename="source.py",
        )
        seconds_elapsed = time.perf_counter() - timer_start

        return RunResult(
            function_name=function_name,
            axis=axis,
            complexity=complexity,
            run_index=run_index,
            model=model,
            mutants_total=mutants_total,
            mutants_killed=mutants_killed,
            mutation_score=mutation_score,
            tokens_in=tokens_in,
            tokens_out=tokens_out,
            seconds_elapsed=seconds_elapsed,
            tests_generated=n_generated,
            tests_kept=n_kept,
            error=None,
        )
    
    except Exception as e:
        seconds_elapsed = 0.0
        if timer_start is not None:
            seconds_elapsed = time.perf_counter() - timer_start

        return RunResult(
            function_name=function_name,
            axis=axis,
            complexity=complexity,
            run_index=run_index,
            model=model,
            mutants_total=0,
            mutants_killed=0,
            mutation_score=0.0,
            tokens_in=tokens_in,
            tokens_out=tokens_out,
            seconds_elapsed=seconds_elapsed,
            error=str(e),
        )


def filter_passing_tests(workdir: Path, test_file: Path) -> tuple[int, int, list[str]]:
    """
    Run all tests in test_file against unmutated source. Drop Failing
    """
    
    result = subprocess.run(
        ["pytest", "--tb=no", "-v", "--no-header", "tests/"],
        cwd=workdir, capture_output=True, text=True, timeout=120,
    )

    failing: set[str] = set()
    total = 0
    for match in PYTEST_RESULT_RE.finditer(result.stdout):
        test_name = match.group(1)
        outcome = match.group(2)
        total += 1
        if outcome in ("FAILED", "ERROR"):
            leaf = test_name.split("::")[-1]
            failing.add(leaf)

    if total == 0:
        raise RuntimeError(
            f"No tests collected in {test_file}.\n"
            f"pytest stdout:\n{result.stdout[:1000]}\n"
            f"pytest stderr:\n{result.stderr[:500]}"
        )

    source_code = test_file.read_text(encoding="utf-8")
    tree = ast.parse(source_code)

    def keep(node: ast.AST) -> bool:
        
        if isinstance(node, ast.FunctionDef) and node.name.startswith("test_"):
            return node.name not in failing
        
        if isinstance(node, ast.ClassDef) and node.name.startswith("Test"):
            node.body = [
                m for m in node.body
                if not (isinstance(m, ast.FunctionDef)
                        and m.name.startswith("test_")
                        and m.name in failing)
            ]
            
            if not any(isinstance(m, ast.FunctionDef) and m.name.startswith("test_")
                       for m in node.body):
                return False
        return True

    tree.body = [n for n in tree.body if keep(n)]

    
    kept = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name.startswith("test_"):
            kept += 1

    if kept == 0:
        raise RuntimeError(f"All {total} tests failed; nothing to mutate-test against.")

    test_file.write_text(ast.unparse(tree), encoding="utf-8")
    return total, kept, sorted(failing)

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key: raise RuntimeError("OPENAI_API_KEY is not set")
    model = "gpt-4o-mini"
    n_runs_per_function = 5
    client = OpenAI(api_key=api_key)

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    run_dir = Path("results") / "runs" / timestamp
    workdir_root = run_dir / "workdir"
    run_dir.mkdir(parents=True, exist_ok=True)
    workdir_root.mkdir(parents=True, exist_ok=True)

    csv_path = run_dir / "naive_baseline.csv"
    benchmark_root = Path("benchmark")
    function_dirs: list[Path] = []

    if IS_DEMO_MODE:
        demo_path = benchmark_root / DEMO_FUNCTION_TIER / DEMO_FUNCTION
        if not demo_path.is_dir():
            raise RuntimeError(f"Demo function not found: {demo_path}")
        function_dirs = [demo_path]
        n_runs_per_function = 1
        print(f"[DEMO MODE] Running {DEMO_FUNCTION} (1 run, naive baseline)")
    else:
        n_runs_per_function = 5
        for group in ["internal", "external"]:
            group_dir = benchmark_root / group
            if not group_dir.is_dir():
                continue
            for fn_dir in sorted(group_dir.iterdir()):
                if fn_dir.is_dir():
                    function_dirs.append(fn_dir)
        print(f"[FULL MODE] Running {len(function_dirs)} functions × {n_runs_per_function} runs")

    fieldnames = list(RunResult.__dataclass_fields__.keys())
    all_results: list[RunResult] = []

    # function_dirs = function_dirs[3:4]
    # n_runs_per_function = 2

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for fn_dir in function_dirs:
            for run_index in range(n_runs_per_function):
                result = run_one_function(
                    client=client,
                    model=model,
                    fn_dir=fn_dir,
                    run_index=run_index,
                    workdir_root=workdir_root,
                )
                all_results.append(result)
                writer.writerow(asdict(result))
                f.flush()

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
    for r in all_results:
        by_function.setdefault(r.function_name, []).append(r.mutation_score)

    print("\nPer-function summary (mutation score):")
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