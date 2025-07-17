# Automatic File Organizer (move files based on extensions) GUI
# Clean, beginner-friendly, practical for Python portfolio and desktop productivity

import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# File organization logic
def organize_files():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return

    try:
        files = os.listdir(folder_path)
        if not files:
            messagebox.showinfo("Empty", "The selected folder is empty.")
            return

        for file in files:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                extension = os.path.splitext(file)[1][1:].lower()
                if extension == '':
                    extension = 'no_extension'
                dest_folder = os.path.join(folder_path, extension)
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                shutil.move(file_path, os.path.join(dest_folder, file))

        messagebox.showinfo("Completed", "Files have been organized by extension.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI setup
root = tk.Tk()
root.title("Automatic File Organizer")
root.geometry("400x250")
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="Automatic File Organizer", font=("Arial", 16))
title_label.pack(pady=20)

# Instruction label
instruction_label = tk.Label(root, text="Select a folder to automatically sort\nfiles into subfolders based on their extensions.", justify="center")
instruction_label.pack(pady=10)

# Organize button
organize_button = tk.Button(root, text="Select Folder & Organize", command=organize_files, font=("Arial", 12))
organize_button.pack(pady=30)

root.mainloop()
