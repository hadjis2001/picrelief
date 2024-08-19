import tkinter
from tkinter import ttk
from tkinter import messagebox
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
    worker_input = 0
    # Define input and output folders
    #input_folder = input("Where are the original photos? Eg: 'C:/Users/Hadjis/Desktop/testfiles': ")  # Replace with your input folder
    #output_folder = input("Where do you want to save the new photos? Eg: 'C:/Users/Hadjis/Desktop/outputfiles': ")  # Replace with your output folder

    input_folder = "C:/Users/Hadjis/Desktop/testfiles" # Replace with your input folder
    output_folder = "C:/Users/Hadjis/Desktop/outputfiles" # Replace with your output folder

    #worker_input = int(input("How many workers? Must be 1-8: "))
    #while (worker_input > 8) or (worker_input < 1):
    #    print("")
    #    print("Incorrect input attributed to user error, please try again.")
    #    worker_input = int(input("How many workers? Must be 1-8: "))

    start_time = time.time()

    # Convert all HEIC files in the directory
    convert_all_heic_in_directory(input_folder, output_folder, max_workers=8)  # Adjust max_workers based on your CPU cores
    
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds")

m = tkinter.Tk()

ttk.Button(text= "Open", command= start_conversion).pack()

m.mainloop()