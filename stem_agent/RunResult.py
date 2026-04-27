from dataclasses import dataclass
from typing import Optional

@dataclass
class RunResult:
    function_name: str
    axis: str
    complexity: str
    run_index: int
    model: str
    mutants_total: int
    mutants_killed: int
    mutation_score: float
    tokens_in: int
    tokens_out: int
    seconds_elapsed: float
    tests_generated: int = 0
    tests_kept: int = 0
    error: Optional[str] = None