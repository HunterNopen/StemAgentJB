import pytest
from source import transition_account_state

def test_valid_transitions():
    assert transition_account_state('active', 'suspend') == 'suspended'
    assert transition_account_state('suspended', 'unsuspend') == 'active'
    assert transition_account_state('locked', 'unlock') == 'active'
    assert transition_account_state('active', 'delete') == 'deleted'
    assert transition_account_state('deleted', 'delete') == 'deleted'
    assert transition_account_state('suspended', 'delete') == 'deleted'
    assert transition_account_state('locked', 'delete') == 'deleted'

def test_automatic_lock_transition():
    assert transition_account_state('active', 'login', failed_login_count=5) == 'locked'
    assert transition_account_state('active', 'login', failed_login_count=6) == 'locked'
    assert transition_account_state('active', 'login', failed_login_count=4) == 'active'

def test_invalid_transitions():
    assert transition_account_state('locked', 'suspend') == 'locked'
    assert transition_account_state('suspended', 'lock') == 'suspended'
    assert transition_account_state('deleted', 'suspend') == 'deleted'
    assert transition_account_state('deleted', 'unlock') == 'deleted'

def test_unknown_action():
    assert transition_account_state('active', 'unknown_action') == 'active'
    assert transition_account_state('suspended', 'random_action') == 'suspended'

def test_invalid_current_state():
    assert transition_account_state('frozen', 'delete') == 'frozen'
    assert transition_account_state('frozen', 'suspend') == 'frozen'
    assert transition_account_state('frozen', 'unsuspend') == 'frozen'

def test_edge_cases():
    assert transition_account_state('active', 'suspend') == 'suspended'
    assert transition_account_state('active', 'login', failed_login_count=5) == 'locked'
    assert transition_account_state('active', 'login', failed_login_count=4) == 'active'
    assert transition_account_state('locked', 'suspend') == 'locked'
    assert transition_account_state('deleted', 'delete') == 'deleted'