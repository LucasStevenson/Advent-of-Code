'''
https://adventofcode.com/2020/day/5#part2
'''
import math
with open("input.txt") as f:
    line = f.readline()
    inputs = []
    while line:
        if line.strip():
            inputs.append(line.rstrip())
        line = f.readline()
seats = []
for i in inputs:
    seatID = 0
    rowsRange = [1, 126]
    colsRange = [0, 7]
    for j in i[:7]:
        total = rowsRange[0]+rowsRange[1]
        if j.lower() == "f":
            rowsRange[1] = int(total/2)
        elif j.lower() == "b":
            rowsRange[0] = math.ceil(total/2)
    seatID += rowsRange[0] * 8

    for k in i[7:]:
        t = colsRange[0] + colsRange[1]
        if k.lower() == "r":
            colsRange[0] = math.ceil(t/2)
        elif k.lower() == "l":
            colsRange[1] = int(t/2)
    seatID += colsRange[1]
    seats.append(seatID)

seats.sort()
for i in range(len(seats)-1):
    if seats[i]+2 == seats[i+1]:
        print(seats[i]+1)
