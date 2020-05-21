#Python program to find and replace ajectives , nouns , adverbs and verbs in a file with those given by the user.

import re

f = open("sentence.txt" , "r")
fcontent = f.read()
print(fcontent)
f.close()
fcontent = re.sub(r"adjective|ADJECTIVE" , input("Adjective: ") , fcontent)
print(fcontent)
fcontent = re.sub(r"noun|NOUN" , input("Noun: ") , fcontent)
print(fcontent)
fcontent = re.sub(r"adverb|ADVERB" , input("Adverb: ") , fcontent)
print(fcontent)
fcontent = re.sub(r"verb|VERB" , input("Verb: ") , fcontent)
print(fcontent)
f = open("sentence.txt" , "w")
f.write(fcontent)
f.close()

