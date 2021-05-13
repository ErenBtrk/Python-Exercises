'''
Implement a function that takes as input three variables, and returns the largest of the three.
Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python normally takes care of for us. 
All you need is some variables and if statements!

'''

def function(x,y,z):
    if(x>y):
        if(x>z):
            return x
    if(y>x):
        if(y>z):
            return y 
    if(z>x):
        if(z>y):
            return z


number1 = int(input("Please enter a number : "))
number2 = int(input("Please enter a number : "))
number3 = int(input("Please enter a number : "))

print(f"Largest is {function(number1,number2,number3)}")