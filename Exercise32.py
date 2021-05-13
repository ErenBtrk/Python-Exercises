'''
This exercise is Part 3 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 2.

You can start your Python journey anywhere, but to finish this exercise you will have to have finished Parts 1 
and 2 or use the solutions (Part 1 and Part 2).

In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses
(head, body, 2 legs, and 2 arms) before they lose the game.

In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing the
letter and displaying that information to the user. In this exercise, we have to put it all together and add logic
for handling guesses.

Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:

Only let the user guess 6 times, and tell the user how many guesses they have left.
Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them
- let them guess again.
Optional additions:

When the player wins or loses, let them start a new game.
Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman.
This is challenging - do the other parts of the exercise first!
Your solution will be a lot cleaner if you make use of functions to help you!

'''
import random

def readFromFileAndReturnWord():
    with open('dictionary.txt') as file:
	    words = list(file)
    file.close()
    return random.choice(words).strip()

##################################################################################################################

def drawUnderscores(word):
    underscoreStr = ""
    for item in word:
        underscoreStr += " _"
    return underscoreStr

##################################################################################################################

def askForInput():
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
    return userGuess

##################################################################################################################

def replaceLetters(userGuess,word,underscoreStrList):
    flag = False
    for index in range(len(word)):
        if(word[index].lower() == userGuess): 
            underscoreStrList[index*2+1] = userGuess
            flag = True
    return flag

##################################################################################################################



word = readFromFileAndReturnWord()
underscoreStr = drawUnderscores(word)
underscoreStrList = list(underscoreStr)
userGuessList = []
count = 0
letterNumber = set(word)


while True:
    print(f"YOUR HEALTH : {len(letterNumber) - count}")

    userGuess = askForInput()
    while userGuess in userGuessList:
        print(f"You already used '{userGuess}' letter")
        userGuess = askForInput()

    userGuessList.append(userGuess)

    doHaveLetter = replaceLetters(userGuess,word,underscoreStrList)
    if(not doHaveLetter):
        count += 1
    
    print(*underscoreStrList)
    
    if(not '_' in underscoreStrList):
        print("YOU WON.")
        break
    if(count == len(letterNumber)):
        print(f"YOU LOST.The word was {word}")
        break 
   
