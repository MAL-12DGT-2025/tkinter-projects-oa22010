import tkinter as tk
from tkinter import ttk

root = tk.Tk()

tk.Spinbox(root, from_=0, to=100000000000).pack()


root.mainloop()