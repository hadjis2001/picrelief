import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk, messagebox, filedialog
import os
from PIL import Image
import pillow_heif
from concurrent.futures import ThreadPoolExecutor
import time

# Function to convert a single HEIC file to PNG using pillow_heif
def convert_heic_to_png(heic_file_path, output_folder):
    try:
        # Open HEIC file using pillow_heif
        heif_image = pillow_heif.open_heif(heic_file_path)
        
        # Convert HEIC to PIL Image
        image = Image.frombytes(
            heif_image.mode, 
            heif_image.size, 
            heif_image.data
        )
        
        # Define output file path
        output_file_path = os.path.join(output_folder, os.path.splitext(os.path.basename(heic_file_path))[0] + ".png")
        
        # Save the image as PNG
        image.save(output_file_path, "PNG")
        
        print(f"Converted {heic_file_path} to {output_file_path}")
    except Exception as e:
        print(f"Failed to convert {heic_file_path}: {e}")

# Function to process all HEIC files in a directory
def convert_all_heic_in_directory(input_folder, output_folder, max_workers=4):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Get all HEIC files in the input folder
    heic_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.heic')]
    
    # Convert files using multithreading
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for heic_file in heic_files:
            heic_file_path = os.path.join(input_folder, heic_file)
            executor.submit(convert_heic_to_png, heic_file_path, output_folder)

def start_conversion():
    worker_input = 8

    # Define input and output folders
    input_folder = input_selection.get() # Replace with your input folder
    output_folder = output_selection.get() # Replace with your output folder

    directory_list = [x[0] for x in os.walk(input_folder)]

    start_time = time.time()

    # Convert all HEIC files in the directory
    if current_only == True:
        convert_all_heic_in_directory(input_folder, output_folder, max_workers=worker_input)
    else:
        for dir in directory_list:
            convert_all_heic_in_directory(dir, output_folder, max_workers=worker_input)
    
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds")

def browse_input():
    selection = filedialog.askdirectory()
    input_selection.set(selection)
    print(input_selection)

def browse_output():
    selection = filedialog.askdirectory()
    output_selection.set(selection)
    print(output_selection)

def debug():
    print(input_selection.get())
    test = [x[0] for x in os.walk(input_selection.get())]
    print(test)

current_only = False

root = tk.Tk()

label_font = tkFont.Font(family="Arial", size=12, weight=tkFont.BOLD)
convert_font = tkFont.Font(family="Arial", size=12, weight=tkFont.BOLD)

root.title('PicRelief')
root.minsize(900, 600)
root.maxsize(900, 600)

separator_label = Label(root, text="", bd=1, relief=SUNKEN, anchor=CENTER)

folder_header = Label(root, text="Select Folders", bd=1, relief=SUNKEN, anchor=CENTER, font=label_font, justify="center")
folder_header.grid(row=0, column=0, columnspan=4, pady=10, sticky="nsew")

input_selection = StringVar()
lbl1 = Label(root, textvariable=input_selection, width=75, bd=1, relief=SUNKEN, anchor=W, justify="center")
lbl1.grid(row=1, column=0, columnspan=4, pady=10)

input_label = Label(root, text="Input Folder:", width=11, bd=1, anchor=E, justify="center")
input_label.grid(row=1, column=0, columnspan=1)

button2 = Button(text="Browse...", command=browse_input)
button2.grid(row=1, column=3, columnspan=1)

output_selection = StringVar()
lbl2 = Label(root, textvariable=output_selection, width=75, bd=1, relief=SUNKEN, anchor=W, justify="center")
lbl2.grid(row=3, column=0, columnspan=4, pady=10)

output_label = Label(root, text="Output Folder:", width=11, bd=1, anchor=E, justify="center")
output_label.grid(row=3, column=0, columnspan=1, pady=10)

button3 = Button(text="Browse...", command=browse_output)
button3.grid(row=3, column=3)

convert_button = Button(text= "Begin Conversion", font=convert_font, command=start_conversion)
convert_button.grid(row=7, column=0, columnspan=4, pady=50)

debug_button = Button(text= "Debug", font=convert_font, command= debug)
debug_button.grid(row=8, column=0, columnspan=4, pady=50)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

root.mainloop()