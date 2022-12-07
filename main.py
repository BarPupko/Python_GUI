import tkinter as tk


class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        # if it's checked we will get a popup

        self.label = tk.Label(self.root, text="Yoour Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()  # state of the check box 1/0

        self.check = tk.Checkbutton(self.root, text="Show MessageBox", font=('Arial', 16))

        # variables that will have the value of checked button
        self.check.pack(padx=10, pady=10)

        self.root.mainloop()
