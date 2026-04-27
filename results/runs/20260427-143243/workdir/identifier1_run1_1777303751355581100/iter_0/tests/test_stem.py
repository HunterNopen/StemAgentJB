import pytest
from source import Identifier

@pytest.fixture
def identifier():
    return Identifier()

def test_valid_short_identifiers(identifier):
    assert identifier.validateIdentifier('a') is True
    assert identifier.validateIdentifier('z') is True
    assert identifier.validateIdentifier('A') is True
    assert identifier.validateIdentifier('Z') is True
    assert identifier.validateIdentifier('a1b2') is True
    assert identifier.validateIdentifier('abc123') is True
    assert identifier.validateIdentifier('a1') is True
    assert identifier.validateIdentifier('1a') is False
    assert identifier.validateIdentifier('abc') is True

def test_invalid_first_character(identifier):
    assert identifier.validateIdentifier('1abc') is False
    assert identifier.validateIdentifier('_abc') is False
    assert identifier.validateIdentifier('!abc') is False
    assert identifier.validateIdentifier('abc-def') is False

def test_invalid_length(identifier):
    assert identifier.validateIdentifier('abcdefg') is False
    assert identifier.validateIdentifier('') is False
    assert identifier.validateIdentifier('abcdef') is True
    assert identifier.validateIdentifier('abcde') is True

def test_invalid_characters(identifier):
    assert identifier.validateIdentifier('abc_def') is False
    assert identifier.validateIdentifier('abc@123') is False
    assert identifier.validateIdentifier('abc#') is False

def test_edge_cases(identifier):
    assert identifier.validateIdentifier('a') is True
    assert identifier.validateIdentifier('z') is True
    assert identifier.validateIdentifier('A') is True
    assert identifier.validateIdentifier('Z') is True
    assert identifier.validateIdentifier('abc') is True
    assert identifier.validateIdentifier('abc1') is True
    assert identifier.validateIdentifier('abc12') is True
    assert identifier.validateIdentifier('abc123') is True
    assert identifier.validateIdentifier('abcdef') is True
    assert identifier.validateIdentifier('abcdefg') is False
    assert identifier.validateIdentifier('1abc') is False
    assert identifier.validateIdentifier('') is False
    assert identifier.validateIdentifier('abc_def') is False
    assert identifier.validateIdentifier('abc@123') is False
    assert identifier.validateIdentifier('abc#') is False

def test_character_validation_methods(identifier):
    assert identifier.valid_s('a') is True
    assert identifier.valid_s('Z') is True
    assert identifier.valid_s('1') is False
    assert identifier.valid_s('_') is False
    assert identifier.valid_f('a') is True
    assert identifier.valid_f('Z') is True
    assert identifier.valid_f('1') is True
    assert identifier.valid_f('_') is False
    assert identifier.valid_f('@') is False