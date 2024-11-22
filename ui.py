import tkinter as tk
from tkinter import PhotoImage

class UI:
    def __init__(self):
        self.screen = tk.Tk(screenName="Star", baseName=None, className="UI")
        self.screen.geometry("700x450")

        self.logo = PhotoImage(file="assets/logo.png")
        self.logo_label = tk.Label(self.screen, image=self.logo, bg='#c2d6d6')
        self.logo_label.pack()

        self.screen.config(bg='#c2d6d6')


    def run(self):
        self.screen.mainloop()