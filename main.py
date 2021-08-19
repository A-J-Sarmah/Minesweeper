import random

print("\n************minesweeper************\n")

mine = []


# drawing the game board
def drawboard():
    NO_OF_COLUMN = 8
    COORDINATES = drawCharacters(17)
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
                        print("   ")
                    else:
                        print("   ", end="")
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


def generateMine():
    TOTAL_MINE_CREATED = 0
    while TOTAL_MINE_CREATED <= 8:
        RANDOM_NUMBER = random.randint(11, 77)
        if RANDOM_NUMBER in mine:
            TOTAL_MINE_CREATED = TOTAL_MINE_CREATED
        else:
            TOTAL_MINE_CREATED = TOTAL_MINE_CREATED + 1
            mine.append(RANDOM_NUMBER)


drawboard()
generateMine()
print(mine)
