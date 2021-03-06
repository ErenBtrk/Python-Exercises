'''
    Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message 
    to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

    1-If the number is a multiple of 4, print out a different message.
    2-Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check 
    divides evenly into num, tell that to the user. If not, print a different appropriate message.

'''

while True:
    try:
        number = int(input("Please enter a number : "))
    except Exception as excObject:
        print(excObject)
    else:
        break

if(number % 4 == 0):
    print(f"You have entered {number}.It is multiple of 4")
else:
    if(number % 2 == 0):
        print(f"You have entered {number}.It is an even number.")
    else:
        print(f"You have entered {number}.It is an odd number.")

while True:
    try:
        number = int(input("Please enter a number : "))
    except Exception as excObject:
        print(excObject)
    else:
        break

while True:
    try:
        check = int(input("Please enter a number : "))
        if(check == 0):
            raise Exception("Please enter something else than 0")
        
    except Exception as excObject:
        print(excObject)
    else:
        break

if(number % check == 0):
    print(f"{number} can be divided evenly to {check}")
else:
    print(f"{number} can NOT be divided evenly to {check}")

