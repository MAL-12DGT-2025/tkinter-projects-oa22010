import tkinter as tk
from tkinter import ttk

def press(event):
    pass

root = tk.Tk()
root.title("Calculator")

entry = ttk.Entry(root)
entry.grid(row = 1, column = 0, columnspan = 4, padx = 10, pady = 10)

button_7 = ttk.Button(root, text = "7", command = press)
button_7.grid(row = 2, column = 0, padx = 1, pady = 1)

button_8 = ttk.Button(root, text = "8", command = press)
button_8.grid(row = 2, column = 1, padx = 1, pady = 1)

button_9 = ttk.Button(root, text = "9", command = press)
button_9.grid(row = 2, column = 2, padx = 1, pady = 1)

button_4 = ttk.Button(root, text = "4", command = press)
button_4.grid(row = 3, column = 0, padx = 1, pady = 1)

button_5 = ttk.Button(root, text = "5", command = press)
button_5.grid(row = 3, column = 1, padx = 1, pady = 1)

button_6 = ttk.Button(root, text = "6", command = press)
button_6.grid(row = 3, column = 2, padx = 1, pady = 1)

button_1 = ttk.Button(root, text = "1", command = press)
button_1.grid(row = 4, column = 0, padx = 1, pady = 1)

button_2 = ttk.Button(root, text = "2", command = press)
button_2.grid(row = 4, column = 1, padx = 1, pady = 1)

button_3 = ttk.Button(root, text = "3", command = press)
button_3.grid(row = 4, column = 2, padx = 1, pady = 1)

button_CLR = ttk.Button(root, text = "CLR", command = press)
button_CLR.grid(row = 5, column = 0, padx = 1, pady = 1)

button_div = ttk.Button(root, text = "/", command = press)
button_div.grid(row = 2, column = 3, padx = 1, pady = 1)

button_mult = ttk.Button(root, text = "*", command = press)
button_mult.grid(row = 3, column = 3, padx = 1, pady = 1)

button_minus = ttk.Button(root, text = "-", command = press)
button_minus.grid(row = 4, column = 3, padx = 1, pady = 1)

button_0 = ttk.Button(root, text = "0", command = press)
button_0.grid(row = 5, column = 1, padx = 1, pady = 1)

button_equal = ttk.Button(root, text = "=", command = press)
button_equal.grid(row = 5, column = 2, padx = 1, pady = 1)

button_plus = ttk.Button(root, text = "+", command = press)
button_plus.grid(row = 5, column = 3, padx = 1, pady = 1)

root.mainloop()