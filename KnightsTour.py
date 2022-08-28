# User Input translated to size of chessboard

dimensionOfChessboard = (int(input("Input a number to act as the squared dimensions for the chessboard \n(standard chessboard's are 8x8): ")))

#variable for the chessboard. 
boardSize = (dimensionOfChessboard) 

# Chessboard - checking spaces to make sure they can be traveled to
def checkSpace(x, y, fillChessboard):
    if (x >= 1 and x <= boardSize and y >= 1 and y <= boardSize):
        if (fillChessboard[x][y] == -1):
            return True
    return False

def theKnightsTour(fillChessboard, x, y, moveCounter, xM, yM):
    if moveCounter == ((boardSize)*(boardSize)):
        return True
    for i in range(0, 8):
        step_x = (x + xM[i])
        step_y = (y + yM[i])
        if( checkSpace( step_x, step_y, fillChessboard )):
            fillChessboard[step_x][step_y] = moveCounter
            if ( theKnightsTour( fillChessboard, step_x, step_y, (moveCounter + 1), xM, yM )):
                return True
            fillChessboard[step_x][step_y] = -1
    return False

def RunProgramTheKnightsTour():
    # Starting Position - empty 'chessboard'
    fillChessboard = []
    # Each possible move for the x and y variables.
    # Their position matches the opposite variables position according to respective lists
    xM = [2, 1, -1, -2, -2, -1, 1, 2]
    yM = [1, 2, 2, 1, -1, -2, -2, -1]
    for index in range(0, boardSize + 1):
        spotFill = [0] + ([-1] * boardSize)
        fillChessboard.append(spotFill)
    fillChessboard[1][1] = 0
    if (theKnightsTour( fillChessboard, 1, 1, 1, xM, yM)):
        for x in range(1, boardSize + 1):
            print(fillChessboard[x][1:])
        return True, print("Successful Tour!")
    return False

if __name__ == '__main__':
    print(RunProgramTheKnightsTour())