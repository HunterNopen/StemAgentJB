# parse_user_id_from_string

## Signature
`parse_user_id_from_string(input_str: str) -> int | None`

## Contract
Extracts a user ID from several accepted string formats.

- Raises `ValueError` if input is `None`.
- Raises `TypeError` if input is not a string.
- Returns `None` when no digits/ID can be extracted.

## Rules
- Empty string returns `None`.
- Pattern precedence:
  - `USER:<digits>` -> parse digits after `USER:`
  - `ID=<digits>` -> parse digits after `ID=`
  - if string contains `_`, parse final segment when fully digits
  - if whole string is digits, parse as integer
  - otherwise fallback to concatenating all digits in the string
- If fallback digit collection yields no digits, return `None`.

## Edge cases
- `"USER:12345"` -> `12345`
- `"USER:abc"` -> `None`
- `"ID=67890"` -> `67890`
- `"account_42"` -> `42`
- `"987"` -> `987`
- `"abc1x2y3"` -> `123`
- `"no_digits"` -> `None`
- `None` -> raises `ValueError`
- non-string input -> raises `TypeError`