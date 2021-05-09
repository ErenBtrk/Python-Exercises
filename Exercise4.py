'''
    Create a program that asks the user for a number and then prints out a list of all the divisors
    of that number. (If you don’t know what a divisor is, it is a number that divides evenly into
    another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

while True:
    try:
        number = int(input("Please enter a number : "))
    except Exception as excObject:
        print(excObject)
    else:
        break

divisor_list = []

for item in range(2,number):
    if(number % item == 0):
        divisor_list.append(item)
    
print(divisor_list)