import os
from PIL import Image
import pillow_heif
import time
from tkinter import ttk, messagebox, filedialog, StringVar
from concurrent.futures import ThreadPoolExecutor
from settings import *
from threading import Lock

number_of_pics = 0
error_given = False
lock = Lock()

# Function to convert a single HEIC file to PNG using pillow_heif
def convert_heic_to_png(heic_file_path, output_folder, delete_after):
    global number_of_pics
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
        
        with lock:
            number_of_pics += 1

        print(f"Converted {heic_file_path} to {output_file_path}")
        if delete_after:
            os.remove(heic_file_path)
    except Exception as e:
        messagebox.showwarning("Warning", "Some of your images failed to be converted. Please try again.")

# Function to process all HEIC files in a directory
def convert_all_heic_in_directory(input_folder, output_folder, max_workers, delete_after):
    global error_given 
    try:
        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)
        
        # Get all HEIC files in the input folder
        heic_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.heic')]
        
        # Convert files using multithreading
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            for heic_file in heic_files:
                heic_file_path = os.path.join(input_folder, heic_file)
                executor.submit(convert_heic_to_png, heic_file_path, output_folder, delete_after)
    except:
        error_given = True
        messagebox.showerror("Error", "An error occured while trying to convert your images. Make sure that the input and output folders exist.")

def start_conversion():
    # Construct list of directories if scan is recursive
    global error_given, number_of_pics
    number_of_pics = 0

    if recursive_scan.get():
        directory_list = [x[0] for x in os.walk(input_selection.get())]
    else:
        directory_list = [input_selection.get()]

    start_time = time.time()
    # Set number of threads appropriately
    worker_input = thread_number.get()

    # Convert all HEIC files in the directory
    for dir in directory_list:
        convert_all_heic_in_directory(dir, output_selection.get(), worker_input, delete_after.get())
    
    end_time = time.time()

    # Calculate execution time
    execution_time = end_time - start_time
    if error_given == False:
        messagebox.showinfo("Success", f"Your images have been succesfuly converted! The process took {execution_time:.2f} seconds and converted {number_of_pics} images.")
    error_given = False
