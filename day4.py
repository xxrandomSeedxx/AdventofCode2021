#!/usr/bin/python
import sys

input = sys.stdin.readlines()
draw_num = input[0].split(",")


def checkHorizontal(toCheck, puzzleLines):
    for i in range(0, len(puzzleLines)):
        line = puzzleLines[i]
        # print("horz", line)
        count = 0
        for digit in toCheck:
            if digit not in line:
                continue
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
        # print("vert", vertLine)
        for digit in toCheck:
            if digit not in vertLine:
                continue
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
        try:
            diagonalLineTL.append(puzzleLines[i][i])
            diagonalLineBL.append(puzzleLines[i][desd_count])
            desd_count -= 1
        except IndexError:
            pass
    print("Diagonal:", diagonalLineTL, diagonalLineBL)
    countTL = 0
    countBL = 0
    for digit in toCheck:
        if digit in diagonalLineTL:
            countTL += 1
        if digit in diagonalLineBL:
            countBL += 1
    if countTL == 5 or countBL == 5:
        return True
    return False


def checkBoard(toCheck, boardToCheck):
    gotMatch = None
    # every time
    print(">>>>>>>>", toCheck)
    gotMatch = checkHorizontal(toCheck, boardToCheck)
    if not gotMatch:
        gotMatch = checkVertical(toCheck, boardToCheck)
    # if not gotMatch:
    #     gotMatch = checkDiagonal(toCheck, boardToCheck)
    if gotMatch:
        print("Match >>>>>>>>>>>>>>")
        return True


def getBoard(puzzleList):
    boardsToCheck = list()

    for i in range(0, len(puzzleList)):
        if i == 0 or i % 6 == 0:
            currBoard = list()
        try:
            puzzleLine = puzzleList[i].split(" ")  # '22 13 17 11  0\n' -->  ["22", "13", "17", " ", "0"]
            # print("puzzleLine: ",puzzleLine)
            if puzzleLine != ["\n"]:
                for j in range(0, 5):  # check every digit str in line and reform into a list of int
                    if puzzleLine[j] == "":
                        puzzleLine.pop(j)
                    if "\n" in puzzleLine[j]:
                        puzzleLine[j] = puzzleLine[j].strip("\n")
                    puzzleLine[j] = int(puzzleLine[j])
                currBoard.append(puzzleLine)
        except IndexError:
            pass
        # print("currBoard: ", currBoard)
        if i % 5 == 0:
            boardsToCheck.append(currBoard)
    return boardsToCheck

def getUnmarkedSum(toCheck, board):
    # print("+++++++++", toCheck, board)
    new_board = list()
    for line in board:
        for digit in line:
            if digit not in toCheck:
                new_board.append(digit)
    sum = 0
    for item in new_board:
        sum += item
    return sum


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
# print("Board list: \n", puzzleList)
i = 0
toCheck = list()
bingo = False
puzzleStartLine = 0
boardsToCheck = getBoard(puzzleList)
print("Board to check: \n", boardsToCheck)
while i < len(draw_num) and not bingo:
    # print("Draw: ", toCheck)
    if puzzleStartLine > len(puzzleList):
        puzzleStartLine = 0
    if (i == 0 or i % 5 != 0) and i <= 5:
        toCheck, i = getDrawNum(toCheck, i)
        # print("Digits to check:", toCheck)
    else:
        # print("Start line: ", puzzleStartLine)
        for board in boardsToCheck:
            # print("Board to check: \n", board)
            bingo = checkBoard(toCheck, board)  # pass in a set of drawnums and list of 5 lines puzzle
            if bingo:
                print("Bingo! ")
                sum = getUnmarkedSum(toCheck, board)
                result = sum * toCheck[-1]
                print(sum, toCheck[-1], result)
                break
        # i += 1
        toCheck, i = getDrawNum(toCheck, i)
