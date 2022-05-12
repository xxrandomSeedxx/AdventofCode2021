import sys

#day2
input = sys.stdin.readlines()
inputList = list()
for i in input:
    inputList.append(i.strip("\n"))
print(inputList)

sumdepth = 0
sumdist = 0
for item in inputList:
    grp = item.split(" ")
    dir = grp[0]
    dist = int(grp[1])
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
for item in inputList:
    grp = item.split(" ")
    dir = grp[0]
    dist = int(grp[1])
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