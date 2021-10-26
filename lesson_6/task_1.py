import tkinter as tk
from time import sleep


class TrafficLight(tk.Tk):

    def __init__(self):
        super().__init__()
        self.__color = 0
        self.title('Светофор')
        self.canvas = tk.Canvas(self, width=110, height=340, bg="#000000")
        self.f = self.canvas.create_rectangle(0, 0, 110, 320, fill="#000000")
        self.r = self.canvas.create_oval(5, 5, 105, 105, outline="#b3b3b3", fill="#ff0000", width=5)
        self.y = self.canvas.create_oval(5, 110, 105, 210, outline="#b3b3b3", fill="#202020", width=5)
        self.g = self.canvas.create_oval(5, 215, 105, 315, outline="#b3b3b3", fill="#202020", width=5)
        self.s = self.canvas.create_text(55, 160, fill="#ff0000", font='Arial 55', text="")
        self.btn = tk.Button(self, text='Переключить', bg="#202020", fg="#b0b0b0", font="16",
                             command=lambda: self.running())
        self.canvas.pack()
        self.btn.pack()

    def running(self):
        if self.__color == 0:
            self.__color = 1
            self.canvas.itemconfigure(self.r, fill='#ff0000')
            self.canvas.itemconfigure(self.y, fill='#202020')
            self.canvas.itemconfigure(self.g, fill='#202020')
            self.counter(7, "#ff0000")
        elif self.__color == 1:
            self.__color = 2
            self.canvas.itemconfigure(self.r, fill='#202020')
            self.canvas.itemconfigure(self.y, fill='#ffff00')
            self.canvas.itemconfigure(self.g, fill='#202020')
            self.after(2000, self.running)
        elif self.__color == 2:
            self.__color = 3
            self.canvas.itemconfigure(self.r, fill='#202020')
            self.canvas.itemconfigure(self.y, fill='#202020')
            self.canvas.itemconfigure(self.g, fill='#00ff00')
            self.counter(10, "#00ff00")
        elif self.__color == 3:
            self.__color = 4
            self.canvas.itemconfigure(self.r, fill='#202020')
            self.canvas.itemconfigure(self.y, fill='#ffff00')
            self.canvas.itemconfigure(self.g, fill='#202020')
            self.after(2000, self.running)
        else:
            self.__color = 0
            self.canvas.itemconfigure(self.r, fill='#ff0000')
            self.canvas.itemconfigure(self.y, fill='#202020')

    def counter(self, sec, ccolor):
        if sec:
            self.canvas.itemconfigure(self.s, fill=ccolor, text=str(sec))
            self.after(1000, lambda: self.counter(sec - 1, ccolor))
        else:
            self.canvas.itemconfigure(self.s, fill=ccolor, text="")
            self.running()


root = TrafficLight()
root.mainloop()
