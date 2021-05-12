'''
    take this .txt file, and count how many of each “category” of each image there are. 
    This text file is actually a list of files corresponding to the SUN database scene 
    recognition database, and lists the file directory hierarchy for the images. 
    Once you take a look at the first line or two of the file, it will be clear which
    part represents the scene category. To do this, you’re going to have to remember
    a bit about string parsing in Python 3. I talked a little bit about it in this post.
'''

dict1 = {}
dict2 = {}
count = 0

with open("images.txt") as file:
    line = file.readline()
    while line:
        count += 1
        str_list = line.strip().split('/')
        #print(str_list)
        #print(line)
        if(str_list[1] in dict1):
            dict1[str_list[1]] += 1
        else:
            dict1[str_list[1]] = 1
        line = file.readline()
        if(str_list[2] in dict2):
            dict2[str_list[2]] += 1
        else:
            dict2[str_list[2]] = 1
print(dict1)
print(dict2)