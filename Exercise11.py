'''
 Ask the user for a number and determine whether the number is prime or not.
 (For those who have forgotten, a prime number is a number that has no divisors.). 
 You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity 
 to practice using functions,described below.

 '''
def isNumberPrime(number):
    isPrime = True
    if(number == 0 or number == 1):
        return False
    for item in range(2,number):
        if(number % item == 0):
            isPrime = False
            break
    return isPrime

while True: 
    try:
        number = int(input("Please enter a number : "))
    except Exception as excObject:
        print(excObject)
    else:
        if(isNumberPrime(number)):
            print(f"The number({number}) you have entered is a prime number.")
        else:
            print(f"The number({number}) you have entered is NOT a prime number.")
        break

