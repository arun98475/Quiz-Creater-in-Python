from tkinter import*

from tkinter.tix import *

win=Tk()

class my:
    def __init__(self,win):
        self.win=win
        self.tkvar = StringVar()
        self.choices = ['2','3','4']
        self.tkvar.set(self.choices[0])
        tk.__init__.OptionMenu(self.win, self.tkvar, *self.choices).grid(row=0,column=0,sticky="w")
        Button(self.win,text="Click Me",command=self.change_dropdow).grid(row=0,column=1)
    def change_dropdow(self):
             x=self.tkvar.get()
             print(x)
x=my(win)
