def can_access_resource(user, resource):
    """Return True if user can access resource based on role, ownership, groups."""
    if user is None or resource is None:
        raise ValueError("user and resource cannot be None")
    if not isinstance(user, dict) or not isinstance(resource, dict):
        raise TypeError("user and resource must be dictionaries")
    
    # Required keys; raise if missing critical fields
    if 'active' not in user:
        raise KeyError("user dict must have 'active' key")
    if 'role' not in user:
        raise KeyError("user dict must have 'role' key")
    if 'id' not in user:
        raise KeyError("user dict must have 'id' key")
    if 'owner_id' not in resource:
        raise KeyError("resource dict must have 'owner_id' key")
    
    # Business logic (returns False for disallowed cases)
    if not user['active']:
        return False
    if resource.get('public', False):
        return True
    if user.get('role') == 'admin':
        return True
    if user.get('id') == resource.get('owner_id'):
        return True
    
    user_groups = user.get('groups', [])
    resource_groups = resource.get('allowed_groups', [])
    if not resource_groups:
        return False
    for ug in user_groups:
        if ug in resource_groups:
            return True
    if 'everyone' in resource_groups:
        return True
    return False