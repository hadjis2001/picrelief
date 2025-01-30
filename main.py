import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from concurrent.futures import ThreadPoolExecutor
import sv_ttk

root = tk.Tk()

from conversion import *

label_font = tkFont.Font(family="Arial", size=12, weight=tkFont.BOLD)
convert_font = tkFont.Font(family="Arial", size=12, weight=tkFont.BOLD)

root.title('PicRelief')
root.minsize(900, 600)
root.maxsize(900, 600)

separator_label = ttk.Label(root, text="", borderwidth=1, relief=SUNKEN, anchor=CENTER)

folder_header = ttk.Label(root, text="Select Folders", borderwidth=1, relief=SUNKEN, anchor=CENTER, justify="center")
folder_header.grid(row=0, column=0, columnspan=4, pady=10, sticky="nsew")

lbl1 = ttk.Label(root, textvariable=input_selection, width=65, borderwidth=1, relief=SUNKEN, anchor=W, justify="center")
lbl1.grid(row=1, column=0, columnspan=4, pady=10)

input_label = ttk.Label(root, text="Input Folder:", width=11, borderwidth=1, anchor=E, justify="center")
input_label.grid(row=1, column=0, columnspan=1)

button2 = ttk.Button(text="Browse...", command=browse_input)
button2.grid(row=1, column=3, columnspan=1)

lbl2 = ttk.Label(root, textvariable=output_selection, widt=65, borderwidth=1, relief=SUNKEN, anchor=W, justify="center")
lbl2.grid(row=3, column=0, columnspan=4, pady=10)

output_label = ttk.Label(root, text="Output Folder:", width=11, borderwidth=1, anchor=E, justify="center")
output_label.grid(row=3, column=0, columnspan=1, pady=10)

button3 = ttk.Button(text="Browse...", command=browse_output)
button3.grid(row=3, column=3)

folder_header = ttk.Label(root, text="Conversion Settings", borderwidth=1, relief=SUNKEN, anchor=CENTER, justify="center")
folder_header.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")

convert_button = ttk.Button(text= "Begin Conversion", command=start_conversion)
convert_button.grid(row=7, column=0, columnspan=4, pady=50)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

sv_ttk.set_theme("dark")

root.mainloop()
