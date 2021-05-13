'''
This exercise is Part 1 of 3 of the Hangman exercise series. 
The other exercises are: Part 2 and Part 3.

In this exercise, the task is to write a function that picks a random word
from a list of words from the SOWPODS dictionary. 
Download this file and save it in the same directory as your Python code. 
This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments.
Each line in the file contains a single word.

Hint: use the Python random library for picking a random word.

'''

import random

with open('dictionary.txt') as f:
	words = list(f)
print(random.choice(words).strip())


#  # import the random library
#   import random

#   # read all the list of words
#   words = []
#   with open('sowpods.txt', 'r') as f:
#     line = f.readline().strip()
#     words.append(line)
#     while line:
#       line = f.readline().strip()
#       words.append(line)

#   # generate a random number
#   random_index = random.randint(0, len(words))

#   # take the word
#   print("Random word: ", words[random_index])