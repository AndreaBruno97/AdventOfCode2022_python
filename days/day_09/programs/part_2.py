from common import *
import numpy as np


KNOTS_NUM = 10


def move_pair(cur_head_coord, cur_tail_coord, direction):
    horizontal_distance = abs(cur_head_coord[0] - cur_tail_coord[0])
    vertical_distance = abs(cur_head_coord[1] - cur_tail_coord[1])

    # Horizontal Movement
    if horizontal_distance > 1 or (horizontal_distance == 1 and vertical_distance > 1):
        cur_tail_coord = (
            cur_tail_coord[0] + np.sign(cur_head_coord[0] - cur_tail_coord[0]),
            cur_tail_coord[1]
        )

    # Horizontal Movement
    if vertical_distance > 1 or (vertical_distance == 1 and horizontal_distance > 1):
        cur_tail_coord = (
            cur_tail_coord[0],
            cur_tail_coord[1] + np.sign(cur_head_coord[1] - cur_tail_coord[1])
        )

    return cur_head_coord, cur_tail_coord


def print_knots(coordinate_list, x_offset=16, y_offset=11):
    map_to_print = np.chararray((31, 37))
    map_to_print[:] = '.'

    for index in reversed(range(len(coordinate_list))):
        x_coord, y_coord = coordinate_list[index]

        x_print_grid_position = x_coord + x_offset
        y_print_grid_position = y_offset - y_coord

        map_to_print[y_print_grid_position, x_print_grid_position] = "H" if index == 0 else str(index)

    for line in map_to_print:
        print("".join((map(str, line))).replace("'", "").replace("b", ""))
    print_debug("---")


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        instruction_list = open_file_lines(filepath)
        visited_coordinates = {(0, 0)}

        coordinates_list = [(0, 0) for x in range(KNOTS_NUM)]

        for direction, steps in [x.split() for x in instruction_list]:

            for i in range(int(steps)):
                if direction == "R":
                    # Head Right
                    coordinates_list[0] = (
                        coordinates_list[0][0] + 1,
                        coordinates_list[0][1]
                    )
                elif direction == "D":
                    # Head Down
                    coordinates_list[0] = (
                        coordinates_list[0][0],
                        coordinates_list[0][1] - 1
                    )
                elif direction == "L":
                    # Head Left
                    coordinates_list[0] = (
                        coordinates_list[0][0] - 1,
                        coordinates_list[0][1]
                    )
                elif direction == "U":
                    # Head Up
                    coordinates_list[0] = (
                        coordinates_list[0][0],
                        coordinates_list[0][1] + 1
                    )

                for cur_head_index, cur_tail_index in zip(range(KNOTS_NUM-1), range(1, KNOTS_NUM)):
                    coordinates_list[cur_head_index], coordinates_list[cur_tail_index] = \
                        move_pair(coordinates_list[cur_head_index], coordinates_list[cur_tail_index], direction)

                visited_coordinates.add(coordinates_list[9])

            # print_knots(coordinates_list)

        return len(visited_coordinates)


p2 = Part_2()
p2.test(1, [("example_2.txt", 36)])
p2.execute()
