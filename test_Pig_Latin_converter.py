import unittest
from Pig_Latin_Converter import PigLatin


class PiglatinTest(unittest.TestCase):

 def test_consonants_method(self):
    self.my_word=PigLatin("silas")
    result=self.my_word.consonants()

    self.assertEqual(result,"ilassay", msg="successful convertered")
    self.assertNotEqual(result,"silas", msg="Not converted")

 def test_vowels_method(self):
    self.my_word=PigLatin("andela")
    result=self.my_word.vowels()

    self.assertEqual(result,"andelaway",msg="successful convertered")
    self.assertNotEqual(result, "andela",msg="word not converted")

 def test_word_game_method(self):
    self.my_word=PigLatin("andela")
    result=self.my_word.vowels()

    self.my_word=PigLatin("silas")
    result2=self.my_word.consonants()

    self.assertEqual(result,"andelaway",msg="successful convertered")
    self.assertNotEqual(result, "andela",msg="word not converted")
    self.assertEqual(result2,"ilassay",msg="successful convertered")
    self.assertNotEqual(result2,"silas", msg="Not converted")

if __name__ == '__main__':
    unittest.main()
