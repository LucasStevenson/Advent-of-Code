import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    ans = 0
    while line := f.readline().strip():
        history = [int(x) for x in line.split()]
        ans += history[-1]
        while not all([ x == 0 for x in history ]):
            history = [ history[i+1]-history[i] for i in range(len(history)-1) ]
            ans += history[-1]
print(ans)
