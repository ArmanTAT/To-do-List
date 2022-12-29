# This code is in Tkinter, there is another version where this one is made using Pygame which is in "pyGame.py"

import tkinter as tk

tasks = []

def add_task():
    task = entry.get()
    tasks.append(task)
    update_list()
    entry.delete(0, tk.END)

def remove_task():
    task = listbox.get(tk.ACTIVE)
    tasks.remove(task)
    update_list()

def update_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

window = tk.Tk()
window.title("Arman-Lists")

label = tk.Label(text="Enter a task:", font=("Helvetica", 16))
entry_frame = tk.Frame(bg="#ecf0f1")
entry = tk.Entry(entry_frame, font=("Helvetica", 16), bg="#ecf0f1")
add_button = tk.Button(text="Add", command=add_task, font=("Helvetica", 16), bg="#2ecc71")
remove_button = tk.Button(text="Remove", command=remove_task, font=("Helvetica", 16), bg="#e74c3c")
listbox = tk.Listbox(font=("Helvetica", 16))

label.pack(pady=10)
entry_frame.pack(pady=10)
entry.pack()
add_button.pack(pady=10)
remove_button.pack(pady=10)
listbox.pack(pady=10)

update_list()

window.mainloop()
