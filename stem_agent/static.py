import re

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

PYTEST_RESULT_RE = re.compile(
    r"(?:tests[/\\])?test_[\w/\\]+\.py::([\w:]+(?:::[\w]+)?)\s+(PASSED|FAILED|ERROR)"
)