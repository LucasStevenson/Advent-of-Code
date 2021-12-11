import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    lines = [ line.rstrip() for line in f.readlines() if line.strip() ]

openDels = "([{<"
closingDels = ")]}>"
mappingVals = {
    ")": (3, 1),
    "]": (57, 2),
    "}": (1197, 3),
    ">": (25137, 4)
}
d = dict(zip(openDels,closingDels))

def opposite(a, b):
    if b == d[a]:
        return True
    return False

def solution(arr, part):
    stacks = []
    badVals = []
    for line in arr:
        stack = []
        for c in line:
            if c in openDels:
                stack.append(c)
                continue
            if not opposite(stack[-1], c):
                stack = []
                badVals.append(c)
                break
            stack.pop()
        if len(stack) > 0: stacks.append(stack)
    if part == "part1":
        return sum(mappingVals[v][0] for v in badVals)

    scores = []
    for s in stacks:
        count = 0
        for c in reversed(s):
            count *= 5
            count += mappingVals[d[c]][1]
        scores.append(count)
    return sorted(scores)[(len(scores)-1) // 2]


print(f"Part 1 solution: {solution(lines, 'part1')}")
print(f"Part 2 solution: {solution(lines, 'part2')}")
