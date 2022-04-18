import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    p1, p2 = [], []
    player = None
    lines = [ line.rstrip() for line in f.readlines() if line.strip()  ]
    for line in lines:
        if "Player" in line:
            player = line
            continue
        p1.append(int(line)) if player == "Player 1:" else p2.append(int(line))


def recursiveGame(p1, p2):
    # this function returns a tuple
    # (player that won, deck)
    p1Sets, p2Sets = [], []
    while len(p1) > 0 and len(p2) > 0:
        if p1 in p1Sets and p2 in p2Sets:
            return ("Player 1", p1)
        p1Sets.append(p1.copy())
        p2Sets.append(p2.copy())

        p1Top, p2Top = p1.pop(0), p2.pop(0)
        if len(p1) >= p1Top and len(p2) >= p2Top:
            winner,_ = recursiveGame(p1[:p1Top], p2[:p2Top])
        else:
            # at least one of the players doesnt have enough cards
            winner = "Player 1" if p1Top > p2Top else "Player 2"

        if winner == "Player 1":
            p1 += [p1Top, p2Top]
        elif winner == "Player 2":
            p2 += [p2Top, p1Top]
    return ("Player 1", p1) if len(p2) == 0 else ("Player 2", p2)

_, deck = recursiveGame(p1,p2)
print(sum([ n*(i+1) for i,n in enumerate(deck[::-1]) ]))
