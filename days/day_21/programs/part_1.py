from common import *


def get_monkey_value(monkey_dict, monkey):
    monkey_job = monkey_dict[monkey]

    if isinstance(monkey_job, int):
        return monkey_job

    first_monkey, operation, second_monkey = monkey_job

    first_operand = get_monkey_value(monkey_dict, first_monkey)
    second_operand = get_monkey_value(monkey_dict, second_monkey)

    if operation == "+":
        result = first_operand + second_operand
    elif operation == "-":
        result = first_operand - second_operand
    elif operation == "*":
        result = first_operand * second_operand
    elif operation == "/":
        result = int(first_operand / second_operand)

    monkey_dict[monkey] = result

    return result


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        input_lines = open_file_lines(filepath)

        monkey_dict = {}

        for line in input_lines:
            monkey, job = line.split(": ")
            job = job.split(" ")

            monkey_dict[monkey] = int(job[0]) if len(job) == 1 else job

        return get_monkey_value(monkey_dict, "root")


p1 = Part_1()
p1.test(152)
p1.execute()
