import sys
import heapq
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    grid = []
    r, c, fr, fc = -1, -1, -1, -1
    for row, line in enumerate(f.read().strip().split("\n")):
        if r == -1 and 'S' in line:
            r, c = row, line.index('S')
        if fr == -1 and 'E' in line:
            fr, fc = row, line.index('E')
        grid.append(list(line))
    R, C = len(grid), len(grid[0])

def dijkstra(start, end):
    pq = [(0, start, (0,1))]
    g_costs = { start: 0 }
    while pq:
        g_cost, (r, c), dir = heapq.heappop(pq) # g_cost, (r,c) pos, (a,b) dir
        if (r, c) == end:
            break 
        for dr, dc in [(0, 1), (0,-1), (1,0), (-1,0)]:
            rr, cc = r+dr, c+dc
            if not (0 <= rr < R and 0 <= cc < C) or grid[rr][cc] == '#':
                continue
            diff = (abs(dir[0]+dr), abs(dir[1]+dc))
            turnWeight = 0
            if diff == (0,0):
                turnWeight = 2000
            elif diff == (1,1):
                turnWeight = 1000
            new_g_cost = g_cost+1+turnWeight
            if (rr,cc) not in g_costs or new_g_cost < g_costs[(rr,cc)]:
                g_costs[(rr,cc)] = new_g_cost
                heapq.heappush(pq, (new_g_cost, (rr,cc), (dr,dc)))
    return g_costs[end]

print(dijkstra((r, c), (fr, fc)))
