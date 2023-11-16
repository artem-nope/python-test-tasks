class SuperHero:
    def __init__(self, name):
        self.name = name

    def greet(self):
        # super().greet()
        print(f"Hello, I'm {self.name}")


class FlyingSuperHero(SuperHero):
    def greet(self):
        super().greet()
        print('I can fly.')


class GirlSuperHero(SuperHero):
    def greet(self):
        super().greet()
        print('I\'m beautiful.')


class FlyingGirlSuperHero(GirlSuperHero, FlyingSuperHero):
    def greet(self):
        super().greet()


if __name__ == '__main__':
    superman = FlyingSuperHero('Superman')
    superman.greet()
    catwoman = GirlSuperHero('Catwoman')
    catwoman.greet()
    supergirl = FlyingGirlSuperHero('Supergirl')
    supergirl.greet()
    print(SuperHero.__mro__)
    print(FlyingSuperHero.__mro__)
    print(GirlSuperHero.__mro__)
    print(FlyingGirlSuperHero.__mro__)