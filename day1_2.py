#!/usr/bin/python3
import sys

input = sys.stdin.readlines()
inputList = input[0].split(",")

count = 0
for i in range(len(inputList) - 1):
    if inputList[i + 1] > inputList[i]:
        count += 1

for i in range(len(inputList) - 1):
    try:
        sum1 = inputList[i] + inputList[i + 1] + inputList[i + 2]
        sum2 = inputList[i + 1] + inputList[i + 2] + inputList[i + 3]
        if sum2 > sum1:
            count += 1
    except IndexError:
        continue


input2 = sys.stdin.readlines()
inputList2 = input2[0].split(",")

sumdepth = 0
sumdist = 0
for i in range(0, len(inputList2) - 1, 2):
    dir = inputList2[i]
    dist = inputList2[i + 1]
    if dir == "up":
        sumdepth -= dist
    elif dir == "down":
        sumdepth += dist
    else:
        sumdist += dist

total = sumdist * sumdepth
print(total)


aim = 0
sumdist = 0
sumdepth = 0
for i in range(0, len(inputList2) - 1, 2):
    dir = inputList2[i]
    dist = inputList2[i + 1]
    # print(dir, dist)
    if dir == "up":
        aim -= dist
    elif dir == "down":
        aim += dist
    else:
        sumdist += dist
        sumdepth += aim * dist
    # print(aim, sumdist, sumdepth)
total = sumdist * sumdepth
print(total)