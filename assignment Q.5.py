import tkinter as tk
from tkinter import ttk, messagebox
import re

contacts = {}  # simulate DB with dictionary

def validate_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|edu|org)$'
    return re.match(pattern, email)

def add_contact():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    category = category_box.get()

    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email format")
        return
    if email in contacts:
        messagebox.showerror("Error", "Duplicate email")
        return

    contacts[email] = (name, phone, category)
    refresh_list()
    messagebox.showinfo("Success", "Contact added")

def refresh_list():
    for row in tree.get_children():
        tree.delete(row)
    for email, (name, phone, category) in contacts.items():
        tree.insert("", "end", values=(name, email, phone, category))

root = tk.Tk()
root.title("Contact Manager")

tk.Label(root, text="Name").grid(row=0, column=0)
tk.Label(root, text="Email").grid(row=1, column=0)
tk.Label(root, text="Phone").grid(row=2, column=0)
tk.Label(root, text="Category").grid(row=3, column=0)

name_entry = tk.Entry(root)
email_entry = tk.Entry(root)
phone_entry = tk.Entry(root)
category_box = ttk.Combobox(root, values=["Friend", "Faculty", "Family"])

name_entry.grid(row=0, column=1)
email_entry.grid(row=1, column=1)
phone_entry.grid(row=2, column=1)
category_box.grid(row=3, column=1)

tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0, columnspan=2)

tree = ttk.Treeview(root, columns=("Name", "Email", "Phone", "Category"), show="headings")
for col in ("Name", "Email", "Phone", "Category"):
    tree.heading(col, text=col)
tree.grid(row=5, column=0, columnspan=2)

root.mainloop()
