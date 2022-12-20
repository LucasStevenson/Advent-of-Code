import sys
import json
infile = sys.argv[1] if len(sys.argv) > 1 else "../input.txt"
with open(infile) as f:
    lines = [ json.loads(line.rstrip()) for line in f.readlines() if line.strip() ]

def compare(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return 1
        if left > right:
            return 0
        return
    # exactly one param is an int, convert non-int param to a list
    if (type(left) == int) ^ (type(right) == int):
        if type(left) == int:
            left = [left]
        else:
            right = [right]
    # both params are of type list
    #print(left, right)
    if type(left) == list and type(right) == list:
        i = 0
        while i < len(left) and i < len(right):
            res = compare(left[i], right[i])
            if res == 1:
                return 1
            if res == 0:
                return 0
            i += 1
        # check if right list ran out of items first
        if len(right) < len(left):
            return 0
        if len(right) > len(left):
            return 1
        return

count = 0
idx = 1
for i in range(0, len(lines), 2):
    l ,r = lines[i:i+2]
    if compare(l, r) == 1:
        count += idx
    idx += 1
print(count)
