import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Favorite Bible Verse')

def confirm():
    verse = user_input.get()
    with open('bible_verse.txt', 'w') as file:
        file.write(verse)
    read_verse = open('bible_verse.txt').read()
    verse_display.config(text = f'Bible verse: {read_verse}')

verse_text = ttk.Label(root, text = 'Insert favorite Bible verse:')
verse_text.pack(pady = 1, padx = 5)

user_input = ttk.Entry(root, text = '(Insert here)')
user_input.pack(pady = 1)

confirm_button = ttk.Button(root, text = 'Confirm', command  = confirm)
confirm_button.pack(pady = 1)

verse_display = ttk.Label(root, text = 'Bible verse:')
verse_display.pack(pady = 1)

root.mainloop()