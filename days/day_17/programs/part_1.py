from common import *
import numpy as np


ROUNDS = 2022

WIDTH = 7
HEIGHT_INCREASE = 20

# Rocks, like the grid, are in reverse in order to have the baseline at row 0
ROCKS = [
    #       ####
    np.array([[1, 1, 1, 1]], dtype="int"),

    #       .#.
    #       ###
    #       .#.
    np.array([
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ], dtype="int"),

    #       ..#
    #       ..#
    #       ###
    np.array([
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1]
    ], dtype="int"),

    #       #
    #       #
    #       #
    #       #
    np.array([
        [1],
        [1],
        [1],
        [1]
    ], dtype="int"),

    #       ##
    #       ##
    np.array([
        [1, 1],
        [1, 1]
    ], dtype="int"),
]


def increase_array_size(grid):
    grid = np.concatenate((grid, np.zeros((HEIGHT_INCREASE, WIDTH), dtype="int")), axis=0)


def get_firs_empty_row(grid):
    return np.where(np.all(grid == 0, axis=1))[0][0]


def get_overlapping_grid(grid, rock, rock_bottom, rock_left):
    return grid[rock_bottom:rock_bottom + len(rock), rock_left:rock_left + len(rock[0])]


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        # Each value is an int: +1 if the direction is right (>), -1 otherwise
        direction_array = [1 if direction == ">" else -1 for direction in open_file_char_array(filepath)]

        grid = np.zeros((HEIGHT_INCREASE, WIDTH), dtype="int")
        cur_level_index = 0

        for cur_round in range(ROUNDS):
            rock = ROCKS[cur_round % len(ROCKS)]

            cur_max_height = get_firs_empty_row(grid)
            if len(grid) < cur_max_height + 5:
                increase_array_size(grid)

            rock_left = 2
            rock_bottom = cur_max_height + 3

            while True:
                cur_wind_direction = direction_array[cur_level_index % len(direction_array)]
                cur_level_index += 1

                if 0 <= rock_left + cur_wind_direction + len(rock[0]) < WIDTH:
                    rock_left += cur_wind_direction

                if rock_bottom == 0 or np.sum(rock * get_overlapping_grid(grid, rock, rock_bottom-1, rock_left)) > 0:
                    break

                rock_bottom -= 1

            # overlapping_grid = get_overlapping_grid(grid, rock, rock_bottom, rock_left)
            grid[rock_bottom:rock_bottom + len(rock), rock_left:rock_left + len(rock[0])] = rock
        return get_firs_empty_row(grid)


p1 = Part_1()
p1.test(3068)
# p1.execute()
