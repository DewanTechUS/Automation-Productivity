# URL Shortener GUI using Tkinter and pyshorteners
# Clean, beginner-friendly, practical for Python portfolio and utility use

import tkinter as tk
from tkinter import messagebox
import pyshorteners

# Shorten URL function
def shorten_url():
    long_url = url_entry.get()
    if not long_url:
        messagebox.showwarning("Input Required", "Please enter a URL to shorten.")
        return
    try:
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(long_url)
        short_url_entry.delete(0, tk.END)
        short_url_entry.insert(0, short_url)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to shorten URL: {e}")

# Copy short URL to clipboard
def copy_to_clipboard():
    short_url = short_url_entry.get()
    if short_url:
        root.clipboard_clear()
        root.clipboard_append(short_url)
        messagebox.showinfo("Copied", "Short URL copied to clipboard.")
    else:
        messagebox.showwarning("No URL", "No URL to copy.")

# GUI setup
root = tk.Tk()
root.title("URL Shortener")
root.geometry("450x250")
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="URL Shortener", font=("Arial", 16))
title_label.pack(pady=10)

# Long URL entry
url_label = tk.Label(root, text="Enter URL to shorten:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Shorten button
shorten_button = tk.Button(root, text="Shorten URL", command=shorten_url, font=("Arial", 12))
shorten_button.pack(pady=10)

# Short URL display
short_url_label = tk.Label(root, text="Shortened URL:")
short_url_label.pack()
short_url_entry = tk.Entry(root, width=50)
short_url_entry.pack(pady=5)

# Copy button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12))
copy_button.pack(pady=10)

# Instruction
instruction_label = tk.Label(root, text="Uses TinyURL to shorten URLs.", wraplength=400, justify="center")
instruction_label.pack(pady=5)

root.mainloop()
