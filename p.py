import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showwarning("Warning", "Length must be greater than 0!")
            return

        # Check character type selections
        use_uppercase = uppercase_var.get()
        use_lowercase = lowercase_var.get()
        use_digits = digits_var.get()
        use_symbols = symbols_var.get()

        if not (use_uppercase or use_lowercase or use_digits or use_symbols):
            messagebox.showwarning("Warning", "Select at least one character type!")
            return

        # Build the character pool
        character_pool = ""
        if use_uppercase:
            character_pool += string.ascii_uppercase
        if use_lowercase:
            character_pool += string.ascii_lowercase
        if use_digits:
            character_pool += string.digits
        if use_symbols:
            character_pool += string.punctuation

        # Generate the password
        password = "".join(random.choices(character_pool, k=length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length!")

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# Main Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Password Length
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root, width=10)
length_entry.pack(pady=5)

# Character Type Selection
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=uppercase_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=lowercase_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Digits (0-9)", variable=digits_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Symbols (!@#$)", variable=symbols_var).pack(anchor="w", padx=20)

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Password Entry
password_entry = tk.Entry(root, width=40)
password_entry.pack(pady=10)

# Copy Button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

# Start GUI
root.mainloop()
