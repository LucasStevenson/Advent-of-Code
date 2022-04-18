import sys
from collections import defaultdict
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


def recursiveGame(p1, p2, setsPlayed=defaultdict(list)):
    # returns a tuple
    # (player that won, deck)
    while len(p1) > 0 and len(p2) > 0:
        if p1 in setsPlayed["Player 1"] and p2 in setsPlayed["Player 2"]:
            return ("Player 1", p1)

        setsPlayed["Player 1"].append(p1.copy())
        setsPlayed["Player 2"].append(p2.copy())

        p1Top, p2Top = p1.pop(0), p2.pop(0)
        if len(p1) >= p1Top and len(p2) >= p2Top:
            winner,_ = recursiveGame(p1[:p1Top], p2[:p2Top], defaultdict(list))
        else:
            # at least one of the players doesnt have enough cards
            winner = "Player 1" if p1Top > p2Top else "Player 2"

        if winner == "Player 1":
            p1.append(p1Top)
            p1.append(p2Top)
        elif winner == "Player 2":
            p2.append(p2Top)
            p2.append(p1Top)
    return ("Player 1", p1) if len(p2) == 0 else ("Player 2", p2)

_, deck = recursiveGame(p1,p2)
print(sum([ n*(i+1) for i,n in enumerate(deck[::-1]) ]))
