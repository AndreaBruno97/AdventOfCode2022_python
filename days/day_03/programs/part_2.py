from common import *


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        backpack_list = open_file_str_array(filepath)

        total_priority = 0

        for index in range(0,len(backpack_list), 3):

            backpack_1 = backpack_list[index]
            backpack_2 = backpack_list[index + 1]
            backpack_3 = backpack_list[index + 2]

            backpack_set_1 = set(backpack_1)
            backpack_set_2 = set(backpack_2)
            backpack_set_3 = set(backpack_3)

            common_element = (backpack_set_1 & backpack_set_2 & backpack_set_3).pop()

            if common_element.islower():
                current_priority = ord(common_element) - ord('a') + 1
            else:
                current_priority = ord(common_element) - ord('A') + 27

            total_priority += current_priority

        return total_priority


p2 = Part_2()
p2.test(70)
p2.execute()
