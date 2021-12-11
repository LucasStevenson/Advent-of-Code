import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    lines = [ list(line.rstrip()) for line in f.readlines() if line.strip() ]
    lines = list(zip(*lines)) # tranpose the array so that the cols become the rows
    # print(lines[0])

def findMostCommon(arr):
    count = 0
    for i in arr:
        i = int(i)
        count += i
    return round(count/len(arr))

G, E = "", ""
for r in range(0, len(lines)):
    G += str(findMostCommon(lines[r]))
    E += str(int(not findMostCommon(lines[r])))
#print((G,E))
print(int(G, 2) * int(E, 2))
