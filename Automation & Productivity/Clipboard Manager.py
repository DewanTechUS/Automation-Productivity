# Clipboard Manager GUI using Tkinter
# Clean, beginner-friendly, practical for Python portfolio and productivity

import tkinter as tk
from tkinter import messagebox

# Global list to store clipboard history
clipboard_history = []

# Save current clipboard text
def save_clipboard():
    try:
        text = root.clipboard_get()
        if text not in clipboard_history:
            clipboard_history.insert(0, text)
            update_listbox()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to get clipboard content: {e}")

# Copy selected text back to clipboard
def copy_to_clipboard():
    try:
        selected = listbox.curselection()
        if not selected:
            messagebox.showwarning("Select Item", "Please select an item to copy.")
            return
        text = listbox.get(selected[0])
        root.clipboard_clear()
        root.clipboard_append(text)
        messagebox.showinfo("Copied", "Text copied to clipboard.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to copy: {e}")

# Update Listbox with clipboard history
def update_listbox():
    listbox.delete(0, tk.END)
    for item in clipboard_history:
        display_text = item if len(item) <= 50 else item[:50] + "..."
        listbox.insert(tk.END, display_text)

# Clear clipboard history
def clear_history():
    if messagebox.askyesno("Clear History", "Are you sure you want to clear the clipboard history?"):
        clipboard_history.clear()
        update_listbox()

# GUI setup
root = tk.Tk()
root.title("Clipboard Manager")
root.geometry("400x400")
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="Clipboard Manager", font=("Arial", 16))
title_label.pack(pady=10)

# Save clipboard button
save_button = tk.Button(root, text="Save Current Clipboard", command=save_clipboard, font=("Arial", 12))
save_button.pack(pady=5)

# Listbox to display clipboard history
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)

# Copy and clear buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

copy_button = tk.Button(button_frame, text="Copy Selected", command=copy_to_clipboard, font=("Arial", 12))
copy_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear History", command=clear_history, font=("Arial", 12))
clear_button.grid(row=0, column=1, padx=10)

root.mainloop()
