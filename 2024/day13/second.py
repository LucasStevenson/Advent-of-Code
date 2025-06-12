import sys, re
from sympy import symbols, Eq, solve
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

# Smarter solution than part1
# Solves the system of linear equations using sympy
# Note: could also be solved with Cramer's rule (code shown at the bottom)
def getTokenCost(x1, x2, y1, y2, X, Y):
    a, b = symbols('a b')
    eq1 = Eq(x1*a + x2*b, X)
    eq2 = Eq(y1*a + y2*b, Y)
    S = solve((eq1, eq2), (a,b))
    x,y = float(S[a]), float(S[b])
    if not (x.is_integer() and y.is_integer()):
        return 0
    return int(3*x + y)

with open(infile) as f:
    blocks = f.read().split("\n\n")
    ans = 0
    for block in blocks:
        x1, x2 = map(int, re.findall(r"X\+(\d+)", block))
        y1, y2 = map(int, re.findall(r"Y\+(\d+)", block))
        X, Y = map(int, re.search(r"X\=(\d+)\, Y\=(\d+)", block).groups())
        ans += getTokenCost(x1, x2, y1, y2, X+10000000000000, Y+10000000000000)
    print(ans)


"""Solve the system of linear equations using Cramer's Rule
Cramer's rule: https://andymath.com/cramers-rule/

- Note: There is a little bit of floating point errors when doing the calculation below, so we need to round the result to determine whether it's a whole number or a decimal. Rounding to 2 decimal places is the sweet spot


def getTokenCost(x1, x2, y1, y2, X, Y):
    denom = np.linalg.det(np.array([
        [x1, x2],
        [y1, y2]
    ]))
    x = np.array([
        [X, x2],
        [Y, y2],
    ])
    y = np.array([
        [x1, X],
        [y1, Y],
    ])
    x = np.linalg.det(x) / denom
    y = np.linalg.det(y) / denom
    x,y = round(x,2), round(y,2)
    if not (x.is_integer() and y.is_integer()):
        return 0
    return int(3*x + y)
"""
