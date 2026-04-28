import pytest
from source import can_access_resource

def test_can_access_resource_active_user():
    user = {'active': True, 'role': 'user', 'id': 1}
    resource = {'owner_id': 1}
    assert can_access_resource(user, resource) is True

def test_can_access_resource_inactive_user():
    user = {'active': False, 'role': 'user', 'id': 1}
    resource = {'owner_id': 1}
    assert can_access_resource(user, resource) is False

def test_can_access_resource_public_resource():
    user = {'active': True, 'role': 'user', 'id': 1}
    resource = {'owner_id': 2, 'public': True}
    assert can_access_resource(user, resource) is True

def test_can_access_resource_admin_user():
    user = {'active': True, 'role': 'admin', 'id': 1}
    resource = {'owner_id': 2}
    assert can_access_resource(user, resource) is True

def test_can_access_resource_owner_user():
    user = {'active': True, 'role': 'user', 'id': 1}
    resource = {'owner_id': 1}
    assert can_access_resource(user, resource) is True

def test_can_access_resource_matching_group():
    user = {'active': True, 'role': 'user', 'id': 1, 'groups': ['group1']}
    resource = {'owner_id': 2, 'allowed_groups': ['group1']}
    assert can_access_resource(user, resource) is True

def test_can_access_resource_everyone_in_groups():
    user = {'active': True, 'role': 'user', 'id': 1, 'groups': ['group2']}
    resource = {'owner_id': 2, 'allowed_groups': ['everyone']}
    assert can_access_resource(user, resource) is True

def test_can_access_resource_no_allowed_groups():
    user = {'active': True, 'role': 'user', 'id': 1, 'groups': ['group2']}
    resource = {'owner_id': 2, 'allowed_groups': []}
    assert can_access_resource(user, resource) is False

def test_can_access_resource_missing_user_key():
    user = {'active': True, 'id': 1}
    resource = {'owner_id': 2}
    with pytest.raises(KeyError):
        can_access_resource(user, resource)

def test_can_access_resource_missing_resource_key():
    user = {'active': True, 'role': 'user', 'id': 1}
    resource = {}
    with pytest.raises(KeyError):
        can_access_resource(user, resource)

def test_can_access_resource_none_user():
    user = None
    resource = {'owner_id': 1}
    with pytest.raises(ValueError):
        can_access_resource(user, resource)

def test_can_access_resource_none_resource():
    user = {'active': True, 'role': 'user', 'id': 1}
    resource = None
    with pytest.raises(ValueError):
        can_access_resource(user, resource)

def test_can_access_resource_invalid_user_type():
    user = 'invalid_user'
    resource = {'owner_id': 1}
    with pytest.raises(TypeError):
        can_access_resource(user, resource)

def test_can_access_resource_invalid_resource_type():
    user = {'active': True, 'role': 'user', 'id': 1}
    resource = 'invalid_resource'
    with pytest.raises(TypeError):
        can_access_resource(user, resource)