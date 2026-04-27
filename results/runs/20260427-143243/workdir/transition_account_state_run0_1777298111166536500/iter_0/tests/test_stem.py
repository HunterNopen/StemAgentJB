import pytest
from source import transition_account_state

def test_valid_transitions():
    assert transition_account_state('active', 'suspend') == 'suspended'
    assert transition_account_state('suspended', 'unsuspend') == 'active'
    assert transition_account_state('locked', 'unlock') == 'active'
    assert transition_account_state('deleted', 'delete') == 'deleted'
    assert transition_account_state('active', 'delete') == 'deleted'
    assert transition_account_state('suspended', 'delete') == 'deleted'
    assert transition_account_state('locked', 'delete') == 'deleted'

def test_automatic_lock_transition():
    assert transition_account_state('active', 'login', failed_login_count=5) == 'locked'
    assert transition_account_state('active', 'login', failed_login_count=6) == 'locked'
    assert transition_account_state('active', 'login', failed_login_count=4) == 'active'

def test_invalid_transitions():
    assert transition_account_state('suspended', 'suspend') == 'suspended'
    assert transition_account_state('locked', 'suspend') == 'locked'
    assert transition_account_state('deleted', 'unsuspend') == 'deleted'
    assert transition_account_state('deleted', 'unlock') == 'deleted'
    assert transition_account_state('deleted', 'login') == 'deleted'

def test_unknown_action():
    assert transition_account_state('active', 'unknown_action') == 'active'
    assert transition_account_state('suspended', 'unknown_action') == 'suspended'
    assert transition_account_state('locked', 'unknown_action') == 'locked'
    assert transition_account_state('deleted', 'unknown_action') == 'deleted'

def test_invalid_current_state():
    assert transition_account_state('frozen', 'delete') == 'frozen'
    assert transition_account_state('frozen', 'suspend') == 'frozen'
    assert transition_account_state('frozen', 'unsuspend') == 'frozen'
    assert transition_account_state('frozen', 'unlock') == 'frozen'

def test_failed_login_count_normalization():
    assert transition_account_state('active', 'login', failed_login_count=-1) == 'active'
    assert transition_account_state('active', 'login', failed_login_count=0) == 'active'
    assert transition_account_state('active', 'login', failed_login_count=1) == 'active'
    assert transition_account_state('active', 'login', failed_login_count=4) == 'active'

def test_type_error_on_non_integer_failed_login_count():
    with pytest.raises(TypeError):
        transition_account_state('active', 'login', failed_login_count='string')
    with pytest.raises(TypeError):
        transition_account_state('active', 'login', failed_login_count=3.5)