# QR Code Generator and Reader GUI using Tkinter, qrcode, and OpenCV
# Clean, beginner-friendly, practical for Python portfolio and productivity

import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
import cv2
from PIL import Image, ImageTk

# Generate QR Code
def generate_qr():
    data = qr_entry.get()
    if not data:
        messagebox.showwarning("Input Required", "Please enter text or URL to generate QR code.")
        return
    try:
        img = qrcode.make(data)
        file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[('PNG Files', '*.png')])
        if file_path:
            img.save(file_path)
            messagebox.showinfo("Success", f"QR Code saved as {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate QR Code: {e}")

# Read QR Code from Image
def read_qr():
    file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.png;*.jpg;*.jpeg;*.bmp')])
    if not file_path:
        return
    try:
        img = cv2.imread(file_path)
        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(img)
        if data:
            messagebox.showinfo("QR Code Data", f"Data: {data}")
        else:
            messagebox.showwarning("No QR Code", "No QR Code detected in the image.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read QR Code: {e}")

# GUI setup
root = tk.Tk()
root.title("QR Code Generator & Reader")
root.geometry("400x300")
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="QR Code Generator & Reader", font=("Arial", 16))
title_label.pack(pady=10)

# QR Entry
tk.Label(root, text="Enter text or URL to generate QR:").pack()
qr_entry = tk.Entry(root, width=40)
qr_entry.pack(pady=5)

# Generate QR Button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr, font=("Arial", 12))
generate_button.pack(pady=10)

# Read QR Button
read_button = tk.Button(root, text="Read QR Code from Image", command=read_qr, font=("Arial", 12))
read_button.pack(pady=10)

# Instruction label
instruction_label = tk.Label(root, text="Generate and save QR codes, or read data from existing QR code images.", wraplength=350, justify="center")
instruction_label.pack(pady=10)

root.mainloop()
