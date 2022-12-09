from common import *
import numpy as np


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        instruction_list = open_file_lines(filepath)
        visited_coordinates = {(0, 0)}

        head_coord = (0, 0)
        tail_coord = (0, 0)

        for direction, steps in [x.split() for x in instruction_list]:
            for i in range(int(steps)):
                if direction == "R":
                    # Head Right
                    head_coord = (
                        head_coord[0] + 1,
                        head_coord[1]
                    )
                elif direction == "D":
                    # Head Down
                    head_coord = (
                        head_coord[0],
                        head_coord[1] - 1
                    )
                elif direction == "L":
                    # Head Left
                    head_coord = (
                        head_coord[0] - 1,
                        head_coord[1]
                    )
                elif direction == "U":
                    # Head Up
                    head_coord = (
                        head_coord[0],
                        head_coord[1] + 1
                    )

                horizontal_distance = abs(head_coord[0] - tail_coord[0])
                vertical_distance = abs(head_coord[1] - tail_coord[1])

                # Horizontal Movement
                if horizontal_distance > 1 or (horizontal_distance == 1 and vertical_distance > 1):
                    tail_coord = (
                        tail_coord[0] + np.sign(head_coord[0] - tail_coord[0]),
                        tail_coord[1]
                    )

                # Horizontal Movement
                if vertical_distance > 1 or (vertical_distance == 1 and horizontal_distance > 1):
                    tail_coord = (
                        tail_coord[0],
                        tail_coord[1] + np.sign(head_coord[1] - tail_coord[1])
                    )

                visited_coordinates.add(tail_coord)

        return len(visited_coordinates)


p1 = Part_1()
p1.test(13)
p1.execute()
