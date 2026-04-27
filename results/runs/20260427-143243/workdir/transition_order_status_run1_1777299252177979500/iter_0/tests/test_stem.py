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
    with pytest.raises(ValueError):
        transition_order_status(None, None)

def test_non_string_arguments():
    with pytest.raises(TypeError):
        transition_order_status(123, 'submit')
    with pytest.raises(TypeError):
        transition_order_status('draft', 456)
    with pytest.raises(TypeError):
        transition_order_status(123, 456)
    with pytest.raises(TypeError):
        transition_order_status(['draft'], 'submit')
    with pytest.raises(TypeError):
        transition_order_status('draft', ['submit'])

def test_edge_cases():
    assert transition_order_status('draft', '') == 'draft'
    assert transition_order_status('', 'submit') == ''
    assert transition_order_status('submitted', '') == 'submitted'
    assert transition_order_status('approved', '') == 'approved'
    assert transition_order_status('shipped', '') == 'shipped'
    assert transition_order_status('delivered', '') == 'delivered'
    assert transition_order_status('cancelled', '') == 'cancelled'