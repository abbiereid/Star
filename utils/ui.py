from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import datetime

class UI:
    def __init__(self):
        self.screen = Tk()
        self.screen.geometry("700x500")
        self.canvas = Canvas(self.screen, width=700, height=500, bg='#c2d6d6')
        self.logo = ImageTk.PhotoImage(Image.open("assets/logo.png"))
        self.canvas.create_image(350, 225, image=self.logo)
        self.canvas.pack()

        try:
            self.date = datetime.datetime.now().strftime("%m-%d-%Y")
            self.canvas.create_text(80, 470, text=self.date, font=("Arial", 20), fill="#6b9797")
        except Exception as e:
            print(f"Error getting date: {e}")
            self.date = "Date Error"

        try:
            self.time = datetime.datetime.now().strftime("%H:%M:%S")
            self.canvas.create_text(350, 20, text=self.time, font=("Arial", 20), fill="#6b9797")
        except Exception as e:
            print(f"Error getting time: {e}")
            self.time = "Time Error"

        self.lineX1 = 40
        self.lineX2 = 40
        self.loadingLine = self.canvas.create_line(self.lineX1, 450, self.lineX2, 450, fill="#6b9797", width=10)

    def run(self):
        self.screen.mainloop()

    def show_listening(self):
        self.listening = True
        self.lineX1 = 40
        self.lineX2 = 40
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
        self.move_line()

    def show_response(self, response):
        self.responseBox = self.canvas.create_rectangle(0, 0, 700, 500, fill="#c2d6d6", outline="#c2d6d6")
        self.response = self.canvas.create_text(350, 250, text=response, font=("Arial", 35), fill="#6b9797", width=600, anchor="center")
        self.canvas.tag_raise(self.response)
        self.screen.update()
        self.screen.after(10000, self.clear_response)

    def clear_response(self):
        self.canvas.delete(self.responseBox)
        self.canvas.delete(self.response)
