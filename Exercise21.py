'''
Take the code from the How To Decode A Website exercise 
(if you didn’t do it or just want to play with some different code, use the code from the solution),
and instead of printing the results to a screen, write the results to a txt file. In your code, 
just make up a name for the file you are saving to.

Extras:

Ask the user to specify the name of the output file that will be saved.

'''

import random

fileName = input("Please enter the file name : ")

number_list = [random.randrange(1, 100, 1) for i in range(10)]
number_list_str = [ str(item) for item in number_list]
print(number_list_str)

with open(fileName,"w") as file:
    for item in number_list_str:
        file.write(item+' ')
    file.close()


