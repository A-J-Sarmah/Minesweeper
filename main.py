import random

print("\n************Minesweeper************\n")

MINE = []
NUMBER_NEAR_MINE = []
DISPLAY_DATA = []


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
            if 11 <= j <= 77 and j % 10 != 0 and j % 10 != 8 and j % 10 != 9:
                NUMBER_NEAR_MINE.append(j)


# the opening of the game is marked by this function
def openGame():
    NUMBER_OF_REVEALED_BOXES = round(len(NUMBER_NEAR_MINE) / 2)
    index = 0
    while index < NUMBER_OF_REVEALED_BOXES:
        RANDOM_NUMBER = random.choice(NUMBER_NEAR_MINE)
        DISPLAY_DATA.append(RANDOM_NUMBER)
        index = index + 1


# detecting STORE_DATA
def printNumberNearBomb(number):
    output = 0
    for element in DISPLAY_DATA:
        if number == element:
            output = output + 1
    return str(output)


generateMine()
generateNumberNearMine(MINE)
openGame()
drawboard(DISPLAY_DATA)
print(DISPLAY_DATA)
