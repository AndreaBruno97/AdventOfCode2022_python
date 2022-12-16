from common import *

MAX_ROW_TEST = 20
MAX_ROW_MAIN = 4000000


def interval_union(range_list):
    result = []
    for begin, end in sorted(range_list):
        if result and result[-1][1] >= begin - 1:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([begin, end])

    return result


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        is_example = "input.txt" not in filepath
        max_row = MAX_ROW_TEST if is_example else MAX_ROW_MAIN

        input_lines = open_file_lines(filepath)
        sensor_list = []
        beacon_list = []

        for line in input_lines:
            line = line\
                .replace("Sensor at ", "")\
                .replace("x=", "")\
                .replace(" y=", "")\
                .replace(" closest beacon is at ", "")\
                .replace(":", ",")

            sensor_col, sensor_row, beacon_col, beacon_row = line.split(",")
            sensor_list.append((int(sensor_row), int(sensor_col)))
            beacon_list.append((int(beacon_row), int(beacon_col)))

        for cur_slice in range(max_row):
            sensor_influence_list = []

            for cur_index in range(len(sensor_list)):
                cur_sensor_row, cur_sensor_col = sensor_list[cur_index]
                cur_beacon_row, cur_beacon_col = beacon_list[cur_index]

                dist_from_beacon_row = abs(cur_sensor_row - cur_beacon_row)
                dist_from_beacon_col = abs(cur_sensor_col - cur_beacon_col)
                distance = dist_from_beacon_row + dist_from_beacon_col

                radius = distance - abs(cur_sensor_row - cur_slice)

                if radius >= 0:
                    sensor_influence_list.append((cur_sensor_col - radius, cur_sensor_col + radius))

            sensor_influence_union_list = interval_union(sensor_influence_list)

            if len(sensor_influence_union_list) > 1:
                final_y = cur_slice
                final_x = sensor_influence_union_list[0][1] + 1

                return (final_x * 4000000) + final_y

        return -1


p2 = Part_2()
p2.test(56000011)
p2.execute()
