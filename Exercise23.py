'''
 Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
 One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of 
 happy numbers up to 1000.
 
 (If you forgot, prime numbers are numbers that can’t be divided by any other number.
 And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia.
 The explanation is easier with an example, which I will describe below.)
'''

with open("happy.txt") as happyFile:
    happyLine = happyFile.readline()
    happyList = []
    while happyLine:
        happyList.append(happyLine.strip())
        happyLine = happyFile.readline()

happyFile.close()
            
with open("prime.txt") as primeFile:
    primeLine = primeFile.readline()
    primeList = []
    while primeLine:
        primeList.append(primeLine.strip())
        primeLine = primeFile.readline()

primeFile.close()

for item in happyList:
    if(item in primeList):
        print(item)



