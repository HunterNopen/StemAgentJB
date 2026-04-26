# validate_date

## Signature
`validate_date(date_str: str) -> bool`

## Contract
Returns `True` if `date_str` is a syntactically and semantically valid
calendar date in `YYYY-MM-DD` format. Returns `False` otherwise.

Does not raise. All malformed input returns `False`.

## Rules
- Format must be exactly `YYYY-MM-DD` (zero-padded month and day, four-digit year).
- Year must be in `[1, 9999]`.
- Month must be in `[1, 12]`.
- Day must be in `[1, days_in_month]`, where `days_in_month` accounts for:
  - 31 days: Jan, Mar, May, Jul, Aug, Oct, Dec
  - 30 days: Apr, Jun, Sep, Nov
  - 28 or 29 days: Feb (29 if leap year)
- Leap year rule: divisible by 4, except centuries not divisible by 400.
  - 2000 is a leap year (divisible by 400).
  - 1900 is not (divisible by 100, not by 400).
  - 2024 is. 2023 is not.

## Edge cases
- `"2024-02-29"` → True (leap)
- `"2023-02-29"` → False (not leap)
- `"2024-13-01"` → False (month out of range)
- `"2024-2-29"` → False (month not zero-padded)
- `""`, `None`, `"not-a-date"` → False
- `"2024/02/29"` → False (wrong separator)