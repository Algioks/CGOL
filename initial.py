import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from random import choice
from typing import List

GENERATIONS = 100
SIZE = 100

def create_map(size: int = SIZE) -> List[List[bool]]:
    return [[choice([True,False]) for _ in range (SIZE)] for _ in range(SIZE)]

def show_map(map_: List[List[bool]]):
    plt.imshow(map_, cmap='binary', interpolation='nearest')
    plt.show()

def get_neighbours(map_, x, y): # Count live neighbors around a cell
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx = x + dx
            ny = y + dy
            if 0 <= nx < SIZE and 0 <= ny < SIZE : 
                count += map_[nx][ny]
    return count

def update_map(old_map):
    new_map = [[False] * SIZE for _ in range(SIZE)]
    for x in range(SIZE):
        for y in range(SIZE):
            alive_neighbors = get_neighbours(old_map, x, y)
            if old_map[x][y]:
                # Cell is alive
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_map[x][y] = False  # Dies due to underpopulation or overpopulation
                else:
                    new_map[x][y] = True   # Survives
            else:
                # Cell is dead
                if alive_neighbors == 3:
                    new_map[x][y] = True   # Becomes alive due to reproduction
    return new_map

def animate_map(map_):
    fig = plt.figure()
    plt.imshow(map_, cmap='binary', interpolation='nearest')

    images = []
    for _ in range(GENERATIONS):
        im = plt.imshow(map_, cmap='binary', interpolation='nearest', animated=True)
        images.append([im])
        map_ = update_map(map_)
    
    ani = animation.ArtistAnimation(fig, images, interval=500, blit=True)
    plt.show()

if __name__ == '__main__':
    initial_map = create_map(SIZE)
    animate_map(initial_map)