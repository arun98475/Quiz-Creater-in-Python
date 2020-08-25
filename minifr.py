from tkinter import *
class MiniWindow:
    def __init__(self,win,photo):
      self.win=win
      self.photo=photo
      canvas = Canvas(self.win,width=300, height=600, bg='black')
      canvas.pack(side=LEFT)
      canvas.create_image(150,300,image=self.photo)
