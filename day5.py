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
        coods = num_grp.strip("\n").split(" -> ")
        start = coods[0]  # 0,9
        end = coods[1]  # 5,9
        # compare x
        if start[0] == end[0]:
            print("x coods are same")
            store_full_coods(start, end, 2)
        # compare y (set[1] is ",")
        elif start[2] == end[2]:
            print("y coods are same")
            store_full_coods(start, end, 0)
    except IndexError:
        pass
