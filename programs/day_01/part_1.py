from common import *


class Part_1(BaseClass):

    def __init__(self):
        super().__init__(1)

    def execute_internal(self, filepath):
        line_array = open_file_lines(filepath)

        # adding a final blank line to compute the last elf's calories
        line_array.append("")

        max_calories = -1
        cur_calories = 0
        for line in line_array:
            if line != "":
                # standard case: accumulating current elf's calories
                cur_calories += int(line)
            else:
                # comparing current elf's calories with current maximum
                if cur_calories > max_calories:
                    max_calories = cur_calories
                cur_calories = 0

        return max_calories


p1 = Part_1()
p1.test(24000)
p1.execute()

