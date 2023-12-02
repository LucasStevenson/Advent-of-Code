import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    digits = sum(map(lambda x: int(x[0]+x[-1]), [[ x for x in line if x.isdigit() ] for line in f.read().split("\n") if line.strip() ]))
    print(digits)
