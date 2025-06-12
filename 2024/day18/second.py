import sys
import heapq
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

def manhattan_distance(p1, p2):
    r1, c1 = p1
    r2, c2 = p2
    return abs(r1-r2) + abs(c1-c2)

def path_exists(start, end, obstacles):
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
    return end in g_costs

with open(infile) as f:
    C, R = (71,71)
    obstacles = set()
    while line := f.readline().strip():
        r, c = map(int, line.split(","))
        obstacles.add((r, c))
        if not path_exists((0,0), (R-1,C-1), obstacles):
            print(f"{r},{c}")
            break
