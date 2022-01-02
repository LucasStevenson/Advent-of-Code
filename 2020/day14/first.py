#!/usr/bin/env python3
import sys
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
        k, v = t[1], f'{int(t[2]):036b}'
        res = ""
        for i in range(len(mask)):
            if mask[i] == "X":
                res += v[i]
            else:
                res += mask[i]
        mem[k] = res
        line = f.readline().rstrip()

print(sum(int(str(v), 2) for k,v in mem.items()))
