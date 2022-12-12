from common import *


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        backpack_list = open_file_str_matrix(filepath)

        total_priority = 0

        for backpack in backpack_list:
            middle_point = int(len(backpack)/2)

            first_half = set(backpack[:middle_point])
            second_half = set(backpack[middle_point:])

            common_element = first_half.intersection(second_half).pop()

            if common_element.islower():
                current_priority = ord(common_element) - ord('a') + 1
            else:
                current_priority = ord(common_element) - ord('A') + 27

            total_priority += current_priority

        return total_priority


p1 = Part_1()
p1.test(157)
p1.execute()
