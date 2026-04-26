# can_access_resource

## Signature
`can_access_resource(user: dict, resource: dict) -> bool`

## Contract
Determines access using activity status, visibility, role, ownership, and groups.

- Raises `ValueError` if `user` or `resource` is `None`.
- Raises `TypeError` if either input is not a dictionary.
- Raises `KeyError` if required keys are missing.
- Returns `True`/`False` for business-rule evaluation.

## Rules
- Required keys:
  - `user`: `active`, `role`, `id`
  - `resource`: `owner_id`
- Access is denied if user is inactive.
- Access is allowed if resource is public.
- Access is allowed for admin users.
- Access is allowed for owners (`user.id == resource.owner_id`).
- Otherwise, access is allowed when any `user.groups` item appears in `resource.allowed_groups`.
- Access is also allowed if `everyone` is in `resource.allowed_groups`.
- If `allowed_groups` is missing/empty, access is denied at group-check stage.

## Edge cases
- inactive user -> `False`
- public resource -> `True`
- owner user -> `True`
- matching group intersection -> `True`
- `allowed_groups` contains `everyone` -> `True`
- missing required keys -> raises `KeyError`
- wrong input type / `None` -> raises `TypeError` / `ValueError`