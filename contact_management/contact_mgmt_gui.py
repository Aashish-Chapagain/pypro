import tkinter as tk
from tkinter import messagebox
from contact_class import Contacts  # Importing the Contacts class

# Initialize Contacts instance
_contacts = Contacts()

class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contacts Manager")
        self.root.geometry("400x400")
        
        # Create widgets (labels, buttons, entry fields)
        self.create_widgets()
        
    def create_widgets(self):
        # Name
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.pack(pady=5)
        
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)

        # Phone Number
        self.phone_label = tk.Label(self.root, text="Phone Number:")
        self.phone_label.pack(pady=5)
        
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.pack(pady=5)

        # Email
        self.email_label = tk.Label(self.root, text="Email:")
        self.email_label.pack(pady=5)
        
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack(pady=5)

        # Address
        self.address_label = tk.Label(self.root, text="Address:")
        self.address_label.pack(pady=5)
        
        self.address_entry = tk.Entry(self.root)
        self.address_entry.pack(pady=5)

        # Buttons
        self.save_button = tk.Button(self.root, text="Save Contact", command=self.save_contact)
        self.save_button.pack(pady=10)

        self.search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        self.search_button.pack(pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=10)

        self.edit_button = tk.Button(self.root, text="Edit Contact", command=self.edit_contact)
        self.edit_button.pack(pady=10)

    def save_contact(self):
        name = self.name_entry.get().strip().lower()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if name and phone and email and address:
            try:
                _contacts.save_contact(name, phone, email, address)
                messagebox.showinfo("Success", "Contact saved!")
                self.clear_entries()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save contact: {str(e)}")
        else:
            messagebox.showwarning("Input Error", "Please fill out all fields")

    def search_contact(self):
        name = self.name_entry.get().strip().lower()
        
        if name:
            _contacts.search_contact(name)
        else:
            messagebox.showwarning("Input Error", "Please enter a name to search.")

    def delete_contact(self):
        name = self.name_entry.get().strip().lower()

        if name:
            _contacts.delete_from_json(name)
            messagebox.showinfo("Success", "Contact deleted.")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please enter a name to delete.")

    def edit_contact(self):
        name = self.name_entry.get().strip().lower()
        
        if name:
            new_phone = self.phone_entry.get().strip() or None
            new_email = self.email_entry.get().strip() or None
            new_address = self.address_entry.get().strip() or None

            _contacts.edit_contact(name, new_phone, new_email, new_address)
            messagebox.showinfo("Success", "Contact updated.")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please enter a name to edit.")
    
    def clear_entries(self):
        """Clear all input fields after an action"""
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

# Set up the Tkinter root window
root = tk.Tk()
app = ContactApp(root)

# Start the Tkinter event loop
root.mainloop()
