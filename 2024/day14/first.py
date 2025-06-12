import sys, re
import numpy as np
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    Y, X = (103,101)
    N = 100
    A = np.zeros((Y, X))
    while line := f.readline().strip():
        x, y, dx, dy = tuple(map(int, re.findall(r"(\-?\d+)", line)))
        fx, fy = (x+dx*N) % X, (y+dy*N) % Y
        A[fy, fx] += 1
    A = np.delete(A, Y//2, 0) # deletes the middle row 
    A = np.delete(A, X//2, 1) # deletes the middle column
    quadrants = [M for SubA in np.split(A,2,axis=0) for M in np.split(SubA,2,axis=1)]
    ans = np.prod([ np.sum(q) for q in quadrants ])
    print(int(ans))
