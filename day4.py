#!/usr/bin/python
import sys

input = sys.stdin.readlines()
draw_num = input[0]
toCheck = list()
print(draw_num)

def checkHorizontal(puzzle):
    for i in range(0, len(puzzle)):
        print(">>>>", puzzle[i])

def checkBoard(toCheck, boardToCheck):
    checkHorizontal(toCheck, boardToCheck)
    #checkVertical()
    #checkDiagonal()

def getBoard(startLine, puzzleList):
    boardToCheck = list()
    for i in range(startLine, startLine + 5):
        boardToCheck.append(puzzleList[i])
    return boardToCheck

puzzleList = input[2:]
i = 0
startLine = 0
while i < len(draw_num):
    if i < 5:
        toCheck.append(draw_num[i])
        continue
    else:
        boardToCheck = getBoard(startLine, puzzleList)
        checkBoard(toCheck, boardToCheck)
    i += 1
