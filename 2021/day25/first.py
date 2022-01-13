import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    lines = [ list(line.rstrip()) for line in f.readlines() ]

def moveEast(arr):
    ret = []
    for r in range(len(arr)):
        tmp = arr[r].copy()
        for c in range(len(arr[r])):
            if arr[r][c] == ">" and arr[r][(c+1)%len(arr[r])] == ".":
                tmp[c] = "."
                tmp[(c+1)%len(arr[r])] = ">"
        ret.append(tmp)
    return ret


def moveSouth(arr):
    tmp = [row[:] for row in arr]
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if arr[r][c] == "v" and arr[(r+1)%len(arr)][c] == ".":
                tmp[r][c] = "."
                tmp[(r+1)%len(arr)][c] = "v"
    return tmp

counter = 0
prev = None
while True:
    prev = [ row[:] for row in lines ]
    lines = moveEast(lines)
    lines = moveSouth(lines)
    counter += 1
    if lines == prev:
        print(counter)
        break
