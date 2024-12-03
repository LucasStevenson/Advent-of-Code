import sys, re
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    ans = sum(list(map(lambda x: int(x[0])*int(x[1]), re.findall(r"mul\((\d+),(\d+)\)", f.read()))))
    print(ans)
