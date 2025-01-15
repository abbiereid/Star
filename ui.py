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

        self.lineX2 = 40
        self.loadingLine = self.canvas.create_line(40, 450, self.lineX2, 450, fill="#6b9797", width=10) #X1 and X2 are the same so that it can't be seen

    def run(self):
        self.screen.mainloop()

    def show_listening(self):
        for i in range(60):
            self.lineX2 += 10
            self.move_line()
        for i in range(60):
            self.lineX2 -= 10
            self.move_line()

    def move_line(self):
        self.canvas.coords(self.loadingLine, 40 , 450, self.lineX2, 450)
        self.screen.update()
        self.screen.after(10)

ui = UI()
ui.show_listening()
ui.run()