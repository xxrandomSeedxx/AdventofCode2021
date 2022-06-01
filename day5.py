#!/usr/bin/python
import sys

input = sys.stdin.readlines()


class Counter(object):
    # def __init__(self):
    #     super().__init__()

    def plot_points(self, constant, start, end):
        count = 1
        points = dict()
        for i in range(int(start), int(end) + 1):
            count += 1
        print(self.plotted_points)

all_points = list()
for num_grp in input:
    try:
        cood_grp = num_grp.strip("\n").split(" -> ")  # ['432,708', '432,160']
        x1, y1 = cood_grp[0].split(",")
        x2, y2 = cood_grp[1].split(",")

        if x1 == x2 or y1 == y2:
            for y in range(int(min(y1, y2)), int(max(y1, y2)) + 1):
                print(">>", x1, y)
                all_points.append((x1, y))
            for x in range(int(min(x1, x2)), int(max(x1, x2)) + 1):
                print("++", x, y1)
                all_points.append((x, y1))
    except IndexError:
        pass
# print(all_points)
