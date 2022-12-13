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


def quick_sort(packet_list, left, right):
    if left >= right:
        return
    if left == right - 1:
        if not evaluate_pair(packet_list[left], packet_list[right]):
            packet_list[left], packet_list[right] = packet_list[right], packet_list[left]
        return

    pivot = int((left + right) / 2)
    quick_sort(packet_list, left, pivot)
    quick_sort(packet_list, pivot + 1, right)

    tmp_list = [None] * (right - left + 1)
    tmp_list_index = 0

    left_index = left
    right_index = pivot + 1

    while left_index <= pivot or right_index <= right:

        if left_index > pivot:
            take_left = False
        elif right_index > right:
            take_left = True
        else:
            take_left = evaluate_pair(packet_list[left_index], packet_list[right_index])

        if take_left:
            tmp_list[tmp_list_index] = packet_list[left_index]
            left_index += 1
        else:
            tmp_list[tmp_list_index] = packet_list[right_index]
            right_index += 1

        tmp_list_index += 1

    for tmp_iter_index in range(len(tmp_list)):
        packet_list[tmp_iter_index + left] = tmp_list[tmp_iter_index]


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        packet_list = [json.loads(x) for x in open_file_lines(filepath) if x != ""]

        start_pack = [[2]]
        end_pack = [[6]]
        packet_list.append(start_pack)
        packet_list.append(end_pack)

        quick_sort(packet_list, 0, len(packet_list) - 1)

        start_index = packet_list.index(start_pack)
        end_index = packet_list.index(end_pack)

        return (start_index + 1) * (end_index + 1)


p2 = Part_2()
p2.test(140)
p2.execute()
