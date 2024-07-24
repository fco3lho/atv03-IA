import maze_funcs
from collections import deque
import time
import tracemalloc

def bfs(maze, start, end):
    # Inicia contagem de tempo
    start_time = time.time()
    
    # Inicia contagem de consumo de memória
    tracemalloc.start()
    start_snapshot = tracemalloc.take_snapshot()

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            # Termina contagem de tempo
            end_time = time.time()
            elapsed_time = end_time - start_time

            # Termina a contagem de consumo de memória
            end_snapshot = tracemalloc.take_snapshot()
            tracemalloc.stop()

            memory_diff = end_snapshot.compare_to(start_snapshot, 'lineno')
            total_memory = sum(stat.size for stat in memory_diff)

            return path, elapsed_time, total_memory
        
        for dx, dy in maze_funcs.DIRECTIONS:
            nx, ny = x + dx, y + dy

            if maze_funcs.is_valid_move(maze, nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    # Termina contagem de tempo
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Termina a contagem de consumo de memória
    end_snapshot = tracemalloc.take_snapshot()
    tracemalloc.stop()

    memory_diff = end_snapshot.compare_to(start_snapshot, 'lineno')
    total_memory = sum(stat.size for stat in memory_diff)

    return None, elapsed_time, total_memory