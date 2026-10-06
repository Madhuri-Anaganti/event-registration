import tkinter as tk
from tkinter import messagebox

def register():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    event = event_var.get()

    if name == "" or email == "" or phone == "" or event == "":
        messagebox.showwarning("Error", "Please fill in all fields.")
    else:
        messagebox.showinfo(
            "Registration Successful",
            f"Thank you, {name}!\n\n"
            f"Email: {email}\n"
            f"Phone: {phone}\n"
            f"Event: {event}"
        )

        # Clear the form
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        event_var.set("")


# Create main window
window = tk.Tk()
window.title("Event Registration Form")
window.geometry("400x400")
window.resizable(False, False)

# Heading
title = tk.Label(
    window,
    text="Event Registration Form",
    font=("Arial", 18, "bold")
)
title.pack(pady=20)

# Name
tk.Label(window, text="Full Name:").pack()
name_entry = tk.Entry(window, width=40)
name_entry.pack(pady=5)

# Email
tk.Label(window, text="Email:").pack()
email_entry = tk.Entry(window, width=40)
email_entry.pack(pady=5)

# Phone
tk.Label(window, text="Phone Number:").pack()
phone_entry = tk.Entry(window, width=40)
phone_entry.pack(pady=5)

# Event selection
tk.Label(window, text="Select Event:").pack()

event_var = tk.StringVar()

events = [
    "Tech Conference",
    "Music Festival",
    "Sports Meet",
    "Python Workshop"
]

event_menu = tk.OptionMenu(window, event_var, *events)
event_menu.config(width=25)
event_menu.pack(pady=5)

# Register button
register_button = tk.Button(
    window,
    text="Register",
    command=register,
    bg="blue",
    fg="white",
    width=20
)
register_button.pack(pady=20)

# Run application
window.mainloop()
