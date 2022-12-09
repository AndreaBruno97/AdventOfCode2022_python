from common import *
import numpy as np


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        grid = np.array(open_file_int_matrix(filepath), np.int32)
        grid_rows, grid_cols = grid.shape

        max_scenic_score = 0

        with np.nditer(grid, flags=['multi_index']) as iterator:
            for tree in iterator:
                cur_x, cur_y = iterator.multi_index

                trees_left = grid[cur_x, :cur_y] if cur_y > 0 else np.array([])
                first_taller_tree_left = np.where(np.flip(trees_left) >= tree)[0]
                scenic_score_left = cur_y if len(first_taller_tree_left) == 0 else first_taller_tree_left[0] + 1

                trees_right = grid[cur_x, cur_y+1:] if cur_y < grid_cols else np.array([])
                first_taller_tree_right = np.where(trees_right >= tree)[0]
                scenic_score_right = grid_cols - 1 - cur_y if len(first_taller_tree_right) == 0 else first_taller_tree_right[0] + 1

                trees_top = grid[:cur_x, cur_y] if cur_x > 0 else np.array([])
                first_taller_tree_top = np.where(np.flip(trees_top) >= tree)[0]
                scenic_score_top = cur_x if len(first_taller_tree_top) == 0 else first_taller_tree_top[0] + 1

                trees_bottom = grid[cur_x+1:, cur_y] if cur_x < grid_rows else np.array([])
                first_taller_tree_bottom = np.where(trees_bottom >= tree)[0]
                scenic_score_bottom = grid_rows - 1 - cur_x if len(first_taller_tree_bottom) == 0 else first_taller_tree_bottom[0] + 1

                cur_scenic_score = scenic_score_left * scenic_score_right * scenic_score_top * scenic_score_bottom

                if cur_scenic_score > max_scenic_score:
                    max_scenic_score = cur_scenic_score

        return max_scenic_score


p2 = Part_2()
p2.test(8)
p2.execute()
