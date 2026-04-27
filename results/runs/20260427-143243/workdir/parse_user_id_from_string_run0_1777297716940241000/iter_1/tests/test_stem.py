import pytest
from source import parse_user_id_from_string

def test_valid_user_id_formats():
    assert parse_user_id_from_string('USER:12345') == 12345
    assert parse_user_id_from_string('ID=67890') == 67890
    assert parse_user_id_from_string('account_42') == 42
    assert parse_user_id_from_string('987') == 987
    assert parse_user_id_from_string('abc1x2y3') == 123

def test_invalid_user_id_formats():
    assert parse_user_id_from_string('USER:abc') is None
    assert parse_user_id_from_string('ID=abc') is None
    assert parse_user_id_from_string('no_digits') is None
    assert parse_user_id_from_string('') is None

def test_none_input():
    with pytest.raises(ValueError):
        parse_user_id_from_string(None)

def test_non_string_input():
    with pytest.raises(TypeError):
        parse_user_id_from_string(123)
    with pytest.raises(TypeError):
        parse_user_id_from_string(45.67)
    with pytest.raises(TypeError):
        parse_user_id_from_string([])

def test_leading_trailing_whitespace():
    assert parse_user_id_from_string('   USER:12345   ') == 12345
    assert parse_user_id_from_string('   ID=67890   ') == 67890
    assert parse_user_id_from_string('   account_42   ') == 42
    assert parse_user_id_from_string('   987   ') == 987
    assert parse_user_id_from_string('   abc1x2y3   ') == 123
    assert parse_user_id_from_string('   no_digits   ') is None

def test_fallback_digit_collection():
    assert parse_user_id_from_string('abc123xyz456') == 123456
    assert parse_user_id_from_string('mixed123abc456def') == 123456
    assert parse_user_id_from_string('no_numbers_here') is None

def test_edge_cases():
    assert parse_user_id_from_string('USER:0') == 0
    assert parse_user_id_from_string('ID=0') == 0
    assert parse_user_id_from_string('account_0') == 0
    assert parse_user_id_from_string('000123') == 123
    assert parse_user_id_from_string('   000456   ') == 456

def test_unexpected_formats():
    assert parse_user_id_from_string('USER:123abc456') is None
    assert parse_user_id_from_string('ID=abc123') is None
    assert parse_user_id_from_string('random_string_with_123') == 123
    assert parse_user_id_from_string('123abc456def') == 123456