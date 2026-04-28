import pytest
from source import transition_account_state

def test_transition_account_state_valid_transitions():
    assert transition_account_state('active', 'suspend') == 'suspended'
    assert transition_account_state('suspended', 'unsuspend') == 'active'
    assert transition_account_state('locked', 'unlock') == 'active'
    assert transition_account_state('active', 'delete') == 'deleted'
    assert transition_account_state('suspended', 'delete') == 'deleted'
    assert transition_account_state('locked', 'delete') == 'deleted'
    assert transition_account_state('deleted', 'delete') == 'deleted'

def test_transition_account_state_automatic_lock():
    assert transition_account_state('active', 'login', failed_login_count=5) == 'locked'
    assert transition_account_state('active', 'login', failed_login_count=6) == 'locked'
    assert transition_account_state('active', 'login', failed_login_count=4) == 'active'

def test_transition_account_state_invalid_transitions():
    assert transition_account_state('locked', 'suspend') == 'locked'
    assert transition_account_state('suspended', 'lock') == 'suspended'
    assert transition_account_state('deleted', 'unsuspend') == 'deleted'
    assert transition_account_state('active', 'unknown_action') == 'active'

def test_transition_account_state_edge_cases():
    assert transition_account_state('active', 'delete') == 'deleted'
    assert transition_account_state('deleted', 'suspend') == 'deleted'
    assert transition_account_state('suspended', 'delete') == 'deleted'
    assert transition_account_state('active', 'suspend', failed_login_count=0) == 'suspended'
    assert transition_account_state('active', 'login', failed_login_count=0) == 'active'