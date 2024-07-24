import maze_funcs

def dfs(maze, start, end):
    stack = [(start, [start])]
    visited = set()

    while stack:
        (x, y), path = stack.pop()

        if (x, y) == end:
            return path
        
        for dx, dy in maze_funcs.DIRECTIONS:
            nx, ny = x + dx, y + dy
            
            if maze_funcs.is_valid_move(maze, nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                stack.append(((nx, ny), path + [(nx, ny)]))
                
    return None