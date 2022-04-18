import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    p1, p2 = [], []
    player = None
    lines = [ line.rstrip() for line in f.readlines() if line.strip()  ]

    for line in lines:
        if line == "Player 1:" or line == "Player 2:":
            player = line
            continue
        p1.append(int(line)) if player == "Player 1:" else p2.append(int(line))

def getWinner(p1, p2):
    while len(p1) > 0 and len(p2) > 0:
        p1Top = p1.pop(0)
        p2Top = p2.pop(0)

        if p1Top > p2Top:
            p1.append(p1Top)
            p1.append(p2Top)
        else:
            p2.append(p2Top)
            p2.append(p1Top)
    return p1 or p2

winner = getWinner(p1, p2)
print(sum([ n*(i+1) for i,n in enumerate(winner[::-1]) ]))
