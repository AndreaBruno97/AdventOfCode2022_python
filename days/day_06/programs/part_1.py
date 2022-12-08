from common import *


class Part_1(BaseClass):

    SUBSEQUENCE_LENGTH = 4

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        sequence = open_file(filepath)

        for cur_position in range(self.SUBSEQUENCE_LENGTH-1, len(sequence)):
            cur_subsequence = set(list(sequence[cur_position-(self.SUBSEQUENCE_LENGTH-1):cur_position]))
            cur_subsequence.add(sequence[cur_position])

            if len(cur_subsequence) == self.SUBSEQUENCE_LENGTH:
                return cur_position + 1

        return -1


p1 = Part_1()
p1.test(7, [
    ("example_2.txt", 5),
    ("example_3.txt", 6),
    ("example_4.txt", 10),
    ("example_5.txt", 11),
])
p1.execute()
