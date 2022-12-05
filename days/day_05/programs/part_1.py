from common import *
from textwrap import wrap


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        file_lines = open_file_lines(filepath)
        split_index = file_lines.index("")
        stack_configuration_lines = file_lines[:split_index]
        instruction_lines = file_lines[split_index + 1:]

        # Stack list construction
        stack_configuration_lines.reverse()
        stack_names = stack_configuration_lines[0].split()
        stack_dict = {stack_name: [] for stack_name in stack_names}

        for stack_configuration_elem in stack_configuration_lines[1:]:
            stack_configuration_elem_split = wrap(stack_configuration_elem, 4, drop_whitespace=False)

            for stack_name, stack_value in zip(stack_names, stack_configuration_elem_split):
                cur_value = stack_value.replace("[", "").replace("]", "").replace(" ", "")

                if cur_value != "":
                    stack_dict[stack_name].append(cur_value)

        # Moves execution
        for instruction in instruction_lines:
            _, iteration_num, _, src_stack, _, dest_stack = instruction.split()

            for i in range(int(iteration_num)):
                moved_value = stack_dict[src_stack].pop()
                stack_dict[dest_stack].append(moved_value)

        # Computing solution
        stack_list = list(stack_dict.values())
        top_stack_list = [x.pop() for x in stack_list]
        solution = ''.join(top_stack_list)

        return solution


p1 = Part_1()
p1.test("CMZ")
p1.execute()
