#!/usr/bin/python
import sys

input = sys.stdin.readlines()


class Counter(object):
    def __init__(self):
        super().__init__()
        self.cood_count = dict()

    def count_points(self, pt_set):
        if pt_set in self.cood_count.keys():
            self.cood_count[pt_set] += 1
        else:
            self.cood_count[pt_set] = 1

all_points = list()
for num_grp in input:
    cood_grp = num_grp.strip("\n").split(" -> ")  # ['432,708', '432,160']
    x1, y1 = cood_grp[0].split(",")
    x2, y2 = cood_grp[1].split(",")

    if x1 == x2 or y1 == y2:
        for y in range(int(min(y1, y2)), int(max(y1, y2)) + 1):
            for x in range(int(min(x1, x2)), int(max(x1, x2)) + 1):
                all_points.append((x, y))

c = Counter()
# count occurrence of each coordinate
for pt_set in all_points:
    c.count_points(pt_set)

danger_zone = 0
for pt, num in c.cood_count.items():
    if num > 1:
        danger_zone += 1

print("num of danger zones {}".format(danger_zone))