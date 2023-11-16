import math
from math import isclose


class Vector2d:
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'<x={self.x:.3f}, y={self.y:.3f}>'

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.x + other.x, self.y + other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return self.__class__(self.x + other, self.y + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.__class__(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return isclose(self.x, other.x) and isclose(self.y, other.y)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, int) or isinstance(other, float):
            return self.__class__(self.x * other, self.y * other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __lt__(self, other):
        return float((self.x ** 2 + self.y ** 2) ** 0.5) < float((other.x ** 2 + other.y ** 2) ** 0.5)



if __name__ == '__main__':
    print(Vector2d(1, 2) + Vector2d(2, 3))
    print(Vector2d(1, 2) + 1)
    print(1 + Vector2d(1, 2))
    # print(Vector2d(1, 2) + str(1))
    print(2 + 3)
    print((2).__add__(3))
