"""
Problem 1
Fill in the Line class methods to accept coordinates as a pair of tuples
and return the slope and distance of the line.
"""

from math import pi


class Line:
    """
    Line operations
    Accepts two coordinates
    distance: finds distance between two points
    slope: find slope between two points
    """

    def __init__(self, coor1: tuple[int, int], coor2: tuple[int, int]):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x_1, y_1 = self.coor1
        x_2, y_2 = self.coor2

        return ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5

    def slope(self):
        x_1, y_1 = self.coor1
        x_2, y_2 = self.coor2
        return (y_2 - y_1) / (x_2 - x_1)


line = Line((3, 2), (8, 10))
print(line.distance())
print(line.slope())


"""
Problem 2
Fill in the Cylinder class methods to accept height and radius
and calculate volume and surface area
"""


class Cylinder:
    """
    Calculate Volume and Surface area of the cylinder
    """

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return round(pi * self.radius**2 * self.height, 2)

    def surface_area(self):
        return round(2 * pi * self.radius * (self.radius + self.height), 2)


cylinder = Cylinder(2, 3)
print(cylinder.volume())
print(cylinder.surface_area())
