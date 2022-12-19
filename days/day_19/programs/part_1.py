from common import *
import re

TOTAL_TIME = 24


class ROBOT_TYPES:
    ORE = "ore"
    CLAY = "clay"
    OBS = "obsidian"
    GEO = "geode"


class Factory:
    def __init__(self, init_line):
        match = re.search(r"Blueprint (\d+): Each ore robot costs (\d+) ore. " +
                          r"Each clay robot costs (\d+) ore. " +
                          r"Each obsidian robot costs (\d+) ore and (\d+) clay. " +
                          r"Each geode robot costs (\d+) ore and (\d+) obsidian.", init_line)

        blueprint_num_str = int(match.group(1))
        ore_num_for_ore_str = int(match.group(2))
        ore_num_for_clay_str = int(match.group(3))
        ore_num_for_obs_str = int(match.group(4))
        clay_num_for_obs_str = int(match.group(5))
        ore_num_for_geo_str = int(match.group(6))
        obs_num_for_geo_str = int(match.group(7))

        self.blueprint_num = blueprint_num_str
        self.ore_num_for_ore = ore_num_for_ore_str
        self.ore_num_for_clay = ore_num_for_clay_str
        self.ore_num_for_obs = ore_num_for_obs_str
        self.clay_num_for_obs = clay_num_for_obs_str
        self.ore_num_for_geo = ore_num_for_geo_str
        self.obs_num_for_geo = obs_num_for_geo_str

        self.ores = 0
        self.ore_robots = 1
        self.clay = 0
        self.clay_robots = 0
        self.obsidian = 0
        self.obs_robots = 0
        self.geodes = 0
        self.geo_robots = 0

    def create_robot(self, robot_type: ROBOT_TYPES, reverse=False):
        reverse_factor = -1 if reverse else 1
        if robot_type == ROBOT_TYPES.ORE:
            if self.ores < self.ore_num_for_ore:
                return False
            else:
                self.ores -= self.ore_num_for_ore * reverse_factor
                self.ore_robots += reverse_factor
                return True

        elif robot_type == ROBOT_TYPES.CLAY:
            if self.ores < self.ore_num_for_clay:
                return False
            else:
                self.ores -= self.ore_num_for_clay * reverse_factor
                self.clay_robots += reverse_factor
                return True

        elif robot_type == ROBOT_TYPES.OBS:
            if self.ores < self.ore_num_for_obs or self.clay < self.clay_num_for_obs:
                return False
            else:
                self.ores -= self.ore_num_for_obs * reverse_factor
                self.clay -= self.clay_num_for_obs * reverse_factor
                self.obs_robots += reverse_factor
                return True
        else:
            if self.ores < self.ore_num_for_geo or self.obsidian < self.obs_num_for_geo:
                return False
            else:
                self.ores -= self.ore_num_for_geo * reverse_factor
                self.obsidian -= self.obs_num_for_geo * reverse_factor
                self.geo_robots += reverse_factor
                return True

    def gather_resources(self, reverse=False):
        reverse_factor = -1 if reverse else 1

        self.ores += self.ore_robots * reverse_factor
        self.clay += self.clay_robots * reverse_factor
        self.obsidian += self.obs_robots * reverse_factor
        self.geodes += self.geo_robots * reverse_factor


def find_max_quality(factory, cur_time, max_geodes):
    if cur_time == TOTAL_TIME:
        if factory.geodes > max_geodes:
            max_geodes = factory.geodes
        return max_geodes

    if factory.create_robot(ROBOT_TYPES.ORE):
        # Create Ore robot
        factory.gather_resources()
        factory.ores -= 1

        max_geodes = find_max_quality(factory, cur_time+1, max_geodes)

        factory.ores += 1
        factory.gather_resources(True)
        factory.create_robot(ROBOT_TYPES.ORE, True)

    if factory.create_robot(ROBOT_TYPES.CLAY):
        # Create Clay robot
        factory.gather_resources()
        factory.clay -= 1

        max_geodes = find_max_quality(factory, cur_time+1, max_geodes)

        factory.clay += 1
        factory.gather_resources(True)
        factory.create_robot(ROBOT_TYPES.CLAY, True)

    if factory.create_robot(ROBOT_TYPES.OBS):
        # Create Obsidian robot
        factory.gather_resources()
        factory.obsidian -= 1

        max_geodes = find_max_quality(factory, cur_time+1, max_geodes)

        factory.obsidian += 1
        factory.gather_resources(True)
        factory.create_robot(ROBOT_TYPES.OBS, True)

    if factory.create_robot(ROBOT_TYPES.OBS):
        # Create Obsidian robot
        factory.gather_resources()
        factory.geodes -= 1

        max_geodes = find_max_quality(factory, cur_time+1, max_geodes)

        factory.geodes += 1
        factory.gather_resources(True)
        factory.create_robot(ROBOT_TYPES.OBS, True)

    # Don't create anything
    factory.gather_resources()
    max_geodes = find_max_quality(factory, cur_time+1, max_geodes)

    return max_geodes


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        lines_str = open_file_lines(filepath)
        factory_list = [Factory(line) for line in lines_str]

        total_quality = 0

        for factory in factory_list:
            cur_quality = find_max_quality(factory, 0, 0)
            total_quality += cur_quality * factory.blueprint_num

        return total_quality


p1 = Part_1()
p1.test(12)
# p1.execute()
