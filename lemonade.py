import tkinter as tk
from tkinter import ttk

root = tk.Tk()

equation = tk.StringVar

root.title("Lemonade stand")

select_text = ttk.Label(root, text = "Select items:")
select_text.grid(row = 0, column = 0, padx = 10, pady =10)

amount_text = ttk.Label(root, text = "Amount:")
amount_text.grid(row = 0, column = 1, padx = 10, pady =10)

cost_text = ttk.Label(root, text = "Cost each:")
cost_text.grid(row = 0, column = 2, padx = 10, pady = 10)

lemonade_button = ttk.Checkbutton(root, text = "Lemonade ($2)")
lemonade_button.grid(row = 1, column = 0, padx = 1, pady = 1)

ice_button = ttk.Checkbutton(root, text = "Ice (50c)")
ice_button.grid(row = 5, column = 0, padx = 1, pady = 1)

straw_button = ttk.Checkbutton(root, text = "Straw (50c)")
straw_button.grid(row = 4, column = 0, padx = 1, pady = 1)

pink_button = ttk.Checkbutton(root, text = "Pink flavor ($1)")
pink_button.grid(row = 2, column = 0, padx = 1, pady = 1)

large_button = ttk.Checkbutton(root, text = "Large cup ($1)")
large_button.grid(row = 3,  column = 0, padx = 1, pady = 1)

amount_enter_a = ttk.Entry(root, text = "", width = 5)
amount_enter_a.grid(row = 1, column = 1, padx = 5, pady = 1)

amount_enter_b = ttk.Entry(root, text = "", width = 5)
amount_enter_b.grid(row = 2, column = 1, padx = 5, pady = 1)

amount_enter_c = ttk.Entry(root, text = "", width = 5)
amount_enter_c.grid(row  = 3, column = 1, padx = 5, pady = 1)

amount_enter_d = ttk.Entry(root, text = "", width = 5)
amount_enter_d.grid(row = 4, column = 1, padx = 5, pady = 1)

amount_enter_e = ttk.Entry(root, text = "", width = 5)
amount_enter_e.grid(row = 5, column = 1, padx = 5, pady = 1)

cost_text_a = ttk.Label(root, text = "")
cost_text_a.grid(row = 1, column = 2, padx = 5, pady = 1)

cost_text_b = ttk.Label(root, text = "")
cost_text_b.grid(row = 2, column = 2, padx = 5, pady = 1)

cost_text_c = ttk.Label(root, text = "")
cost_text_c.grid(row = 3, column = 2, padx = 5, pady = 1)

cost_text_d = ttk.Label(root, text = "")
cost_text_d.grid(row = 4, column = 2, padx = 5, pady = 1)

cost_text_e = ttk.Label(root, text = "")
cost_text_e.grid(row = 5, column = 2, padx = 5, pady = 1)

root.mainloop()