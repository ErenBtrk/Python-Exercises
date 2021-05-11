'''
    Given a .txt file that has a list of a bunch of names, 
    count how many of each name there are in the file, 
    and print out the results to the screen. 

Extra:

    Instead of using the .txt file from above (or instead of, if you want the challenge),
    
    
'''

counter_dict = {}
with open('example.txt') as f:
	line = f.readline()
	while line:
		line = line.strip()
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()
 

print(counter_dict)
dict2 = {}
string = "Bat"
if string in dict2:
    dict2[string] += 1
else:
    dict2[string] = 1

print(dict2)

dict2["Apple"] = 1
dict2["Pear"] = 0

print(dict2)