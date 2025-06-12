import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

def isPossible(design, patterns):
    if design in patterns:
        return True
    possible = False
    for pattern in patterns:
        if design.startswith(pattern):
            possible = possible or isPossible(design[len(pattern):], patterns)
    return possible

with open(infile) as f:
    patterns, designs = f.read().strip().split("\n\n")
    patterns, designs = set(patterns.split(", ")), designs.split("\n")
    ans = sum([ int(isPossible(design, patterns)) for design in designs ])
    print(ans)
