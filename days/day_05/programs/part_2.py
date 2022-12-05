from common import *
from textwrap import wrap


class Part_2(BaseClass):

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
            _, blocks_num_str, _, src_stack_key, _, dest_stack_key = instruction.split()

            blocks_num = int(blocks_num_str)

            src_stack = stack_dict[src_stack_key]
            removing_index = len(src_stack) - blocks_num
            moved_values = src_stack[removing_index:]
            del src_stack[removing_index:]
            stack_dict[dest_stack_key].extend(moved_values)

        # Computing solution
        stack_list = list(stack_dict.values())
        top_stack_list = [x.pop() for x in stack_list]
        solution = ''.join(top_stack_list)

        return solution


p2 = Part_2()
p2.test("MCD")
p2.execute()
