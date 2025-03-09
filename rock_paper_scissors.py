import tkinter as tk
import random
from tkinter import ttk

root = tk.Tk()

root.title("Rock Paper Scissors Game")

options = ["Rock", "Paper", "Scissors"]

def rock():
    result_text.config(text = "")

def paper():
    result_text.config(text = "")

def scissors():
    result_text.config(text = "")

choice_text = ttk.Label(root, text = "Choose one:")
choice_text.grid(row = 0, column = 1, padx = 1, pady = 1)

result_text = ttk.Label(root, text = "Result:")
result_text.grid(row = 2, column = 1, padx = 1, pady = 1)

rock_button = ttk.Button(root, text = "Rock", command = rock)
rock_button.grid(row = 1, column = 0, padx = 1, pady = 1)

paper_button = ttk.Button(root, text = "Paper", command = paper)
paper_button.grid(row = 1, column = 1, padx = 1, pady = 1)

scissor_button = ttk.Button(root, text = "Scissors", command = scissors)
scissor_button.grid(row = 1, column = 2, padx = 1, pady = 1)

root.mainloop()