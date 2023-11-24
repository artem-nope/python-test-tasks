import tkinter as tk

# px
FONT = (None, 30)
root = tk.Tk()
root.title('New window')
# root.geometry('500x400+300+200')
root.geometry('+400+300')
# def handler1():
#     print('Hello')
# btn1 = tk.Button(root, text='Click me', command=handler1)
entry_b = tk.Entry(root, font=FONT, width=5)
entry_b.insert(0, '-2')
entry_b.grid(row=0, column=1)

entry_c = tk.Entry(root, font=FONT, width=5)
entry_c.insert(0, '-3')
entry_c.grid(row=0, column=3)

btn1 = tk.Button(root, text='Calculate', font=FONT, width=20)
btn1.grid(row=1, column=0, columnspan=5, pady=10)
label1 = tk.Label(root, width=20, height=3, bg='white', font=FONT)
label1.grid(row=2, column=0, columnspan=5, pady=(0, 20))

tk.Label(root, font=FONT, text='X\u00B2 + ').grid(row=0, column=0)
tk.Label(root, font=FONT, text=' X + ').grid(row=0, column=2)
tk.Label(root, font=FONT, text=' = 0').grid(row=0, column=4)


def handler1():
    print('Hello')
    # label1.config(text='Hello')
    try:
        b = float(entry_b.get())
        c = float(entry_c.get())
    except ValueError:
        text = 'Wrong format. Must be numbers'
    else:
        d = b ** 2 - 4 * c
        if d > 0:
            x1 = (-b - d ** 0.5) / 2
            x2 = (-b + d ** 0.5) / 2
            text = f'x\u2081 = {x1:.3f}\nx\u2082 = {x2:.3f}'
        elif d == 0:
            x = -b / 2
            text = f'x = {x:.3f}'
        else:
            x1 = f'{-b/2:.3f} - {(-d) ** 0.5:.3f} i'
            x2 = f'{-b/2:.3f} + {(-d) ** 0.5:.3f} i'
            text = f'x\u2081 = {x1}\nx\u2082 = {x2}'

    finally:
        label1.config(text=text)


btn1.config(command=handler1)

root.mainloop()
