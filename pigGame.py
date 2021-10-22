import random

def printInstructions():
    print("""Welcome to PIG... Here are the rules:
    1) Each player starts with a score of 0
    2) At your turn you roll a die
    3) If you roll anything other than 1, it is added to your turn score
    4) Then you get to choose to roll again or stop
    5) If you stop then your turn score is added to your game score
    6) If you choose to keep rolling, you can increase your score
    7) Any time you roll a 1, your turn ends and you lose the turn score
    8) First player to 100 wins""")

#Pass the total score for the current Player
#Return the total score for the turn
def runOneTurn(totalScore):
    turnScore = 0
    while True:
        #Rolling die
        dieOutcome = random.randint(1, 6)

        #Check if the turn ends with a roll of 1
        if dieOutcome == 1:
            print("You rolled 1. Your turn ends and you lose your turn's score")
            return 0
        #Handling all other rolls
        else:
            #Update turn score
            turnScore += dieOutcome
            print("You rolled: ", dieOutcome)
            print("Your current score: ", turnScore)

            #Check if game ended
            if turnScore + totalScore >= 100:
                return turnScore

            #Give the player the choice to roll or hold
            choice = input("Roll or hold? (r, h)")
            if choice.lower() == "h":
                return turnScore

def runGame():
    #variables to store the scores for each player
    p1Score = 0
    p2Score = 0

    #keeps track of whose turn
    currentPlayer = 1
    while True:
        print("Player", currentPlayer, "'s turn")
        #run player 1's turn
        if currentPlayer == 1:
            p1Score += runOneTurn(p1Score)
            print("Total Score for player 1:", p1Score, "\n\n")
            currentPlayer = 2
        #run player 2's turn
        else:
            p2Score += runOneTurn(p2Score)
            print("Total Score for player 2:", p2Score, "\n\n")
            currentPlayer = 1
        #check if game is over
        if p1Score >= 100:
            print("Player 1 wins!")
            return
        elif p2Score >= 100:
            print("Player 2 wins!")
            return

printInstructions()
runGame()
