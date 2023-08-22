import matplotlib.pyplot as plt

from pprint import pprint
from random import choice
from typing import List

# constant
GENERATIONS = 10


def create_map(size: int = 5) -> List[List[bool]]:
    """Create a 2d map for given size
    [
    [1,1,1],
    [1,1,1],
    [1,1,1]
    ]

    """
    # map_ = []
    # for _ in range(size):
    #     row = []
    #     for _ in range(size):
    #         row.append(choice([False, True]))
    #     map_.append(row)
    #
    # return map_
    return [[choice([False, True]) for _ in range(size)] for _ in range(size)]


def show_map(map_: List[List[bool]]):
    plt.imshow(map_, cmap='binary', interpolation='nearest')
    plt.show()
    pprint(map_)


def get_neighbours(map_, coordinate_row, coordinate_column) -> int:
    """"""
    count = 0
    # HOMEWORK
    # code....
    return count


def update_map(old_map: List[List[bool]]) -> List[List[bool]]:
    """Updates given map to next generation"""
    # HOMEWORK
    # we iterate over whole map
    # check number of alive neighbours
    # decision: live or die
    # return updated/new map


if __name__ == '__main__':
    current_map = create_map()
    show_map(current_map)