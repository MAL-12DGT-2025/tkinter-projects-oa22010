import tkinter as tk
from tkinter import ttk

def press(button):
    current = equation.get()
    current = current + button
    equation.set(current)

def clear():
    equation.set("")

def calculate():
    try:
        result = eval(equation.get())
        equation.set(result)
    except SyntaxError:
        equation.set("Syntax Error")

root = tk.Tk()

root.title("Calculator")

equation = tk.StringVar()

calc = ttk.Entry(root, textvariable = equation)
calc.grid(row = 1, column = 0, columnspan = 4, padx = 10, pady = 10)

button_7 = ttk.Button(root, text = "7", command = lambda:press("7"))
button_7.grid(row = 2, column = 0, padx = 1, pady = 1)

button_8 = ttk.Button(root, text = "8", command = lambda:press("8"))
button_8.grid(row = 2, column = 1, padx = 1, pady = 1)

button_9 = ttk.Button(root, text = "9", command = lambda:press("9"))
button_9.grid(row = 2, column = 2, padx = 1, pady = 1)

button_4 = ttk.Button(root, text = "4", command = lambda:press("4"))
button_4.grid(row = 3, column = 0, padx = 1, pady = 1)

button_5 = ttk.Button(root, text = "5", command = lambda:press("5"))
button_5.grid(row = 3, column = 1, padx = 1, pady = 1)

button_6 = ttk.Button(root, text = "6", command = lambda:press("6"))
button_6.grid(row = 3, column = 2, padx = 1, pady = 1)

button_1 = ttk.Button(root, text = "1", command = lambda:press("1"))
button_1.grid(row = 4, column = 0, padx = 1, pady = 1)

button_2 = ttk.Button(root, text = "2", command = lambda:press("2"))
button_2.grid(row = 4, column = 1, padx = 1, pady = 1)

button_3 = ttk.Button(root, text = "3", command = lambda:press("3"))
button_3.grid(row = 4, column = 2, padx = 1, pady = 1)

button_CLR = ttk.Button(root, text = "CLR", command = clear)
button_CLR.grid(row = 5, column = 0, padx = 1, pady = 1)

button_div = ttk.Button(root, text = "/", command = lambda:press("/"))
button_div.grid(row = 2, column = 3, padx = 1, pady = 1)

button_mult = ttk.Button(root, text = "*", command = lambda:press("*"))
button_mult.grid(row = 3, column = 3, padx = 1, pady = 1)

button_minus = ttk.Button(root, text = "-", command = lambda:press("-"))
button_minus.grid(row = 4, column = 3, padx = 1, pady = 1)

button_0 = ttk.Button(root, text = "0", command = lambda:press("0"))
button_0.grid(row = 5, column = 1, padx = 1, pady = 1)

button_equal = ttk.Button(root, text = "=", command = calculate)
button_equal.grid(row = 5, column = 2, padx = 1, pady = 1)

button_plus = ttk.Button(root, text = "+", command = lambda:press("+"))
button_plus.grid(row = 5, column = 3, padx = 1, pady = 1)

root.mainloop()