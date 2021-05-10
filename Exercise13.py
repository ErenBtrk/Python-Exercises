'''
Write a program that asks the user how many Fibonnaci numbers to generate
and then generates them. Take this opportunity to think about how you can
use functions. Make sure to ask the user to enter the number of numbers
in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence
of numbers where the next number in the sequence is the sum of the
previous two numbers in the sequence. 
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …
'''

def generateFibNums(number):
    new_list = []
    a = 1
    b = 1
    c = 0
    for item in range(0,number):
        new_list.append(a)
        c = a+b
        a = b
        b = c

    return new_list

while True:
    try:
        howMany = int(input("Please enter how many Fibonacci numbers you want to generate : "))
    except Exception as excObject:
        print(excObject)
    else:
        new_list = generateFibNums(howMany)
        print(new_list)
        break