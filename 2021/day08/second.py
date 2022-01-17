from itertools import permutations
import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    line = f.readline().rstrip()
    sigPatterns = []
    outputVals = []
    while line:
        first, second  = line.split(" | ")
        outputVals.append(second)
        sigPatterns.append(first)
        line = f.readline().rstrip()
perms = list(permutations("abcdefg"))

'''
 0000    <--- array below is based on this 
1    2      
1    2      Each index in the array represents the number the element represents
 3333       
4    5      For example, arr[0] is a list of all the segments that would have to 
4    5      be turned on to represent the number 0
 6666 
'''

arr = [
    [0,1,2,4,5,6],
    [2,5],
    [0,2,3,4,6],
    [0,2,3,5,6],
    [1,2,3,5],
    [0,1,3,5,6],
    [0,1,3,4,5,6],
    [0,2,5],
    [0,1,2,3,4,5,6],
    [0,1,2,3,5,6]
]

def getConfig(pattern):
    for perm in perms:
        valid = True
        for seq in pattern.split():
            if sorted([ perm.index(c) for c in seq ]) not in arr:
                valid = False
                break
        if valid:
            return perm

ans = 0
for i in range(len(outputVals)):
    config = getConfig(sigPatterns[i])
    n = ""
    for seq in outputVals[i].split():
        n += str(arr.index(sorted([ config.index(c) for c in seq ])))
    ans += int(n)

print(ans)
