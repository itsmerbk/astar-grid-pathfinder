import heapq

def astar(grid, start, goal):
    R, C = len(grid), len(grid[0])
    h = lambda p: abs(p[0]-goal[0]) + abs(p[1]-goal[1])
    pq, g_score = [(h(start), 0, start)], {start: 0}
    while pq:
        _, g, cur = heapq.heappop(pq)
        if cur == goal: return g
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = cur[0]+dr, cur[1]+dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:
                nxt = (nr, nc)
                if g + 1 < g_score.get(nxt, 10**9):
                    g_score[nxt] = g + 1; heapq.heappush(pq, (g + 1 + h(nxt), g + 1, nxt))
    return -1

if __name__ == "__main__":
    m = [[0,0,0],[1,1,0],[0,0,0]]
    assert astar(m, (0,0), (2,0)) == 6
    print("[PASS] 012_astar_grid_pathfinder")
