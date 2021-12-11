import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    line = list(map(int,f.read().rstrip().split(",")))

# naive approach, automating every step and creating a massive array
def getFish(arr, days):
    t = arr.copy()
    for _ in range(days):
        for i, el in enumerate(arr):
            if el == 0:
                t[i] = 6
                t.append(8)
            else:
                t[i] = t[i] - 1
        arr = t.copy()
    return len(arr)

print(getFish(line, 80))
