'''
This exercise is Part 1 of 4 of the birthday data exercise series. 
The other exercises are: Part 2, Part 3, and Part 4.

For this exercise, we will keep track of when our friend’s birthdays are,
and be able to find that information based on their name. 
Create a dictionary (in your file) of names and birthdays.
When you run your program it should ask the user to enter a name,
and return the birthday of that person back to them. 
The interaction should look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.
Happy coding!

'''

import time

birthdays = {}
count = 0
doExit = False

while True:
    count += 1
    print(f"Please enter {count}.information : ")
    while True:
        try:
            name = input("Please enter a name : ")
            if(not name.isalpha()):
                raise Exception("Please enter a valid name.")
        except Exception as excObject:
            print(excObject)
        else:
            break
    if(name == 'exit'):
        print("Quitting.")
        time.sleep(2)
        break 
    
    while True:
        try:
            day = input("Please enter the day : ")
            if(not day.isdigit()):
                raise Exception("Please enter a valid day.")
            else:
                if(int(day) <= 0 or int(day) > 31):
                    raise Exception("Day must be between 1-31.")
        except Exception as excObject:
            print(excObject)
        else:
            break
    
    while True:
        try:
            month = input("Please enter the month : ")
            if(not month.isdigit()):
                raise Exception("Please enter a valid month.") 
            else:
                if(int(month) <= 0 or int(month) > 12):
                    raise Exception("Month must be between 1-12.")
        except Exception as excObject:
            print(excObject)
        else:
            break
    
    while True:
        try:
            year = input("Please enter the year : ")
            if(not year.isdigit()):
                raise Exception("Please enter a valid year.") 
            else:
                if(len(year) != 4):
                    raise Exception("Invalid year length.")
        except Exception as excObject:
            print(excObject)
        else:
            break
    birthdays.update({
        name : day + '/'+ month + '/' + year
    })  
    time.sleep(2)  
    
        
nameInput = input("Please enter a name to display information about birthday : ")
if(nameInput in birthdays):
    print(birthdays[nameInput])              
else:
    print("No information is found.")

