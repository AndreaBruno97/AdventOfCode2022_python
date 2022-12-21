from common import *


class Node:
    def __init__(self, monkey, value, left=None, right=None, operation=None):
        self.is_human = monkey == "humn"
        self.is_root = monkey == "root"

        self.name = monkey
        self.value = value
        self.left = left
        self.right = right
        self.parent = None
        self.operation = operation

        self.is_human_line = left is not None and left.is_human_line and right is not None and right.is_human_line


def get_monkey_node(monkey_dict, monkey):
    monkey_job = monkey_dict[monkey]

    if isinstance(monkey_job, int):
        return Node(monkey, monkey_job)
    else:
        left_monkey, operation, right_monkey = monkey_job
        left = get_monkey_node(monkey_dict, left_monkey)
        right = get_monkey_node(monkey_dict, right_monkey)
        monkey_node = Node(monkey, None, left, right, operation)

        left.parent = monkey_node
        right.parent = monkey_node

        return monkey_node


# This recursive function reduces the tree to an almost linear structure:
# each non-leaf node will have as children a leaf node and a node connected to "humn"
# The function returns the new reduced node, or None otherwise
def evaluate_monkey_tree(monkey: Node):
    if monkey.value is not None:
        return None

    if monkey.is_human or monkey.is_root:
        return None

    new_left = evaluate_monkey_tree(monkey.left)
    if new_left is not None:
        monkey.left = new_left

    new_right = evaluate_monkey_tree(monkey.right)
    if new_right is not None:
        monkey.right = new_right

    if monkey.left is None or new_right is None:
        return None

    if monkey.operation == "+":
        result = new_left.value + new_right.value
    elif monkey.operation == "-":
        result = new_left.value - new_right.value
    elif monkey.operation == "*":
        result = new_left.value * new_right.value
    elif monkey.operation == "/":
        result = int(new_left.value / new_right.value)

    return Node("new", result)


def evaluate_human_node(monkey: Node, current_total):
    if monkey.is_human:
        return current_total

    if monkey.left.is_human_line:
        next_in_human_line, num_value = monkey.left, monkey.right.value
    else:
        next_in_human_line, num_value = monkey.right, monkey.left.value

    if monkey.is_root:
        result = num_value
    elif monkey.operation == "+":
        result = current_total - num_value
    elif monkey.operation == "-":
        result = current_total + num_value
    elif monkey.operation == "*":
        result = int(current_total / num_value)
    elif monkey.operation == "/":
        result = current_total * num_value

    return evaluate_human_node(next_in_human_line, result)


def print_tree(monkey: Node, depth=0):
    if monkey is None:
        return

    string_to_print = "\t" * depth + monkey.name + ("" if monkey.value is None else f": {monkey.value}")

    if monkey.is_human:
        print_debug(string_to_print)
    else:
        print(string_to_print)

    print_tree(monkey.left, depth + 1)
    print_tree(monkey.right, depth + 1)


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        input_lines = open_file_lines(filepath)

        monkey_dict = {}

        for line in input_lines:
            monkey, job = line.split(": ")
            job = job.split(" ")

            monkey_dict[monkey] = int(job[0]) if len(job) == 1 else job

        root = get_monkey_node(monkey_dict, "root")

        evaluate_monkey_tree(root)
        print_tree(root)

        return evaluate_human_node(root, 0)


p2 = Part_2()
p2.test(301)
p2.execute()
