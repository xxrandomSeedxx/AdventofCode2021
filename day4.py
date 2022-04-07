#!/usr/bin/python
import sys

input = sys.stdin.readlines()
draw_num = input[0].split(",")


def checkHorizontal(toCheck, puzzleLines):
    for i in range(0, len(puzzleLines)):
        line = puzzleLines[i]
        print("horz", line)
        count = 0
        for digit in toCheck:
            if digit not in line:
                break
            else:
                count += 1
        # print("Horz Line {} match count: {}".format(i, count))
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
            vertLine.append(puzzleLines[j][i])  # extract nth digit on every line to form vertival line
        print("vert", vertLine)
        for digit in toCheck:
            if digit not in vertLine:
                break
            else:
                count += 1
        # print("Vert ine {} match count: {}".format(i, count))
        if count == 5:
            return True
        else:
            continue
    return False


def checkDiagonal(toCheck, puzzleLines):
    diagonalLineTL = list()
    diagonalLineBL = list()
    desd_count = 4
    for i in range(0, 5):
        diagonalLineTL.append(puzzleLines[i][i])
        diagonalLineBL.append(puzzleLines[i][desd_count])
        desd_count -= 1
    print("Diagonal:", diagonalLineTL, diagonalLineBL)
    countTL = 0
    countBL = 0
    for digit in toCheck:
        if digit in diagonalLineTL:
            countTL += 1
        if digit in diagonalLineBL:
            countBL += 1
    if countTL == 5 or countBL ==5:
        return True
    return False

def checkBoard(toCheck, boardToCheck):
    gotMatch = None
    # every time
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
            puzzleLine = puzzleList[i].split(" ")  # '22 13 17 11  0\n' -->  ["22", "13", "17", " ", "0"]
            for i in range(0, 5):  # check every digit str in line and reform into a list of int
                if puzzleLine[i] == "":
                    puzzleLine.pop(i)
                if "\n" in puzzleLine[i]:
                    puzzleLine[i] = puzzleLine[i].strip("\n")
                puzzleLine[i] = int(puzzleLine[i])
            boardToCheck.append(puzzleLine)
        except IndexError:
            pass
    return boardToCheck


def getDrawNum(toCheck, index):
    toCheck.append(int(draw_num[index]))
    index += 1
    return toCheck, index

puzzleList = input[2:]
# for i in range(0, len(puzzleInput) - 1):
#     boardList = list()
#     if i == 0 or i % 5 != 0 or puzzleInput[i] != ['\n']:
#         boardList.append(puzzleInput[i])
#     puzzleList.append(boardList)
print("Board list: \n", puzzleList)
i = 0
toCheck = list()
puzzleStartLine = 0
while i < len(draw_num):
    print("Draw: ", draw_num[i])
    if i > len(puzzleList):
        puzzleStartLine = 0
    if (i == 0 or i % 5 != 0) and i <= 5:
        toCheck, i = getDrawNum(toCheck, i)
    else:
        print("Start line: ", puzzleStartLine)
        boardToCheck = getBoard(puzzleStartLine, puzzleList)
        if boardToCheck != []:
            print("Digits to check:", toCheck)
            print("Board to check: \n", boardToCheck)
            checkBoard(toCheck, boardToCheck)  # pass in a set of drawnums and list of 5 lines puzzle
            puzzleStartLine += 6

        toCheck, i = getDrawNum(toCheck, i)
