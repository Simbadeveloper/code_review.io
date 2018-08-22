#!/usr/bin/python
import unittest  #import module unittest
from longest import longstring  #import class longest from longest module

class Testlongstring(unittest.TestCase):

#tests to be run
#declare your method with test_ for the test to run
#instanciate your class with my_word variable
#assign variable result to the outcome of the output
#use assert to test your result with different assert method

    def test_long_or_short_method(self,*args):#tset length of string according to its width
        self.my_word=longstring("silas","omurunga")
        result=self.my_word.long_or_short("silas","omurunga")

        self.assertEqual(result,"omurunga", msg="string2 is longer than string1") #assertion tests
        self.assertNotEqual(result,"silas", msg="string1 is short than string2")

    def test_same_word_length_method(self,*args):  #test same word lengthof two strings
        self.my_word=longstring("omurunga","omurunga")
        result=self.my_word.same_word_length("omurunga","omurunga")

        self.assertEqual(result,("omurunga","omurunga"), msg="the strings have same length") #assertion tests
        self.assertNotEqual(result,("silas","omurunga"), msg="the string have different length")

if __name__=='__main__':
    unittest.main()     #add unittest to main()