import tkinter as tk
from itertools import product
from copy import deepcopy

SQ_SIZE = 25
ROWS, COLUMNS = 20, 25
W, H = SQ_SIZE * COLUMNS, SQ_SIZE * ROWS
COLOR_GRID, COLOR_PRIMARY, COLOR_SECONDARY = 'grey', 'red', 'white'
FONT = (None, SQ_SIZE // 2)
BORN = (3,)
KEEP_ALIVE = (2, 3)


matrix_cells = [[0 for j in range(COLUMNS)] for i in range(ROWS)]
matrix_neighbors = [[0 for j in range(COLUMNS)] for i in range(ROWS)]

root = tk.Tk()
canvas = tk.Canvas(root, width=W, height=H, bg=COLOR_SECONDARY)
canvas.pack()


def draw():
    canvas.delete('all')
    calc_neighbors()

    for i, j in product(range(ROWS), range(COLUMNS)):
        x1, y1 = j * SQ_SIZE, i * SQ_SIZE
        if matrix_cells[i][j] == 1:
            x2 = x1 + SQ_SIZE
            y2 = y1 + SQ_SIZE
            canvas.create_rectangle(x1, y1, x2, y2, fill=COLOR_PRIMARY)
        canvas.create_text(x1 + SQ_SIZE // 2, y1 + SQ_SIZE // 2, fill=COLOR_GRID, font=FONT, text=f'{matrix_neighbors[i][j]}')

    for i in range(1, ROWS):
        x1, y1, x2, y2 = 0, i * SQ_SIZE, W, i * SQ_SIZE
        canvas.create_line(x1, y1, x2, y2, fill=COLOR_GRID, width=3)

    for i in range(1, COLUMNS):
        x1, y1, x2, y2 = 0, i * SQ_SIZE, W, i * SQ_SIZE
        canvas.create_line(y1, x1, y2, x2, fill=COLOR_GRID, width=3)


def left_click_handler(event):
    x, y = event.x, event.y
    i = y // SQ_SIZE
    j = x // SQ_SIZE
    matrix_cells[i][j] = 1 if matrix_cells[i][j] == 0 else 0
    draw()


def calc_neighbors():
    for i, j in product(range(ROWS), range(COLUMNS)):
        i1, i2 = max(0, i - 1), min(ROWS - 1, i + 1)
        j1, j2 = max(0, j - 1), min(COLUMNS - 1, j + 1)
        s = 0
        for row, col in product(range(i1, i2 + 1), range(j1, j2 + 1)):
            s += matrix_cells[row][col]
        matrix_neighbors[i][j] = s - matrix_cells[i][j]


def clear():
    for i, j in product(range(ROWS), range(COLUMNS)):
        matrix_cells[i][j] = 0
    draw()


def next_generation():
    matrix_cells_copy = deepcopy(matrix_cells)
    for i, j in product(range(ROWS), range(COLUMNS)):
        if matrix_cells_copy[i][j] == 0:
            if matrix_neighbors[i][j] in BORN:
                matrix_cells[i][j] = 1
        else:
            if matrix_neighbors[i][j] not in KEEP_ALIVE:
                matrix_cells[i][j] = 0
    draw()


frame = tk.Frame(root)
btn1 = tk.Button(frame, text='Eval', command=next_generation)
btn2 = tk.Button(frame, text='Clear', command=clear)
btn1.pack(side='left')
btn2.pack(side='right')

frame.pack(side='bottom')


draw()
canvas.bind('<Button-1>', left_click_handler)
root.mainloop()
