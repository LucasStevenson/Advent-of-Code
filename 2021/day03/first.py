import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    lines = [ list(line.rstrip()) for line in f.readlines() if line.strip() ]
    lines = list(zip(*lines)) # tranpose the array so that the cols become the rows
    # print(lines[0])

def findMostCommon(arr):
    count = sum(map(int, arr))
    return round(count/len(arr))

G, E = "", ""
for r in range(0, len(lines)):
    mostCommonBit = findMostCommon(lines[r])
    G += str(mostCommonBit)
    E += str(int(not mostCommonBit))
#print((G,E))
print(int(G, 2) * int(E, 2))
