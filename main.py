import maze_funcs
import dfs
import bfs
import a_star
import greedy_search

bfs_time = []
bfs_memory = []

dfs_time = []
dfs_memory = []

a_star_time = []
a_star_memory = []

greedy_search_time = []
greedy_search_memory = []

for num in range(5000):
  # Cria o labirinto e define o ponto de partida e de chegada
  maze, start, end = maze_funcs.initialize_maze()
  # print("Labirinto:")
  # maze_funcs.print_maze(maze)

  # print("Ponto de partida:", start)
  # print("Ponto de chegada:", end)

  bfs_path = bfs.bfs(maze, start, end)
  bfs_time.append(bfs_path[1])
  bfs_memory.append(bfs_path[2])
  # print(bfs_path[0])
  # print("Tempo de execução em segundos:", bfs_path[1])
  # print("Consumo de memória por número de alocações:", bfs_path[2])

  dfs_path = dfs.dfs(maze, start, end)
  dfs_time.append(dfs_path[1])
  dfs_memory.append(dfs_path[2])
  # print(dfs_path[0])
  # print("Tempo de execução em segundos:", dfs_path[1])
  # print("Consumo de memória por número de alocações:", dfs_path[2])

  a_star_path = a_star.a_star(maze, start, end)
  a_star_time.append(a_star_path[1])
  a_star_memory.append(a_star_path[2])
  # print(a_star_path[0])
  # print("Tempo de execução em segundos:", a_star_path[1])
  # print("Consumo de memória por número de alocações:", a_star_path[2])

  greedy_search_path = greedy_search.greedy_search(maze, start, end)
  greedy_search_time.append(greedy_search_path[1])
  greedy_search_memory.append(greedy_search_path[2])
  # print(greedy_path[0])
  # print("Tempo de execução em segundos:", greedy_path[1])
  # print("Consumo de memória por número de alocações:", greedy_path[2])

print("Performance BFS:")
print("Average time:", sum(bfs_time)/len(bfs_time))
print("Average memory: ", sum(bfs_memory)/len(bfs_memory))

print("\nPerformance DFS:")
print("Average time:", sum(dfs_time)/len(dfs_time))
print("Average memory: ", sum(dfs_memory)/len(dfs_memory))

print("\nPerformance A*:")
print("Average time:", sum(a_star_time)/len(a_star_time))
print("Average memory: ", sum(a_star_memory)/len(a_star_memory))

print("\nPerformance Busca Gulosa:")
print("Average time:", sum(greedy_search_time)/len(greedy_search_time))
print("Average memory: ", sum(greedy_search_memory)/len(greedy_search_memory))