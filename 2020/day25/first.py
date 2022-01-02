import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    pk1 = int(f.readline())
    pk2 = int(f.readline())

def findLoopSize(pk, subjectNum):
    loopSize = 1
    while pow(subjectNum, loopSize, 20201227) != pk:
        loopSize += 1
    return loopSize

ls1 = findLoopSize(pk1, 7)

print(pow(pk2, ls1, 20201227))
