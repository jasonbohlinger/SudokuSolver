sudokuGrid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]

def printGrid():
    print()
    endStr = " "
    for i in range(9):
        for j in range(9):
            if (j % 3 == 2):
                endStr = "  "
            else:
                endStr = " "
            print(sudokuGrid[i][j], end = endStr)
        print()
        if (i % 3 == 2):
            print()

def getGridFromUser():
    for i in range(9):
        print("Row " + str(i + 1) + ": ", end = "")
        rowStr = str(input())
        if (len(rowStr) != 9):
            print("Invalid input row")
            break

        for j in range(9):
            sudokuGrid[i][j] = int(rowStr[j])

printGrid()
getGridFromUser()
printGrid()