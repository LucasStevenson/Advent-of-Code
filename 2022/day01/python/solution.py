import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

'''
# quicker way to read input and compute sums for each block
with open(infile) as f:
    sums = [ sum([int(x) for x in block.split("\n") if x.strip() ]) for block in f.read().split("\n\n") ]
'''

with open(infile) as f:
    sums = []
    s = 0 # holds the sum of each "block"
    while line := f.readline():
        if line == "\n":
            # if we hit a newline, append sum of current "block" into array
            # reset "s" variable
            sums.append(s)
            s = 0
            continue
        # we are still inside a block
        # add number to `s`
        s += int(line.rstrip())
    if s != 0:
        # corner case for if input file doesn't have empty line at the very end
        # if this check wasn't here, it would read the last block, but not save it to `sums`
        sums.append(s)

print(f"Part 1: {max(sums)}")
print(f"Part 2: {sum(sorted(sums)[-3:])}")
