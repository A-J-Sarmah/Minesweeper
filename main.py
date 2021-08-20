import random

print("\n************Minesweeper************\n")

MINE = []
NUMBER_NEAR_MINE = []
DISPLAY_DATA = []
IS_WON = False
IS_PLAYING = True
FIRST_INPUT = 0


# drawing the game board
def drawboard(data):
    NO_OF_COLUMN = 8
    for i in range(NO_OF_COLUMN):
        # checks if we are currently executing first column.
        if 0 == i:
            # renders list of number in first column.
            for j in range(NO_OF_COLUMN):
                if j == 7:
                    print(" \033[1m" + str(j) + " \033[0m")
                else:
                    print(" \033[1m" + str(j) + " \033[0m", end="")
        else:
            # renders all other column
            for j in range(NO_OF_COLUMN):
                elementFound = False
                if j == 0:
                    print(" \033[1m" + str(i) + " \033[0m", end="")
                else:
                    for element in data:
                        COORDINATES = drawCharacters(element)
                        COORDINATE_X = COORDINATES[0]
                        COORDINATE_Y = COORDINATES[1]
                        if i == COORDINATE_X and j == COORDINATE_Y:
                            elementFound = True
                            break
                    if elementFound:
                        BOMB_DATA = printNumberNearBomb(element)
                        if j == 7:
                            print(" " + BOMB_DATA + " ")
                        else:
                            print(" " + BOMB_DATA + " ", end="")
                    if not elementFound:
                        BOMB_DATA = "-"
                        if j == 7:
                            print(" " + BOMB_DATA + " ")
                        else:
                            print(" " + BOMB_DATA + " ", end="")


# drawing numbers and character in game board which are provided as input by the user.
def drawCharacters(number):
    COORDINATES_OF_NUMBER = [int(x) for x in str(number)]
    return COORDINATES_OF_NUMBER


# generates mine in random positions
def generateMine():
    TOTAL_MINE_CREATED = 0
    # the loop that continues until 10 mines are generated
    while TOTAL_MINE_CREATED <= 10:
        RANDOM_NUMBER = random.randint(11, 77)
        if RANDOM_NUMBER in MINE:
            TOTAL_MINE_CREATED = TOTAL_MINE_CREATED
        elif RANDOM_NUMBER % 10 == 0:
            TOTAL_MINE_CREATED = TOTAL_MINE_CREATED
        elif RANDOM_NUMBER == FIRST_INPUT:
            TOTAL_MINE_CREATED = TOTAL_MINE_CREATED
        else:
            TOTAL_MINE_CREATED = TOTAL_MINE_CREATED + 1
            MINE.append(RANDOM_NUMBER)


# generate number near the mines
def generateNumberNearMine(mine):
    for i in mine:
        # checks if current index is last index in column
        isLastNumber = i - 17
        if isLastNumber == 0 or isLastNumber % 10 == 0:
            indexes = [i - 1, i + 10, i - 10, i + 9, i - 9]
            for j in indexes:
                if 11 <= j <= 77:
                    NUMBER_NEAR_MINE.append(j)
        # default case
        indexes = [i - 1, i + 1, i + 10, i - 10, i + 9, i - 9, i + 11, i - 11]
        for j in indexes:
            if 11 <= j <= 77 and j % 10 != 0 and j % 10 != 8 and j % 10 != 9 and j not in MINE:
                NUMBER_NEAR_MINE.append(j)


# the opening of the game is marked by this function
def openGame():
    NUMBER_OF_REVEALED_BOXES = round(len(NUMBER_NEAR_MINE) / 2)
    index = 0
    while index < NUMBER_OF_REVEALED_BOXES:
        RANDOM_NUMBER = random.choice(NUMBER_NEAR_MINE)
        DISPLAY_DATA.append(RANDOM_NUMBER)
        index = index + 1


# function to determine the BOMB_DATA
def printNumberNearBomb(number):
    output = 0
    for element in DISPLAY_DATA:
        if number == element:
            output = output + 1
    return str(output)


# check win
def checkWin():
    global IS_PLAYING
    for element in DISPLAY_DATA:
        if element in MINE:
            print(element)
            IS_PLAYING = False
            return
    if len(DISPLAY_DATA) + len(MINE) == 49:
        global IS_WON
        IS_WON = True
        IS_PLAYING = False


# handle user input
def validateUserInputAndActions():
    INPUT = ""
    while True:
        try:
            INPUT = int(input("Please Enter the index where you want to insert the element."))
            if 11 <= INPUT <= 77 and INPUT % 10 != 0 and INPUT % 10 != 8 and INPUT % 10 != 9:
                break
            else:
                print("Please enter a valid index")
                continue
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    global FIRST_INPUT
    FIRST_INPUT = INPUT
    DISPLAY_DATA.append(INPUT)
    checkWin()


RENDER = 0
while IS_PLAYING:
    if RENDER == 0:
        validateUserInputAndActions()
        generateMine()
        generateNumberNearMine(MINE)
        openGame()
        drawboard(DISPLAY_DATA)
    else:
        validateUserInputAndActions()
        drawboard(DISPLAY_DATA)
    RENDER = RENDER + 1
    print(MINE)
    print(DISPLAY_DATA)


if not IS_PLAYING and IS_WON:
    print("Congrats!You won")
else:
    print("You Lost")
