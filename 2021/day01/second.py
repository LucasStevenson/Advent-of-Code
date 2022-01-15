with open("input.txt") as f:
    lines = [ int(line.rstrip()) for line in f.readlines() if line.strip() ]

counter = 0
for i in range(0, len(lines) - 3):
    A = lines[i] + lines[i+1] + lines[i+2]
    B = A - lines[i] + lines[i+3]
    if B > A:
        counter += 1

print(counter)
