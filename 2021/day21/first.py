import sys
import re
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

p1Space, p2Space = map(int,re.findall(r": (\d*)", open(infile).read()))
p1Score, p2Score = 0, 0
diceRolls = 1
player1 = True
count = 0

while p1Score < 1000 and p2Score < 1000:
    rollTotal = diceRolls + (diceRolls+1) + (diceRolls+2)
    count += 3
    if player1:
        p1Space = (p1Space+rollTotal - 1) % 10 + 1
        p1Score += p1Space
    else:
        p2Space = (p2Space+rollTotal - 1) % 10 + 1
        p2Score += p2Space
    diceRolls += 3
    diceRolls %= 100
    player1 = not player1

print(min(p1Score, p2Score) * count)
