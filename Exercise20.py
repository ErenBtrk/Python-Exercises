'''
  Write a function that takes an ordered list of numbers (a list where the elements are
  in order from smallest to largest) and another number. The function decides whether or
  not the given number is inside the list and returns (then prints) an appropriate boolean.

  Extras:

  Use binary search.
'''
import random

def function(argList,number):
    min = 0
    max = len(argList)-1
    
    while( min <= max ):
      mid = (min + max) // 2 
      if(number == argList[mid]):
        return mid
      elif(number > argList[mid]):
        min = mid + 1
      else:
        max = mid - 1

    return -1


list = [random.randrange(1, 50, 1) for i in range(7)]
list.sort()
print(list)
number = int(input("Please enter a number to see if it is in the list : "))

index = function(list,number)
if( index >= 0):
  print(f"The number({number}) you have entered is found at {index} index.")
else:
  print(f"The number({number}) you have entered is NOT found in the list.")
