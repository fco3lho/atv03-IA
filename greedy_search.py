import heapq
import maze_funcs
import time
import tracemalloc

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def greedy_search(maze, start, end):
    # Inicia contagem de tempo
    start_time = time.time()
    
    # Inicia contagem de consumo de memória
    tracemalloc.start()
    start_snapshot = tracemalloc.take_snapshot()

    open_set = []
    heapq.heappush(open_set, (heuristic(start, end), start, [start]))
    visited = set()

    while open_set:
        _, (x, y), path = heapq.heappop(open_set)

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

                heapq.heappush(open_set, (heuristic((nx, ny), end), (nx, ny), path + [(nx, ny)]))
                
    # Termina contagem de tempo
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Termina a contagem de consumo de memória
    end_snapshot = tracemalloc.take_snapshot()
    tracemalloc.stop()

    memory_diff = end_snapshot.compare_to(start_snapshot, 'lineno')
    total_memory = sum(stat.size for stat in memory_diff)

    return None, elapsed_time, total_memory
