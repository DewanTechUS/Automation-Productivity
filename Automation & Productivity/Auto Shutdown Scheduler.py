# Auto Shutdown Scheduler GUI using Tkinter
# Clean, beginner-friendly, practical for Python portfolio and personal productivity

import tkinter as tk
from tkinter import messagebox
import os
import platform
import time
import threading

# Schedule shutdown function
def schedule_shutdown():
    try:
        delay_minutes = int(minutes_entry.get())
        if delay_minutes <= 0:
            raise ValueError

        confirm = messagebox.askyesno("Confirm", f"Schedule shutdown in {delay_minutes} minutes?")
        if not confirm:
            return

        threading.Thread(target=shutdown_after_delay, args=(delay_minutes * 60,), daemon=True).start()
        messagebox.showinfo("Scheduled", f"Shutdown scheduled in {delay_minutes} minutes.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive integer for minutes.")

# Execute shutdown after delay
def shutdown_after_delay(delay_seconds):
    time.sleep(delay_seconds)
    try:
        if platform.system() == "Windows":
            os.system("shutdown /s /t 1")
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            os.system("shutdown -h now")
        else:
            messagebox.showerror("Unsupported", "Shutdown is not supported on this OS.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to execute shutdown: {e}")

# Cancel shutdown (Windows only)
def cancel_shutdown():
    if platform.system() == "Windows":
        os.system("shutdown /a")
        messagebox.showinfo("Cancelled", "Shutdown has been cancelled.")
    else:
        messagebox.showwarning("Unavailable", "Shutdown cancel is only available on Windows.")

# GUI setup
root = tk.Tk()
root.title("Auto Shutdown Scheduler")
root.geometry("350x250")
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="Auto Shutdown Scheduler", font=("Arial", 16))
title_label.pack(pady=15)

# Entry for minutes
tk.Label(root, text="Enter delay in minutes before shutdown:").pack()
minutes_entry = tk.Entry(root, width=10, font=("Arial", 14), justify="center")
minutes_entry.pack(pady=10)

# Schedule button
schedule_button = tk.Button(root, text="Schedule Shutdown", command=schedule_shutdown, font=("Arial", 12))
schedule_button.pack(pady=10)

# Cancel button
cancel_button = tk.Button(root, text="Cancel Scheduled Shutdown", command=cancel_shutdown, font=("Arial", 12))
cancel_button.pack(pady=5)

# Instruction label
instruction_label = tk.Label(root, text="Note: Cancel feature works only on Windows.", fg="red")
instruction_label.pack(pady=5)

root.mainloop()