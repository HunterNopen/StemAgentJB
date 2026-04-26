# is_future_date

## Dependencies
This function imports `validate_date` from the same module. Tests should
import only `is_future_date` from `source` — do not assume access to
`validate_date` directly in tests.

## Signature
`is_future_date(date_str: str, current_date_str: str) -> bool`

## Contract
Returns `True` only when `date_str` is strictly later than `current_date_str`.

- Raises `ValueError` if either input is `None`.
- Raises `TypeError` if either input is not a string.
- Returns `False` if either date is invalid per `validate_date`.

## Rules
- Inputs are expected in `YYYY-MM-DD` format.
- Validity is delegated to `validate_date`.
- Comparison is performed by converting date parts to `YYYYMMDD` integers.
- Equal dates return `False` (strictly future only).

## Edge cases
- `("2026-01-02", "2026-01-01")` -> `True`
- `("2026-01-01", "2026-01-01")` -> `False`
- `("2025-12-31", "2026-01-01")` -> `False`
- invalid date in either argument -> `False`
- `None` input -> raises `ValueError`
- non-string input -> raises `TypeError`