import sys
from itertools import product
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    schematics = [line.split("\n") for line in f.read().strip().split("\n\n")]

key_heights, lock_heights = [], []
for schematic in schematics:
    if schematic[0] == '#'*len(schematic[0]):
        lock_heights.append([line.count('#') for line in zip(*schematic[1:])])
    else:
        key_heights.append([line.count('#') for line in zip(*schematic[:-1])])
ans = 0
for lock, key in product(lock_heights, key_heights):
    ans += int(all([a+b <= 5 for a,b in zip(lock, key)]))
print(ans)
