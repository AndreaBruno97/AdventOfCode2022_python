from common import *
import math

NUM_ROUNDS = 10000


class Monkey:

    def __init__(self, init_string):
        init_list = init_string.split("\n")
        self.name = int(init_list[0].replace("Monkey ", "").replace(":", ""))
        self.item_list = [int(x) for x in init_list[1].replace("  Starting items: ", "").split(", ")]

        self.operation_sign, self.operation_value = init_list[2].replace("  Operation: new = old ", "").split(" ")

        self.divisibility_test = int(init_list[3].replace("  Test: divisible by ", ""))
        self.destination_monkey_if_true = int(init_list[4].replace("    If true: throw to monkey ", ""))
        self.destination_monkey_if_false = int(init_list[5].replace("    If false: throw to monkey ", ""))

        self.activity_level = 0

    def update_item_level(self, item_level):
        new_operation_value = item_level if self.operation_value == "old" else int(self.operation_value)

        if self.operation_sign == "+":
            increased_item_level = item_level + new_operation_value
        else:
            increased_item_level = item_level * new_operation_value

        return increased_item_level

    def choose_next_monkey(self, item_level):
        if item_level % self.divisibility_test == 0:
            return self.destination_monkey_if_true
        else:
            return self.destination_monkey_if_false

    # It returns a list of couples:
    #   First - New item level
    #   Second - Monkey to trow the item to
    def take_turn(self):
        self.activity_level += len(self.item_list)
        result_list = []

        for cur_item in self.item_list:
            new_item_level = self.update_item_level(cur_item)
            new_monkey = self.choose_next_monkey(new_item_level)
            result_list.append((new_item_level, new_monkey))

        self.item_list = []
        return result_list


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        monkey_init_list = open_file(filepath).split("\n\n")
        monkey_list = [Monkey(x) for x in monkey_init_list]

        common_divisor = math.prod(map(lambda x: x.divisibility_test, monkey_list))

        for i in range(NUM_ROUNDS):
            for cur_monkey in monkey_list:
                new_item_list = cur_monkey.take_turn()

                for new_item_val, new_monkey in new_item_list:
                    monkey_list[new_monkey].item_list.append(new_item_val % common_divisor)

        activity_level_list = sorted(map(lambda x: x.activity_level, monkey_list))
        first_monkey, second_monkey = activity_level_list[-2:]

        return first_monkey * second_monkey


p2 = Part_2()
p2.test(2713310158)
p2.execute()
