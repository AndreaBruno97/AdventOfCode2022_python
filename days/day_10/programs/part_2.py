from common import *


def print_cycle(cur_cycle, register_value):
    horizontal_position = (cur_cycle - 1) % 40
    character_to_print = ""

    if horizontal_position == 0 and cur_cycle != 1:
        character_to_print += "\n"

    character_to_print += u"\u2588" if horizontal_position in range(register_value - 1, register_value + 2) else "."

    return character_to_print


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        instruction_list = open_file_lines(filepath)
        register = 1
        cur_cycle = 1
        result = ""

        for instruction in [x.split() for x in instruction_list]:
            result += print_cycle(cur_cycle, register)

            cur_cycle += 1

            if instruction[0] == "addx":
                result += print_cycle(cur_cycle, register)

                cur_cycle += 1
                register += int(instruction[1])

        return result


p2 = Part_2()
p2.test(
    """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....""",
    solution_in_new_line=True
)
p2.execute(solution_in_new_line=True)
