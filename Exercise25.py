'''
 EXERCISE 24-26-27-29
 This exercise is Part 1 of 4 of the Tic Tac Toe exercise series.
 The other exercises are: Part 2, Part 3, and Part 4.

 Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
 This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes
 (8x8 for chess, 19x19 for Go, and many more).

 Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

 Remember that in Python 3, printing to the screen is accomplished by

  print("Thing to show on screen")
 Hint: this requires some use of functions, as were discussed previously on
 this blog and elsewhere on the Internet, like this TutorialsPoint link.
 
 '''
# while True:
#     try:
#         size = int(input("Please enter the size of game board you want to create : "))
#         if(size>50 or size<0):
#             raise Exception("Please enter a valid size.")
#     except Exception as excObject:
#         print(excObject)
#     else:
#         break

# with open("deneme.txt","w") as file:
#     for item in range(size*2+1):
#         if(item % 2 == 0):
#             file.write((' ' + '-'*3) *size +'\n')
#         elif(item % 2 == 1):
#             file.write(('|' + ' '*3)*size + '|' +'\n')

################################################################################################################

def createGameboard(size):
    string1 = list((" ---") *size )
    string2 = list(('|' + ' '*3)*size + '|' )
    return [ string1.copy() if x % 2 == 0  else string2.copy()  for x in range(size*2+1)]

################################################################################################################

def setupGameboardSize():
    while True:
        try:
            size = int(input("Please enter the size of game board you want to create : "))
            if(size>50 or size<0):
                raise Exception("Please enter a valid size.")
        except Exception as excObject:
            print(excObject)
        else:
            return size

################################################################################################################

def checkGameboard(gameBoard,size,char):
    for index in range(size):
        flag = True
        for index2 in range(size):
            newIndex = (index)*2 + 1
            newIndex2 = (index2)*4 + 2
            if(gameBoard[newIndex][newIndex2] != char):
                flag = False
                break
        if(flag):
            return flag

    
    for index2 in range(size):
        flag = True
        for index in range(size):
            newIndex = (index)*2 + 1
            newIndex2 = (index2)*4 + 2
            if(gameBoard[newIndex][newIndex2] != char):
                flag = False
                break
        if(flag):
            return flag

    flag = True
    for index in range(size):
        for index2 in range(size):
            if(index == index2):
                newIndex = (index)*2 + 1
                newIndex2 = (index2)*4 + 2
                if(gameBoard[newIndex][newIndex2] != char):
                    flag = False
                    break
    if(flag):
        return flag

    flag = True
    for index in range(size):
        for index2 in range(size):
            if(index + index2 == size-1):
                newIndex = (index)*2 + 1
                newIndex2 = (index2)*4 + 2
                if(gameBoard[newIndex][newIndex2] != char):
                    flag = False
                    break
    if(flag):
        return flag
    
################################################################################################################

def askForRowColumn(gameBoard):
    rowColumn = []
    while True:
        try:
            rowInput = int(input("Please enter row  : "))
            columnInput = int(input ( "Please enter column : "))
            if(rowInput > size) or (columnInput > size):
                raise Exception("Invalid row or column.")
            else:
                rowInput = (rowInput-1)*2 + 1
                columnInput = (columnInput-1)*4 + 2
            if(gameBoard[rowInput][columnInput] == 'X' or gameBoard[rowInput][columnInput] == 'O'):
                raise Exception("Player already moved here.Please enter different row and column.")
        except Exception as excObject:
            print(excObject)
        else:
            rowColumn.append(rowInput)
            rowColumn.append(columnInput)
            return rowColumn

################################################################################################################

def drawXO(gameBoard,count,rowInput,columnInput):
    for index in range(len(gameBoard)):
        if(index == rowInput and (gameBoard[index][columnInput] != 'X' and gameBoard[index][columnInput] != 'O')):
            if(count % 2):
                gameBoard[index][columnInput] = 'X'
            else:
                gameBoard[index][columnInput] = 'O'
            break

################################################################################################################

def drawGameboard(gameBoard):
    for item in gameBoard:
        str1 = ''.join(item)
        print(str1)

################################################################################################################

size = setupGameboardSize()
gameBoard = createGameboard(size)

count = 0

while True:
    if(count == size**2):
        break
    count += 1
    if(count % 2 == 0):
        print("*** PLAYER-2 ***")
    else:
        print("*** PLAYER-1 ***")
    
    rowAndColumnList = askForRowColumn(gameBoard)
    
    rowInput = rowAndColumnList[0]
    columnInput = rowAndColumnList[1]
    
    drawXO(gameBoard,count,rowInput,columnInput)

    drawGameboard(gameBoard)

    if(count % 2 == 0):
        if(checkGameboard(gameBoard,size,'O')):
            print("PLAYER 2 WINS")
            break
    else:
        if(checkGameboard(gameBoard,size,'X')):
            print("PLAYER 1 WINS")
            break

    if(count == size**2):
        print("TIE")
        break

    



