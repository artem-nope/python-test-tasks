import tkinter as tk
from itertools import product
from copy import deepcopy


W, H = 600, 700
COLOR_BG, COLOR_BALL, COLOR_PAD = 'grey', 'red', 'white'
RADIUS = 20
PAD_W, PAD_H = 200, 30
DELAY = 50
KEY_LEFT, KEY_RIGHT = 2063660802, 2080438019
x, y = 100, 200
vx, vy = -10, -10
x_pad = W // 2


root = tk.Tk()
canvas = tk.Canvas(root, width=W, height=H, bg=COLOR_BG)
canvas.pack()
ball = canvas.create_oval(x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS, fill=COLOR_BALL, outline=COLOR_BALL)
pad = canvas.create_rectangle(x_pad - PAD_W // 2, H - PAD_H, x_pad + PAD_W // 2, H, fill=COLOR_PAD, outline=COLOR_PAD)


def key_pressed(e):
    # print(e.keycode)
    global x_pad
    if e.keycode == KEY_LEFT:
        x_pad -= 50
        canvas.coords(pad, x_pad - PAD_W // 2, H - PAD_H, x_pad + PAD_W // 2, H)
    if e.keycode == KEY_RIGHT:
        x_pad += 50
        canvas.coords(pad, x_pad - PAD_W // 2, H - PAD_H, x_pad + PAD_W // 2, H)


def mouse_move(e):
    global x_pad
    x_pad = e.x
    canvas.coords(pad, x_pad - PAD_W // 2, H - PAD_H, x_pad + PAD_W // 2, H)


def game():
    global vx, vy, x, y
    x += vx
    y += vy
    if x == 0 or x == W:
        vx = -vx
    if y == 0:
        vy = -vy
    if y == H - PAD_H and x_pad - PAD_W // 2 <= x <= x_pad + PAD_W // 2:
        vy = -vy
    if y == H:
        canvas.create_text(W // 2, H // 2, text='GAME OVER', font=(None, 50), fill=COLOR_BALL)
    else:
        canvas.coords(ball, x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS)
        root.after(DELAY, game)


game()
root.bind('<Key>', key_pressed)
canvas.bind('<Motion>', mouse_move)
root.mainloop()
