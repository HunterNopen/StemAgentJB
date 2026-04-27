import pytest
from source import transition_order_status

def test_valid_transitions():
    assert transition_order_status('draft', 'submit') == 'submitted'
    assert transition_order_status('draft', 'cancel') == 'cancelled'
    assert transition_order_status('submitted', 'approve') == 'approved'
    assert transition_order_status('submitted', 'cancel') == 'cancelled'
    assert transition_order_status('approved', 'ship') == 'shipped'
    assert transition_order_status('shipped', 'deliver') == 'delivered'

def test_terminal_statuses():
    assert transition_order_status('delivered', 'anything') == 'delivered'
    assert transition_order_status('cancelled', 'anything') == 'cancelled'

def test_unknown_status():
    assert transition_order_status('unknown', 'submit') == 'unknown'
    assert transition_order_status('unknown', 'cancel') == 'unknown'

def test_invalid_actions():
    assert transition_order_status('draft', 'invalid_action') == 'draft'
    assert transition_order_status('submitted', 'invalid_action') == 'submitted'
    assert transition_order_status('approved', 'invalid_action') == 'approved'
    assert transition_order_status('shipped', 'invalid_action') == 'shipped'
    assert transition_order_status('delivered', 'invalid_action') == 'delivered'
    assert transition_order_status('cancelled', 'invalid_action') == 'cancelled'

def test_none_arguments():
    with pytest.raises(ValueError):
        transition_order_status(None, 'submit')
    with pytest.raises(ValueError):
        transition_order_status('draft', None)

def test_non_string_arguments():
    with pytest.raises(TypeError):
        transition_order_status(123, 'submit')
    with pytest.raises(TypeError):
        transition_order_status('draft', 456)
    with pytest.raises(TypeError):
        transition_order_status([], 'submit')
    with pytest.raises(TypeError):
        transition_order_status('draft', {})

def test_empty_string_arguments():
    assert transition_order_status('', 'submit') == ''
    assert transition_order_status('draft', '') == 'draft'
    assert transition_order_status('', '') == ''

def test_whitespace_arguments():
    assert transition_order_status('   ', 'submit') == '   '
    assert transition_order_status('draft', '   ') == 'draft'
    assert transition_order_status('   ', '   ') == '   '

def test_all_combinations_of_actions():
    statuses = ['draft', 'submitted', 'approved', 'shipped', 'delivered', 'cancelled']
    actions = ['submit', 'cancel', 'approve', 'ship', 'deliver', 'invalid_action']
    for status in statuses:
        for action in actions:
            result = transition_order_status(status, action)
            if status == 'draft':
                if action == 'submit':
                    assert result == 'submitted'
                elif action == 'cancel':
                    assert result == 'cancelled'
                else:
                    assert result == status
            elif status == 'submitted':
                if action == 'approve':
                    assert result == 'approved'
                elif action == 'cancel':
                    assert result == 'cancelled'
                else:
                    assert result == status
            elif status == 'approved':
                if action == 'ship':
                    assert result == 'shipped'
                else:
                    assert result == status
            elif status == 'shipped':
                if action == 'deliver':
                    assert result == 'delivered'
                else:
                    assert result == status
            elif status == 'delivered':
                assert result == status
            elif status == 'cancelled':
                assert result == status
            else:
                assert result == status

def test_edge_case_comparisons():
    assert transition_order_status('draft', 'submit') == 'submitted'
    assert transition_order_status('submitted', 'approve') == 'approved'
    assert transition_order_status('approved', 'ship') == 'shipped'
    assert transition_order_status('shipped', 'deliver') == 'delivered'
    assert transition_order_status('delivered', 'anything') == 'delivered'
    assert transition_order_status('cancelled', 'anything') == 'cancelled'
    assert transition_order_status('unknown', 'submit') == 'unknown'
    assert transition_order_status('unknown', 'cancel') == 'unknown'
    assert transition_order_status('draft', 'invalid_action') == 'draft'
    assert transition_order_status('submitted', 'invalid_action') == 'submitted'
    assert transition_order_status('approved', 'invalid_action') == 'approved'
    assert transition_order_status('shipped', 'invalid_action') == 'shipped'
    assert transition_order_status('delivered', 'invalid_action') == 'delivered'
    assert transition_order_status('cancelled', 'invalid_action') == 'cancelled'