"""
So basically to test your code with unittest, you create a test.py file and import
Your functions from the main py file and the unittest module. To test each functions
you must def a test_functionname(self), inside a test classthat inherited from unittest.TestCase.
The unittest give you some assertion methodes to check your function are return expected values.
Following are the three possible outcomes of unittest:
    OK: The test is OK; no exception raised.
    Fail: An AssertionError was raised (the test has failed).
    Error: An exception was raised that is not an AssertionError.
"""
import unittest
from simple_unittest import first, last

list_num = [7,9,5]
list_chars = ['m', 'd', 'Z', 'l']

class TestPPMath(unittest.TestCase):

    def test_fist(self):
        self.assertEqual(first(list_num), 5) # assertion methode that came with unittest.TestCase

    def test_last(self):
        self.assertTrue(last(list_chars), 'm')

    def test_fist_again(self):
        self.assertFalse(first(list_num), 9)

    def testFirstAgain(self):
        self.failUnless(first(list_chars), 'Z')

'''
The issues with unittest is that you they may be a input that you have not tested that causes an error
'''

if __name__=='__main__':
    unittest.main() # you run your test file like this

