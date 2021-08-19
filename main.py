print("************minesweeper************")


# drawing the game board
def drawboard():
    NO_OF_COLUMN = 8
    for i in range(NO_OF_COLUMN):
        # checks if we are currently executing first column.
        if 0 == i:
            # renders list of number in first column.
            for j in range(NO_OF_COLUMN):
                if j == 7:
                    print(" " + str(j) + " ")
                else:
                    print(" " + str(j) + " ", end="")
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


drawboard()
