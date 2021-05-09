'''
    Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
    compare them, print out a message of congratulations to the winner, and ask if the players 
    want to start a new game)

    Remember the rules:

    1-Rock beats scissors
    2-Scissors beats paper
    3-Paper beats rock
'''
def game():
    while True:
        try:
            player1 = input('PLAYER 1 - Please enter one of these ("Rock"-"Paper"-"Scissors") : ').lower().strip().replace(' ','')
            if(player1 != "rock" and player1 != "paper" and player1 != "scissors"):
                raise Exception("Invalid input.")
        except Exception as excObject:
            print(excObject)
        else:
            break

    while True:
        try:
            player2 = input('PLAYER 2 - Please enter one of these ("Rock"-"Paper"-"Scissors") : ').lower().strip().replace(' ','')
            if(player2 != "rock" and player2 != "paper" and player2 != "scissors"):
                    raise Exception("Invalid input.")
        except Exception as excObject:
                print(excObject)
        else:
            break

    if(player1 == "rock" and player2 == "paper") or (player1 == "paper" and player2 == "scissors") or (player1 == "scissors" and player2 == "rock"):
        print("PLAYER 2 WINS!!!!")
    elif(player1 == "rock" and player2 == "scissors") or (player1 == "paper" and player2 == "rock") or (player1 == "scissors" and player2 == "paper"):
        print("PLAYER 1 WINS!!!")
    elif(player1 == player2):
        print("DRAW!")



while True:
    game()
    while True:
        try:
            choice = input('Please enter "Y" to play again , "N" to Exit Game : ').lower().strip().replace(' ','')
            if(choice != 'n' and choice != 'y'):
                raise Exception("Invalid input.")
        except Exception as excObject:
            print(excObject)
        else:
            break
    if(choice == 'n'):
        print("Quitting Game.")
        break
    else:
        print("Starting a New Game ...")


    


