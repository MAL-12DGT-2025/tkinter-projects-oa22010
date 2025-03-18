# Import the tkinter module
# Import the ttk module from tkinter
import tkinter as tk
from tkinter import ttk

# Create the window
root = tk.Tk()

# Title of the window
root.title("Lemonade stand")

# Variables of amount of each item
amount_1 = 0
amount_2 = 0
amount_3 = 0
amount_4 = 0
amount_5 = 0

# Functions for each button
def click_1():
    global amount_1
    amount_1 += 1
    amount_enter_a.config(text = f"{amount_1}")

def click_2():
    global amount_2
    amount_2 += 1
    amount_enter_b.config(text = f"{amount_2}")

def click_3():
    global amount_3
    amount_3 += 1
    amount_enter_c.config(text = f"{amount_3}")

def click_4():
    global amount_4
    amount_4 += 1
    amount_enter_d.config(text = f"{amount_4}")

def click_5():
    global amount_5
    amount_5 += 1
    amount_enter_e.config(text = f"{amount_5}")

# Function to calculate the total
def calculate():
    total = amount_1 * 2 + amount_2 + amount_3 + amount_4 / 2 + amount_5 / 2
    total_text.config(text = f"Total: ${total}")

# Create and place the widgets
select_text = ttk.Label(root, text = "Select items:")
select_text.grid(row = 0, column = 0, padx = 10, pady = 10)

amount_text = ttk.Label(root, text = "Amount:")
amount_text.grid(row = 0, column = 1, padx = 10, pady = 10)

cost_text = ttk.Label(root, text = "Cost each:")
cost_text.grid(row = 0, column = 2, padx = 10, pady = 10)

lemonade_button = ttk.Button(root, text = "Lemonade", command = click_1)
lemonade_button.grid(row = 1, column = 0, padx = 1, pady = 1)

ice_button = ttk.Button(root, text = "Ice", command = click_5)
ice_button.grid(row = 5, column = 0, padx = 1, pady = 1)

straw_button = ttk.Button(root, text = "Straw", command = click_4)
straw_button.grid(row = 4, column = 0, padx = 1, pady = 1)

pink_button = ttk.Button(root, text = "Pink flavor", command = click_2)
pink_button.grid(row = 2, column = 0, padx = 1, pady = 1)

large_button = ttk.Button(root, text = "Large cup", command = click_3)
large_button.grid(row = 3, column = 0, padx = 1, pady = 1)

amount_enter_a = ttk.Label(root, text = "0", width = 5)
amount_enter_a.grid(row = 1, column = 1, padx = 5, pady = 1)

amount_enter_b = ttk.Label(root, text = "0", width = 5)
amount_enter_b.grid(row = 2, column = 1, padx = 5, pady = 1)

amount_enter_c = ttk.Label(root, text = "0", width = 5)
amount_enter_c.grid(row = 3, column = 1, padx = 5, pady = 1)

amount_enter_d = ttk.Label(root, text = "0", width = 5)
amount_enter_d.grid(row = 4, column = 1, padx = 5, pady = 1)

amount_enter_e = ttk.Label(root, text = "0", width = 5)
amount_enter_e.grid(row = 5, column = 1, padx = 5, pady = 1)

cost_text_a = ttk.Label(root, text = "$2")
cost_text_a.grid(row = 1, column = 2, padx = 5, pady = 1)

cost_text_b = ttk.Label(root, text = "50c")
cost_text_b.grid(row = 2, column = 2, padx = 5, pady = 1)

cost_text_c = ttk.Label(root, text = "50c")
cost_text_c.grid(row = 3, column = 2, padx = 5, pady = 1)

cost_text_d = ttk.Label(root, text = "$1")
cost_text_d.grid(row = 4, column = 2, padx = 5, pady = 1)

cost_text_e = ttk.Label(root, text = "$1")
cost_text_e.grid(row = 5, column = 2, padx = 5, pady = 1)

total_text = ttk.Label(root, text = "Total: $0.0")
total_text.grid(row = 6, column = 0, columnspan = 3, padx = 10, pady = 10)

calculate_button = ttk.Button(root, text = "Complete Order:", command = calculate)
calculate_button.grid(row = 7, column = 0, columnspan = 3, padx = 10, pady = 10)

# Start the main loop
root.mainloop()