# parse_log_line

## Signature
`parse_log_line(line: str) -> dict | None`

## Contract
Parses a log line into a dictionary with keys `datetime`, `level`, and `message`.

- Returns a dictionary when parsing succeeds.
- Returns `None` for malformed but non-exceptional input.
- Raises on invalid argument type/value:
  - `ValueError` if `line is None`
  - `TypeError` if `line` is not a string

## Rules
- Input format is expected as: `<date> <time> <level> <message...>`.
- Splits by spaces and requires at least 4 tokens.
  - token 1: `date_str`
  - token 2: `time_str`
  - token 3: `level`
  - token 4+ joined with spaces: `message`
- `time_str` must contain exactly 3 colon-separated parts (`HH:MM:SS` or `HH:MM:SS,ms`).
- `hour`, `minute`, and `second` must be integers in valid ranges:
  - `0 <= hour <= 23`
  - `0 <= minute <= 59`
  - `0 <= second <= 59`
- If seconds include milliseconds (e.g., `12:10:05,123`), only the part before `,` is validated as seconds.
- Return value on success:
  - `datetime`: `"{date_str} {time_str}"`
  - `level`: parsed level token
  - `message`: joined message text

## Concrete examples
- `parse_log_line("[2024-01-15 10:30:45] INFO: User logged in")` → 
    `{"timestamp": "2024-01-15 10:30:45", "level": "INFO", "message": "User logged in"}`
- `parse_log_line("malformed")` → `None`
- `parse_log_line("")` → `None`

## Edge cases
- `""` → `None`
- `"2024-01-05 12:10 INFO"` → `None` (missing message token)
- `"2024-01-05 25:10:00 INFO Boot"` → `None` (hour out of range)
- `"2024-01-05 12:61:00 INFO Boot"` → `None` (minute out of range)
- `"2024-01-05 12:10:61 INFO Boot"` → `None` (second out of range)
- `"2024-01-05 12:10:05,123 INFO Boot complete"` → valid dict
- `None` → raises `ValueError`
- non-string input (e.g. `123`) → raises `TypeError`