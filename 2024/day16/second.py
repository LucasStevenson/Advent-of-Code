import sys
import heapq
from collections import defaultdict, deque
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

def dijkstra_all_best_paths(start, end):
    pq = [(0, start, (0,1))]
    g_costs = { (start[0], start[1], 0, 1): 0 } # (r, c, dr, dc): cost
    prev_states = defaultdict(set) # (rr, cc, dr, dc): {previous states}
    while pq:
        g_cost, (r, c), dir = heapq.heappop(pq) # g_cost, (r,c) pos, (a,b) dir
        state = (r, c, dir[0], dir[1])
        if (r, c) == end:
            continue
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
            new_state = (rr, cc, dr, dc)
            if new_state not in g_costs or new_g_cost <= g_costs[new_state]:
                g_costs[new_state] = new_g_cost
                heapq.heappush(pq, (new_g_cost, (rr,cc), (dr,dc)))
                prev_states[new_state].add(state)

    # Find min-cost end states
    end_states = [ s for s in g_costs if s[0] == end[0] and s[1] == end[1] ]
    min_cost = min([g_costs[s] for s in end_states])
    final_states = [ s for s in end_states if g_costs[s] == min_cost ]

    # Backtrack to find all visited positions on optimal paths
    Q = deque(final_states)
    seen = set()
    tiles_on_best_paths = set()
    while Q:
        r, c, dr, dc = state = Q.popleft()
        tiles_on_best_paths.add((r,c))
        for prev_state in prev_states[state]:
            if prev_state not in seen:
                seen.add(prev_state)
                Q.append(prev_state)
    return tiles_on_best_paths

tiles_on_best_paths = dijkstra_all_best_paths((r, c), (fr, fc))
print(len(tiles_on_best_paths))
