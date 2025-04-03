import tkinter as tk
from tkinter import ttk

root = tk.Tk()

spinbox = tk.Spinbox(root, from_=0, to=100000000000, increment=1)
spinbox.grid(row=0, column=0, padx=10, pady=10)
spinbox.bind("<FocusIn>", lambda event: spinbox.select_range(0, tk.END))
spinbox.bind("<FocusOut>", lambda event: spinbox.select_clear(0, tk.END))

root.mainloop()