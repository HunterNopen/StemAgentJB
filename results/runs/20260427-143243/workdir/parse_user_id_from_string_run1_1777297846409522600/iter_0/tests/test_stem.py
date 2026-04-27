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
    with pytest.raises(TypeError):
        parse_user_id_from_string({})
    with pytest.raises(TypeError):
        parse_user_id_from_string(set())

def test_edge_cases():
    assert parse_user_id_from_string('USER:0') == 0
    assert parse_user_id_from_string('ID=0') == 0
    assert parse_user_id_from_string('account_0') == 0
    assert parse_user_id_from_string('000123') == 123
    assert parse_user_id_from_string('abc_') is None
    assert parse_user_id_from_string('123abc456') == 123456

def test_large_string():
    large_string = 'a' * 10 ** 6 + 'USER:12345'
    assert parse_user_id_from_string(large_string) == 12345

def test_fallback_digit_collection():
    assert parse_user_id_from_string('abc123xyz456') == 123456
    assert parse_user_id_from_string('no_digits_here') is None
    assert parse_user_id_from_string('mixed123abc456def') == 123456

def test_empty_string():
    assert parse_user_id_from_string('') is None

def test_string_with_only_special_characters():
    assert parse_user_id_from_string('!@#$%^&*()') is None
    assert parse_user_id_from_string('abc!@#') is None

def test_string_with_leading_trailing_spaces():
    assert parse_user_id_from_string('   USER:12345   ') == 12345
    assert parse_user_id_from_string('   ID=67890   ') == 67890
    assert parse_user_id_from_string('   account_42   ') == 42
    assert parse_user_id_from_string('   987   ') == 987
    assert parse_user_id_from_string('   abc1x2y3   ') == 123

def test_string_with_digits_only():
    assert parse_user_id_from_string('1234567890') == 1234567890
    assert parse_user_id_from_string('00001234') == 1234

def test_string_with_no_digits():
    assert parse_user_id_from_string('no_digits_here') is None
    assert parse_user_id_from_string('just_letters') is None
    assert parse_user_id_from_string('!@#$%^&*()') is None
    assert parse_user_id_from_string('abc') is None
    assert parse_user_id_from_string('xyz') is None