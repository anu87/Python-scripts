# -*- coding: utf-8 -*-
# this utf-8 comment tells python to use standard English lang
"""
Created on Sat Mar 26 14:40:13 2016

@author: Bhuti
"""

#bilingual dictionary : Spanish

#try:
   # input = raw_input # this is used to ensure that any input by a user is taken directly as input
    #because python will evaluate whatever the user enters as a python code; if the user types
    # sth wrong the program will crash; This is the only in p2, p3 already reads input as raw input
# expect NameError:
  #  pass

#user_said = input("Please enter a phrase: ")
#print("The user said: ", user_said)

translations = {
"merry": "feliz",
"christmas": "navidad",
"and": "y",
"happy": "feliz",
"new": "nuevo",
"year": "año", # ñ doesn't exist in python [not english] - utf-8 can address it
}
# "," after the last entry doesn't make any difference; {} don't require indentation

phrase = input("Please enter a phrase: ")

spanish_phrase =[]
for word in phrase.split(): #phrases have a built in fn split (check python.org documentation)
#() refers to split the word on white space - can be replaced w (";") or ","
    word = word.lower() # to recognize upper case when they don't exist in the lib translations
    spanish_word = translations.get(word,word) # tells to get the spanish word that word, if it's 
    #not there return the word; .get is also a built in fn
    spanish_phrase.append(spanish_word)

spanish_phrase = " ".join(spanish_phrase) # " " is the separator b/w the phrases
print("In Spanish that's: ", spanish_phrase)

#for english, spanish in translations.items():
 #   print(english, "translations to:", spanish)
  #  print(english, "translations to:", spanish, end =", ") # end="" refers to how you want to end
    # the output
