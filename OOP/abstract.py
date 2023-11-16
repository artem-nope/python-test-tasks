from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass


class Snake(Animal):
    def eat(self):
        print('snake is eating')


class Predator(Animal):
    def __init__(self, base):
        self.base = base

    def eat(self):
        self.base.eat()
        print('... other animals')


if __name__ == '__main__':
    # animal = Animal()
    # print(animal)
    snake = Snake()
    snake.eat()
    pr = Predator(snake)
    pr.eat()
