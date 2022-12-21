import sys
import sympy
from sympy.parsing.sympy_parser import parse_expr
infile = sys.argv[1] if len(sys.argv) > 1 else "../input.txt"

with open(infile) as f:
    G = {}
    while line := f.readline().rstrip():
        k, v = line.split(": ")
        if v.isdigit():
            G[k] = int(v)
            continue
        G[k] = v.split()
    G["root"][1] = "="

def setupEquation(key):
    if key == "humn":
        return 'x'
    if type(G[key]) == int:
        return G[key]
    m1, op, m2 = G[key]
    return f"({setupEquation(m1)}){op}({setupEquation(m2)})"

equation = setupEquation("root")
lhs, rhs = map(parse_expr, equation.split("="))
ans = sympy.solve(sympy.Eq(lhs,rhs))[0]
print(ans)
