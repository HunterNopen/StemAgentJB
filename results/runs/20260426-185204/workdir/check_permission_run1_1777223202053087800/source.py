def check_permission(user_role, action_required):
    """Return True if user_role is allowed to perform action_required, else False."""
    if user_role is None or action_required is None:
        raise ValueError("user_role and action_required cannot be None")
    if not isinstance(user_role, str) or not isinstance(action_required, str):
        raise TypeError("user_role and action_required must be strings")
    
    valid_roles = ['admin', 'manager', 'user', 'guest']
    if user_role not in valid_roles:
        return False
    
    if user_role == 'admin':
        return True
    elif user_role == 'manager':
        return action_required in ('approve', 'view', 'edit')
    elif user_role == 'user':
        return action_required == 'view'
    elif user_role == 'guest':
        return action_required == 'view_public'
    return False