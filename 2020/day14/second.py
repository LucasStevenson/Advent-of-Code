#!/usr/bin/env python3
import sys
from itertools import product
import re
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    line = f.readline().rstrip()
    mask = None
    mem = {}
    while line:
        if line.startswith("mask"):
            mask = line.split(" = ")[1]
            line = f.readline().rstrip()
            continue
        t = re.search(r"mem\[(\d+)\]\s=\s(\d+)", line)
        k,v = f'{int(t[1]):036b}', int(t[2])
        res = ""
        for i in range(len(mask)):
            if mask[i] == "X":
                res += "X"
            elif mask[i] == "1":
                res += "1"
            else:
                res += k[i]

        xIdx = [k for k,v in enumerate(res) if v=="X"]
        for tup in list(product([0,1], repeat=len(xIdx))):
            tmpRes = list(res)
            for i in range(len(xIdx)):
                tmpRes[xIdx[i]] = str(tup[i])
            mem[str(int("".join(tmpRes),2))] = v
        line = f.readline().rstrip()

print(sum(v for k,v in mem.items()))
