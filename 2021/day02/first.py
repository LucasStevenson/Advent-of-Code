with open("input.txt") as f:
    lines = [ line.rstrip() for line in f.readlines() if line.strip() ]

x, y = 0, 0
for cmd in lines:
    d, amt = cmd.split()
    amt = int(amt)
    if d == "forward":
        x += amt
    elif d == "up":
        y -= amt
    elif d == "down":
        y += amt

print(x*y) 
