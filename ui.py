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
        self.frames = []
        self.gif = Image.open("assets/runningLine.gif")
        
        for frame in range(0, self.gif.n_frames):
            self.gif.seek(frame)
            self.frames.append(ImageTk.PhotoImage(self.gif.copy()))

        self.listening_label = tk.Label(self.screen, bg='#c2d6d6')
        self.listening_label.place(x=60, y=0)
        self.update_listening_frames(0)

    def update_listening_frames(self, i):
        frame = self.frames[i]
        i = (i + 1) % len(self.frames)
        self.listening_label.config(image=frame)
        self.screen.after(50, self.update_listening_frames, i)
