import numpy as np
import random
from simanneal import Annealer

sudokuGrid = [[0, 3, 9, 5, 7, 4, 1, 8, 2],
              [5, 4, 1, 8, 2, 9, 3, 7, 6],
              [7, 8, 2, 6, 1, 3, 9, 5, 4],
              [1, 9, 8, 4, 6, 7, 5, 2, 3],
              [3, 6, 5, 9, 8, 2, 4, 1, 7],
              [4, 2, 7, 1, 3, 5, 8, 6, 9],
              [9, 5, 6, 7, 4, 8, 2, 3, 1],
              [8, 1, 3, 2, 9, 6, 7, 4, 5],
              [2, 7, 4, 3, 5, 1, 6, 9, 8]]
def getCol(i, grid):
    return [row[i] for row in grid]

def printGrid(grid):
    print()
    endStr = " "
    for i in range(9):
        for j in range(9):
            if (j % 3 == 2):
                endStr = "  "
            else:
                endStr = " "
            print(grid[i][j], end = endStr)
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

validRowCol = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def isWinCondition(grid):
    ## Check Rows
    for row in grid:
        if sorted(row) != validRowCol:
            return False
    
    ## Check Cols
    for i in range(9):
        if (sorted(getCol(i, grid)) != validRowCol):
            return False
        
    ## Check 3x3s
    for row in range(0, 9, 3):
        for column in range(0, 9, 3):
            line = (grid[row][column:column+3]
                + grid[row+1][column:column+3]
                + grid[row+2][column:column+3])
            if sorted(line) != validRowCol:
                return False
    return True

def generateRandomSolution():
    solution = []
    for i in range(9):
        solutionRow = []
        row = sudokuGrid[i]
        missingNumbers = [n for n in range(1, 10) if n not in row]
        random.shuffle(missingNumbers)
        solutionRow.extend([n or missingNumbers.pop() for n in row])
        solution.append(solutionRow)
    return solution

printGrid(sudokuGrid)
print(isWinCondition(sudokuGrid))
possibleSolution = generateRandomSolution()
printGrid(possibleSolution)
print(isWinCondition(possibleSolution))