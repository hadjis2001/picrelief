from tkinter import filedialog, StringVar, BooleanVar, DoubleVar
from concurrent.futures import ThreadPoolExecutor
import json
import os

# Settings file path
settings_file = "settings.json"

# Settings initialisation
input_selection = StringVar()
output_selection = StringVar()
recursive_scan = BooleanVar()
limited_threads = BooleanVar()
delete_after = BooleanVar()
thread_number = DoubleVar(value=8)

def load_settings():
    # Load settings from a JSON file if it exists.
    if os.path.exists(settings_file):
        with open(settings_file, "r") as f:
            try:
                data = json.load(f)
                input_selection.set(data.get("input_folder", ""))
                output_selection.set(data.get("output_folder", ""))
            except json.JSONDecodeError:
                print("Error reading settings file.")

def save_settings():
    # Save settings to a JSON file when the application closes.
    data = {
        "input_folder": input_selection.get(),
        "output_folder": output_selection.get(),
    }
    with open(settings_file, "w") as f:
        json.dump(data, f)

def browse_input():
    global input_selection
    selection = filedialog.askdirectory()
    input_selection.set(selection)  # Update input folder
    print(selection)

def browse_output():
    global output_selection
    selection = filedialog.askdirectory()
    output_selection.set(selection)  # Update output folder
    print(selection)