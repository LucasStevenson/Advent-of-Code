with open("input.txt") as f:
    lines = [ int(line.rstrip()) for line in f.readlines() if line.strip() ]

counter = 0
for i in range(0, len(lines) - 1):
    if lines[i+1] > lines[i]:
        counter += 1
print(counter)

