import tkinter as tk

root = tk.Tk()

title = tk.Label(root, text="Temperature\nConverter")
title.grid(row = 0, column = 0)

number = tk.Entry(root)
number.grid(row = 1, column = 0)

c_to_f_rb = tk.Radiobutton(root, text="C to F", value=1)
c_to_f_rb.grid(row = 2, column = 0)

f_to_c_rb = tk.Radiobutton(root, text="F to C", value=2)
f_to_c_rb.grid(row = 2, column = 1)

convert_b = tk.Button(root, text="Convert")
convert_b.grid(row = 3, column = 0)

result_l = tk.Label(root, text="")
result_l.grid(row = 4, column = 0)

root.mainloop()