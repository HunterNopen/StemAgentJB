# transition_order_status

## Signature
`transition_order_status(current_status: str, action: str) -> str`

## Contract
Returns the next order status according to allowed state transitions.

- Raises `ValueError` if `current_status` or `action` is `None`.
- Raises `TypeError` if either argument is not a string.
- Returns current status unchanged for unknown status values or invalid actions.

## Rules
- Valid statuses: `draft`, `submitted`, `approved`, `shipped`, `delivered`, `cancelled`.
- Unknown `current_status` returns unchanged.
- Allowed transitions:
  - `draft` + `submit` -> `submitted`
  - `draft` + `cancel` -> `cancelled`
  - `submitted` + `approve` -> `approved`
  - `submitted` + `cancel` -> `cancelled`
  - `approved` + `ship` -> `shipped`
  - `shipped` + `deliver` -> `delivered`
- `delivered` and `cancelled` are terminal in this function (always unchanged).

## Edge cases
- `("draft", "submit")` -> `submitted`
- `("approved", "cancel")` -> `approved`
- `("unknown", "submit")` -> `unknown`
- `("delivered", "anything")` -> `delivered`
- `None` in any argument -> raises `ValueError`
- non-string input -> raises `TypeError`