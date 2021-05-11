'''
Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
For every digit that the user guessed correctly in the correct place, they have a “cow”.
For every digit the user guessed correctly in the wrong place is a “bull.” 
Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
Once the user guesses the correct number, the game is over. 
Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

Say the number generated by the computer is 1038. An example interaction could look like this:

  Welcome to the Cows and Bulls Game! 
  Enter a number: 
  >>> 1234
  2 cows, 0 bulls
  >>> 1256
  1 cow, 1 bull
  ...
Until the user guesses the number.
'''

import string
import random


randomNumber = random.randint(1000,9999)
randomNumberList = list(str(randomNumber))



countRounds = 0

while True:
    countRounds += 1
    while True:
        try:
            userInput = input(f"Round.{countRounds} : Please enter a 4 digits number : ").replace(" ","")
            if(not userInput.isdigit()):
                raise Exception("You did not enter a number.")
            else:
                if(len(userInput) < 4):
                    raise Exception("You have entered a number less than 4 digits.")
                elif(len(userInput) > 4):
                    raise Exception("You have entered a number more than 4 digits.")
        except Exception as excObject:
            print(excObject)
        else:
            break

    if(int(userInput) == randomNumber):
        print(f"Your guess is RIGHT!!! You guessed the number in {countRounds} rounds!")
        break
    else:
        userInputList = list(userInput)
    
    cowbullList1 = ["0","1","2","3"]
    cowbullList2 = ["0","1","2","3"]
    cowCount = 0
    for index in range(len(randomNumberList)):
        if(randomNumberList[index] == userInputList[index]):
            cowbullList1[index] = "Cow"
            cowbullList2[index] = "Cow"
            cowCount += 1
    

    bullCount = 0
    for index in range(len(randomNumberList)):
        if(cowbullList1[index] == "Cow" or cowbullList1[index] == "Bull"):
            continue
        for index2 in range(len(userInputList)):
            if(cowbullList2[index2] == "Cow" or cowbullList2[index2] == "Bull"):
                continue
            if(randomNumberList[index] == userInputList[index2] and cowbullList1[index] != "Bull" and cowbullList2[index2] != "Bull"):
                cowbullList1[index] = "Bull"
                cowbullList2[index2] = "Bull"
                bullCount += 1
            
    print(f"Cows = {cowCount} , Bulls = {bullCount}")


print(f"random number was = {randomNumber}")   

        
        
