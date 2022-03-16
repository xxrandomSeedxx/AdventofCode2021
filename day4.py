#!/usr/bin/python
import sys

input = sys.stdin.readlines()
draw_num = input[0].split(",")


def checkHorizontal(toCheck, puzzleLines):
    for i in range(0, len(puzzleLines)):
        line = puzzleLines[i]
        count = 0
        for digit in toCheck:
            if digit not in line:
                break
            else:
                count += 1
        print("Horz Line {} match count: {}".format(i, count))
        if count == 5:
            return True
        else:
            continue
    return False


def checkVertical(toCheck, puzzleLines):
    for i in range(0, 5):
        vertLine = list()
        count = 0
        for j in range(0, len(puzzleLines)):
            vertLine.append(puzzleLines[j][i])

        for digit in toCheck:
            if digit not in vertLine:
                break
            else:
                count += 1
        print("Vert ine {} match count: {}".format(i, count))
        if count == 5:
            return True
        else:
            continue
    return False


def checkDiagonal():



def checkBoard(toCheck, boardToCheck):
    gotMatch = None
    gotMatch = checkHorizontal(toCheck, boardToCheck)
    if not gotMatch:
        gotMatch = checkVertical(toCheck, boardToCheck)
    if not gotMatch:
        gotMatch = checkDiagonal(toCheck, boardToCheck)
    else:
        print("Match >>>>>>>>>>>>>>")


def getBoard(puzzleStartLine, puzzleList):
    boardToCheck = list()
    for i in range(puzzleStartLine, puzzleStartLine + 5):
        try:
            boardToCheck.append(puzzleList[i])
        except IndexError:
            pass
    return boardToCheck

puzzleList = input[2:]
i = 0
puzzleStartLine = 0
toCheck = list()

while i < len(draw_num):
    print("Draw: ", draw_num[i])
    if i == 0 or i % 5 != 0:
        toCheck.append(draw_num[i])
        i += 1
    else:
        print("Start line: ", puzzleStartLine)
        boardToCheck = getBoard(puzzleStartLine, puzzleList)
        print("Digits to check:", toCheck)
        print("Board to check: \n", boardToCheck)
        checkBoard(toCheck, boardToCheck)
        puzzleStartLine += 6

        toCheck = [draw_num[i]]  # reset digits to check after every five lines
        i += 1
