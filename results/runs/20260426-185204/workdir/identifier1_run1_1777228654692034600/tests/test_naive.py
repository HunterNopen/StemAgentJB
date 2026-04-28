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
        assert self.identifier.validateIdentifier('abc@def') == False

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
        assert self.identifier.validateIdentifier('0') == False
        assert self.identifier.validateIdentifier('A1') == True
        assert self.identifier.validateIdentifier('A1B2') == True
        assert self.identifier.validateIdentifier('A1B2C3') == True
        assert self.identifier.validateIdentifier('A1B2C3D') == False
        assert self.identifier.validateIdentifier('A1B2C3D4') == False
        assert self.identifier.validateIdentifier('A1B2C3D!') == False
        assert self.identifier.validateIdentifier('A1B2C3D_') == False

    def test_mixed_case_identifiers(self):
        assert self.identifier.validateIdentifier('aBc123') == True
        assert self.identifier.validateIdentifier('AbC') == True
        assert self.identifier.validateIdentifier('aBcD1') == True
        assert self.identifier.validateIdentifier('aBcD1E') == True
        assert self.identifier.validateIdentifier('aBcD1E2') == False
        assert self.identifier.validateIdentifier('aBcD1E!') == False
        assert self.identifier.validateIdentifier('aBcD1E_') == False