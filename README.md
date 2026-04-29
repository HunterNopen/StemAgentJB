# StemAgentJB - Specialized Test Generation vs Mutation Score

> Research => generate => execute <=> feedback
> Loop for LLM-driven Python test generation against Internal & External Benchmarks. Built as the JetBrains AI Engineering internship test task


## Overview
Single-shot LLM prompting writes decent Python tests, BUT under-specifies edge-case coverage and produces unstable results across runs. This project implements 4-phase **Stem Agent** that researches each function before testing, iterates on its own output with structured feedback from `cosmic-ray` mutation testing and stops on a deterministic saturation/plateu rule.

The Stem Agent improves mutation kill-rate by a mean of **+11.7%** over single-shot prompting across 12 compared functions, with three functions exceeding **+20% gain** Total experiment cost: **~$0.13** in `gpt-4o-mini` API calls.

Full write-up: [REPORT.md](./REPORT.md)

## Highlights
- **Full Naive vs Stem Pipelines Benchmark:** Naive baseline (5 runs/fn) vs Stem agent (3 runs/fn, up to 3 iterations). With tweakable parameters for ablation tests
- **Hybrid benchmark:** 9 handwritten functions (built specifically to resist memorization-based generalization) + 6 textbook programs with published Pynguin baselines for external calibration.
- **0 Regressions Score:** Variance reduction up to 11x on unstable functions => bidirectional variance for exceptions

## Quick Start
### 1. Requirements
- Python 3.10+
- OpenAI API key

### 2. Setup
```bash
git clone https://github.com/HunterNopen/StemAgentJB
cd StemAgentJB
python -m venv .venv && source .venv/Scripts/activate
pip install -r requirements.txt
echo "OPENAI_API_KEY=sk-..." > .env
```

### 3. Run (Demo Mode by Default)
[static.py](./stem_agent/static.py) has var `IS_DEMO_MODE` When True => project will run both pipelines on `validate_date.py` with N=1, MAX_ITER=1
**ETA:** ~2-5 minutes for naive, ~5-10 minutes for stem. Verifies installation and creates artifacts in results/demos

```bash
python -m stem_agent.naive    # ~3 min; output >>> results/runs/demos/naive_baseline.csv
python -m stem_agent.stem     # ~8 min;  output >>> results/runs/demos/stem_baseline.csv
                              # specialization_record.yaml per function
```

### 4. Full benchmark
Set `IS_DEMO_MODE = False` in [static.py](./stem_agent/static.py)

| Pipeline | Functions | Runs/fn | Wall-clock | Cost |
|---|---|---|---|---|
| Naive | 14 | 5 | ~75 min | ~$0.05 |
| Stem agent | 11 | 3 | ~5 hours | ~$0.08 |

## Repo Structure

```
stem_agent/
    naive.py        single-shot LLM baseline
    stem.py         multi-phase agent
    static.py       constants, prompts, demo-mode flag
benchmark/
    internal/           9 handwritten function benchmarks (source.py, spec.md, meta.yaml)
    external/           6 textbook programs from aurimrv/python_experiments
results/runs/       timestamp folders
docs/REPORT.md      => this document
```

## Configuration
```env
OPENAI_API_KEY="your_api_key_here"
```