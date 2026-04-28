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
        assert self.identifier.validateIdentifier('2xyz') == False

    def test_invalid_characters(self):
        assert self.identifier.validateIdentifier('abc_def') == False
        assert self.identifier.validateIdentifier('abc@123') == False
        assert self.identifier.validateIdentifier('abc#') == False

    def test_length_constraints(self):
        assert self.identifier.validateIdentifier('abcdefg') == False
        assert self.identifier.validateIdentifier('abcdef') == True
        assert self.identifier.validateIdentifier('abcde') == True
        assert self.identifier.validateIdentifier('abc') == True
        assert self.identifier.validateIdentifier('ab') == True
        assert self.identifier.validateIdentifier('a') == True
        assert self.identifier.validateIdentifier('') == False