import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    instructions = f.readline().rstrip().split(",")
    line = f.readline()
    lines = []
    tmp = []
    while line:
        if line == "\n":
            lines.append(tmp)
            tmp = []
        else:
            tmp.append(list(map(int, line.rstrip().split())))
        line = f.readline()
    del lines[0]
    lines.append(tmp)

def getColumn(arr, index):
    return [ row[index] for row in arr ]

def getSumOfUnmarkedNums(arr):
    count = 0
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if type(arr[r][c]) != int:
                continue
            else:
                count += arr[r][c]
    return count



def getLosingBoard(boardCopy):
    winners = []
    t = []
    for i, num in enumerate(instructions):
        num = int(num)
        for idx, board in enumerate(boardCopy):
            for row in range(len(board)):
                for col in range(len(board[row])):
                    if board[row][col] == num:
                        boardCopy[idx][row][col] = "pog"
                    if all(v == "pog" for v in board[row]) or all(v == "pog" for v in getColumn(board, col)):
                        if idx not in winners:
                             t.append((getSumOfUnmarkedNums(boardCopy[idx]), instructions[i]))
                             winners.append(idx)

                    
    return int(t[-1][1]) * t[-1][0]

print(getLosingBoard(lines))
