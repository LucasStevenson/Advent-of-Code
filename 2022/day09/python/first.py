import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "../input.txt"

with open(infile) as f:
    lines = [ line.split() for line in f.readlines() if line.strip() ]
    obj = { # key: direction, value: (dx,dy)
            'R': (1, 0),
            'L': (-1, 0),
            'U': (0, 1),
            'D': (0, -1)
    }

def isTouching(hx, hy, tx, ty):
    # know two points are touching if xCoords and yCoords differ by at most 1
    return abs(hx-tx) <= 1 and abs(hy-ty) <= 1

hx, hy, tx, ty = 0, 0, 0, 0
visited = set() # visited points
for line in lines:
    dir, amt = line
    dx, dy = obj[dir]
    for i in range(int(amt)):
        visited.add((tx, ty))
        hx += dx
        hy += dy
        if isTouching(hx, hy, tx, ty): # if head and tail are touching, don't move tail
            continue
        # head and tail aren't touching, adjust tail coords
        # adjust tail yCoord by first determining whether head and tail are in the same row (hy==ty).
        # if they are, don't change tail yPos
        # else, add or subtract 1, depending on whether head is above or below tail
        #   we determine which direction it's in by subtracting hy and ty. hy-ty>1 -> head is above tail. hy-ty<1 -> head is below tail
        #   hy-ty will sometimes give us a number thats not 1 or -1. The sign will be correct, but the number wont. To convert it to either 1 or -1, divide (hy-ty) by abs(hy-ty)
        ty += 0 if hy == ty else (hy-ty)/(abs(hy-ty)) 
        # same process for adjusting xCoord. First determine if head and tail are in same column (hx==tx)
        # if they are, don't change xPos
        # else, add or subtract 1 depending on whether head is to the left or right of tail
        #   do same thing as described above, except hx and tx instead of hy and ty
        tx += 0 if hx == tx else (hx-tx)/(abs(hx-tx))

print(len(visited))
