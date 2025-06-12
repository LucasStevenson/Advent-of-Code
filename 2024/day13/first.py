import sys, re
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

# Brute force
# Part1 said "You estimate that each button would need to be pressed no more than 100 times to win a prize"
def getTokenCost(x1, x2, y1, y2, X, Y):
    for a in range(1, 101):
        for b in range(1, 101):
            if x1*a + x2*b == X and y1*a + y2*b == Y:
                return a*3 + b
    return 0

with open(infile) as f:
    blocks = f.read().split("\n\n")
    ans = 0
    for block in blocks:
        x1, x2 = map(int, re.findall(r"X\+(\d+)", block))
        y1, y2 = map(int, re.findall(r"Y\+(\d+)", block))
        X, Y = map(int, re.search(r"X\=(\d+)\, Y\=(\d+)", block).groups())
        ans += getTokenCost(x1, x2, y1, y2, X, Y)
    print(ans)
