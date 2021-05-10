'''
    Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list
     of only the first and last elements of the given list. For practice, write this code inside a function.

'''
def function(numberList):
    newList = []
    newList.append(numberList[0])
    newList.append(numberList[-1])
    return newList

a = [5, 10, 15, 20, 25]

newList = function(a)
print(newList)
