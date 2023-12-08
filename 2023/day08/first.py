import sys
import re
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    instruction, lines = f.read().split("\n\n")

D = {} # { "AAA": {"L": BBB, "R": CCC}, ... }
for line in lines.strip().split("\n"):
    parent, left, right = re.search(r"(\w+) = \((\w+), (\w+)\)", line).groups()
    D[parent] = { "L": left, "R": right }

currNode, instructIdx, ans = "AAA", 0, 0
while currNode != "ZZZ":
    currNode = D[currNode][instruction[instructIdx]]
    instructIdx = (instructIdx+1)%len(instruction)
    ans += 1
print(ans)
