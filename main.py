import random

print("\n************Minesweeper************\n")

MINE = []
NUMBER_NEAR_MINE = []
USER_DATA = "X"


# drawing the game board
def drawboard(number):
    NO_OF_COLUMN = 8
    COORDINATES = drawCharacters(number)
    COORDINATE_X = COORDINATES[0]
    COORDINATE_Y = COORDINATES[1]
    for i in range(NO_OF_COLUMN):
        # checks if we are currently executing first column.
        if 0 == i:
            # renders list of number in first column.
            for j in range(NO_OF_COLUMN):
                if j == 7:
                    print(" " + str(j) + " ")
                else:
                    print(" " + str(j) + " ", end="")
        # checks if we are dealing with x coordinate
        elif COORDINATE_X == i:
            # renders all other column
            for j in range(NO_OF_COLUMN):
                # the first cell representing the row number of the board.
                if j == 0:
                    print(" " + str(i) + " ", end="")
                # checks if we are dealing with second digit of number
                elif j == COORDINATE_Y:
                    if j == 7:
                        print(" " + str(USER_DATA) + " ")
                    else:
                        print(" " + str(USER_DATA) + " ", end="")
                # checks if we are dealing with the last digit.
                elif j == 7:
                    print(" - ")
                # draws required number for remaining cell .
                else:
                    print(" - ", end="")
        else:
            # renders all other column
            for j in range(NO_OF_COLUMN):
                # the first cell representing the row number of the board.
                if j == 0:
                    print(" " + str(i) + " ", end="")
                # checks if we are dealing with the last digit.
                elif j == 7:
                    print(" - ")
                # draws required number for remaining cell .
                else:
                    print(" - ", end="")


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
    numbers = []
    for i in mine:
        # checks if current index is last index in column
        isLastNumber = i - 17
        if isLastNumber == 0 or isLastNumber % 10 == 0:
            indexes = [i - 1, i + 10, i - 10, i + 9, i - 9]
            for j in indexes:
                if 11 <= j <= 77:
                    NUMBER_NEAR_MINE.append(j)
        # default case
        indexes = [i - 1, i + 1, i + 10, i - 10, i + 9, i - 9,  i+11, i-11]
        for j in indexes:
            if 11 <= j <= 77 and j % 10 != 0:
                NUMBER_NEAR_MINE.append(j)


drawboard(45)
generateMine()
generateNumberNearMine(MINE)
print(MINE)
print(NUMBER_NEAR_MINE)