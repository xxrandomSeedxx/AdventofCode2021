#!/usr/bin/python
import sys

input = sys.stdin.readlines()

def store_full_coods(start, end, value):
    line_full_cood = list()
    start = start[value]
    end = end[value]
    print(">>>>", start, end)

for num_grp in input:
    all_coods = list()
    try:
        cood_grp = num_grp.strip("\n").split(" -> ")
        start = cood_grp[0].split(",")  # ['432,708', '432,160'] -> [[432,708], [432,160]]
        end = cood_grp[1].split(",")
        print(start, end)
        # compare x
        if start[0] == end[0]:
            print("x coods are same")
            store_full_coods(start, end, 1)
        # compare y
        elif start[1] == end[1]:
            print("y coods are same")
            store_full_coods(start, end, 0)
    except IndexError:
        pass
