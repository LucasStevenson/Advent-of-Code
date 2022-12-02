import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    # the key for `iWin` and `iLose` dicts is opponents move
    # value is my move
    iWin = {
            "A": "B",
            "B": "C",
            "C": "A"
    }
    iLose = { v: k for k,v in iWin.items() } # invert `iWin` dict
    weights = { "A": 1, "B": 2, "C": 3 }
    score = 0
    for line in f.readlines():
        oppMove, outcome = line.split()
        if outcome == "X":
            # i lose
            score += weights[iLose[oppMove]]
        elif outcome == "Z":
            # i win
            score += 6 + weights[iWin[oppMove]]
        else:
            # draw
            score += 3 + weights[oppMove]
    print(score)
