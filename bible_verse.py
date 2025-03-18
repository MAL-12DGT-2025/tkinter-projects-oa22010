import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Favorite Bible Verse')

verse = open('bible_verse.txt')
verse.write()

user_input = ttk.Label(root, text='Favorite Bible Verse')
user_input.grid(row = 0, column = 0)

root.mainloop()