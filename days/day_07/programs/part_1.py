from common import *

MAXIMUM_DIRECTORY_SIZE = 100000


class Node:

    TYPE_FILE = 0
    TYPE_DIR = 1

    def __init__(self, name, node_type, size, parent):
        self.name = name
        self.node_type = node_type
        self.size = 0 if node_type == self.TYPE_DIR else size
        self.parent = parent


def print_node_list(node_list, cur_node: Node = None, depth=0):
    if cur_node is None:
        cur_node = find_node(node_list, "/", None)

    current_tab = "\t" * depth
    print_debug(
        current_tab + "- " +
        cur_node.name + " (" +
        ("dir" if cur_node.node_type == Node.TYPE_DIR else f"file, size={cur_node.size}") +
        ")"
    )

    if cur_node.node_type == Node.TYPE_FILE:
        return
    else:
        for next_node in find_direct_children(node_list, cur_node):
            print_node_list(node_list, next_node, depth + 1)


def find_node(node_list, node_name, parent):
    return [
        x for x in node_list if
        x.name == node_name and x.parent == parent
    ][0]


def find_direct_children(node_list, node, node_type=None):

    return [
        x for x in node_list if
        x.parent == node and
        (
            node_type is None or
            x.node_type == node_type
        )
    ]


def directory_size(node_list, directory):
    total_size = 0

    for cur_file in find_direct_children(node_list, directory, Node.TYPE_FILE):
        total_size += cur_file.size

    for cur_directory in find_direct_children(node_list, directory, Node.TYPE_DIR):
        total_size += directory_size(node_list, cur_directory)

    return total_size


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        cmd_list = open_file_lines(filepath)

        # Node list initialization: root directory always present
        node_list = [Node("/", Node.TYPE_DIR, 0, None)]

        current_directory = None

        # Populate file system
        for cmd_line in cmd_list:
            command = cmd_line.split()

            if command[0] == "$":
                # User operations
                command_name = command[1]

                if command_name == "cd":
                    new_dir_name = command[2]

                    if new_dir_name == "..":
                        # Move up
                        current_directory = current_directory.parent
                    else:
                        # Move down
                        current_directory = find_node(node_list, new_dir_name, current_directory)

                elif command_name == "ls":
                    pass
            else:
                # Directory listing
                size_or_dir, node_name = command

                if size_or_dir == "dir":
                    # Directory
                    node_list.append(Node(node_name, Node.TYPE_DIR, 0, current_directory))
                else:
                    # File
                    node_list.append(Node(node_name, Node.TYPE_FILE, int(size_or_dir), current_directory))

        # Directory sizes computation

        total_directory_size = 0

        for cur_directory in [x for x in node_list if x.node_type == Node.TYPE_DIR]:
            cur_directory_size = directory_size(node_list, cur_directory)
            if cur_directory_size <= MAXIMUM_DIRECTORY_SIZE:
                total_directory_size += cur_directory_size

        return total_directory_size


p1 = Part_1()
p1.test(95437)
p1.execute()
