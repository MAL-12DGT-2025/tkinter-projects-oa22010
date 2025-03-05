import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Calculator")

entry = ttk.Entry(root)
entry.grid(row = 1, column = 0, columnspan = 4)

button_7 = ttk.Button(root, text = "7")
button_7.grid(row = 2, column = 0)

button_8 = ttk.Button(root, text = "8")
button_8.grid(row = 2, column = 1)

button_9 = ttk.Button(root, text = "9")
button_9.grid(row = 2, column = 2)

button_4 = ttk.Button(root, text = "4")
button_4.grid(row = 3, column = 0)

button_5 = ttk.Button(root, text = "5")
button_5.grid(row = 3, column = 1)

button_6 = ttk.Button(root, text = "6")
button_6.grid(row = 3, column = 2)

button_1 = ttk.Button(root, text = "1")
button_1.grid(row = 4, column = 0)

button_2 = ttk.Button(root, text = "2")
button_2.grid(row = 4, column = 1)

button_3 = ttk.Button(root, text = "3")
button_3.grid(row = 4, column = 2)

button_CLR = ttk.Button(root, text = "CLR")
button_CLR.grid(row = 5, column = 0)

button_div = ttk.Button(root, text = "/")
button_div.grid(row = 2, column = 3)

button_mult = ttk.Button(root, text = "*")
button_mult.grid(row = 3, column = 3)

button_minus = ttk.Button(root, text = "-")
button_minus.grid(row = 4, column = 3)

button_0 = ttk.Button(root, text = "0")
button_0.grid(row = 5, column = 1)

button_equal = ttk.Button(root, text = "=")
button_equal.grid(row = 5, column = 2)

button_plus = ttk.Button(root, text = "+")
button_plus.grid(row = 5, column = 3)

root.mainloop()