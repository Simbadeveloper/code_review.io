class PigLatin():


         def __init__(self,word):
          self.word=word


         def consonants(self):
           self.word=self.word.lower()
           first=self.word[0]
           others=self.word[1:]
           another_word =others+first+"ay"
           return another_word

         def vowels(self):
           vowel="aeiou"
           if self.word[0] in vowel:
            new_word=self.word+"way"
            return new_word

         def word_game(self,word):
            self.word=input("Enter a word: ")
            if len(self.word)>1 and self.word.isalpha():
             vowel="aeiou"
            if self.word[0] in vowel:
                return self.vowels()
            else:
                return self.consonants()


