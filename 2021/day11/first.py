import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    lines = [ list(map(int,list(line.rstrip()))) for line in f.readlines() ]

def checkPos(r, c, arr, flashed):
    if arr[r][c] == 9:
        arr[r][c] = 0
        flashed.add((r, c))
        updateNeighbors(r, c, arr, flashed)
    else:
        arr[r][c] += 1
    return arr, flashed

def updateNeighbors(r, c, arr, flashed):
    if r-1 >= 0 and c-1 >= 0 and (r-1, c-1) not in flashed:
        # diagUpLeft
        arr, flashed = checkPos(r-1, c-1, arr, flashed)
    if r-1 >= 0 and (r-1, c) not in flashed:
        # up
        arr, flashed = checkPos(r-1, c, arr, flashed)
    if r-1 >= 0 and c+1 < len(arr[r-1]) and (r-1, c+1) not in flashed:
        # diagUpRight
        arr, flashed = checkPos(r-1, c+1, arr, flashed)
    if c+1 < len(arr[r]) and (r, c+1) not in flashed:
        # right
        arr, flashed = checkPos(r, c+1, arr, flashed)
    if c-1 >= 0 and (r, c-1) not in flashed:
        # left
        arr, flashed = checkPos(r, c-1, arr, flashed)
    if r+1 < len(arr) and c-1 >= 0 and (r+1, c-1) not in flashed:
        # diagDownLeft
        arr, flashed = checkPos(r+1, c-1, arr, flashed)
    if r+1 < len(arr) and (r+1, c) not in flashed:
        # down
        arr, flashed = checkPos(r+1, c, arr, flashed)
    if r+1 < len(arr) and c+1 < len(arr[r+1]) and (r+1, c+1) not in flashed:
        # diagDownRight
        arr, flashed = checkPos(r+1, c+1, arr, flashed)
    return arr, flashed


def solution(arr, iterations):
    count = 0
    for _ in range(iterations):
        flashed = set()
        for r in range(len(arr)):
            for c in range(len(arr[r])):
                if arr[r][c] == 9:
                    arr[r][c] = 0
                    flashed.add((r, c))
                    arr, flashed = updateNeighbors(r, c, arr, flashed)
                else:
                    if (r, c) not in flashed:
                        arr[r][c] += 1
        count += len(flashed)
    return count
print(solution(lines, 100))
