from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

class UI:
    def __init__(self):
        self.screen = Tk()
        self.screen.geometry("700x500")
        self.canvas = Canvas(self.screen, width=700, height=500, bg='#c2d6d6')
        self.logo = ImageTk.PhotoImage(Image.open("assets/logo.png"))
        self.canvas.create_image(350, 225, image=self.logo)
        self.canvas.pack()

        self.lineX1 = 40
        self.lineX2 = 40
        self.loadingLine = self.canvas.create_line(self.lineX1, 450, self.lineX2, 450, fill="#6b9797", width=10) #X1 and X2 are the same so that it can't be seen

    def run(self):
        self.screen.mainloop()

    def show_listening(self):
        self.listening = True
        while self.listening:
            for i in range(60):
                self.lineX2 += 10
                self.lineX1 += 7
                self.move_line()
            for i in range(60):
                self.lineX2 -= 10
                self.lineX1 -= 7
                self.move_line()

    def move_line(self):
        self.canvas.coords(self.loadingLine, self.lineX1 , 450, self.lineX2, 450)
        self.screen.update()
        self.screen.after(10)

    def stop_listening(self):
        self.listening = False