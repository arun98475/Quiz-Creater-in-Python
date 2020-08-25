from tkinter import*
class CustButton:
    def __init__(self,win,width,height,border_radius,color):
      self.win=win
      self.width=width
      self.height=height
      self.color=color
      self.border_radius=border_radius
     
      
      try :
          self.textcolor=textcolor
      except:
          self.textcolor="white"
      self.C = Canvas(self.win,height=self.height, width=self.width,relief="raised")
      self.C.pack()
      
      W=self.width
      H=self.height
      br=self.border_radius
      x=2
      x1=x+br
      x2=x+W-br
      x3=x+W
      y=2
      y1=y
      y2=y+br
      y3=y+H-br
      y4=y+H
      coord1 = x,y,x+2*br,y+2*br
      arc1 = self.C.create_oval(coord1, fill=self.color)
      coord2 = x+W-2*br,y,x+W,y+2*br
      arc2 = self.C.create_oval(coord2, fill=self.color)
      coord3 = x2-br,y3-br,x+W,y+H
      arc3 = self.C.create_oval(coord3, fill=self.color)
      coord4 = x1+br,y3-br,x,y+H
      arc3 = self.C.create_oval(coord4, fill=self.color)
      poly=self.C.create_polygon(x1,y1,x2,y1,x2,y2,x3,y2,x3,y3,x2,y3,x2,y4,x1,y4,x1,y3,x,y3,x,y2,x1,y2,fill=self.color)
    def scoretext(self,textcolor):
      textcolor
      text=self.C.create_text(250,25,text="Your score is 10 out of 10",fill=textcolor,font="Times 20 italic bold")
    def questiontext(self,textcolor):
      text=self.C.create_text(175,20,text="Your Question is here",fill=textcolor,font="Times 12 italic bold")
      text=self.C.create_text(150,40,text="Option_A",fill=textcolor,font="Times 10 italic bold")
      text=self.C.create_text(150,60,text="Option_B",fill=textcolor,font="Times 10 italic bold")
      text=self.C.create_text(150,80,text="Option_C",fill=textcolor,font="Times 10 italic bold")
      text=self.C.create_text(150,100,text="Option_D",fill=textcolor,font="Times 10 italic bold")
    def interLabel(self,textcolor):
      text=self.C.create_text(100,10,text="Question No",fill=textcolor,font="Times 18 italic bold") 
'''
win=Tk()
for i in range (3):
      CustButton(win,500,20,0,"white").interLabel("black")
      CustButton(win,500,125,10,"black").questiontext("white")
      
CustButton(win,500,50,25,"#400040").scoretext("white")
'''

