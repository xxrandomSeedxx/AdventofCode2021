#!/usr/bin/python
import sys


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
    # print(">>>>>>>>", toCheck)
    gotMatch = checkHorizontal(toCheck, boardToCheck)
    if not gotMatch:
        gotMatch = checkVertical(toCheck, boardToCheck)
    # if not gotMatch:
    #     gotMatch = checkDiagonal(toCheck, boardToCheck)
    if gotMatch:
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
            continue
        if i == 5 or (i != 0 and i % 6 == 0):
            # print(">>>>\n{}".format(currBoard))
            boardsToCheck.append(currBoard)
    # print("++++", boardsToCheck[0], boardsToCheck[-1])
    return boardsToCheck

def getUnmarkedSum(toCheck, board):
    unmarked_list = list()
    for line in board:
        for digit in line:
            if digit not in toCheck:
                unmarked_list.append(digit)
    print("unmarked_list", unmarked_list)
    sum = 0
    for item in unmarked_list:
        sum += item
    return sum


def getDrawNum(toCheck, index):
    toCheck.append(int(draw_num[index]))
    index += 1
    return toCheck, index

input = sys.stdin.readlines()
draw_num = input[0].split(",")
puzzleList = input[2:]
i = 0
toCheck = list()
bingo = False
puzzleStartLine = 0
boardsToCheck = getBoard(puzzleList)
# print("Boards to check: \n", boardsToCheck)
print(len(draw_num), len(boardsToCheck))

while i < len(draw_num):
    # print("Draw: ", toCheck)
    boardsToRemove = list()
    if puzzleStartLine > len(puzzleList):
        puzzleStartLine = 0
    # After the 5th draw num, check all boards for every number drawn
    if (i == 0 or i % 5 != 0) and i <= 5:
        toCheck, i = getDrawNum(toCheck, i)
    else:
        # print("Start line: ", puzzleStartLine)
        for board in boardsToCheck:
            # print("\nChecking board: \n", board)
            bingo = checkBoard(toCheck, board)  # pass in a set of drawnums and list of 5 lines puzzle
            if bingo:
                curr_board_index = boardsToCheck.index(board)
                # there might be multiple boards to remove at each round
                if curr_board_index not in boardsToRemove:
                    print("\nBoard {} bingo!".format(curr_board_index))
                    print(board)
                    boardsToRemove.append(curr_board_index)
                    print("index of board to remove: ", boardsToRemove)

                if len(boardsToCheck) == 1:
                    sum = getUnmarkedSum(toCheck, board)
                    result = sum * toCheck[-1]
                    print("Sum {} Draw {} Result {}".format(sum, toCheck[-1], result))

    for boardNum in boardsToRemove:
        latestIndex = boardNum - boardsToRemove.index(boardNum)
        # print("Removing {}\n{}".format(latestIndex, boardsToCheck[latestIndex]))
        boardsToCheck.pop(latestIndex)
        print("remaining: {}".format(len(boardsToCheck)))
    bingo = False
    toCheck, i = getDrawNum(toCheck, i)
