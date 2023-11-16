class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def __str__(self):
        return f'<{self.breed} - {self.name}>'

    def __repr__(self):
        s = ', '.join(f'{k}={v}' for k, v in self.__dict__.items())
        return f'<{self.__class__.__name__} object ({s})>'

    def sound(self, n):
        print(f'{self.name} is ')
        for i in range(n):
            print('Woof')


if __name__ == '__main__':
    print(Dog.__name__)
    dog1 = Dog('Tuzik', 'Pitbull', 5)
    print(str(dog1))
    print(repr(dog1))
    # dog1.sound(5)
    # Dog.sound(self=dog1, n=5)
    # print(dog1.__class__.__name__)
    # print(type(dog1).__name__)

    dog2 = Dog('Bobik', 'Pitbull', 3)
    print(dog2)
    # dog2.sound(3)

    dogs = [dog1, dog2]
    for dog in dogs:
        dog.sound(1)
        print(dog.__dict__)

    print(dogs)


# magic methods in python