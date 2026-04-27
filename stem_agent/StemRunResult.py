from dataclasses import dataclass
from typing import Optional

@dataclass
class StemRunResult:
    function_name: str
    axis: str
    complexity: str
    run_index: int
    model: str
    n_iterations: int
    stopped_because: str # "iteration_cap" | "saturation" | "plateau" | "error"
    final_mutation_score: float
    final_mutants_total: int
    final_mutants_killed: int
    final_tests_generated: int
    final_tests_kept: int
    research_category: str
    total_tokens_in: int
    total_tokens_out: int
    total_seconds: float
    error: Optional[str] = None