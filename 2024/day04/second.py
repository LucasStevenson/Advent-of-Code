import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    lines = [ list(line.strip()) for line in f.readlines() if line.strip()  ]

ans = 0
for r in range(len(lines)):
    for c in range(len(lines[r])):
        if lines[r][c] != 'A':
            continue
        if (r-1) < 0 or (c-1) < 0 or r+1 >= len(lines) or c+1 >= len(lines[r]):
            continue
        lr_diag = lines[r-1][c-1]+lines[r][c]+lines[r+1][c+1]
        rl_diag = lines[r-1][c+1]+lines[r][c]+lines[r+1][c-1]
        if (lr_diag == "MAS" or lr_diag == "SAM") and (rl_diag == "MAS" or rl_diag == "SAM"):
            ans += 1
print(ans)
