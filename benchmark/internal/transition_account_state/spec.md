# transition_account_state

## Signature
`transition_account_state(current_state: str, action: str, failed_login_count: int = 0) -> str`

## Contract
Returns the new state after applying `action` to an account currently in
`current_state`. If the action is invalid for the current state, returns
`current_state` unchanged.

Raises `ValueError` if `current_state` is not one of the valid states.
Raises `ValueError` if `failed_login_count` is negative.

## Valid states
`active`, `suspended`, `locked`, `deleted`.

## Rules
- Automatic transition: if `current_state == 'active'` and
  `failed_login_count >= 5`, returns `'locked'` regardless of `action`.
- `delete` action: from any state except `deleted`, returns `'deleted'`.
  From `deleted`, returns `'deleted'` unchanged.
- `suspend` action: only valid from `active`; returns `'suspended'`.
  From any other state, returns `current_state`.
- `unsuspend` action: only valid from `suspended`; returns `'active'`.
- `unlock` action: only valid from `locked`; returns `'active'`.
- Unknown actions: returns `current_state`.

## Edge cases
- `transition_account_state('active', 'suspend')` → `'suspended'`
- `transition_account_state('active', 'login', failed_login_count=5)` → `'locked'`
- `transition_account_state('active', 'login', failed_login_count=4)` → `'active'`
- `transition_account_state('locked', 'suspend')` → `'locked'` (invalid transition)
- `transition_account_state('deleted', 'delete')` → `'deleted'`
- `transition_account_state('frozen', 'delete')` raises `ValueError`
- `transition_account_state('active', 'login', failed_login_count=-1)` raises `ValueError`