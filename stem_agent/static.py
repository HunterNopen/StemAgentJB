import re

##################################
# CONSTS                         #
##################################

MAX_ITER = 3
SATURATION_THRESHOLD = 95.0
PLATEAU_THRESHOLD = 2.0

##################################
# REGEX                          #
##################################

PYTEST_RESULT_RE = re.compile(
    r"(?:tests[/\\])?test_[\w/\\]+\.py::([\w:]+(?:::[\w]+)?)\s+(PASSED|FAILED|ERROR)"
)

##################################
# PROMPTS                        #
##################################

NAIVE_SYSTEM = (
    "You are a Python testing expert. Given a function spec and source, "
    "write a comprehensive pytest test suite that thoroughly validates the "
    "function's behavior. Output ONLY valid Python code — no markdown fences, "
    "no explanations. The output must be a complete pytest file ready to save and run."
)

NAIVE_USER_TEMPLATE = """Specification:
{spec}

Source:
```python
{source}
```

The function under test is `{function_name}`. In your test file, import it with:
    from source import {function_name}

Generate the pytest test file now."""

RESEARCH_SYSTEM = (
    "You are a senior test engineer analyzing a Python function. Your job is to "
    "categorize what KIND of function it is and propose which test patterns are "
    "most relevant for thoroughly validating it. Be especially careful to detect "
    "wrapper, delegating, adapter, and validation-forwarding functions where most "
    "behavior is inherited from a helper or dependency rather than computed locally.\n\n"
    "Output strict JSON with this schema (no markdown fences, no commentary):\n"
    "{\n"
    '  "category": "<short label, e.g. \'input validator\', \'state machine\', \'wrapper\', \'parser\'>",\n'
    '  "rationale": "<1-2 sentences on what makes this function distinct>",\n'
    '  "test_patterns": [\n'
    '    {"name": "<pattern>", "why_relevant": "<short reason>"}\n'
    "  ],\n"
    '  "concerns": ["<potential blind spots that naive testing might miss>"]\n'
    "}"
)

RESEARCH_USER_TEMPLATE = """Specification:
{spec}

Source:
```python
{source}
```

The function under test is `{function_name}`. Analyze and respond with JSON only."""


GENERATE_SYSTEM = (
    "You are a Python testing expert. Given a function spec, source, prior research, "
    "and (optionally) feedback from a previous attempt, write a comprehensive pytest "
    "suite that maximally exercises the function's behavior — including edge cases, "
    "exception paths, and the specific blind spots noted in research and feedback.\n\n"
    "Output ONLY valid Python code — no markdown fences, no explanations. The output "
    "must be a complete pytest file ready to save and run."
)

GENERATE_USER_TEMPLATE = """Specification:
{spec}

Source:
```python
{source}
```

Prior research on this function:
- Category: {category}
- Why: {rationale}
- Test patterns to apply: {patterns_list}
- Known blind spots: {concerns}

{feedback_block}

The source file is `source.py`. Use `from source import <whatever you need>` 
to access the functions or classes defined in it. Read the source carefully 
to know what's available.

The function under test is `{function_name}`. In your test file, import it with:
    from source import {function_name}

The source file may also contain helper functions (validators, parsers, etc.) 
that {function_name} calls internally. These will be available in the same 
mutated source during testing. Do NOT mock them — test the function as it 
actually behaves with its real dependencies.

Generate the pytest test file now. Aim for thorough coverage of the patterns above."""


FEEDBACK_BLOCK_TEMPLATE = """Previous attempt scored {previous_score:.1f}% mutation kill rate.

Below is your previous test file. KEEP all the tests that are present in it 
exactly as written. ADD new tests that target the surviving mutants listed below.
Do not delete or rewrite working tests — only ADD.

Previous test file:
```python
{previous_test_code}
```

Surviving mutants (where your previous tests did NOT detect the change):
{surviving_summary}

Tests that were dropped because they failed the unmutated source:
{dropped_summary}

Write the COMPLETE test file: all the previous tests above, PLUS new tests 
targeting the surviving mutants. Do not omit any of the previous tests."""