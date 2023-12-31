import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def remove_metadata(input_path, output_path):
    try:
        image = Image.open(input_path)
        # Create the output path with the "metnew" word added
        base_name, extension = os.path.splitext(input_path)
        output_path = f"{base_name}_metnew{extension}"
        image.save(output_path)
        status_label.config(text=f"Metadata removed and saved as {output_path}")
    except Exception as e:
        status_label.config(text=f"Error: {e}")

def browse_input():
    input_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, input_path)

def remove_metadata_gui():
    input_path = input_entry.get()
    remove_metadata(input_path, None)  # Pass None for output_path

app = tk.Tk()
app.title("Remove Image Metadata")

frame = tk.Frame(app)
frame.pack(padx=20, pady=20)

input_label = tk.Label(frame, text="Input Image:")
input_label.pack(anchor="w")

input_entry = tk.Entry(frame, width=50)
input_entry.pack(anchor="w")

input_button = tk.Button(frame, text="Browse", command=browse_input)
input_button.pack()

remove_button = tk.Button(frame, text="Remove Metadata", command=remove_metadata_gui)
remove_button.pack()

status_label = tk.Label(frame, text="")
status_label.pack()

app.mainloop()
