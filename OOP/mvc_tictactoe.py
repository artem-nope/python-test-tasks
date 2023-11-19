class View:
    def __init__(self, mask):
        self.mask = mask

    def start_game(self):
        print('TIC TAC TOE')

    def end_free_cells(self):
        print('There are no possible moves')
        print('Draw!')

    def end_game(self):
        print('Game over')

    def win_game(self, name):
        print(f'{name} won!')

    def display_field(self, cells_values):
        for i in range(3):
            for j in range(3):
                print(f'{self.mask[cells_values[i * 3 + j]]}', end='  ')
            print()

    def get_move(self, name, free_cells_idxs):
        print(f'Player {name} is next: ', free_cells_idxs)
        while True:
            try:
                move = int(input('>>> '))
            except ValueError:
                print('Wrong format')
            else:
                if move not in free_cells_idxs:
                    print('The cell is not empty')
                else:
                    return move


class Field:
    win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6))

    def __init__(self):
        self.cells = [0] * 9

    def get_cells_values(self):
        return tuple(self.cells)

    def get_free_cells_idxs(self):
        return tuple(i for i, v in enumerate(self.cells) if v == 0)

    def is_win(self, value):
        # for wc in self.win_combinations:
        #     if all(value == self.cells[i] for i in wc):
        #         return True
        # return False
        if any(self.cells[a] == self.cells[b] == self.cells[c] == value for a, b, c in self.win_combinations):
            return True
        else:
            return False
        # if self.cells[0] == self.cells[1] == self.cells[2] == value \
        #         or self.cells[0] == self.cells[4] == self.cells[8] == value \
        #         or self.cells[2] == self.cells[4] == self.cells[6] == value \
        #         or self.cells[3] == self.cells[4] == self.cells[5] == value \
        #         or self.cells[6] == self.cells[7] == self.cells[8] == value \
        #         or self.cells[0] == self.cells[3] == self.cells[6] == value \
        #         or self.cells[1] == self.cells[4] == self.cells[7] == value \
        #         or self.cells[2] == self.cells[5] == self.cells[8] == value:
        #     return True
        # else:
        #     return False

    def set_cell_value(self, idx, value):
        self.cells[idx] = value

    def is_any_free_cells(self):
        return 0 in self.cells


class Player:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value


class Game:
    def __init__(self):
        self.view = View({
            1: '\u00D8',
            2: '\u0058',
            0: '\u22C5'
        })
        self.field = Field()
        self.player1 = Player('Ivan', 1)
        self.player2 = Player('Petr', 2)
        self.is_first = True

    def start(self):
        self.view.start_game()
        self.show_field()
        while True:
            if self.is_first:
                active_player = self.player1
            else:
                active_player = self.player2
            move = self.view.get_move(
                active_player.get_name(),
                self.field.get_free_cells_idxs()
            )
            self.field.set_cell_value(move, active_player.get_value())
            self.show_field()
            if self.field.is_win(active_player.get_value()):
                self.view.win_game(active_player.get_name())
                break
            if not self.field.is_any_free_cells():
                self.view.end_free_cells()
                break
            self.is_first = not self.is_first

        self.view.end_game()

    def show_field(self):
        self.view.display_field(self.field.get_cells_values())


if __name__ == '__main__':
    game = Game()
    game.start()
