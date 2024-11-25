import tkinter as tk
from tkinter import PhotoImage
import threading

class UI:
    def __init__(self):
        self.screen = tk.Tk(screenName="Star", baseName=None, className="Star")
        self.screen.geometry("700x450")

        self.setLogo("assets/logo.png")
        
        self.screen.config(bg='#c2d6d6')

    def run(self):
        self.screen.mainloop()
    
    def setLogo(self, path):
        self.logo = PhotoImage(file=path)
        self.logo_label = tk.Label(self.screen, image=self.logo, bg='#c2d6d6')
        self.logo_label.pack()