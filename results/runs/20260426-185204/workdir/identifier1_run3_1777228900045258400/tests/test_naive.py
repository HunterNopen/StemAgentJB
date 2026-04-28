import pytest
from source import Identifier

class TestIdentifier:

    def setup_method(self):
        self.identifier = Identifier()

    def test_valid_short_identifiers(self):
        assert self.identifier.validateIdentifier('a') == True
        assert self.identifier.validateIdentifier('a1b2') == True

    def test_invalid_first_character(self):
        assert self.identifier.validateIdentifier('1abc') == False
        assert self.identifier.validateIdentifier('!abc') == False
        assert self.identifier.validateIdentifier('@abc') == False

    def test_invalid_characters(self):
        assert self.identifier.validateIdentifier('abc_def') == False
        assert self.identifier.validateIdentifier('abc#def') == False
        assert self.identifier.validateIdentifier('abc$def') == False

    def test_length_constraints(self):
        assert self.identifier.validateIdentifier('abcdefg') == False
        assert self.identifier.validateIdentifier('abcdef') == True
        assert self.identifier.validateIdentifier('abcde') == True
        assert self.identifier.validateIdentifier('abcd') == True
        assert self.identifier.validateIdentifier('abc') == True
        assert self.identifier.validateIdentifier('ab') == True
        assert self.identifier.validateIdentifier('a') == True

    def test_empty_string(self):
        assert self.identifier.validateIdentifier('') == False

    def test_boundary_cases(self):
        assert self.identifier.validateIdentifier('A') == True
        assert self.identifier.validateIdentifier('Z') == True
        assert self.identifier.validateIdentifier('a') == True
        assert self.identifier.validateIdentifier('z') == True
        assert self.identifier.validateIdentifier('A1') == True
        assert self.identifier.validateIdentifier('Z9') == True
        assert self.identifier.validateIdentifier('a1b2') == True
        assert self.identifier.validateIdentifier('z9y8') == True

    def test_invalid_length(self):
        assert self.identifier.validateIdentifier('abcdefg') == False
        assert self.identifier.validateIdentifier('abcdefgh') == False
        assert self.identifier.validateIdentifier('123456') == False
        assert self.identifier.validateIdentifier('abc1234') == False

    def test_valid_length_with_numbers(self):
        assert self.identifier.validateIdentifier('a1b2') == True
        assert self.identifier.validateIdentifier('a1') == True
        assert self.identifier.validateIdentifier('a2b3c') == True
        assert self.identifier.validateIdentifier('a1b2c3') == True

    def test_invalid_characters_in_middle(self):
        assert self.identifier.validateIdentifier('a1b2@') == False
        assert self.identifier.validateIdentifier('a1b2c!') == False
        assert self.identifier.validateIdentifier('a1b2c#') == False

    def test_valid_identifiers_with_mixed_case(self):
        assert self.identifier.validateIdentifier('Abc1') == True
        assert self.identifier.validateIdentifier('aBcD2') == True
        assert self.identifier.validateIdentifier('ZyX3') == True

    def test_invalid_identifiers_with_mixed_case(self):
        assert self.identifier.validateIdentifier('1Abc') == False
        assert self.identifier.validateIdentifier('abcD@') == False
        assert self.identifier.validateIdentifier('abcD#') == False