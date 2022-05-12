#!/usr/bin/python3
# day1
import sys

input = sys.stdin.readlines()
inputList = list()
for i in input:
    inputList.append(i.strip("\n"))

# part1
count = 0
for i in range(len(inputList) - 1):
    if inputList[i + 1] > inputList[i]:
        count += 1
print(count)
# part2
for i in range(len(inputList) - 1):
    try:
        sum1 = inputList[i] + inputList[i + 1] + inputList[i + 2]
        sum2 = inputList[i + 1] + inputList[i + 2] + inputList[i + 3]
        if sum2 > sum1:
            count += 1
    except IndexError:
        continue
print(count)
