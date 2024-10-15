
import tkinter as tk

root = tk.Tk()

lbox = tk.Listbox(width=15, height=8, selectmode=tk.MULTIPLE)
lbox.pack()

for i in range(10):
    lbox.insert(0, i)

root.mainloop()

