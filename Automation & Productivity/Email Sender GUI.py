# Email Sender GUI using Tkinter and smtplib
# Clean, beginner-friendly for Python GUI and practical projects

import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Send email function
def send_email():
    sender_email = sender_entry.get()
    password = password_entry.get()
    receiver_email = receiver_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END).strip()

    if not sender_email or not password or not receiver_email or not subject or not message:
        messagebox.showwarning("Input Required", "All fields must be filled.")
        return

    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)

        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {e}")

# GUI setup
root = tk.Tk()
root.title("Email Sender")
root.geometry("450x500")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Email Sender", font=("Arial", 16))
title_label.pack(pady=10)

# Sender email
sender_label = tk.Label(root, text="Your Email:")
sender_label.pack()
sender_entry = tk.Entry(root, width=40)
sender_entry.pack(pady=5)

# Password
password_label = tk.Label(root, text="Password (App Password recommended):")
password_label.pack()
password_entry = tk.Entry(root, width=40, show="*")
password_entry.pack(pady=5)

# Receiver email
receiver_label = tk.Label(root, text="Receiver Email:")
receiver_label.pack()
receiver_entry = tk.Entry(root, width=40)
receiver_entry.pack(pady=5)

# Subject
subject_label = tk.Label(root, text="Subject:")
subject_label.pack()
subject_entry = tk.Entry(root, width=40)
subject_entry.pack(pady=5)

# Message
message_label = tk.Label(root, text="Message:")
message_label.pack()
message_text = tk.Text(root, width=50, height=10)
message_text.pack(pady=5)

# Send button
send_button = tk.Button(root, text="Send Email", command=send_email, font=("Arial", 12))
send_button.pack(pady=20)

# Instructions
instructions = tk.Label(root, text="Note: Enable 'Less secure app access' or use App Passwords in Gmail settings.", wraplength=400, justify="center", fg="red")
instructions.pack(pady=5)

root.mainloop()
