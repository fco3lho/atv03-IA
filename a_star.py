import heapq
import maze_funcs

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(maze, start, end):
    open_set = []
    heapq.heappush(open_set, (0, start, [start]))
    g_scores = {start: 0}

    while open_set:
        _, (x, y), path = heapq.heappop(open_set)

        if (x, y) == end:
            return path
        
        for dx, dy in maze_funcs.DIRECTIONS:
            nx, ny = x + dx, y + dy

            if maze_funcs.is_valid_move(maze, nx, ny):
                tentative_g_score = g_scores[(x, y)] + 1

                if (nx, ny) not in g_scores or tentative_g_score < g_scores[(nx, ny)]:
                    g_scores[(nx, ny)] = tentative_g_score
                    f_score = tentative_g_score + heuristic((nx, ny), end)

                    heapq.heappush(open_set, (f_score, (nx, ny), path + [(nx, ny)]))

    return None