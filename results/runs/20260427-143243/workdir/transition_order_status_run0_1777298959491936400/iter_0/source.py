def transition_order_status(current_status, action):
    """Return new status based on allowed transitions, or current status if action invalid."""
    if current_status is None or action is None:
        raise ValueError("current_status and action cannot be None")
    if not isinstance(current_status, str) or not isinstance(action, str):
        raise TypeError("current_status and action must be strings")
    
    valid_statuses = ['draft', 'submitted', 'approved', 'shipped', 'delivered', 'cancelled']
    if current_status not in valid_statuses:
        return current_status  # unknown status, no change
    
    # Business logic transitions (domain rules)
    if current_status == 'draft':
        if action == 'submit':
            return 'submitted'
        elif action == 'cancel':
            return 'cancelled'
        else:
            return current_status
    elif current_status == 'submitted':
        if action == 'approve':
            return 'approved'
        elif action == 'cancel':
            return 'cancelled'
        else:
            return current_status
    elif current_status == 'approved':
        if action == 'ship':
            return 'shipped'
        else:
            return current_status  # cannot cancel after approval
    elif current_status == 'shipped':
        if action == 'deliver':
            return 'delivered'
        else:
            return current_status
    elif current_status == 'delivered':
        return current_status  # no valid actions from delivered
    elif current_status == 'cancelled':
        return current_status  # immutable
    return current_status