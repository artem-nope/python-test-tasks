import tkinter as tk

W, H = 500, 500
sq_size = 50
max_board_size = 401
is_white = True

root = tk.Tk()
canvas = tk.Canvas(root, width=W, height=H)
canvas.pack()

for i in range(sq_size, max_board_size, sq_size):
    for j in range(sq_size, max_board_size, sq_size):
        if is_white:
            canvas.create_rectangle(i, j, i + sq_size, j + sq_size, fill='white')
        else:
            canvas.create_rectangle(i, j, i + sq_size, j + sq_size, fill='black')
        is_white = not is_white
    is_white = not is_white
root.mainloop()
