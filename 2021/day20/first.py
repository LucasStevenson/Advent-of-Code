import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

# I will probably replace this code once I come up with a better solution. This solution does not work for part 2

PADDING = 4
with open(infile) as f:
    algo, img = f.read().split("\n\n")
    algo = algo.replace("\n", "")
    img = [ ["."]*PADDING + list(line) + ["."]*PADDING for line in  img.rstrip().split("\n") ]


for i in range(PADDING):
    img.insert(0, ["."]*len(img[0]))
    img.append(["."]*len(img[0]))

def pp(arr):
    # This function only neatly prints out the img
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            print(arr[r][c], end="")
        print()

def countLight(arr):
    count = 0
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if arr[r][c] == "#":
                count += 1
    return count


# # = light pixels (BIT 1)
# . = dark pixels (BIT 0)
imgCopy = [ row[:] for row in img ]
for _ in range(2):
    for r in range(len(img)):
        for c in range(len(img[r])):
            # check neighbors
            bits = ""
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0,-1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if not (0 <= r+dr < len(img) and 0 <= c+dc < len(img[r])):
                    # outside the map
                    bits += "0"
                    continue
                rr = r+dr
                cc = c+dc
                bits += "1" if img[rr][cc] == "#" else "0"

            algoIdx = int(bits, 2)
            # update the copy img
            imgCopy[r][c] = algo[algoIdx]
    img = [ row[:] for row in imgCopy ]

del img[0]
del img[-1]
#pp(img)
print(countLight(img))
