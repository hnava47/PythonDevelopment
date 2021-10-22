graphics = (5 * "_", 4 * " " + "0", 4 * " " + "|", 3 * " " +"/|", "\\", 4 * " " + "|", 3 * " " + "/", "\\")

def initGame(word, guessCount):
    gameState = {"Word" : word.lower(), "Word so far" : len(word) * "_",
    "Remaining guesses" : guessCount, "Guessed letters" : set(), "Wrong guess count" : 0}

    return gameState

def displayGame(state):
    drawPerson(state)
    print(2 * "\n")
    print(f'Word so far: {state["Word so far"]}')
    print(f'Guessed letters so far: {", ".join(state["Guessed letters"])}')
    print(f'Remaining guesses:{state["Remaining guesses"]}')


def drawPerson(state):
    for i in range(min(len(graphics), state["Wrong guess count"])):
        if i in (3, 6):
            print(graphics[i], end = "")
        else:
            print(graphics[i])

def runOneTurn(state):
    letter = input("Next letter? ").lower()

    #Letter has been guessed before
    if letter in state["Guessed letters"]:
        print("You have already made this guess!")
        return False
    else:
        state["Guessed letters"].add(letter)
    #Letter is in the word
    if letter in state["Word"]:
        modifyWordSoFar(state, letter)
        if "_" not in state["Word so far"]:
            print("You have won!")
            return True
        return False
    print("Wrong guess!")
    state["Wrong guess count"] += 1
    state["Remaining guesses"] -= 1

    if state["Remaining guesses"] == 0:
        print("You lost!!")
        return True
    return False

def modifyWordSoFar(state, letter):
    index = -1
    while True:
        index = state["Word"].find(letter, index+1)
        if index == -1:
            return
        state["Word so far"] = state["Word so far"][0:index] + letter + state["Word so far"][index+1:]

def runGame():
    gameState = initGame("Hangman", 9)
    while not runOneTurn(gameState):
        displayGame(gameState)

runGame()
