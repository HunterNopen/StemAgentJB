import pytest
from source import transition_account_state

def test_transition_account_state_active_to_suspended():
    assert transition_account_state('active', 'suspend') == 'suspended'

def test_transition_account_state_active_to_locked_due_to_failed_logins():
    assert transition_account_state('active', 'login', failed_login_count=5) == 'locked'

def test_transition_account_state_active_with_failed_logins_below_threshold():
    assert transition_account_state('active', 'login', failed_login_count=4) == 'active'

def test_transition_account_state_locked_with_invalid_suspend_action():
    assert transition_account_state('locked', 'suspend') == 'locked'

def test_transition_account_state_deleted_with_delete_action():
    assert transition_account_state('deleted', 'delete') == 'deleted'

def test_transition_account_state_deleted_with_delete_action_from_other_state():
    assert transition_account_state('active', 'delete') == 'deleted'
    assert transition_account_state('suspended', 'delete') == 'deleted'
    assert transition_account_state('locked', 'delete') == 'deleted'

def test_transition_account_state_invalid_current_state():
    assert transition_account_state('frozen', 'delete') == 'frozen'

def test_transition_account_state_suspended_to_active():
    assert transition_account_state('suspended', 'unsuspend') == 'active'

def test_transition_account_state_active_to_active_with_unknown_action():
    assert transition_account_state('active', 'unknown_action') == 'active'

def test_transition_account_state_locked_to_active_with_unlock_action():
    assert transition_account_state('locked', 'unlock') == 'active'

def test_transition_account_state_invalid_type_current_state():
    with pytest.raises(TypeError):
        transition_account_state(123, 'suspend')

def test_transition_account_state_invalid_type_action():
    with pytest.raises(TypeError):
        transition_account_state('active', 123)

def test_transition_account_state_invalid_type_failed_login_count():
    with pytest.raises(TypeError):
        transition_account_state('active', 'login', failed_login_count='five')

def test_transition_account_state_none_current_state():
    with pytest.raises(ValueError):
        transition_account_state(None, 'suspend')

def test_transition_account_state_none_action():
    with pytest.raises(ValueError):
        transition_account_state('active', None)