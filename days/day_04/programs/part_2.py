from common import *


def is_overlapped(pair_a, pair_b) -> bool:
    return pair_a[1] >= pair_b[0] and pair_a[0] <= pair_b[1]


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    # true if pair_a is fully contained in pair_b

    def execute_internal(self, filepath):
        assignment_list = open_file_lines(filepath)

        overlapping_count = 0

        for assignment_pair in assignment_list:
            assignment_1, assignment_2 = assignment_pair.split(",")
            assignment_1 = [int(x) for x in assignment_1.split("-")]
            assignment_2 = [int(x) for x in assignment_2.split("-")]

            if is_overlapped(assignment_1, assignment_2):
                overlapping_count += 1

        return overlapping_count


p2 = Part_2()
p2.test(4)
p2.execute()
