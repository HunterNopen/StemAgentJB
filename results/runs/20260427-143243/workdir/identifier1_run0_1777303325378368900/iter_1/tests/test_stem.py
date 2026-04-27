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
    assert identifier.validateIdentifier('A1B2') is True
    assert identifier.validateIdentifier('abc123') is True
    assert identifier.validateIdentifier('a1') is True
    assert identifier.validateIdentifier('abc') is True

def test_invalid_first_character(identifier):
    assert identifier.validateIdentifier('1abc') is False
    assert identifier.validateIdentifier('!abc') is False
    assert identifier.validateIdentifier('@abc') is False
    assert identifier.validateIdentifier('#abc') is False

def test_invalid_characters(identifier):
    assert identifier.validateIdentifier('abc_def') is False
    assert identifier.validateIdentifier('abc!') is False
    assert identifier.validateIdentifier('abc@') is False
    assert identifier.validateIdentifier('abc#') is False

def test_length_constraints(identifier):
    assert identifier.validateIdentifier('') is False
    assert identifier.validateIdentifier('abcdefg') is False
    assert identifier.validateIdentifier('abcdef') is True
    assert identifier.validateIdentifier('abcde') is True
    assert identifier.validateIdentifier('abcd') is True
    assert identifier.validateIdentifier('abc') is True
    assert identifier.validateIdentifier('ab') is True
    assert identifier.validateIdentifier('a') is True

def test_edge_cases(identifier):
    assert identifier.validateIdentifier('a1') is True
    assert identifier.validateIdentifier('A1') is True
    assert identifier.validateIdentifier('a2b3c') is True
    assert identifier.validateIdentifier('abc123') is True
    assert identifier.validateIdentifier('abcde1') is True
    assert identifier.validateIdentifier('abcdefg') is False
    assert identifier.validateIdentifier('1abc') is False
    assert identifier.validateIdentifier('abc_def') is False
    assert identifier.validateIdentifier('') is False
    assert identifier.validateIdentifier('abc!') is False
    assert identifier.validateIdentifier('abc@') is False
    assert identifier.validateIdentifier('abc#') is False