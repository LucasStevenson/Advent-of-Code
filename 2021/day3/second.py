import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    lines = [ line.rstrip() for line in f.readlines() if line.strip() ] 

def findMostCommon(arr, t):
    count = 0
    for i in arr:
        i = int(i)
        count += i
    ans = float(count)/len(arr)
    if ans == 0.5:
        return 1
    #print(ans)
    return round(ans)


def getO(lines, t):
    i = 0
    while len(lines) > 1:
        transposed = list(zip(*lines))
        if t == "O2":
            oxy = findMostCommon(transposed[i], t)
        else:
            oxy = int(not findMostCommon(transposed[i], t))
        newLines = []
        for el in lines:
            if int(el[i]) == oxy:
                newLines.append(el)
        lines = newLines.copy()
        i += 1
    return lines[0]

A = (int((getO(lines, "co2")), 2))
B = (int((getO(lines, "O2")), 2))

print((A, B))
print(A*B)
