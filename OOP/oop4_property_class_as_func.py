class Square:
    def __init__(self, a: int):
        self.a = a

    def __str__(self):
        return '\n'.join('*  ' * self.a for i in range(self.a))

    def get_area(self):
        return self.a ** 2

    def set_area(self, area):
        # assert float.is_integer(area ** 0.5), 'Wrong area value!' # throw error
        if float.is_integer(area ** 0.5):
            self.a = int(area ** 0.5)
        else:
            print('Wrong area value!')

    area = property(fget=get_area, fset=set_area)


if __name__ == '__main__':
    square = Square(4)
    print(square.area)
    square.area = 36
    print(square)

