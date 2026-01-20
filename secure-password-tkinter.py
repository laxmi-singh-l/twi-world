import secrets
import string
import tkinter as tk

def generate_password():
    alphabet = (string.ascii_letters + string.digits + string.punctuation)
    password = ''.join(secrets.choice(alphabet) for i in range(12))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)  

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    status_label.config(text="Password copied to clipboard!")

root = tk.Tk()
root.geometry("400x200")
root.title("Secure Password Generator")

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=20)
password_entry = tk.Entry(root, width=40 , font=('Arial', 12)) 
password_entry.pack(pady=10)
status_label = tk.Label(root, text="")
status_label.pack(pady=10)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=10)
root.mainloop()

# Random password generator
