class Boy:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'Boy with name={self.__name} and age={self.__age}'

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def plus_year(self):
        self.__age += 1


if __name__ == '__main__':
    boy1 = Boy('Misha', 17)
    print(boy1)
    # print(boy1.__name, boy1.__age)
    print(boy1.get_name(), boy1.get_age())
    # boy1.__age += 1
    boy1.set_name('Michael')
    boy1.plus_year()
    print(boy1)
    # print(boy1._Boy__name) #!!!!!don't use it!!!!!


