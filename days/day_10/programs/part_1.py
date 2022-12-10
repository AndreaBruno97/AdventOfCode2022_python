from common import *


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        instruction_list = open_file_lines(filepath)
        register = 1
        cur_cycle = 1
        result = 0

        for instruction in [x.split() for x in instruction_list]:
            cur_cycle += 1

            if cur_cycle in range(20, 221, 40):
                result += cur_cycle * register

            if instruction[0] == "addx":
                cur_cycle += 1
                register += int(instruction[1])

                if cur_cycle in range(20, 221, 40):
                    result += cur_cycle * register

        return result


p1 = Part_1()
p1.test(13140)
p1.execute()
