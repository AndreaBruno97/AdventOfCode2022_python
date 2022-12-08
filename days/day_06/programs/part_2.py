from common import *


class Part_2(BaseClass):

    SUBSEQUENCE_LENGTH = 14

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


p2 = Part_2()
p2.test(19, [
    ("example_2.txt", 23),
    ("example_3.txt", 23),
    ("example_4.txt", 29),
    ("example_5.txt", 26),
])
p2.execute()
