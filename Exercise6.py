'''
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
'''

userString = input("Please enter a string : ")
listString = list(userString)
reversedString = list(userString)
reversedString.reverse()
print(listString)
print(reversedString)
if(reversedString == listString):
    print(f"{userString} is a palindrome.")
else:
    print(f"{userString} is NOT palindrome.")

################################################################

userString = input("Please enter a string : ")
new_list1 = list(userString)
new_list2 = []
for item in userString:
    new_list2.insert(0,item)

if(new_list1 == new_list2):
    print(f"{userString} is a palindrome.")
else:
    print(f"{userString} is NOT palindrome.")




