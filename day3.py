#!/usr/bin/python3
import sys

def decToBin(binNum):
    i = 0
    decimal = 0
    while binNum != 0:
        decimal += (binNum % 10) * pow(2, i)
        binNum = binNum // 10
        i += 1
    return decimal


def filterList(digit, inputList, filterType="O2"):
    occurance1 = 0
    occurance0 = 0
    listWithOnes = list()
    listWithZeros = list()
    filterFormatMap = {
        "O2": {
            "hasMore0": listWithZeros,
            "hasMore1": listWithOnes
        },
        "CO2": {
            "hasMore0": listWithOnes,
            "hasMore1": listWithZeros
        }
    }

    for i in inputList:
        if i[digit] == str(1):
            occurance1 += 1
            listWithOnes.append(i)
        else:
            occurance0 += 1
            listWithZeros.append(i)

    if occurance0 == occurance1:
        return filterFormatMap[filterType]["hasMore1"]
    elif max(occurance0, occurance1) == occurance0:
        return filterFormatMap[filterType]["hasMore0"]
    else:
        return filterFormatMap[filterType]["hasMore1"]


def runFiltering(inputList, filterType):
    numLength = len(inputList[0])
    for digit in range(numLength):
        if len(inputList) > 1:
            inputList = filterList(digit, inputList, filterType)
    gasGenRate = decToBin(int(inputList[0]))
    return gasGenRate


gammaRate = ""
epsilonRate = ""
input = sys.stdin.readlines()
numLength = input[0].split(",")
# numLength = len(inputList[0])
for digit in range(numLength):
    occurance1 = 0
    occurance0 = 0
    for i in inputList:
        if i[digit] == str(1):
            occurance1 += 1
        else:
            occurance0 += 1
    if max(occurance0, occurance1) == occurance0:
        gammaRate += str(0)
        epsilonRate += str(1)
    else:
        epsilonRate += str(0)
        gammaRate += str(1)

gammaRateDec = decToBin(int(gammaRate))
epsilonRateDec = decToBin(int(epsilonRate))
total = gammaRateDec * epsilonRateDec
print(gammaRate, epsilonRate, gammaRateDec, epsilonRateDec, total)


O2GenRate = runFiltering(inputList, "O2")
CO2ScrubRate = runFiltering(inputList, "CO2")

total = O2GenRate * CO2ScrubRate
print(total)
