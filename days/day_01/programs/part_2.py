from common import *
from queue import PriorityQueue
from functools import reduce


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        line_array = open_file_lines(filepath)

        # adding a final blank line to compute the last elf's calories
        line_array.append("")

        max_calories = PriorityQueue()
        cur_calories = 0
        for line in line_array:
            if line != "":
                # standard case: accumulating current elf's calories
                cur_calories += int(line)
            else:
                # The new calorie count is added into a priority queue
                # and if there are more than three elements, the smallest one is removed
                # smaller number = higher priority, so the biggest numbers remain in the queue
                max_calories.put(cur_calories)
                if max_calories.qsize() > 3:
                    max_calories.get()

                cur_calories = 0

        return reduce(lambda a, b: a+b, max_calories.queue)


p2 = Part_2()
p2.test(45000)
p2.execute()
