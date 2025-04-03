# Import the tkinter module
# Import the ttk module from tkinter
import tkinter as tk
from tkinter import ttk

# Create the window
root = tk.Tk()

# Title of the window
root.title("Lemonade stand")

# Function to calculate the total
def calculate():
    amount_1 = int(lemonade_var.get())
    amount_2 = int(pink_var.get())
    amount_3 = int(large_var.get())
    amount_4 = int(straw_var.get())
    amount_5 = int(ice_var.get())
    total = amount_1 * 2 + amount_2 + amount_3 + amount_4 / 2 + amount_5 / 2
    total_text.config(text=f"Total: ${total:.2f}")

# Create StringVar variables for the spinboxes
lemonade_var = tk.StringVar(value="0")
ice_var = tk.StringVar(value="0")
straw_var = tk.StringVar(value="0")
pink_var = tk.StringVar(value="0")
large_var = tk.StringVar(value="0")

# Create and place the widgets
add_text = ttk.Label(root, text="Items:")
add_text.grid(row=0, column=0, padx=10, pady=10)

less_text = ttk.Label(root, text="Amount:")
less_text.grid(row=0, column=1, padx=10, pady=10)

cost_text = ttk.Label(root, text="Cost each:")
cost_text.grid(row=0, column=3, padx=10, pady=10)

lemonade_button = ttk.Spinbox(root, from_=0, to=100000000000, increment=1, textvariable=lemonade_var, command=calculate)
lemonade_button.grid(row=1, column=1, padx=1, pady=1)

ice_button = ttk.Spinbox(root, from_=0, to=100000000000, increment=1, textvariable=ice_var, command=calculate)
ice_button.grid(row=2, column=1, padx=1, pady=1)

straw_button = ttk.Spinbox(root, from_=0, to=100000000000, increment=1, textvariable=straw_var, command=calculate)
straw_button.grid(row=3, column=1, padx=1, pady=1)

pink_button = ttk.Spinbox(root, from_=0, to=100000000000, increment=1, textvariable=pink_var, command=calculate)
pink_button.grid(row=4, column=1, padx=1, pady=1)

large_button = ttk.Spinbox(root, from_=0, to=100000000000, increment=1, textvariable=large_var, command=calculate)
large_button.grid(row=5, column=1, padx=1, pady=1)

amount_enter_a = ttk.Label(root, text="Lemonade", width=12)
amount_enter_a.grid(row=1, column=0, padx=5, pady=1)

amount_enter_b = ttk.Label(root, text="Pink Flavor", width=12)
amount_enter_b.grid(row=2, column=0, padx=5, pady=1)

amount_enter_c = ttk.Label(root, text="Large cup", width=12)
amount_enter_c.grid(row=3, column=0, padx=5, pady=1)

amount_enter_d = ttk.Label(root, text="Straw", width=12)
amount_enter_d.grid(row=4, column=0, padx=5, pady=1)

amount_enter_e = ttk.Label(root, text="Ice", width=12)
amount_enter_e.grid(row=5, column=0, padx=5, pady=1)

cost_text_a = ttk.Label(root, text="$2")
cost_text_a.grid(row=1, column=3, padx=5, pady=1)

cost_text_b = ttk.Label(root, text="$1")
cost_text_b.grid(row=2, column=3, padx=5, pady=1)

cost_text_c = ttk.Label(root, text="$1")
cost_text_c.grid(row=3, column=3, padx=5, pady=1)

cost_text_d = ttk.Label(root, text="50c")
cost_text_d.grid(row=4, column=3, padx=5, pady=1)

cost_text_e = ttk.Label(root, text="50c")
cost_text_e.grid(row=5, column=3, padx=5, pady=1)

total_text = ttk.Label(root, text="Total: $0.0")
total_text.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

calculate_button = ttk.Button(root, text="Complete Order", command=root.quit)
calculate_button.grid(row=7, column=1, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()