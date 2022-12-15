import sys

from common import *

START_SAND_COL = 500
START_SAND_ROW = 0

AIR = "."
ROCK = "#"
SAND = "o"
START = "+"
START_POS = (500, 0)


def get_side(is_min, is_row, tmp_input_list_pairs):
    result = sys.maxsize if is_min else 0
    for tmp_pair_list in tmp_input_list_pairs:

        for tmp_pair in tmp_pair_list:
            value_to_compare = tmp_pair[1 if is_row else 0]

            if is_min:
                result = min(result, value_to_compare)
            else:
                result = max(result, value_to_compare)

    return result


def print_grid(grid):
    for line in grid:
        for point in line:
            if point == SAND:
                print_result(point, end="")
            elif point == ROCK:
                print_debug(point, end="")
            elif point == START:
                print_success(point, end="")
            else:
                print(point, end="")
        print()
    print()


# Return value: True if the sand stops, False otherwise
def drop_sand(grid, start_pos, min_col, max_col, max_row):
    cur_row, cur_col = start_pos

    while min_col < cur_col < max_col and cur_row < max_row:
        if grid[cur_row+1][cur_col] == AIR:
            # Go down
            cur_row, cur_col = cur_row+1, cur_col
        elif grid[cur_row+1][cur_col-1] == AIR:
            # Go down-left
            cur_row, cur_col = cur_row+1, cur_col-1
        elif grid[cur_row+1][cur_col+1] == AIR:
            # Go down-right
            cur_row, cur_col = cur_row+1, cur_col+1
        else:
            # Stop sand
            grid[cur_row][cur_col] = SAND

            if (cur_row, cur_col) == start_pos:
                # The sand didn't move, stop execution:
                return False
            else:
                # The sand moved, continue execution
                return True

    # Sand didn't stop
    return False


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        input_lines = open_file_lines(filepath)

        input_list_pairs = []

        for pair_list in input_lines:
            input_list_pairs.append([])
            for pair in pair_list.split(" -> "):
                pair = pair.split(",")
                input_list_pairs[-1].append((int(pair[0]), int(pair[1])))

        min_row = 0
        max_row = get_side(False, True, input_list_pairs) + 2

        min_col = START_POS[0] - max_row
        max_col = START_POS[0] + max_row

        start_pos = (START_POS[1] - min_row, START_POS[0] - min_col)

        rows = max_row - min_row + 1
        cols = max_col - min_col + 1

        grid = [[AIR] * cols for x in range(rows-1)]
        grid.append([ROCK] * cols)

        for pair_list in input_list_pairs:
            start = pair_list[0]

            for end in pair_list[1:]:
                if start[0] == end[0]:
                    step = 1 if start[1] <= end[1] else -1
                    for i in range(start[1], end[1]+step, step):
                        i = i - min_row
                        grid[i][start[0]-min_col] = ROCK

                else:
                    step = 1 if start[0] <= end[0] else -1
                    for i in range(start[0], end[0]+step, step):
                        i = i-min_col
                        grid[start[1]-min_row][i] = ROCK

                start = end

        grid[start_pos[0]][start_pos[1]] = START

        print_grid(grid)

        counter = 0

        while drop_sand(grid, start_pos, 0, cols - 1, rows - 1):
            counter += 1

        print_grid(grid)

        return counter + 1


p2 = Part_2()
p2.test(93)
p2.execute()
