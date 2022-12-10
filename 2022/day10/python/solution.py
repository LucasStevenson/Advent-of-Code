import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "../input.txt"

with open(infile) as f:
    X = 1
    cycle = 0
    obj = {}
    while line := f.readline().rstrip():
        op = line.split()[0]
        if op == "noop":
            cycle += 1
            obj[cycle] = X
        elif op == "addx":
            amt = int(line.split()[1])
            cycle += 1
            obj[cycle] = X
            cycle += 1
            obj[cycle] = X
            X += amt

def part1(obj):
    s = 0
    for i in [20, 60, 100, 140, 180, 220]:
        s += i*obj[i]
    return s

def part2(obj):
    img = [[' ' for _ in range(40) ] for _ in range(6)] # made ' ' the default value instead of '.' so that the final result is more readable
    pixelPos = 0
    for r in range(len(img)):
        for c in range(len(img[r])):
            spritePos = obj[pixelPos+1]
            if c in range(spritePos-1, spritePos+2): # c is the same thing as pixelPos%40
                img[r][c] = "#"
            pixelPos += 1
    return img

print("Part 1:", part1(obj))
print("Part 2:")
finalImg = part2(obj)
for r in finalImg:
    for c in r:
        print(c, end=" ")
    print()
