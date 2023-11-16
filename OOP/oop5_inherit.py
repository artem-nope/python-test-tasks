class Tree:
    def __init__(self, species, height):
        self.species = species
        self.height = height

    def __str__(self):
        return f'The {self.species} tree has {self.height} m'

    def cut(self, x):
        if x < self.height:
            self.height -= x
        else:
            print('Too much!')


class FruitTree(Tree):
    def __init__(self, species, height, harvest):
        # Tree.__init__(self, species, height)
        super().__init__(species, height)
        self.harvest = harvest

    def __str__(self):
        return super().__str__() + f', harvest is {self.harvest} kg'

    def fruit(self):
        print(f'We get {self.harvest} kilos of {self.species}s')


if __name__ == '__main__':
    tree = Tree('oak', 2)
    tree.cut(0.2)
    print(tree)
    apple = FruitTree('Apple', 2, 10)
    apple.cut(0.5)
    print(apple)
    apple.fruit()