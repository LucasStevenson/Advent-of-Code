import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    line = list(map(int,f.readline().rstrip().split(",")))

average = round(sum(line) / len(line))

total = float("inf")
for i in range(average+1):
    tmpTotal = 0
    for num in line:
        tmpTotal += abs(num - i)
    if tmpTotal < total:
        total = tmpTotal

print(total)
