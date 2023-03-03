import tkinter as tk
from tkinter import *
import threading

class Dickscord():
    def __init__(self, s, name):
        # Define Discord colors
        discord_bg = "#36393F"
        discord_fg = "#FFFFFF"
        discord_gray = "#2F3136"
        discord_blue = "#7289DA"

        self.root = tk.Tk()
        self.root.title("Dickscord")
        self.root.config(bg=discord_bg,width='600', height='400')

        self.s = s
        self.name = name
        # Messages List
        self.message_frame = tk.Frame(self.root, bg=discord_gray)
        self.message_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # Create a label for the message history
        self.history_label = tk.Label(self.message_frame, text="Messages", bg=discord_gray, fg=discord_fg,
                                font=("Helvetica", 14))
        self.history_label.pack(side=tk.TOP, padx=10, pady=10)
        # Message list
        self.message_list = tk.Listbox(self.message_frame, bg=discord_bg, fg=discord_fg, 
                             font=("Helvetica", 12), highlightbackground=discord_blue,
                             highlightcolor=discord_blue, selectbackground=discord_blue,
                             selectforeground=discord_fg)
        self.message_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Message Entry Frame
        self.entry_frame = tk.Frame(self.root, bg=discord_gray)
        self.entry_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Create a label for the message input
        self.input_label = tk.Label(self.entry_frame, text="Send", bg=discord_gray, fg=discord_fg,
                            font=("Helvetica", 14))
        self.input_label.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Message entry
        self.message = tk.Entry(self.entry_frame, bg=discord_bg, fg=discord_fg, 
                       font=("Helvetica", 12), insertbackground=discord_fg)
        self.message.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Message button
        self.buttonMsg = tk.Button(self.root, text='Send',
                        command=lambda: self.sendButton(self.message.get()),
                        bg=discord_blue, fg=discord_fg, 
                        font=("Helvetica", 12), activebackground=discord_blue, 
                        activeforeground=discord_fg)
        
        self.root.bind('<Return>',lambda event:self.sendButton(self.message.get()))

        # Start the receive thread 
        rcv = threading.Thread(target=self.receiver)
        rcv.start()

        # End the GUI functionality by running the mainloop
        self.root.mainloop()

    def sendButton(self, msg):
        self.msg = msg
        # Delete the text in the box as soon as the message is saved in self
        self.message.delete(0,END)
        # Create an independent thread for sending
        snd = threading.Thread(target=self.sendMessage)
        snd.start()

    def insert_message(self,text):
        # Insert the message in the message list
        self.message_list.insert(tk.END,text)
        
    def sendMessage(self):
        while True:
            message = (f"{self.msg}")
            self.s.send(message.encode())
            break

    def receiver(self):
        while True:
            receiving_message = self.s.recv(1024)
            if receiving_message:
                self.message_list.insert(END,receiving_message.decode())

