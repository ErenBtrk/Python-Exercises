'''
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
    then tell them whether they guessed too low, too high, or exactly right. 
    (Hint: remember to use the user input lessons from the very first exercise)

    Extras:

    1-Keep the game going until the user types “exit”
    2-Keep track of how many guesses the user has taken, and when the game ends, print this out.

'''
import random



while True:
    flag = False
    counter = 0
    randomNumber = random.randint(1,10)
    print(randomNumber)
    while True:
        try:
            userInput = input("Please enter a number between 1-10(Type 'exit' to quit) : ").lower().strip().replace(' ','')
            if(userInput == "exit"):
                flag = True
                break
            if(int(userInput) < 1 or int(userInput) > 10):
                raise Exception(f"The number({userInput}) you have entered is not in range.")
        except Exception as excObject:
            print(excObject)
        else:
            counter += 1
            if int(userInput) > randomNumber:
                print("Too HIGH.")
            elif int(userInput) < randomNumber:
                print("Too LOW.")
            else:
                print(f"Your guess is RIGHT in {counter} try/tries!!!!!")
                print("Starting a new game...")
                break
    if(flag):
        print("Quitting...")
        break

        



    
    