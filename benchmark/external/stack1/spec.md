# stack1

## Signature
Primary APIs:
- `Stack.push(item) -> None`
- `Stack.pop() -> Any`
- `Stack.peek() -> Any`
- `len(Stack)` via `__len__`
- `check_parenthesis(string: str) -> bool`
- `postfix_eval(string: str) -> int | float`

## Contract
Implements a linked-list LIFO stack and two stack-based utilities.

- `push` adds top item.
- `pop` removes and returns top, raising `ValueError` if empty.
- `peek` returns top without removal, raising `ValueError` if empty.
- `check_parenthesis` validates balanced bracket pairs.
- `postfix_eval` evaluates space-separated postfix expressions.

## Rules
- Bracket pairs supported: `{}`, `[]`, `()`.
- Parenthesis check returns `False` on mismatch, premature closing, or leftover opens.
- Postfix evaluator supports `+ - * / % ^` with integer token parsing.
- Invalid tokens or insufficient operands raise `ValueError`.
- Extra operands (stack size > 1 at end) raise `ValueError`.

## Edge cases
- Empty stack pop/peek -> raises `ValueError`
- `check_parenthesis("")` -> `True`
- `check_parenthesis("([)]")` -> `False`
- `postfix_eval("2 3 +")` -> `5`
- `postfix_eval("2 +")` -> raises `ValueError`
- `postfix_eval("2 3")` -> raises `ValueError`
