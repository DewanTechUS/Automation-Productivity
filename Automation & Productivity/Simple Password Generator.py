# Simple Password Generator GUI using Tkinter
# Clean, beginner-friendly, practical for Python portfolio and daily utility

import tkinter as tk
from tkinter import messagebox
import random
import string


# Generate password function
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError

        use_upper = upper_var.get()
        use_lower = lower_var.get()
        use_digits = digits_var.get()
        use_symbols = symbols_var.get()

        if not (use_upper or use_lower or use_digits or use_symbols):
            messagebox.showwarning("Selection Required", "Select at least one character type.")
            return

        characters = ""
        if use_upper:
            characters += string.ascii_uppercase
        if use_lower:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive integer for length.")


# GUI setup
root = tk.Tk()
root.title("Simple Password Generator")
root.geometry("400x350")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Password Generator", font=("Arial", 16))
title_label.pack(pady=10)

# Length entry
length_frame = tk.Frame(root)
length_frame.pack(pady=5)
tk.Label(length_frame, text="Password Length:").grid(row=0, column=0, padx=5)
length_entry = tk.Entry(length_frame, width=10)
length_entry.grid(row=0, column=1, padx=5)

# Options
options_frame = tk.Frame(root)
options_frame.pack(pady=10)
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=False)

tk.Checkbutton(options_frame, text="Include Uppercase", variable=upper_var).pack(anchor="w")
tk.Checkbutton(options_frame, text="Include Lowercase", variable=lower_var).pack(anchor="w")
tk.Checkbutton(options_frame, text="Include Digits", variable=digits_var).pack(anchor="w")
tk.Checkbutton(options_frame, text="Include Symbols", variable=symbols_var).pack(anchor="w")

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12))
generate_button.pack(pady=15)

# Password display
password_entry = tk.Entry(root, font=("Arial", 14), justify="center")
password_entry.pack(pady=10, fill='x', padx=50)

# Instruction
instruction_label = tk.Label(root, text="Select options and length, then generate a secure password.", wraplength=300,
                             justify="center")
instruction_label.pack(pady=5)

root.mainloop()
