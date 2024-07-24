import maze_funcs
from collections import deque

def bfs(maze, start, end):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return path
        
        for dx, dy in maze_funcs.DIRECTIONS:
            nx, ny = x + dx, y + dy

            if maze_funcs.is_valid_move(maze, nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
                
    return None