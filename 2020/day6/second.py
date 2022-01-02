'''
https://adventofcode.com/2020/day/6#part2
'''
import re
with open("input.txt") as f:
    line = f.readline()
    string = ""
    numPeople = 0
    inputs = []
    while line:
        if line.strip():
            string += line.rstrip()
            numPeople += 1
        else:
            inputs.append([string, numPeople])
            numPeople = 0
            string = ""
        line = f.readline()
    inputs.append([string, numPeople])

counter = 0
for s in inputs:
    # count the number of occurances of each char
    # if it's equal to numPeople, then increment counter
    chars = set(s[0])
    for c in chars:
        if len(re.findall(c, s[0])) == s[1]:
            counter += 1
print(counter)
