import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    seeds = [int(x) for x in f.readline().split(": ")[1].split()]
    lines = [x.strip() for x in f.read().split("\n\n")]

def solution(seed):
    for map in lines:
        for line in map.split("\n")[1:]:
            dest, source, rng = [int(x) for x in line.split()]
            if seed in range(source, source+rng):
                seed += dest - source
                break
    return seed

print(min([solution(seed) for seed in seeds]))
