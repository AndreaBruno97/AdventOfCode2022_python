from common import *

ROW_TO_SLICE_TEST = 10
ROW_TO_SLICE_MAIN = 2000000


def interval_union(range_list):
    result = []
    for begin, end in sorted(range_list):
        if result and result[-1][1] >= begin - 1:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([begin, end])

    return result


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        is_example = "input.txt" not in filepath
        row_to_slice = ROW_TO_SLICE_TEST if is_example else ROW_TO_SLICE_MAIN

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

        sensor_influence_list = []

        for cur_index in range(len(sensor_list)):
            cur_sensor_row, cur_sensor_col = sensor_list[cur_index]
            cur_beacon_row, cur_beacon_col = beacon_list[cur_index]

            dist_from_beacon_row = abs(cur_sensor_row - cur_beacon_row)
            dist_from_beacon_col = abs(cur_sensor_col - cur_beacon_col)
            distance = dist_from_beacon_row + dist_from_beacon_col

            radius = distance - abs(cur_sensor_row - row_to_slice)

            if radius >= 0:
                sensor_influence_list.append((cur_sensor_col-radius, cur_sensor_col+radius))

        sensor_influence_union_list = interval_union(sensor_influence_list)

        result = 0
        for interval in sensor_influence_union_list:
            result += interval[1] - interval[0] + 1

        overlapped_beacons = set()
        for beacon in beacon_list:
            if beacon[0] == row_to_slice:
                overlapped_beacons.add(beacon)

        return result - len(overlapped_beacons)


p1 = Part_1()
p1.test(26)
p1.execute()
