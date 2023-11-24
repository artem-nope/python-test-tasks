import tkinter as tk

W, H = 600, 500
R, C = 5, 5

root = tk.Tk()
canvas = tk.Canvas(root, width=W, height=H, bg='black')
canvas.pack()

for i in range(1, R):
    x1 = 0
    y1 = i * H / R
    x2 = W
    y2 = y1
    canvas.create_line(x1, y1, x2, y2, fill='white', width=3)

for i in range(1, C):
    x1 = 0
    y1 = i * W / C
    x2 = W
    y2 = y1
    canvas.create_line(y1, x1, y2, x2, fill='white', width=3)


root.mainloop()
