#!/usr/bin/env python3
import re

def isInRange(num, ranges):
    for k in range(len(ranges)):
        for i in range(2): # this loop is technically not needed, but it keeps the code clean
            rangeValues = ranges[str(k)][i].split("-")
            if num in range(int(rangeValues[0]), int(rangeValues[1])+1):
                return True
    return False

with open("input.txt") as f:
    lines = f.read().split("\n")
    ranges = {}
    numLineBreaks = 0
    counter = 0
    for i, line in enumerate(lines):
        if line == "":
            numLineBreaks += 1
            continue
        if numLineBreaks == 0:
            ranges[str(i)] = re.findall(r"(\d+\-\d+)", line)
        if numLineBreaks == 2 and line != "nearby tickets:":
            for num in line.split(","):
                num = int(num)
                if not isInRange(num, ranges):
                    counter += num
print(counter)
