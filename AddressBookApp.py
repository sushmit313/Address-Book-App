import tkinter as tk
from tkinter import messagebox

class AddressBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Address Book")
        
        self.contacts = []

        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(master, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_label = tk.Label(master, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(master, width=30)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(master, width=30)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.listbox = tk.Listbox(master, width=50)
        self.listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=5, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        if name and phone and email:
            contact = {"Name": name, "Phone": phone, "Email": email}
            self.contacts.append(contact)
            self.update_listbox()
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Please fill in all fields.")

    def delete_contact(self):
        try:
            index = self.listbox.curselection()[0]
            del self.contacts[index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a contact to delete.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.listbox.insert(tk.END, f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = AddressBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
