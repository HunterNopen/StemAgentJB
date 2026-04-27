from dataclasses import dataclass

@dataclass
class IterationRecord:
    iteration: int
    tests_generated: int
    tests_kept: int
    mutation_score: float
    mutants_total: int
    mutants_killed: int
    tokens_in: int
    tokens_out: int