import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    # A, X for rock, 1
    # B, Y for paper, 2
    # C, Z scissors, 3
    # lost: 0, draw: 3, win: 6
    outcomes = {
            "AX": 3,
            "AY": 6,
            "AZ": 0,
            "BX": 0,
            "BY": 3,
            "BZ": 6,
            "CX": 6,
            "CY": 0,
            "CZ": 3
    }
    # how much rock, paper, scissors is worth
    weights = { "X": 1, "Y": 2, "Z": 3 }
    score = 0
    for line in f.readlines():
        line = line.replace(" ", "").rstrip()
        score += weights[line[1]]
        score += outcomes[line]
    print(score)
