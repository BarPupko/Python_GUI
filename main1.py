import tkinter as tk
from tkinter import messagebox


class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        # self.menubar = tk.menu(self.root)
        # if it's checked we will get a popup

        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()  # state of the check box 1/0

        self.check = tk.Checkbutton(self.root, text="Show MessageBox", font=('Arial', 16))
        self.check.pack(padx=10, pady=10)

        # variables that will have the value of checked button
        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self)  # when we close the button we call this function
        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event):

        if event.state == 12 and event.keysym == "Return":
            self.show_message()

    def on_closing(self):
        print("Hello World")

        # print(event.state)


MyGUI()
