import math


class Circle:
    @staticmethod
    def circle_def():
        print('This is a circle')

    @classmethod
    def circle_origin(cls, radius):
        return f'Circle centered at the origin and radius={radius}'

    def __init__(self, dot_x, dot_y, radius):
        self.dot_x = dot_x
        self.dot_y = dot_y
        self.radius = radius

    def __str__(self):
        return f'The circle with center x={self.dot_x}, y={self.dot_y} and radius={self.radius}'

    def circle_square(self):
        return math.pi * self.radius ** 2

    def circle_len(self):
        return 2 * math.pi * self.radius

    def is_inside(self, x, y):
        return True if (x - self.dot_x) ** 2 + (y - self.dot_y) ** 2 <= self.radius ** 2 else False


class ColoredCircle(Circle):
    def __init__(self, dot_x, dot_y, radius, color):
        super().__init__(dot_x, dot_y, radius)
        self.color = color

    def __str__(self):
        return super().__str__() + f' with color {self.color}'

