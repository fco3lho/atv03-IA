import maze_funcs
import dfs
import bfs
import a_star
import greedy_search

# Cria o labirinto e define o ponto de partida e de chegada
maze, start, end = maze_funcs.initialize_maze(10, 10)
print("Labirinto:")
maze_funcs.print_maze(maze)

print("Ponto de partida:", start)
print("Ponto de chegada:", end)

# Executa e exibe os resultados de cada algoritmo
print("Resultado BFS:")
bfs_path = bfs.bfs(maze, start, end)
print(bfs_path)

print("Resultado DFS:")
dfs_path = dfs.dfs(maze, start, end)
print(dfs_path)

print("Resultado A*:")
a_star_path = a_star.a_star(maze, start, end)
print(a_star_path)

print("Resultado Caminho Guloso:")
greedy_path = greedy_search.greedy_search(maze, start, end)
print(greedy_path)
