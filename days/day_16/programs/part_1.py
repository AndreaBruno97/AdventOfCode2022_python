from common import *
import sys

TOTAL_TIME = 30


class Valve:
    def __init__(self, name, flow_rate, neighbor_init_list):
        self.name = name
        self.flow_rate = flow_rate
        self.is_open = False
        self.neighbors = []
        self.neighbor_init_list = neighbor_init_list

    def print_valve(self):
        print(f"Valve {self.name}: flow {self.flow_rate}, " + ("open" if self.is_open else "closed"))
        [print(f"\tNear valve {neighbor.name}") for neighbor in self.neighbors]


def find_max_flow(cur_valve: Valve, cur_flow, cur_time_left, max_flow, max_flow_rate):
    if cur_time_left == 0:
        if cur_flow > max_flow:
            max_flow = cur_flow
            print(max_flow)
        return max_flow

    new_time_left = cur_time_left - 1

    if cur_flow + (max_flow_rate * new_time_left * new_time_left)/2 < max_flow:
        return max_flow

    if cur_valve.is_open is False and cur_valve.flow_rate > 0:
        # Try to open valve
        cur_valve.is_open = True
        max_flow = find_max_flow(cur_valve, cur_flow + (cur_valve.flow_rate * new_time_left), new_time_left,
                                 max_flow, max_flow_rate)
        cur_valve.is_open = False

    for neighbor in cur_valve.neighbors:
        # Go to other valves
        max_flow = find_max_flow(neighbor, cur_flow, new_time_left, max_flow, max_flow_rate)

    return max_flow


class Valve_list:

    def __init__(self, init_lines):
        self.valves = []
        separator = "|"

        # Init Valves
        for line in init_lines:
            line = line \
                .replace("Valve ", "") \
                .replace(" has flow rate=", separator) \
                .replace("; tunnels lead ", "") \
                .replace("; tunnel leads ", "") \
                .replace("to valve ", separator) \
                .replace("to valves ", separator)

            valve_name, valve_flow, valve_neighbor_list = line.split(separator)

            self.valves.append(
                Valve(
                    valve_name,
                    int(valve_flow),
                    valve_neighbor_list.split(", ")
                )
            )

        # Init Valve Neighbors
        for valve in self.valves:
            valve.neighbors = [self.find_valve(cur_neighbor) for cur_neighbor in valve.neighbor_init_list]

    def find_valve(self, valve_name):
        return [valve for valve in self.valves if valve.name == valve_name][0]

    def print_valve_list(self):
        for valve in self.valves:
            valve.print_valve()


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        input_lines = open_file_lines(filepath)

        valve_list = Valve_list(input_lines)

        start_valve = valve_list.find_valve("AA")
        max_flow_rate = max(map(lambda x: x.flow_rate, valve_list.valves))

        return find_max_flow(start_valve, 0, TOTAL_TIME, 0, max_flow_rate)


p1 = Part_1()
p1.test(1651)
p1.execute()
