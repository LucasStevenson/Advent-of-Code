import sys
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv) > 1 else "../input.txt"

with open(infile) as f:
    lines = [ line.rstrip() for line in f.readlines() if line.strip() ]

tree = {}
path = []
def updateCurrPath(path):
    currPath = tree
    for p in path:
        currPath = currPath[p]
    return currPath
currPath = tree
for line in lines:
    if line[0] == "$":
        if "ls" in line:
            continue
        # cd
        dir = line.split()[2]
        if dir == "..":
            if len(path) > 0:
                path.pop()
                currPath = updateCurrPath(path)
            continue
        path.append(dir)
        currPath[dir] = {}
        currPath = updateCurrPath(path)
    else:
        line = line.split()
        if line[0] == "dir":
            currPath[line[1]] = {}
        else: # is a file
            currPath[line[1]] = int(line[0])

dir_sizes = []
def get_all_dir_sizes(t):
    # populates 'dir_sizes' with all subdir sizes
    # at the end, returns size of root directory 
    size = 0
    for v in t.values():
        if type(v) == int:
            size += v
            continue
        size += get_all_dir_sizes(v)
    dir_sizes.append(size)
    return size

get_all_dir_sizes(tree)
print(sum([ x for x in dir_sizes if x <= 100000 ]))
