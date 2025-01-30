import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from concurrent.futures import ThreadPoolExecutor

root = tk.Tk()

from conversion import *

label_font = tkFont.Font(family="Arial", size=12, weight=tkFont.BOLD)
convert_font = tkFont.Font(family="Arial", size=12, weight=tkFont.BOLD)

root.title('PicRelief')
root.minsize(900, 600)
root.maxsize(900, 600)

separator_label = Label(root, text="", bd=1, relief=SUNKEN, anchor=CENTER)

folder_header = Label(root, text="Select Folders", bd=1, relief=SUNKEN, anchor=CENTER, font=label_font, justify="center")
folder_header.grid(row=0, column=0, columnspan=4, pady=10, sticky="nsew")

lbl1 = Label(root, textvariable=input_selection, width=75, bd=1, relief=SUNKEN, anchor=W, justify="center")
lbl1.grid(row=1, column=0, columnspan=4, pady=10)

input_label = Label(root, text="Input Folder:", width=11, bd=1, anchor=E, justify="center")
input_label.grid(row=1, column=0, columnspan=1)

button2 = Button(text="Browse...", command=browse_input)
button2.grid(row=1, column=3, columnspan=1)

lbl2 = Label(root, textvariable=output_selection, width=75, bd=1, relief=SUNKEN, anchor=W, justify="center")
lbl2.grid(row=3, column=0, columnspan=4, pady=10)

output_label = Label(root, text="Output Folder:", width=11, bd=1, anchor=E, justify="center")
output_label.grid(row=3, column=0, columnspan=1, pady=10)

button3 = Button(text="Browse...", command=browse_output)
button3.grid(row=3, column=3)

convert_button = Button(text= "Begin Conversion", font=convert_font, command=start_conversion)
convert_button.grid(row=7, column=0, columnspan=4, pady=50)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

root.mainloop()
