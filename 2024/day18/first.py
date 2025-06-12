import sys
import heapq
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    C, R = (71,71)
    obstacles = set()
    for _ in range(1024):
        r, c = map(int, f.readline().strip().split(","))
        obstacles.add((r, c))

def manhattan_distance(p1, p2):
    r1, c1 = p1
    r2, c2 = p2
    return abs(r1-r2) + abs(c1-c2)

def aStar(start, end, obstacles):
    """finds the shortest path from `start` point to `end` point using A* algorithm
    Params:
        start:     (r,c) coordinate of starting point
        end:       (r,c) coordinate of ending point
        obstacles: Set of (r,c) coordinates
    """
    pq = [(0, start)]
    g_costs = { start: 0 }
    f_costs = {}
    while pq:
        _, coord = heapq.heappop(pq) # f_cost, (r,c) coord
        r, c = coord
        if coord == end:
            break 
        for dr, dc in [(0, 1), (0,-1), (1,0), (-1,0)]:
            neighbor = (r+dr, c+dc)
            if not (0 <= neighbor[0] < R and 0 <= neighbor[1] < C) or neighbor in obstacles:
                continue
            if neighbor not in g_costs or g_costs[coord]+1 < g_costs[neighbor]:
                new_f_cost = g_costs[coord]+1+manhattan_distance(neighbor, end) 
                f_costs[neighbor] = new_f_cost
                g_costs[neighbor] = g_costs[coord]+1
                heapq.heappush(pq, (new_f_cost, neighbor))
    return g_costs[end]

print(aStar((0,0), (R-1, C-1), obstacles))
