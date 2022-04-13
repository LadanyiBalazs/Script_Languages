#!/usr/bin/env python3
from cmath import pi
import math
math.pi


class Ellipse:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return  self.a * self.b * pi

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
    ellipse = Ellipse(10, 10)
    ellipse2 = Ellipse(11, 11)
    print("Area: ", ellipse.area())
    print("Area 2: ", ellipse.area())
    print("ellipse > than ellipse2: ", ellipse  > ellipse2)
    print("ellipse < than ellipse2: ", ellipse  < ellipse2)
    print("ellipse >= than ellipse2: ", ellipse  >= ellipse2)
    print("ellipse <= than ellipse2: ", ellipse  <= ellipse2)

    
if __name__ == "__main__":
    main()