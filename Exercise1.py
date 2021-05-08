'''
    Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''

import re

while True:
    try:
        name = input("Please enter your name : ")
        if(not name.isalpha()):
            raise Exception("Please enter a valid name.")
    except Exception as excObject:
        print(excObject)
    else:
        break

while True:
    try:
        age = int(input("Please enter your age : "))
    except Exception as excObject:
        print("Not a valid age.")
    else:
        break
    
whenHundred = (100 - age) + 2021

message = f"Hello {name}.You will turn 100 years old in {whenHundred}"

print(message)

while True:
    try:
        number = int(input("Please enter a number : "))
    except Exception as excObject:
        print("Please enter a numerical character.")
    else:
        break

for item in range(1,number+1):
    print(message)
        