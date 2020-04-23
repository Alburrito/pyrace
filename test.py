import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

canvas = tk.Canvas(root, height=800, width=800, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

openFile = tk.Button(root, text="Open File", padx=10, pady=5,
                     fg="white", bg="#263D42")

root.mainloop()
