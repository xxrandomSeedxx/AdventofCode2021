#!/usr/bin/python
import sys

input = sys.stdin.readlines()

for num_grp in input:
    try:
        coods = num_grp.strip("\n").split(" -> ")
        set1 = coods[0]
        set2 = coods[1]
        # print(set1, set2)
        if set1[0] == set2[0]:
            print(set1[0], set2[0], "x is same")
        elif set1[2] == set2[2]:
            print(set1[2], set2[2], "y is same")
    except IndexError:
        pass
