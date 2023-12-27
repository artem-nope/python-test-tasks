import tkinter as tk
import requests
from tkinter import simpledialog


URL_GET = 'http://127.0.0.1:8000/'
URL_POST = 'http://127.0.0.1:8000/create/'
URL_DELETE = 'http://127.0.0.1:8000/delete/'
URL_UPDATE = 'http://127.0.0.1:8000/update/'


def get_languages_data():
    return requests.get(URL_GET).json()


def update_label():
    data = get_languages_data()
    label.config(
        text='\n'.join(f"{item.get('id')}: {item.get('name')} ({item.get('rating')})" for item in data),
        height=len(data)+2
    )


def create_language():
    lang_data = ['name', 'year', 'rating']
    lang_dict = {}
    for n in lang_data:
        answer = simpledialog.askstring(f'{n}', f'Input language {n}')
        lang_dict[n] = answer
    requests.post(URL_POST, json=lang_dict)
    update_label()


def delete_language():
    answer = simpledialog.askstring('Delete', 'Input language id to delete')
    url = URL_DELETE + f'{answer}/'
    requests.delete(url)
    update_label()


def update_language():
    id = simpledialog.askstring('Update', 'Input language id to update')
    rating = simpledialog.askstring('Update', 'Input a new rating')
    data = {
        'rating': rating
    }
    url = URL_UPDATE + f'{id}/'
    req = requests.put(url, json=data)
    update_label()


root = tk.Tk()
label = tk.Label(root, width=30, height=3, font=(None, 20), bg='white')
label.pack()
but1 = tk.Button(root, text='Create', command=create_language)
but1.pack(side='left')
but2 = tk.Button(root, text='Delete', command=delete_language)
but2.pack(side='left')
but3 = tk.Button(root, text='Update', command=update_language)
but3.pack(side='left')
update_label()
root.mainloop()

