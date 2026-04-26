# check_permission

## Signature
`check_permission(user_role: str, action_required: str) -> bool`

## Contract
Returns whether `user_role` is allowed to perform `action_required`.

- Returns `True` for allowed role/action combinations.
- Returns `False` for disallowed combinations and unknown roles.
- Raises on invalid arguments:
  - `ValueError` if either argument is `None`
  - `TypeError` if either argument is not a string

## Rules
- Supported roles: `admin`, `manager`, `user`, `guest`.
- Unknown roles always return `False`.
- Permission matrix:
  - `admin`: all actions allowed (`True`)
  - `manager`: only `approve`, `view`, `edit`
  - `user`: only `view`
  - `guest`: only `view_public`

## Edge cases
- `("admin", "delete")` → `True`
- `("manager", "approve")` → `True`
- `("manager", "delete")` → `False`
- `("user", "view")` → `True`
- `("user", "edit")` → `False`
- `("guest", "view_public")` → `True`
- `("guest", "view")` → `False`
- `("superadmin", "view")` → `False` (unknown role)
- `None` in any argument → raises `ValueError`
- non-string input (e.g. `123`) → raises `TypeError`