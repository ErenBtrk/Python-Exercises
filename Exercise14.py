'''
Write a program (function!) that takes a list and returns a new list that contains all the elements of the 
first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.

'''

def function(listArg):
    new_list = []
    for item in listArg:
        if(not item in new_list):
            new_list.append(item)
    return new_list

list1 = [1,10,2,2,5,8,4,11,8,42,10,1]

new_list = function(list1)

print(new_list)

###############################################################

list2 = [2,2,1,1,1,3,5,10,21,31,41,21,41,31,41]

def function2(listArg): 
    return set(listArg)

new_list2 = function(list2)

print(new_list2)