import sys

from common import *
import itertools


class Node:

    def __init__(self, row, col, altitude):
        self.row = row
        self.col = col
        self.altitude = altitude
        self.weight = sys.maxsize
        self.parent = self

    def compare_point(self, point):
        return self.row == point[0] and self.col == point[1]

    def is_adjacent(self, node):
        horizontal_distance = abs(self.col - node.col)
        vertical_distance = abs(self.row - node.row)

        return horizontal_distance + vertical_distance <= 1 and self.altitude <= node.altitude + 1


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        initialization_grid = open_file_str_matrix(filepath)

        rows = len(initialization_grid)
        cols = len(initialization_grid[0])
        start_point = (-1, -1)
        end_point = (-1, -1)

        permanent = []
        temporary = []
        all_nodes = []

        for cur_row, cur_col in itertools.product(range(rows), range(cols)):
            cur_val = initialization_grid[cur_row][cur_col]

            if cur_val == "S":
                cur_val = "a"
            elif cur_val == "E":
                start_point = (cur_row, cur_col)
                cur_val = 'z'

            all_nodes.append(Node(cur_row, cur_col, ord(cur_val) - ord("a")))

        # Dijkstra
        start_node = [x for x in all_nodes if x.compare_point(start_point)][0]
        temporary.append(start_node)
        start_node.weight = 0

        while len(temporary) > 0:

            # Assign permanent labels
            if all(node.weight == sys.maxsize for node in temporary):
                break

            temporary.sort(key=lambda x: x.weight)
            new_permanent = temporary[0]
            temporary.remove(new_permanent)
            permanent.append(new_permanent)

            # Assign temporary labels
            for adjacent_to_new_permanent in [x for x in all_nodes if new_permanent.is_adjacent(x) and x not in permanent]:
                if adjacent_to_new_permanent.weight > new_permanent.weight + 1:
                    adjacent_to_new_permanent.weight = new_permanent.weight + 1
                    adjacent_to_new_permanent.parent = new_permanent
                    temporary.append(adjacent_to_new_permanent)

        return min([x.weight for x in all_nodes if x.altitude == 0])


p2 = Part_2()
p2.test(29)
p2.execute()
