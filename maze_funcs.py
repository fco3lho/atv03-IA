import random

# Dimensões do labirinto
WIDTH, HEIGHT = 10, 10

# Definição de obstáculos
OBSTACLE = '#'
FREE = '0'
START = 'S'
END = 'E'

# Movimentos possíveis: esquerda, direita, cima, baixo
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def initialize_maze(width, height):
    maze = [[OBSTACLE if random.random() < 0.3 else FREE for _ in range(width)] for _ in range(height)]
    start = (random.randint(0, height-1), random.randint(0, width-1))
    end = (random.randint(0, height-1), random.randint(0, width-1))

    while end == start:
        end = (random.randint(0, height-1), random.randint(0, width-1))

    maze[start[0]][start[1]] = START
    maze[end[0]][end[1]] = END
    
    return maze, start, end

def print_maze(maze):
    for row in maze:
        print(' '.join(row))
    print()

def is_valid_move(maze, x, y):
    return 0 <= x < WIDTH and 0 <= y < HEIGHT and maze[x][y] != OBSTACLE