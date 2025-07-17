# Screenshot Tool GUI using Tkinter and PIL
# Clean, beginner-friendly, practical for Python portfolio and utility creation

import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import ImageGrab
import datetime

# Capture and save screenshot
def take_screenshot():
    try:
        # Hide the window before taking screenshot
        root.withdraw()
        root.after(500, capture_screen)
    except Exception as e:
        messagebox.showerror("Error", f"Error taking screenshot: {e}")

def capture_screen():
    try:
        screenshot = ImageGrab.grab()
        file_path = filedialog.asksaveasfilename(
            defaultextension='.png',
            filetypes=[('PNG files', '*.png'), ('JPEG files', '*.jpg'), ('All files', '*.*')],
            initialfile=f'screenshot_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
        )
        if file_path:
            screenshot.save(file_path)
            messagebox.showinfo("Saved", f"Screenshot saved to {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving screenshot: {e}")
    finally:
        root.deiconify()

# GUI setup
root = tk.Tk()
root.title("Screenshot Tool")
root.geometry("300x200")
root.resizable(False, False)

label = tk.Label(root, text="Screenshot Tool", font=("Arial", 16))
label.pack(pady=20)

take_button = tk.Button(root, text="Take Screenshot", command=take_screenshot, font=("Arial", 12))
take_button.pack(pady=20)

instruction_label = tk.Label(root, text="Click the button to capture the entire screen.\nYou will be prompted to save the file.", justify="center")
instruction_label.pack(pady=10)

root.mainloop()
