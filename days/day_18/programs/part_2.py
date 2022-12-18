from common import *


# Each cube's coordinate is mapped into a new set of coordinates
# that maps the center of each of its surface planes.
# As an example in 2D:
#
# The coordinates inside the grid are the starting ones, and the axes refer to the new coordinate system
# for the surfaces. Each "#" inside the grid is a contact surface for the squares (starting coordinates)
# adjacent to it.
# For example, the square (2,2) is mapped into [Left: (2, 3), Right: (4, 3), Bottom: (3, 2), Top: (3, 4)]
#
# Along each axis, the surfaces are defined by a coordinate value 2*coord and (2*coord)-2
# The coordinates at the level of the square's middle have a value of (2*coord)-1
# (for example the x coordinate for top and bottom surfaces, and the y coordinate for left and right surfaces)
#
# 6   |      #             #             #
#     |
# 5   #     1,3     #     2,3     #     3,3     #
#     |
# 4   |      #             #             #
#     |
# 3   #     1,2     #     2,2     #     3,2     #
#     |
# 2   |      #             #             #
#     |
# 1   #     1,1     #     2,1     #     3,1     #
#     |
# 0  -+------#-------------#-------------#--------
#     0      1      2      3      4      5      6
#
# In 3D, defining as x+, y+, z+ the surface's coordinates "ahead of the cube's middle point",
# x-, y-, z- the ones "behind" it and x, y, z the ones "at the same level",
# the sides are:
#   - Right:    x+, y, z
#   - Left:     x-, y, z
#   - Front:    x, y+, z
#   - Back:     x, y-, z
#   - Top:      x, y, z+
#   - Bottom:   x, y, z-

# Comments for part 2:
# Instead of calculating the surface of the lava droplet, calculate the surface of the "inverse lava droplet":
# considering all the air cubes outside the droplet, visiting only the air cubes adjacent to the external ones,
# and counting only the contact surface, the result is the same one as counting only the droplet's external surface


def update_surface_counter(surface_dict_counter, new_surface_tuple):
    new_surface_key = str(new_surface_tuple)

    if new_surface_key in surface_dict_counter:
        surface_dict_counter[new_surface_key] += 1
    else:
        surface_dict_counter[new_surface_key] = 1


def get_adjacent(cube, min_x, max_x, min_y, max_y, min_z, max_z):
    x, y, z = cube
    result = []

    if x > min_x:
        result.append([x-1, y, z])
    if x < max_x:
        result.append([x+1, y, z])
    if y > min_y:
        result.append([x, y-1, z])
    if y < max_y:
        result.append([x, y+1, z])
    if z > min_z:
        result.append([x, y, z-1])
    if z < max_z:
        result.append([x, y, z+1])

    return result


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        cubes_list = [[int(i) for i in cube.split(",")] for cube in open_file_lines(filepath)]

        # Get minimum and maximum coordinates for the air cube:
        min_x = min(map(lambda cur_cube: cur_cube[0], cubes_list)) - 1
        max_x = max(map(lambda cur_cube: cur_cube[0], cubes_list)) + 1
        min_y = min(map(lambda cur_cube: cur_cube[1], cubes_list)) - 1
        max_y = max(map(lambda cur_cube: cur_cube[1], cubes_list)) + 1
        min_z = min(map(lambda cur_cube: cur_cube[2], cubes_list)) - 1
        max_z = max(map(lambda cur_cube: cur_cube[2], cubes_list)) + 1

        visited = {}

        for cur_x in range(min_x, max_x + 1):
            for cur_y in range(min_y, max_y + 1):
                for cur_z in range(min_z, max_z + 1):
                    visited[str([cur_x, cur_y, cur_z])] = False

        next_air_cubes = [[min_x, min_y, min_z]]

        while len(next_air_cubes) > 0:
            new_next_air_cubes = []
            for cur_cube in next_air_cubes:
                for next_cube in get_adjacent(cur_cube, min_x, max_x, min_y, max_y, min_z, max_z):
                    next_cube_str = str(next_cube)
                    if visited[next_cube_str] is False and next_cube not in cubes_list:
                        visited[next_cube_str] = True
                        new_next_air_cubes.append(next_cube)
            next_air_cubes = new_next_air_cubes

        air_list_str = [cube_coord for cube_coord, is_visited in visited.items() if is_visited is True]

        # Counter dictionary:
        #       - key is the surface coordinate as described below
        #       - value is the number of times the surface is present
        surface_dict_counter = {}

        for air_cube_str in air_list_str:
            cube_x, cube_y, cube_z = [int(x) for x in air_cube_str.replace("[", "").replace("]", "").split(",")]

            x_plus = (2 * cube_x)
            x = x_plus - 1
            x_minus = x_plus - 2

            y_plus = (2 * cube_y)
            y = y_plus - 1
            y_minus = y_plus - 2

            z_plus = (2 * cube_z)
            z = z_plus - 1
            z_minus = z_plus - 2

            # Right
            update_surface_counter(surface_dict_counter, (x_plus, y, z))
            # Left
            update_surface_counter(surface_dict_counter, (x_minus, y, z))
            # Front
            update_surface_counter(surface_dict_counter, (x, y_plus, z))
            # Back
            update_surface_counter(surface_dict_counter, (x, y_minus, z))
            # Top
            update_surface_counter(surface_dict_counter, (x, y, z_plus))
            # Bottom
            update_surface_counter(surface_dict_counter, (x, y, z_minus))

        total_air_surface = len([x for x in surface_dict_counter.values() if x == 1])
        width = max_x - min_x + 1
        height = max_y - min_y + 1
        depth = max_z - min_z + 1
        external_air_surface = 2*(width * height) + 2*(height * depth) + 2*(width * depth)

        return total_air_surface - external_air_surface


p2 = Part_2()
p2.test(58)
p2.execute()
