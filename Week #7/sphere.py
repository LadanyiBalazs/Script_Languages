#!/usr/bin/env python3
from cmath import pi
import math
math.pi


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return  4 * pi * self.radius ** 2
    
    def volume(self):
        return (4 * pi * self.radius ** 3) / 3

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __str__(self):
        return "Sphere: {0}".format(self.radius)

def main():
    sphere = Sphere(10)
    sphere2 = Sphere(11)
    print("Surface area: ", sphere.area())
    print("Volume: ", sphere.volume())
    print("Surface area 2: ", sphere2.area())
    print("Volume 2: ", sphere2.volume())
    print("sphere > than sphere2: ", sphere  > sphere2)
    print("sphere < than sphere2: ", sphere  < sphere2)
    print("sphere >= than sphere2: ", sphere  >= sphere2)
    print("sphere <= than sphere2: ", sphere  <= sphere2)

    
if __name__ == "__main__":
    main()