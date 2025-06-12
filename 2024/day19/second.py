import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

MEMO = {} # {design: num of arrangements}
def numArrangements(design, patterns):
    if design in MEMO:
        return MEMO[design]
    possible = 0 if design not in patterns else 1
    for pattern in patterns:
        if design.startswith(pattern):
            MEMO[design[len(pattern):]] = numArrangements(design[len(pattern):], patterns)
            possible += MEMO[design[len(pattern):]]
    return possible

with open(infile) as f:
    patterns, designs = f.read().strip().split("\n\n")
    patterns, designs = set(patterns.split(", ")), designs.split("\n")
    ans = sum([ numArrangements(design, patterns) for design in designs ])
    print(ans)
