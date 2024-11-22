import tkinter as tk

class UI:
    def __init__(self):
        self.screen = tk.Tk(screenName="Star", baseName=None, className="UI")
    
    def run(self):
        self.screen.mainloop()