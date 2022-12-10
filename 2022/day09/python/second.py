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

rope = [ [0,0] for _ in range(10) ] # 0 is the head, 9 is the last tail
visited = set() # visited points
for line in lines:
    dir, amt = line
    dx, dy = obj[dir]
    for _ in range(int(amt)):
        # just like before, automatically add to head
        rope[0][0] += dx
        rope[0][1] += dy
        for i in range(len(rope)-1): # deal with all other knots 
            hx,hy = rope[i]
            tx,ty = rope[i+1]
            if isTouching(hx, hy, tx, ty):
                continue
            ty += 0 if hy == ty else (hy-ty)/(abs(hy-ty))
            tx += 0 if hx == tx else (hx-tx)/(abs(hx-tx))
            rope[i+1] = [tx, ty]
        visited.add((rope[9][0], rope[9][1]))

print(len(visited))
