'''
  Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
  and write a program that returns a list that contains only the elements that are common between the lists
  (without duplicates). Make sure your program works on two lists of different sizes.

 Extras:

 1-Randomly generate two lists to test this
 2-Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new_list = []

for item in a:
    if(not item in new_list):
        new_list.append(item)

for item in b:
    if(not item in new_list):
        new_list.append(item)

new_list.sort()
print(new_list)

################################################################

import random

randomList = range(30)
list1 = random.sample(randomList,random.randint(5,20))
list2 = random.sample(randomList,random.randint(5,20))

print(list1)
print(list2)

new_list2 = []

for item in list1:
    if(not item in new_list2):
        new_list2.append(item)

for item in list2:
    if(not item in new_list2):
        new_list2.append(item)

new_list2.sort()
print(new_list2)












