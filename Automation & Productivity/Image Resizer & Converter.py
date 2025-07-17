# Image Resizer & Converter GUI using Tkinter and PIL
# Clean, beginner-friendly, practical for Python portfolio and productivity tools

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

# Resize and convert image
def process_image():
    try:
        file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.png;*.jpg;*.jpeg;*.bmp;*.gif')])
        if not file_path:
            return
        img = Image.open(file_path)

        # Get target width and height
        try:
            width = int(width_entry.get())
            height = int(height_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Width and height must be integers.")
            return

        img_resized = img.resize((width, height))

        # Select output format
        format_selected = format_var.get()
        extension = format_selected.lower()

        # Save resized and converted image
        save_path = filedialog.asksaveasfilename(
            defaultextension=f'.{extension}',
            filetypes=[(f'{format_selected} files', f'*.{extension}'), ('All files', '*.*')]
        )
        if save_path:
            img_resized.save(save_path, format=format_selected)
            messagebox.showinfo("Saved", f"Image saved as {save_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI setup
root = tk.Tk()
root.title("Image Resizer & Converter")
root.geometry("400x300")
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="Image Resizer & Converter", font=("Arial", 16))
title_label.pack(pady=10)

# Dimension entry frame
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

tk.Label(entry_frame, text="Width:").grid(row=0, column=0, padx=5)
tk.Label(entry_frame, text="Height:").grid(row=0, column=1, padx=5)

width_entry = tk.Entry(entry_frame, width=10)
width_entry.grid(row=1, column=0, padx=5)

height_entry = tk.Entry(entry_frame, width=10)
height_entry.grid(row=1, column=1, padx=5)

# Format selection
format_var = tk.StringVar(value='PNG')
tk.Label(root, text="Select Format:").pack()
format_options = tk.OptionMenu(root, format_var, 'PNG', 'JPEG', 'BMP', 'GIF')
format_options.pack(pady=5)

# Process button
process_button = tk.Button(root, text="Select Image and Process", command=process_image, font=("Arial", 12))
process_button.pack(pady=20)

# Instruction label
instruction_label = tk.Label(root, text="Enter target dimensions, select format,\nthen choose an image to resize and convert.", justify="center")
instruction_label.pack(pady=10)

root.mainloop()
