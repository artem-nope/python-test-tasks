class Girl:
    ADULT_AGE = 18

    counter = 0

    @staticmethod
    def info():
        print('Women rule the world.')

    # @staticmethod
    # def get_dg_girl(name, age):
    #     return (Girl(name, age, 'D&G')

    @classmethod
    def get_dg_girl(cls, name, age):
        return cls(name, age, 'D&G')

    def __init__(self, name, age, brand):
        self.name = name
        self.age = age
        self.brand = brand
        self.__class__.counter += 1
        self.index = self.__class__.counter
        # self.counter += 1
        # self.index = self.counter

    def __str__(self):
        return f'{self.name} with age {self.age} wears "{self.brand}"({self.index})'

    def is_adult(self):
        # return self.age >= self.ADULT_AGE
        return self.age >= self.__class__.ADULT_AGE


class StudentGirl(Girl):
    def __init__(self, name, age, brand, edu):
        super().__init__(name, age, brand)
        self.edu = edu

    def __str__(self):
        return super().__str__() + f', education is {self.edu}'

    def study(self):
        print(f'{self.name} is studying')


if __name__ == '__main__':
    Girl.info()
    # girl1 = Girl('Olya', 21, 'D&G')
    girl1 = Girl.get_dg_girl('Olya', 21)
    girl2 = Girl('Inna', 17, 'Gucci')
    girl3 = Girl.get_dg_girl('Natasha', 22)
    girl4 = StudentGirl('Sasha', 16, 'Armani', 'Math')
    girls = [girl4, girl2, girl1, girl3]

    for g in girls:
        print(g)
        if g.is_adult():
            print('Can drink champagne')

        # if type(g) == StudentGirl:
        if isinstance(g, StudentGirl):
            g.study()
