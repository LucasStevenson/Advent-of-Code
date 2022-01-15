import sys
import re
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def solve(eq):
    inners = re.findall(r"\([^\(]*?\)", eq)
    if len(inners) == 0:
        return evaluate(eq)
    for i in inners:
        eq = eq.replace(i, str(evaluate(i)))
    return solve(eq)

    
def evaluate(eq):
    eq = eq.replace("(", "").replace(")", "").split()
    ans = int(eq[0])
    for i in range(1, len(eq)-1, 2):
        if eq[i] == "*":
            ans *= int(eq[i+1])
        elif eq[i] == "+":
            ans += int(eq[i+1])
    return ans

with open(infile) as f:
    lines = [ solve(line.rstrip()) for line in f.readlines() ]
    print(sum(lines))
