import tkinter as tk # Importing the tkinter module
from tkinter import ttk # Importing ttk from the tkinter module

root = tk.Tk() # Creating the root window
root.title("My First Tkinter Program") # Setting the title of the window
root.geometry("300x500") # Changing dimensions of the window

button_one = tk.Button(root, text="Click Me!", bg="blue", fg="white", font="ComicSans") # Creating a button
button_one.pack() # Packing the button

button_two = tk.Button(root, text="Don't click Me!", bg="red", fg="white", font="ComicSans") # Creating a button
button_two.pack() # Packing the button

button_three = ttk.Button(root, text="Click Me Too!") # Creating a button using the ttk module
button_three.pack() # Packing the button

text_one = tk.Label(root, text="Hello World!", bg="black", fg="white", font="ComicSans") # Creating text
text_one.pack() # Packing the text

text_two = ttk.Label(root, text="I'm here too!") # Creating text using the ttk module
text_two.pack() # Packing the text

entry_one = tk.Entry(root, bg="white", fg="black", font="ComicSans") # Creating an entry
entry_one.pack() # Packing the entry

checkbox_one = tk.Checkbutton(root, text="Check Me!") # Creating a checkbox
checkbox_one.pack()

checkbox_two = tk.Checkbutton(root, text="Check Me Too!") # Creating a checkbox using the ttk module
checkbox_two.pack()

radiobutton_one = tk.Radiobutton(root, text="Radio Me!") # Creating a radio button
radiobutton_one.pack()

radiobutton_two = ttk.Radiobutton(root, text="Radio Me Too!") # Creating a radio button using the ttk module
radiobutton_two.pack()

root.mainloop() # Running the main loop