import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    line = list(map(int, f.readline().split()))

# Brute force solution
def solve(numIterations):
    global line
    for _ in range(numIterations):
        nextLine = []
        for num in line:
            if num == 0:
                nextLine.append(1)
                continue
            num_str = str(num)
            if len(num_str) % 2 == 0:
                nextLine.append(int(num_str[0:len(num_str)//2]))
                nextLine.append(int(num_str[len(num_str)//2:]))
            else:
                nextLine.append(num*2024)
        line = nextLine
    return len(line)

print(solve(25))
