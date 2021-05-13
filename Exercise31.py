'''
This exercise is Part 2 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 3.

Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program
that the player has to guess, letter by letter. The player guesses one letter at a time until
the entire word has been guessed. (In the actual game, the player can only guess 6 letters incorrectly before losing).

Let’s say the word the player has to guess is “EVAPORATE”. For this exercise,
write the logic that asks a player to guess a letter and displays letters 
in the clue word that were guessed correctly. For now, let the player guess
an infinite number of times until they get the entire word. As a bonus, 
keep track of the letters the player guessed and display a different message
if the player tries to guess that letter again. Remember to stop the game 
when all the letters have been guessed correctly! Don’t worry about choosing
a word randomly or keeping track of the number of guesses the player has 
remaining - we will deal with those in a future exercise.

An example interaction can look like this:

>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...
And so on, until the player gets the word.

'''

import random

with open('dictionary.txt') as f:
	words = list(f)
f.close()

word = random.choice(words).strip()
lineStr = ""
for item in word:
    lineStr += " _"
print(word)
print(lineStr)
lineStrList = list(lineStr)

count = 0

while True:
    while True:
        try:
            userGuess = input("Please enter a letter : ").lower().strip().replace(' ','')
            if(len(userGuess) > 1 or len(userGuess) < 0):
                raise Exception("Invalid length.")
            if(not userGuess.isalpha()):
                raise Exception("Invalid character.")
        except Exception as excObject:
            print(excObject)
        else:
            break
    for index in range(len(word)):
        if(word[index].lower() == userGuess):
            count += 1
            lineStrList[index*2+1] = userGuess
    print(*lineStrList)
    if(count == len(word)):
        break
    

