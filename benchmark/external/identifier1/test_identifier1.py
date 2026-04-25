import unittest

from identifier1 import Identifier

class TestIdentifier(unittest.TestCase):
    def setUp(self):
        self.identifier = Identifier()

    def test_validateIdentifier_valid_inputs(self):
        self.assertTrue(self.identifier.validateIdentifier("a"))
        self.assertTrue(self.identifier.validateIdentifier("abcdef"))
        self.assertTrue(self.identifier.validateIdentifier("ABCDEF"))
        self.assertTrue(self.identifier.validateIdentifier("AbCdEf"))
        self.assertTrue(self.identifier.validateIdentifier("abc123"))
    
    def test_validateIdentifier_invalid_inputs(self):
        self.assertFalse(self.identifier.validateIdentifier(""))
        self.assertFalse(self.identifier.validateIdentifier("abcdefg"))
        self.assertFalse(self.identifier.validateIdentifier("123456"))
        self.assertFalse(self.identifier.validateIdentifier("@#$%^&"))
        self.assertFalse(self.identifier.validateIdentifier("abc#123"))

    def test_valid_s_valid_inputs(self):
        self.assertTrue(self.identifier.valid_s("A"))
        self.assertTrue(self.identifier.valid_s("a"))
        self.assertTrue(self.identifier.valid_s("Z"))
        self.assertTrue(self.identifier.valid_s("z"))
    
    def test_valid_s_invalid_inputs(self):
        self.assertFalse(self.identifier.valid_s("0"))
        self.assertFalse(self.identifier.valid_s("9"))
        self.assertFalse(self.identifier.valid_s("#"))
        self.assertFalse(self.identifier.valid_s("&"))
        
    def test_valid_f_valid_inputs(self):
        self.assertTrue(self.identifier.valid_f("A"))
        self.assertTrue(self.identifier.valid_f("a"))
        self.assertTrue(self.identifier.valid_f("Z"))
        self.assertTrue(self.identifier.valid_f("z"))
        self.assertTrue(self.identifier.valid_f("0"))
        self.assertTrue(self.identifier.valid_f("9"))
    
    def test_valid_f_invalid_inputs(self):
        self.assertFalse(self.identifier.valid_f("#"))
        self.assertFalse(self.identifier.valid_f("&"))
        
if __name__ == '__main__':
    unittest.main()