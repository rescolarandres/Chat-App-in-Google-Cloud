import tkinter as tk
from tkinter import *

class Login_form():
    def __init__(self):
        # Create main self.window
        self.window = tk.Tk()
        self.window.title("Login")
        self.window.geometry("200x100")
        # Create labels
        tk.Label(self.window, text="IP Address: ").grid(row=0)
        tk.Label(self.window, text="Username: ").grid(row=1)
        tk.Label(self.window, text="Password: ").grid(row=2)
        # Create input fields for IP, username, and password
        self.ip_entry = tk.Entry(self.window)
        self.username_entry = tk.Entry(self.window)
        self.password_entry = tk.Entry(self.window, show="*") # Use show="*" to hide password characters
        # Place the input fields in the self.window
        self.ip_entry.grid(row=0, column=1)
        self.username_entry.grid(row=1, column=1)
        self.password_entry.grid(row=2, column=1)


    def submit(self):
        # Function to retrieve input values when the "Submit" button is clicked
        self.HOST = self.ip_entry.get()
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        # Destroy the self.window one data is loaded
        self.window.destroy()

    def run(self):
        # Create a "Submit" button to retrieve input values
        self.button = tk.Button(self.window, text="Submit", command=self.submit).grid(row=3, column=1)
        self.window.bind('<Return>',lambda event:self.submit())
        # Run the main event loop
        self.window.mainloop()