import tkinter as tk
import random
from tkinter import ttk

root = tk.Tk()

root.title("Rock Paper Scissors Game")

options = ["Rock", "Paper", "Scissors"]

score = 0
computer_score = 0

def ai_choice():
    return random.choice(options)

def rock():
    ai = ai_choice()
    if ai == "Rock":
        result_text.config(text = "Tie")
    elif ai == "Paper":
        result_text.config(text = "You lose")
    elif ai == "Scissors":
        result_text.config(text = "You win")
    score_count()

def paper():
    ai = ai_choice()
    if ai == "Paper":
        result_text.config(text = "Tie")
    elif ai == "Scissors":
        result_text.config(text = "You lose")
    elif ai == "Rock":
        result_text.config(text = "You win")
    score_count()

def scissors():
    ai = ai_choice()
    if ai == "Scissors":
        result_text.config(text = "Tie")
    elif ai == "Rock":
        result_text.config(text = "You lose")
    elif ai == "Paper":
        result_text.config(text = "You win")
    score_count()

def score_count():
    global score, computer_score
    if result_text.cget("text") == "You win":
        score += 1
        score_text.config(text = "Score: " + str(score))
    elif result_text.cget("text") == "You lose":
        computer_score += 1
        computer_score_text.config(text = "Computer score: " + str(computer_score))

choice_text = ttk.Label(root, text = "Choose one:")
choice_text.grid(row = 0, column = 1, padx = 1, pady = 1)

result_text = ttk.Label(root, text = "Result:")
result_text.grid(row = 3, column = 1, padx = 1, pady = 1)

score_text = ttk.Label(root, text = "Score: 0")
score_text.grid(row = 4, column = 1, padx = 1, pady = 1)

computer_score_text = ttk.Label(root, text = "Computer score: 0")
computer_score_text.grid(row = 5, column = 1, padx = 1, pady = 1)

rock_button = ttk.Button(root, text = "Rock", command = rock)
rock_button.grid(row = 1, column = 0, padx = 1, pady = 1)

paper_button = ttk.Button(root, text = "Paper", command = paper)
paper_button.grid(row = 1, column = 1, padx = 1, pady = 1)

scissor_button = ttk.Button(root, text = "Scissors", command = scissors)
scissor_button.grid(row = 1, column = 2, padx = 1, pady = 1)

root.mainloop()