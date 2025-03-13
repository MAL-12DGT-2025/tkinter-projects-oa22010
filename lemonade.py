import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Lemonade stand")

item_1 = tk.IntVar()
item_2 = tk.IntVar()
item_3 = tk.IntVar()
item_4 = tk.IntVar()
item_5 = tk.IntVar()

amount = 0

def click_1():
    global amount
    if item_1.get() == 1:
        amount += 1
        amount_enter_a.config(text=f"{amount}")

def click_2():
    global amount
    if item_5.get() == 1:
        amount += 1
        amount_enter_b.config(text=f"{amount}")

def click_3():
    global amount
    if item_4.get() == 1:
        amount += 1
        amount_enter_c.config(text=f"{amount}")

def click_4():
    global amount
    if item_2.get() == 1:
        amount += 1
        amount_enter_d.config(text=f"{amount}")

def click_5():
    global amount
    if item_3.get() == 1:
        amount += 1
        amount_enter_e.config(text=f"{amount}")

select_text = ttk.Label(root, text="Select items:")
select_text.grid(row=0, column=0, padx=10, pady=10)

amount_text = ttk.Label(root, text="Amount:")
amount_text.grid(row=0, column=1, padx=10, pady=10)

cost_text = ttk.Label(root, text="Cost each:")
cost_text.grid(row=0, column=2, padx=10, pady=10)

lemonade_button = tk.Button(root, text="Lemonade ($2)", variable=item_1, onvalue=1, offvalue=0, command=click_1)
lemonade_button.grid(row=1, column=0, padx=1, pady=1)

ice_button = tk.Button(root, text="Ice (50c)", variable=item_5, onvalue=1, offvalue=0, command=click_2)
ice_button.grid(row=5, column=0, padx=1, pady=1)

straw_button = tk.Button(root, text="Straw (50c)", variable=item_4, onvalue=1, offvalue=0, command=click_3)
straw_button.grid(row=4, column=0, padx=1, pady=1)

pink_button = tk.Button(root, text="Pink flavor ($1)", variable=item_2, onvalue=1, offvalue=0, command=click_4)
pink_button.grid(row=2, column=0, padx=1, pady=1)

large_button = tk.Button(root, text="Large cup ($1)", variable=item_3, onvalue=1, offvalue=0, command=click_5)
large_button.grid(row=3, column=0, padx=1, pady=1)

amount_enter_a = ttk.Label(root, text="", width=5)
amount_enter_a.grid(row=1, column=1, padx=5, pady=1)

amount_enter_b = ttk.Label(root, text="", width=5)
amount_enter_b.grid(row=2, column=1, padx=5, pady=1)

amount_enter_c = ttk.Label(root, text="", width=5)
amount_enter_c.grid(row=3, column=1, padx=5, pady=1)

amount_enter_d = ttk.Label(root, text="", width=5)
amount_enter_d.grid(row=4, column=1, padx=5, pady=1)

amount_enter_e = ttk.Label(root, text="", width=5)
amount_enter_e.grid(row=5, column=1, padx=5, pady=1)

cost_text_a = ttk.Label(root, text="$2")
cost_text_a.grid(row=1, column=2, padx=5, pady=1)

cost_text_b = ttk.Label(root, text="50c")
cost_text_b.grid(row=2, column=2, padx=5, pady=1)

cost_text_c = ttk.Label(root, text="50c")
cost_text_c.grid(row=3, column=2, padx=5, pady=1)

cost_text_d = ttk.Label(root, text="$1")
cost_text_d.grid(row=4, column=2, padx=5, pady=1)

cost_text_e = ttk.Label(root, text="$1")
cost_text_e.grid(row=5, column=2, padx=5, pady=1)

root.mainloop()