from tkinter import*
win=Tk()
win.geometry('500x500')
win.configure(bg="light blue")
no_of_qns=5
var=[StringVar() for i in range(5)]
choices = ["A","B","C","D"]
tkvar=StringVar()
tkvar.set("A")

class entry:
    def __init__(self,win):
        self.win=win
        self.question='Question'
        self.optionA='OptionA'
        self.optionB='OptionB'
        self.optionC='OptionC'
        self.optionD='OptionD'
        
    def qn_entry(self):
        e1=Entry(self.win,width=50,textvariable=var[0])
        Label(self.win,text=self.question).grid(row=0,column=0)
        return e1
    def opA_entry(self):
        e2=Entry(self.win,width=50,textvariable=var[1])
        e2
        Label(self.win,text=self.optionA).grid(row=1,column=0)
        return e2
    def opB_entry(self):
        e3=Entry(self.win,width=50,textvariable=var[2])
        e3
        Label(self.win,text=self.optionB).grid(row=2,column=0)
        return e3
    def opC_entry(self):
        e4=Entry(self.win,width=50,textvariable=var[3])
        e4
        Label(self.win,text=self.optionC).grid(row=3,column=0)
        return e4
    def opD_entry(self):  
        e5=Entry(self.win,width=50,textvariable=var[4])
        e5
        Label(self.win,text=self.optionD).grid(row=4,column=0)
        return e5
    def drop_down(self):
        OptionMenu(win, tkvar, *choices).grid(row=5,column=1,sticky="e")
        Label(self.win,text="Select the Correct Answer->").grid(row=5,column=1)
    def clearall(self):
        for i in var:
             i.set("")
        

        
content=[["" for i in range (6)] for i in range (no_of_qns)]
q1=entry(win).qn_entry()
qA=entry(win).opA_entry()
qB=entry(win).opB_entry()
qC=entry(win).opC_entry()
qD=entry(win).opD_entry()
qans=entry(win).drop_down()

q1.grid(row=0,column=1)
qA.grid(row=1,column=1)
qB.grid(row=2,column=1)
qC.grid(row=3,column=1)
qD.grid(row=4,column=1)


j=0
def En():
    global j
    content[j][0]=q1.get()
    content[j][1]=qA.get()
    content[j][2]=qB.get()
    content[j][3]=qC.get()
    content[j][4]=qD.get()
    content[j][5]=tkvar.get()
    
    j=j+1
def Next():
    entry(win).clearall()
          
def Prt():
    
    pt=Tk()
    pt.config(bg="white")
    pt.geometry('500x500')
    va=[StringVar() for i in range(5)]
    Entry(pt,textvariable=va[0]).pack()
    Entry(pt,textvariable=va[1]).pack()
    Entry(pt,textvariable=va[2]).pack()
    Entry(pt,textvariable=va[3]).pack()
    Entry(pt,textvariable=va[4]).pack()
    va[0].set("hai")
    pt.mainloop()
Button(win,text="Save",command=En).grid(row=7,column=1,sticky="w")
Button(win,text="Next",command=Next).grid(row=7,column=1,sticky="e")
Button(win,text="Print",command=Prt).grid(row=8,column=1)
win.mainloop()
   


