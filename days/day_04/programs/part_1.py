from common import *


def is_fully_contained(pair_a, pair_b) -> bool:
    return pair_a[0] >= pair_b[0] and pair_a[1] <= pair_b[1]


class Part_1(BaseClass):

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

            if(
                    is_fully_contained(assignment_1, assignment_2) or
                    is_fully_contained(assignment_2, assignment_1)
            ):
                overlapping_count += 1

        return overlapping_count


p1 = Part_1()
p1.test(2)
p1.execute()
