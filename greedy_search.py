import heapq
import maze_funcs

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def greedy_search(maze, start, end):
    open_set = []
    heapq.heappush(open_set, (heuristic(start, end), start, [start]))
    visited = set()

    while open_set:
        _, (x, y), path = heapq.heappop(open_set)

        if (x, y) == end:
            return path
        
        for dx, dy in maze_funcs.DIRECTIONS:
            nx, ny = x + dx, y + dy

            if maze_funcs.is_valid_move(maze, nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))

                heapq.heappush(open_set, (heuristic((nx, ny), end), (nx, ny), path + [(nx, ny)]))
                
    return None
