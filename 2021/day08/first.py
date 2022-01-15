import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    line = f.readline().rstrip()
    lengths = [2, 4, 3, 7]
    count = 0
    while line:
        first, second = line.split(" | ")
        for i in second.split():
            if len(i) in lengths:
                count += 1
        line = f.readline().rstrip()
    print(count)
