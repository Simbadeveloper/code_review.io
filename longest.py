#!/usr/bin/python
#presetation_interview_manenos
#class longstring to check for
#longest stri
class longstring():

	def __init__(self,word1,word2):
		self.word1=word1
		self.word2=word2


#method to check for long or short string
#len() method check for the length of a string
#use if statement to compare the two string
	def long_or_short(self,*args):
		if len(self.word1)>len(self.word2):
			return self.word1
		elif len(self.word2)>len(self.word1):
			return self.word2
		else:
			return "the strings have same length"


     #method to check if string have same length
     #len() method check for the length of a string
     #i used if statement to compare the two string
	def same_word_length(self,*args):
		if len(self.word1)==len(self.word2):
	         return (self.word1, self.word2)
		else:
			return "the strings have different length"


