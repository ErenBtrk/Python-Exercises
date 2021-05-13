'''
In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.
This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100.
The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
At the end of this exchange, your program should print out how many guesses it took to get your number.

As the writer of this program, you will have to choose how your program will strategically guess. 
A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number.
But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 
(right in the middle of the range), and then increase / decrease by 1 as needed. 
After you’ve written the program, try to find the optimal strategy! 
(We’ll talk about what is the optimal one next week with the solution.)
 
 '''

myList = [x for x in range(1,1001)]
myGuess = 500
lowest = 1
highest = 1000
count = 0
while True:
    print(f"My Guess is {myGuess}")
    count += 1
    while True:
        try:
            userInputStr = input("Please enter 'too high' if the number is higher than my guess.\n"
                                "Enter 'too low' if the number is lower than my guess.\n"
                                "Enter 'right' if the number is equal to my guess : ").lower().strip().replace(' ','')
            print(userInputStr)
            if(userInputStr != "toohigh" and userInputStr != "toolow" and userInputStr != "right"):
                raise Exception("Invalid input.")
        except Exception as excObject:
            print(excObject)
        else:
            break
    if(userInputStr == "toohigh"):
        indexGuess = myList.index(myGuess)
        print(indexGuess)
        highestIndex = myList.index(highest)
        del myList[indexGuess:highestIndex+1]
        myGuess = myList[len(myList) // 2]
        highest = myList[len(myList)-1]
        lowest = myList[0]
        print(myList)
        
    elif(userInputStr == "toolow"):
        indexGuess = myList.index(myGuess)
        print(indexGuess)
        lowestIndex = myList.index(lowest)
        del myList[lowestIndex:indexGuess]
        myGuess = myList[len(myList) // 2]
        lowest = myList[0]
        highest = myList[len(myList)-1]
        print(myList)
    else:
        print(f"I KNEW IT IN {count} ROUNDS!!")
        break
    

