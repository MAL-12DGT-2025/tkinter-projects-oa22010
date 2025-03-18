import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Favorite Bible Verse')

verse = open('bible_verse.txt')
answer = input('Favorite Bible verse: ')
verse.write(answer)

root.mainloop()