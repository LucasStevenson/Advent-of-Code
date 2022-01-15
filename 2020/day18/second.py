import sys
import math
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
    while "+" in eq:
        for i in range(len(eq)):
            if eq[i] == "+":
                eq = eq[:i-1] + [str(int(eq[i-1])+int(eq[i+1]))] + eq[i+2:]
                break
    nums = [ int(num) for num in eq if num.isdigit() ]
    return math.prod(nums)


with open(infile) as f:
    lines = [ solve(line.rstrip()) for line in f.readlines() ]
    print(sum(lines))
