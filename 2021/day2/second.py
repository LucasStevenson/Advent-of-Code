with open("input.txt") as f:
    lines = [ line.rstrip() for line in f.readlines() if line.strip() ]

x, y, aim = 0, 0, 0
for cmd in lines:
    d, amt = cmd.split()
    amt = int(amt)
    if d == "down":
        aim += amt
    elif d == "up":
        aim -= amt
    elif d == "forward":
        x += amt
        y += aim*amt
print(x*y)
