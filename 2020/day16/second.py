#!/usr/bin/env python3
import re

def isInRange(num, ranges):
    for k in range(len(ranges)):
        for i in range(2): # this loop is technically not needed, but it keeps the code clean
            rangeValues = ranges[str(k)][i].split("-")
            if num in range(int(rangeValues[0]), int(rangeValues[1])+1):
                return True
    return False


def testField(num, fields):
    num = int(num)
    validFields = []
    for k in fields:
        for i in range(2): # this loop is technically not needed, but it keeps the code clean
            rangeValues = ranges[str(k)][i].split("-")
            if num in range(int(rangeValues[0]), int(rangeValues[1])+1):
                validFields.append(k)
                break
    return validFields



with open("input.txt") as f:
    lines = f.read().split("\n")
    ranges = {}
    numLineBreaks = 0
    ret = []
    for i, line in enumerate(lines):
        if line == "":
            numLineBreaks += 1
            continue
        if numLineBreaks == 0:
            ranges[str(i)] = re.findall(r"(\d+\-\d+)", line)
        if numLineBreaks == 1 and line != "your ticket:":
            tmp = []
            for i in line.split(","):
                tmp.append(i)

        if numLineBreaks == 2 and line != "nearby tickets:":
            lineArr = line.split(",")
            for num in lineArr:
                num = int(num)
                if not isInRange(num, ranges):
                    lineArr.remove(str(num))
            #lineArr.append(tmp[])
            #print(lineArr)
            ret.append(lineArr)
    ret.append(tmp)
    tickets = list(map(list,zip(*ret))) # swap the rows and columns so that we can easily loop through each row to find out which field it is.

blacklist = set()
d = {}
for _ in range(30):
    for rowNum,row in enumerate(tickets):
        fields = [str(i) for i in range(20) if str(i) not in blacklist]
        for num in row:
            fields = testField(num, fields)
        print("POSSIBLE FIELDS FOR ROW {}".format(rowNum))
        print(fields)
        print("\n")
        if len(fields) == 1:
            blacklist.add(fields[0])
            d["Group " + str(rowNum)] = fields[0]
print(blacklist)
print(d)
