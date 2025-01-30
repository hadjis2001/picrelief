from tkinter import filedialog, StringVar
from concurrent.futures import ThreadPoolExecutor

input_selection = StringVar()
output_selection = StringVar()

def browse_input():
    global input_selection
    selection = filedialog.askdirectory()
    input_selection.set(selection)  # Update StringVar
    print(selection)

def browse_output():
    global output_selection
    selection = filedialog.askdirectory()
    output_selection.set(selection)  # Update StringVar
    print(selection)