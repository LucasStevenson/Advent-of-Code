import sys
import re
import math
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    instruction, lines = f.read().split("\n\n")

D = {} # { "AAA": {"L": BBB, "R": CCC}, ... }
for line in lines.strip().split("\n"):
    parent, left, right = re.search(r"(\w+) = \((\w+), (\w+)\)", line).groups()
    D[parent] = { "L": left, "R": right }

currentPositions = [ node for node in D.keys() if node[-1] == 'A' ]
instructIdx, numSteps, ans = 0, 0, 1
while len(currentPositions) > 0:
    numSteps += 1
    newPositions = []
    for node in currentPositions:
        nextNode = D[node][instruction[instructIdx]]
        if nextNode[-1] == "Z":
            ans = math.lcm(ans, numSteps)
        else:
            newPositions.append(nextNode)
    currentPositions = newPositions.copy()
    instructIdx = (instructIdx+1)%len(instruction)
print(ans)
