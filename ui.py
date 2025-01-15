import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import threading

class UI:
    def __init__(self):
        self.screen = tk.Tk(screenName="Star", baseName=None, className="Star")
        self.screen.geometry("700x450")

        self.setLogo("assets/logo.png")
        
        self.screen.config(bg='#c2d6d6')

    def run(self):
        self.screen.mainloop()
    
    def setLogo(self, path): #This method is not really necessary anymore, may aswell simplifiy it.
        self.logo = PhotoImage(file=path)
        if hasattr(self, 'logo_label'):
            self.logo_label.config(image=self.logo)
        else:
            self.logo_label = tk.Label(self.screen, image=self.logo, bg='#c2d6d6')
            self.logo_label.pack()

    def show_listening(self):
        pass

    def update_listening_frames(self, i):
        pass
