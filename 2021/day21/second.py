import sys
import re
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

p1Space, p2Space = map(int,re.findall(r": (\d*)", open(infile).read()))

