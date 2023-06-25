import tkinter as tk
import random
import string
import tkinter.messagebox as messagebox
import pyperclip

def generate_password():
    # password requirements
    length = length_entry.get()
    uppercase = uppercase_entry.get()
    lowercase = lowercase_entry.get()
    numbers = numbers_entry.get()
    special = special_entry.get()

    # check if requirements unfilled
    if '' in [length, uppercase, lowercase, numbers, special]:
        password_result.config(text="Please fill in all requirements.")
        return

    # check if length is a valid number in range
    try:
        length = int(length)
        if length < 1 or length > 100:
            raise ValueError
    except ValueError:
        password_result.config(text="Length must be a valid number between 1 and 100.")
        return

    # check if requirements are valid non-negative integers
    for value in [uppercase, lowercase, numbers]:
        try:
            value = int(value)
            if value < 0:
                raise ValueError
        except ValueError:
            password_result.config(text="Requirements must be valid non-negative integers.")
            return

    # check if special characters requirement is a valid non-negative integer
    try:
        special = int(special)
        if special < 0:
            raise ValueError
    except ValueError:
        password_result.config(text="Special characters must be a valid non-negative integer.")
        return

    # check if requirements exceed the length
    if int(uppercase) + int(lowercase) + int(numbers) + int(special) > length:
        password_result.config(text="Requirements exceed length.")
        return

    # generate password
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''

    if int(uppercase) > 0:
        password += ''.join(random.sample(string.ascii_uppercase, int(uppercase)))

    if int(lowercase) > 0:
        password += ''.join(random.sample(string.ascii_lowercase, int(lowercase)))

    if int(numbers) > 0:
        password += ''.join(random.sample(string.digits, int(numbers)))

    if int(special) > 0:
        password += ''.join(random.sample(string.punctuation, int(special)))

    remaining_length = length - len(password)
    if remaining_length > 0:
        password += ''.join(random.choices(chars, k=remaining_length))

    password = ''.join(random.sample(password, len(password)))

    password_result.config(text=password)
    copy_button.config(state=tk.NORMAL)

def copy_to_clipboard():
    password = password_result.cget("text")
    pyperclip.copy(password)
    messagebox.showinfo("Copy to Clipboard", "Password copied to clipboard.")

# gui
window = tk.Tk()
window.title("Password Generator")
window.configure(bg="black")

# req label and entries
length_label = tk.Label(window, text="Length:", bg="black", fg="white")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(window, bg="white", fg="black")
length_entry.grid(row=0, column=1, padx=10, pady=10)

uppercase_label = tk.Label(window, text="Uppercase Letters:", bg="black", fg="white")
uppercase_label.grid(row=1, column=0, padx=10, pady=10)

uppercase_entry = tk.Entry(window, bg="white", fg="black")
uppercase_entry.grid(row=1, column=1, padx=10, pady=10)

lowercase_label = tk.Label(window, text="Lowercase Letters:", bg="black", fg="white")
lowercase_label.grid(row=2, column=0, padx=10, pady=10)

lowercase_entry = tk.Entry(window, bg="white", fg="black")
lowercase_entry.grid(row=2, column=1, padx=10, pady=10)

numbers_label = tk.Label(window, text="Numbers:", bg="black", fg="white")
numbers_label.grid(row=3, column=0, padx=10, pady=10)

numbers_entry = tk.Entry(window, bg="white", fg="black")
numbers_entry.grid(row=3, column=1, padx=10, pady=10)

special_label = tk.Label(window, text="Special Characters:", bg="black", fg="white")
special_label.grid(row=4, column=0, padx=10, pady=10)

special_entry = tk.Entry(window, bg="white", fg="black")
special_entry.grid(row=4, column=1, padx=10, pady=10)

generate_button = tk.Button(window, text="Generate Password", command=generate_password, bg="white", fg="black")
generate_button.grid(row=5, column=0, columnspan=2, pady=10)

password_result = tk.Label(window, text="", bg="black", fg="white")
password_result.grid(row=6, column=0, columnspan=2, pady=10)

copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard, bg="white", fg="black")
copy_button.grid(row=7, column=0, columnspan=2, pady=5)
copy_button.config(state=tk.DISABLED)

# center
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry(f"{width}x{height}+{x}+{y}")

window.mainloop()
