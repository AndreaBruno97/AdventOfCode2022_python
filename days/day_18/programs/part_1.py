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


def update_surface_counter(surface_dict_counter, new_surface_tuple):
    new_surface_key = str(new_surface_tuple)

    if new_surface_key in surface_dict_counter:
        surface_dict_counter[new_surface_key] += 1
    else:
        surface_dict_counter[new_surface_key] = 1


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):

        cubes_list = open_file_lines(filepath)

        # Counter dictionary:
        #       - key is the surface coordinate as described below
        #       - value is the number of times the surface is present
        surface_dict_counter = {}

        for cube in cubes_list:
            cube_x, cube_y, cube_z = [int(i) for i in cube.split(",")]

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

        return len([x for x in surface_dict_counter.values() if x == 1])


p1 = Part_1()
p1.test(64)
p1.execute()
