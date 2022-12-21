from common import *


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def print_node(self):
        print(f"{str(self.value)} -> {str(self.next.value)}")


class Node_list:
    def __init__(self, int_list):
        self.node_list_array = []
        self.head = Node(int_list[0])
        self.node_list_array.append(self.head)

        prev_node = self.head
        for cur_int in int_list[1:]:
            cur_node = Node(cur_int)
            self.node_list_array.append(cur_node)

            prev_node.next = cur_node
            cur_node.prev = prev_node

            prev_node = cur_node

        # Circular list: last node is followed by the first
        prev_node.next = self.head
        self.head.prev = prev_node

    def find_node_by_value(self, value):
        cur_node = self.head

        while True:
            if cur_node.value == value:
                return cur_node

            if cur_node.next == self.head:
                return None

            cur_node = cur_node.next

    def switch_nodes(self, node_to_switch: Node, new_previous_node: Node):
        if node_to_switch == new_previous_node:
            return

        node_to_switch.prev.next = node_to_switch.next
        node_to_switch.next.prev = node_to_switch.prev

        node_to_switch.next = new_previous_node.next
        new_previous_node.next.prev = node_to_switch

        new_previous_node.next = node_to_switch
        node_to_switch.prev = new_previous_node

    def move_n_nodes(self, start_node: Node, moves_num):
        cur_node = start_node
        new_moves_num = moves_num if moves_num >= 0 else 1 + (moves_num * -1)
        for i in range(new_moves_num):
            if moves_num > 0:
                cur_node = cur_node.next
            else:
                cur_node = cur_node.prev

        return cur_node

    def iterate_on_nodes(self, iteration_function):
        for cur_node in self.node_list_array:
            iteration_function(self, cur_node)

    def print_node_list(self):
        cur_node = self.head

        while True:
            print(str(cur_node.value), end="")

            if cur_node.next == self.head:
                break
            else:
                cur_node = cur_node.next
                print(", ", end="")

    def get_list_len(self):
        return len(self.node_list_array)


def update_nodes(node_list: Node_list, node: Node):
    target_node = node_list.move_n_nodes(node, node.value)
    node_list.switch_nodes(node, target_node)


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        num_list = open_file_int_array(filepath)

        node_list = Node_list(num_list)

        node_list.iterate_on_nodes(update_nodes)

        # Result
        zero_index = node_list.find_node_by_value(0)
        first_num = node_list.move_n_nodes(zero_index, 1000 % node_list.get_list_len()).value
        second_num = node_list.move_n_nodes(zero_index, 2000 % node_list.get_list_len()).value
        third_num = node_list.move_n_nodes(zero_index, 3000 % node_list.get_list_len()).value

        return first_num + second_num + third_num


p1 = Part_1()
p1.test(3)
p1.execute()
