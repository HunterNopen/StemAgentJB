def transition_account_state(current_state, action, failed_login_count=0):
    """Return new account state based on state machine rules."""
    if current_state is None or action is None:
        raise ValueError("current_state and action cannot be None")
    if not isinstance(current_state, str) or not isinstance(action, str):
        raise TypeError("current_state and action must be strings")
    if not isinstance(failed_login_count, int):
        raise TypeError("failed_login_count must be an integer")
    
    valid_states = ['active', 'suspended', 'locked', 'deleted']
    if current_state not in valid_states:
        return current_state  # unknown state, unchanged
    
    # Normalize failed_login_count (negative -> 0, but this is a business rule, not exception)
    if failed_login_count < 0:
        failed_login_count = 0
    
    # Automatic transition due to too many failures (business rule)
    if current_state == 'active' and failed_login_count >= 5:
        return 'locked'
    
    # Manual actions (business rules)
    if action == 'delete':
        if current_state != 'deleted':
            return 'deleted'
        return current_state
    elif action == 'suspend':
        if current_state == 'active':
            return 'suspended'
        return current_state
    elif action == 'unsuspend':
        if current_state == 'suspended':
            return 'active'
        return current_state
    elif action == 'unlock':
        if current_state == 'locked':
            return 'active'
        return current_state
    else:
        return current_state  # unknown action, no change