import pytest
from identifier import Identifier

@pytest.fixture
def identifier():
    return Identifier()

def test_valid_short_identifier(identifier):
    assert identifier.validateIdentifier("a") == True
    assert identifier.validateIdentifier("a1b2") == True

def test_invalid_first_character(identifier):
    assert identifier.validateIdentifier("1abc") == False
    assert identifier.validateIdentifier("!abc") == False
    assert identifier.validateIdentifier("@abc") == False

def test_invalid_characters(identifier):
    assert identifier.validateIdentifier("abc_def") == False
    assert identifier.validateIdentifier("abc#123") == False
    assert identifier.validateIdentifier("abc!123") == False

def test_length_constraints(identifier):
    assert identifier.validateIdentifier("abcdefg") == False
    assert identifier.validateIdentifier("abcdef") == True
    assert identifier.validateIdentifier("abcde") == True
    assert identifier.validateIdentifier("abcd") == True
    assert identifier.validateIdentifier("abc") == True
    assert identifier.validateIdentifier("ab") == True
    assert identifier.validateIdentifier("a") == True

def test_empty_string(identifier):
    assert identifier.validateIdentifier("") == False

def test_boundary_cases(identifier):
    assert identifier.validateIdentifier("a1") == True
    assert identifier.validateIdentifier("a1234") == True
    assert identifier.validateIdentifier("a12345") == True
    assert identifier.validateIdentifier("a123456") == False
    assert identifier.validateIdentifier("A") == True
    assert identifier.validateIdentifier("Z") == True
    assert identifier.validateIdentifier("z") == True
    assert identifier.validateIdentifier("Y1") == True
    assert identifier.validateIdentifier("1Y") == False
    assert identifier.validateIdentifier("Y!") == False
    assert identifier.validateIdentifier("Y_") == False