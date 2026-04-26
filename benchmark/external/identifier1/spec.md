# identifier1

## Signature
Primary API is class-based:
- `Identifier.valid_s(ch: str) -> bool`
- `Identifier.valid_f(ch: str) -> bool`
- `Identifier.validateIdentifier(s: str) -> bool`

## Contract
Validates short identifiers using a custom character policy.

- First character must be alphabetic (`A-Z` or `a-z`).
- Remaining characters may be alphanumeric (`A-Z`, `a-z`, `0-9`).
- Length must be between 1 and 6 inclusive.

## Rules
- Empty string is invalid.
- If the first character is invalid, identifier is invalid.
- Characters after index 0 are validated with `valid_f`.
- Any invalid trailing character makes result `False`.

## Edge cases
- `"a"` -> `True`
- `"a1b2"` -> `True`
- `"1abc"` -> `False` (invalid first char)
- `"abc_def"` -> `False` (underscore not allowed)
- `"abcdefg"` -> `False` (length > 6)
- `""` -> `False`
