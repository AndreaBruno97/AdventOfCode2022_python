from common import *
import json


def is_int(obj):
    return isinstance(obj, int)


def is_list(obj):
    return isinstance(obj, list)


def evaluate_pair(left, right):
    if is_int(left) and is_int(right):
        # Both integers
        if left == right:
            return None
        else:
            return left < right

    if is_int(left):
        left = [left]
    elif is_int(right):
        right = [right]

    for new_left, new_right in list(zip(left, right)):
        result = evaluate_pair(new_left, new_right)
        if result is not None:
            return result

    return evaluate_pair(len(left), len(right))


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        input_string = open_file(filepath)
        input_pairs = input_string.split("\n\n")

        pair_counter = 1
        result = 0

        for left, right in [[json.loads(x) for x in pair_str.split("\n")] for pair_str in input_pairs]:
            if evaluate_pair(left, right):
                result += pair_counter

            pair_counter += 1

        return result


p1 = Part_1()
p1.test(13)
p1.execute()
