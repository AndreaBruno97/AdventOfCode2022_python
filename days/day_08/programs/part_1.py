from common import *
import numpy as np


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        grid = np.array(open_file_int_matrix(filepath), np.int32)
        grid_rows, grid_cols = grid.shape

        visible_trees_counter = 0

        with np.nditer(grid, flags=['multi_index']) as iterator:
            for tree in iterator:
                cur_x, cur_y = iterator.multi_index

                trees_left = grid[cur_x, :cur_y] if cur_y > 0 else np.array([])
                trees_right = grid[cur_x, cur_y+1:] if cur_y < grid_cols else np.array([])
                trees_top = grid[:cur_x, cur_y] if cur_x > 0 else np.array([])
                trees_bottom = grid[cur_x+1:, cur_y] if cur_x < grid_rows else np.array([])

                if (
                    np.all(trees_left < tree) or
                    np.all(trees_right < tree) or
                    np.all(trees_top < tree) or
                    np.all(trees_bottom < tree)
                ):
                    visible_trees_counter += 1

        return visible_trees_counter


p1 = Part_1()
p1.test(21)
p1.execute()
