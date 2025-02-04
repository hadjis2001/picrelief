import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk, messagebox, filedialog, IntVar
from concurrent.futures import ThreadPoolExecutor
import sv_ttk

root = tk.Tk()
root.iconbitmap("icon.ico")

from conversion import *

load_settings()
root.protocol("WM_DELETE_WINDOW", lambda: (save_settings(), root.destroy()))  # Save settings on close

# Function to enable and disable spinbox for setting thread number
def toggle_spinbox():
    if limited_threads.get():
        thread_spinbox.config(state="normal")
    else:
        thread_spinbox.config(state="disabled")

label_font = tkFont.Font(family="Arial", size=12, weight=tkFont.BOLD)
convert_font = tkFont.Font(family="Arial", size=12, weight=tkFont.BOLD)

root.title('PicRelief')
root.minsize(900, 300) # Fixed Window Size
root.maxsize(900, 300)

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

settings_header = ttk.Label(root, text="Conversion Settings", borderwidth=1, relief=SUNKEN, anchor=CENTER, justify="center")
settings_header.grid(row=4, column=0, columnspan=4, pady=10, sticky="nsew")

c1 = ttk.Checkbutton(root, text='Scan Sub-Folders',variable=recursive_scan, onvalue=True, offvalue=False)
c1.grid(row=5, column=0, columnspan=1)

c2 = ttk.Checkbutton(root, text='Delete After Conversion',variable=delete_after, onvalue=True, offvalue=False)
c2.grid(row=5, column=1, columnspan=1)

c3 = ttk.Checkbutton(root, text='Limit Threads',variable=limited_threads, onvalue=True, offvalue=False, command=toggle_spinbox)
c3.grid(row=5, column=2, columnspan=1)

thread_spinbox = ttk.Spinbox(root, from_=1, to=32, width=5, state="disabled", textvariable=thread_number)
thread_spinbox.grid(row=5, column=3, columnspan=1, pady=10)

convert_button = ttk.Button(text= "Start Conversion", command=start_conversion)
convert_button.grid(row=7, column=0, columnspan=4, pady=10)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

sv_ttk.set_theme("dark")

root.mainloop()
