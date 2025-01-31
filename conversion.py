import os
from PIL import Image
import pillow_heif
import time
from tkinter import ttk, messagebox, filedialog, StringVar
from concurrent.futures import ThreadPoolExecutor
from settings import *

worker_input = 8

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
def convert_all_heic_in_directory(input_folder, output_folder, max_workers):
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
    directory_list = [x[0] for x in os.walk(input_selection.get())]

    start_time = time.time()

    # Convert all HEIC files in the directory
    if recursive_scan.get():
        for dir in directory_list:
            convert_all_heic_in_directory(dir, output_selection.get(), max_workers=worker_input)
    else:
        convert_all_heic_in_directory(input_selection.get(), output_selection.get(), max_workers=worker_input)
    
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds")
