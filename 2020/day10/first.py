with open("input.txt") as f:
    lines = f.readlines()
    lines = [int(line.rstrip()) for line in lines if line.strip()]
lines.sort()
# print(lines)

threeCounter = 1
oneCounter = 1

for i in range(0, len(lines)-1):
    if lines[i+1] - lines[i] == 1:
        oneCounter += 1
    elif lines[i+1] - lines[i] == 3:
        threeCounter += 1

print(oneCounter * threeCounter)
