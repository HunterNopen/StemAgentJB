import pytest
from source import check_permission

def test_admin_permissions():
    assert check_permission('admin', 'delete') is True
    assert check_permission('admin', 'approve') is True
    assert check_permission('admin', 'view') is True
    assert check_permission('admin', 'edit') is True
    assert check_permission('admin', 'view_public') is True

def test_manager_permissions():
    assert check_permission('manager', 'approve') is True
    assert check_permission('manager', 'view') is True
    assert check_permission('manager', 'edit') is True
    assert check_permission('manager', 'delete') is False
    assert check_permission('manager', 'view_public') is False

def test_user_permissions():
    assert check_permission('user', 'view') is True
    assert check_permission('user', 'edit') is False
    assert check_permission('user', 'approve') is False
    assert check_permission('user', 'delete') is False
    assert check_permission('user', 'view_public') is False

def test_guest_permissions():
    assert check_permission('guest', 'view_public') is True
    assert check_permission('guest', 'view') is False
    assert check_permission('guest', 'approve') is False
    assert check_permission('guest', 'edit') is False
    assert check_permission('guest', 'delete') is False

def test_unknown_role():
    assert check_permission('superadmin', 'view') is False
    assert check_permission('unknown', 'edit') is False

def test_none_arguments():
    with pytest.raises(ValueError):
        check_permission(None, 'view')
    with pytest.raises(ValueError):
        check_permission('admin', None)

def test_non_string_arguments():
    with pytest.raises(TypeError):
        check_permission(123, 'view')
    with pytest.raises(TypeError):
        check_permission('admin', 456)
    with pytest.raises(TypeError):
        check_permission([], 'view')
    with pytest.raises(TypeError):
        check_permission('admin', {})