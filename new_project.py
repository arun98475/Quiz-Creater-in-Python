from tkinter import*
from tkinter import filedialog
from tkinter.tix import*
from tkcolorpicker import askcolor
from tkinter import RButton
from PIL import Image
from PIL import ImageTk
import minifr
from preview import CustButton
masterwin=Tk()
masterwin.title("Quiz Creator")
masterwin.geometry('1084x500')
masterwin.config(bg="light blue")

'''
photo=Image.open("Capture.png")
photo = photo.resize((300,600), Image.ANTIALIAS)
photo =ImageTk. PhotoImage(photo)     
minifr.MiniWindow(masterwin,photo)
'''




class Menubar:
   
    def __init__(self,wind):
        self.wind=wind
        menu=Menu(self.wind)
        self.wind.config(menu=menu)
        saveFilename=""
        Menubar.fileCounter=0
        self.tkvar = StringVar()
        self.choices = ['2','3','4','5','6']
        self.tkvar.set(self.choices[0])
       
        filemenu=Menu(menu,tearoff=0)
        filemenu.add_command(label="New",command=self.newProject)
        filemenu.add_command(label="Open",command=self.openDialog)
        filemenu.add_command(label="Save",command=self.saveDialog)
        filemenu.add_command(label="Save as",command=self.saveAsDialog)
        filemenu.add_separator()
        filemenu.add_command(label="Exit",command=self.exitFrom)
        menu.add_cascade(label="File",menu=filemenu)

        previewmenu=Menu(menu,tearoff=0)
        previewmenu.add_command(label="Preview",command=self.Preview)
        menu.add_cascade(label="Preview",menu=previewmenu)
    
    def exitFrom(self):
        exit()
        
    def Preview(self):
        preWindow=Tk()
        for i in range (3):
             CustButton(preWindow,500,20,0,"white").interLabel("black")
             CustButton(preWindow,500,125,customize.B,customize.Fcolor).questiontext(customize.Tcolor)
        CustButton(preWindow,500,50,customize.A,customize.Scolor).scoretext(customize.STcolor)

    def butcall(self):
        Menubar.newProject(self)
    def newProject(self,*arg):
        self.newpwin=Tk()
        
        self.newpwin.title("Quiz Creator")
        self.newpwin.geometry('300x200')
        Label(self.newpwin,text="No of Questions").grid(row=0,column=0,sticky="E")
        Label(self.newpwin,text="No of Options").grid(row=1,column=0,sticky="E")
        L=Label(self.newpwin,text="2")
        L.grid(row=1,column=1)
        Label(self.newpwin,text="Marks for Correct Ans.").grid(row=2,column=0,sticky="E")
        Label(self.newpwin,text="Marks(-) for Wrong Ans.").grid(row=3,column=0,sticky="E")
        self.qnNos=Entry(self.newpwin)
        def onchange(*arg):
            L.config(text=self.tkvar.get())
        tkinter.OptionMenu(self.newpwin,self.tkvar,*self.choices,command=onchange).grid(row=1,column=1,sticky="E")
        self.cMarks=Entry(self.newpwin)
        self.wMarks=Entry(self.newpwin)
        self.qnNos.grid(row=0,column=1,sticky="w")
      
        self.cMarks.grid(row=2,column=1,sticky="W")
        self.wMarks.grid(row=3,column=1,sticky="W")
        Button(self.newpwin,text="OK",width=6,command=self.pressOk).grid(row=4,column=1,sticky="E")
        Menubar.fileCounter=0
    
    def pressOk(self):
        Menubar.noOfQns=int(self.qnNos.get())
        Menubar.noOfOptions=int(self.tkvar.get())+1
        if self.cMarks.get()=="": Menubar.corrMarks="0"
        else : Menubar.corrMarks=self.cMarks.get()
        if self.wMarks.get()=="":Menubar.wrongMarks="0"
        else:Menubar.wrongMarks=self.wMarks.get()
        y=MainProg(masterwin)
        self.newpwin.destroy()
    def openDialog(self):
        Menubar.openFilename=filedialog.askopenfilename(title="select",filetypes=[("Text","*.txt")])
        z=fileImporter(masterwin)
    def saveDialog(self):
        if Menubar.fileCounter==0 :
           Menubar.saveFilename = filedialog.asksaveasfilename(title="select", defaultextension="*.txt",filetypes=[("Text","*.txt")])
           Menubar.fileCounter=1
        else:
            f=open(Menubar.saveFilename,"w")
            f.close()
        filename=Menubar.saveFilename
        z=textWriter(filename)
    def saveAsDialog(self):
        Menubar.saveFilename = filedialog.asksaveasfilename(title="select", defaultextension="*.txt",filetypes=[("Text","*.txt")])



class MainProg(Menubar):
        def __init__(self,win):
            super().__init__(win)
          
            self.wind=win
            MainProg.swin = ScrolledWindow(self.wind, width=650,bg="yellow")
            MainProg.swin.pack()
            MainProg.Swind = self.swin.window
            MainProg.option=[StringVar() for i in range(self.noOfQns)]
            MainProg.k=0
            MainProg.qnEntryVar=[[StringVar() for i in range(self.noOfOptions)] for j in range(self.noOfQns)]
            MainProg.qnAns=[['' for i in range(self.noOfOptions+1)]for j in range (self.noOfQns)]
            MainProg.Values=['A','B','C','D','E','F','G']
            MainProg.labele=['Question No:','Option-A','Option-B','Option-C','Option-D','Option-E','Option-F','Option-G']
            MainProg.qnEntry=[[self.createEntry(a) for a in range (self.noOfOptions)] for i in range (self.noOfQns)]
            MainProg.qnLabel=[[self.createLabel(a,i) for a in range (self.noOfOptions)] for i in range (self.noOfQns)]
            MainProg.correct=[[self.createRadio(R,r) for r in range(self.noOfOptions-1)] for R in range (self.noOfQns)]
            for i in range (self.noOfQns):
                self.option[i].set(self.Values[0])
            for i in range(self.noOfQns):
               for j in range(self.noOfOptions):
                   if j!=0:
                     self.qnEntry[i][j].config(textvariable=MainProg.qnEntryVar[i][j])
                 
            for i in range (self.noOfQns):
                   for j in range (self.noOfOptions):
                       self.qnLabel[i][j].grid(row=MainProg.k,column=0,sticky="E")
                       self.qnEntry[i][j].grid(row=MainProg.k,column=1,sticky="W")
                       if j!=0:
                           self.correct[i][j-1].grid(row=self.k,column=3,sticky="W")
                       MainProg.k=MainProg.k+1
            MainProg.htmlbutton=Button(self.Swind,text="Create Html Code",command=self.getAns)
            MainProg.htmlbutton.grid(row=MainProg.k,column=1)
        def createEntry(self,a):
            if a==0:
              return Text(self.Swind,width=50,height=3,bd=4)
            else:
              return Entry(self.Swind,width=40)
        def createLabel(self,a,i):
            if a==0:
              lab=self.labele[0]+str(i+1)
              return Label(self.Swind,text=lab)
            else:
              return Label(self.Swind,text=self.labele[a])
            
        def createRadio(self,R,r):
                
                return Radiobutton(self.Swind,text="Correct Ans",variable=self.option[R],value=self.Values[r])
            
        def getAns(self):
            Marks=Menubar.noOfQns*int(self.corrMarks)
            for i in range(Menubar.noOfQns):
                for j in range (Menubar.noOfOptions):
                    if j==0:
                       newAns=""
                       answers=MainProg.qnEntry[i][j].get("1.0",END)
                       for m in answers:
                           if m!='\n':newAns+=m
                           else:newAns+=" "
                       MainProg.qnAns[i][j]= newAns  
                    else:
                       MainProg.qnAns[i][j]=self.qnEntry[i][j].get() 
                    
            for i in range (Menubar.noOfQns):
                  MainProg.qnAns[i][self.noOfOptions]=self.option[i].get()
            htmlFilename = filedialog.asksaveasfilename(title="select", defaultextension="*.html",filetypes=[("Web","*.html")])
            f=open(htmlFilename,"w",encoding="utf-8")      
            f.write('<!DOCTYPE html><html><head><title>Multiple choice</title></head><style>.foms{background-color:'+customize.Fcolor+';width:500px;height:auto;padding:25px;border-radius:'+customize.Fborder_Radii+';}\n\
            .lettercolor{color:'+customize.Tcolor+';}\n\
            .score{ background-color:'+customize.Scolor+'; width:500px; height:50px; border-radius:'+customize.Sborder_Radii+';}</style><body>\n')
            for j in range(1,self.noOfQns+1):
               i=str(j)
               f.write('<h2>Question '+i+'</h2>\n\
               <form action="" method="post" class="foms">\n\
               <label class="lettercolor"><h3>'+MainProg.qnAns[j-1][0]+'</h3></label>\n')
               for m in range(self.noOfOptions-1):
                    f.write('<label id="'+i+self.Values[m]+'"  class="lettercolor"><input type="radio" name="q'+i+'" id="'+i+self.Values[m]+'" class="Radios" value="'+self.Values[m]+'" onclick="radSelect('+i+')"/>'+MainProg.qnAns[j-1][m+1]+'</label><br />\n')
               f.write('</form>\n')
            f.write('<h1><u>Your Score</u></h1><form class="score"><label style="position:relative;left:30px;top:5px"><h1 style="color:'+customize.STcolor+'" id="Mark" out of '+str(Marks)+'></h1></label></form>\n\
            </body> \n\
            <script>\n\
            var correctAns = new Array('+str(self.noOfQns-1)+');\n')
            for k in range(self.noOfQns):
               f.write('correctAns['+str(k)+']="'+MainProg.qnAns[k][self.noOfOptions]+'";\n')
            f.write('score=0;\n\
            function radSelect(val)\n\
            { \n\
            v=val-1;\n\
            var radios=document.getElementsByName("q"+val);\n\
            for(i=0;i<radios.length;i++)\n\
            {\n\
            if(radios[i].checked)\n\
            {\n\
            radioid=radios[i].id;\n\
		 radovalue=radios[i].value;\n\
		 }\n\
		radios[i].disabled=true;\n\
            }	\n\
            if(correctAns[v]==radovalue)\n\
            {\n\
            score=score+'+self.corrMarks+';\n\
		    document.getElementById(radioid).style.color="'+customize.Rcolor+'";\n\
            document.getElementById(radioid).style.fontWeight="bold";}\n\
            else\n\
            {\n\
            score=score-'+self.wrongMarks+';\n\
		    document.getElementById(radioid).style.color="'+customize.Wcolor+'";\n\
		    x=val+correctAns[v]\n\
		    document.getElementById(x).style.color="'+customize.Rcolor+'";\n\
		    document.getElementById(x).style.fontWeight="bold";\n\
            }\n\
            var n = score.toFixed(2);\n\
            Mark.innerHTML="Your score is "+n+" out of '+str(Marks)+'";  } \n\
            </script> \n\
            </html> \n')    
            f.close()
class fileImporter(Menubar):
    
    def __init__(self,win):
        super().__init__(win)
        
        self.win=win
        fileImporter.Temp=[[0 for j in range (Menubar.noOfOptions+1)] for i in range (Menubar.noOfQns)]
        f=open(self.openFilename,"r",encoding="utf-8")
        count = sum(1 for _ in f)
        f.close()
        f=open(Menubar.openFilename,"r",encoding="utf-8")      
        content=[f.readline() for i in range (count)]
        f.close()
        x=0
        for i in range (Menubar.noOfQns):
            for j in range (Menubar.noOfOptions+1):
              if j==5 :
                 fileImporter.Temp[i][j]=content[x].strip()
              else :
                fileImporter.Temp[i][j]=content[x].rstrip('\n')
              x=x+1
        for i in range(Menubar.noOfQns):
            for j in range(Menubar.noOfOptions):
                if j==0:
                    MainProg.qnEntry[i][j].delete("1.0", END)
                    MainProg.qnEntry[i][j].insert(END,fileImporter.Temp[i][j]) 
                else: 
                    MainProg.qnEntryVar[i][j].set(fileImporter.Temp[i][j])
        

class textWriter:
    def __init__(self,saveFilename):
        self.saveFilename=saveFilename
        f=open(saveFilename,"w")
        for i in range(Menubar.noOfQns):
                for j in range (Menubar.noOfOptions):
                    if j==0:
                       newAns=""
                       answers=MainProg.qnEntry[i][j].get("1.0",END)
                       
                       for m in answers:
                           if m!='\n':newAns+=m
                           else:newAns+=" "
                       f.write(newAns+'\n')
                    else:    
                       f.write(MainProg.qnEntry[i][j].get())
                       f.write("\n")
                try:
                   f.write(fileImporter.Temp[i][Menubar.noOfOptions])
                except:
                   f.write(MainProg.qnAns[i][Menubar.noOfOptions])
                f.write("\n")
        f.close()
                
class customize:
         
    def __init__(self,win):
        customize.wind=win
        customize.Fcolor='#344574'
        customize.Scolor='#400040'
        customize.Rcolor='#008000'
        customize.Wcolor='#FF0000'
        customize.Tcolor='#FFFFFF'
        customize.STcolor='#FFFFFF'
        self.swin = ScrolledWindow(self.wind, width=300,bg="Blue")
        self.swin.pack(side=RIGHT,anchor=N)
        self.Swind = self.swin.window
        Button(self.Swind,text="Select the Background color",width=30,command=self.formBackground).grid(row=0,column=0)
        self.CFormbg=Canvas(self.Swind,height=20,width=50,bg='#344574')
        
        Button(self.Swind,text="Select the Score background color",width=30,command=self.scoreBackground).grid(row=1,column=0)
        self.CScorebg=Canvas(self.Swind,height=20,width=50,bg='#400040')
        
        Button(self.Swind,text="Select the Right choice color",width=30,command=self.rightAnsColor).grid(row=2,column=0)
        self.CRightAnsColor=Canvas(self.Swind,height=20,width=50,bg='green')
        
        Button(self.Swind,text="Select the Wrong choice color",width=30,command=self.wrongAnsColor).grid(row=3,column=0)
        self.CWrongAnsColor=Canvas(self.Swind,height=20,width=50,bg='red')
        
        Button(self.Swind,text="Select the Text color",width=30,command=self.textColor).grid(row=4,column=0)
        self.CTextColor=Canvas(self.Swind,height=20,width=50,bg='white')

        Button(self.Swind,text="Select Score Text color",width=30,command=self.scoretextColor).grid(row=5,column=0)
        self.CSTextColor=Canvas(self.Swind,height=20,width=50,bg='white')

        self.FormC=Canvas(self.Swind,width=220,height=30,bg="brown")
        

        self.ScoreC=Canvas(self.Swind,width=220,height=30,bg="brown")
        

        self.FormCline=self.FormC.create_line(0,15,220,15,fill="black")
        self.FormCbar=self.FormC.create_polygon(23,0,33,0,33,30,23,30,fill="black")
        
        self.Scoreline=self.ScoreC.create_line(0,15,220,15,fill="black")
        self.ScoreCbar=self.ScoreC.create_polygon(210,0,220,0,220,30,210,30,fill="black")
        
        self.FormC.bind("<Button-1>",self.changeFormC)
        self.ScoreC.bind("<Button-1>",self.changeScoreC)
        self.F=StringVar()
        self.S=StringVar()
        self.formRadii=Entry(self.Swind,textvariable=self.F,width=6,bd=3)
        self.scoreRadii=Entry(self.Swind,textvariable=self.S,width=6,bd=3)

        self.F.set("23px")
        self.S.set("214px")

        self.formRadii.bind("<Return>",self.FEntry)
        self.scoreRadii.bind("<Return>",self.SEntry)
        
        customize.Fborder_Radii="10px"
        customize.Sborder_Radii="25px"

        self.m=RButton.CustButton(self.Swind,"Add more questions",150,50,10,"blue",command=self.clicki).CBbutton
        self.E=RButton.CustButton(self.Swind,"END THIS",150,50,10,"red",command=self.endAll).CBbutton
        self.CFormbg.grid(row=0,column=1)
        self.CScorebg.grid(row=1,column=1)
        self.CRightAnsColor.grid(row=2,column=1)
        self.CWrongAnsColor.grid(row=3,column=1)
        self.CTextColor.grid(row=4,column=1)
        self.CSTextColor.grid(row=5,column=1)
        self.FormC.grid(row=6,column=0)
        self.ScoreC.grid(row=7,column=0)
        self.formRadii.grid(row=6,column=1)
        self.scoreRadii.grid(row=7,column=1)
        self.m.grid(row=8,column=0)
        self.E.grid(row=9,column=0)
    def clicki(self,*arg):
        if hasattr(Menubar,'noOfQns'):
              w=addNew(masterwin,1)
        else:
             Menubar(masterwin).butcall()
           
           
    def endAll(self,*arg):
        
       MainProg.swin.pack_forget()
       
        
    def FEntry(self,*arg):
        try:
          x1=int(self.formRadii.get())
        except:
          x1=int(self.formRadii.get().rstrip("px"))
        if x1>0 and x1<220:
          x2=x1+10
          self.F.set(str(x1)+"px")
          self.FormC.delete(self.FormCbar)
          self.FormCbar=self.FormC.create_polygon(x1,0,x2,0,x2,30,x1,30,fill="black")
          customize.Fborder_Radii=str(x1*100//220)+"px"
         
    def SEntry(self,*arg):
        try:
           x1=int(self.scoreRadii.get())
        except:
           x1=int(self.scoreRadii.get().rstrip("px"))
        
        if x1>0 and x1<220:
          x2=x1+10
          self.S.set(str(x1)+"px")
          self.ScoreC.delete(self.ScoreCbar)
          self.ScoreCbar=self.ScoreC.create_polygon(x1,0,x2,0,x2,30,x1,30,fill="black")
          customize.Sborder_Radii=str(x1*25//220)+"px"
         
    def changeScoreC(self,event):
        x1=event.x
        if x1>0 and x1<220:
          x2=x1+10
          self.S.set(str(x1)+"px")
          self.ScoreC.delete(self.ScoreCbar)
          self.ScoreCbar=self.ScoreC.create_polygon(x1,0,x2,0,x2,30,x1,30,fill="black")
          customize.Sborder_Radii=str(x1*25//220)+"px"
          customize.A=x1*25//220
          
    def changeFormC(self,event):
        x1=event.x
        if x1>0 and x1<220:
          x2=x1+10
          self.F.set(str(x1)+"px")
          self.FormC.delete(self.FormCbar)
          self.FormCbar=self.FormC.create_polygon(x1,0,x2,0,x2,30,x1,30,fill="black")
          customize.Fborder_Radii=str(x1*100//220)+"px"
          customize.B=x1*100//220
         
    def formBackground(self):
        color=[(52, 69, 116),'#344574']
        color=askcolor((52, 69, 116))
        self.CFormbg.config(bg=color[1])
        if color[1]!=None:
            customize.Fcolor=color[1]
    def scoreBackground(self):
        color=[(64, 0, 64),'#400040']
        color=askcolor((64, 0, 64))
        self.CScorebg.config(bg=color[1])
        if color[1]!=None:
            customize.Scolor=color[1]
    def rightAnsColor(self):
        color=[(0, 255, 0),'#008000']
        color=askcolor((0, 255, 0))
        self.CRightAnsColor.config(bg=color[1])
        if color[1]!=None:
            customize.Rcolor=color[1]
    def wrongAnsColor(self):
        color=[(255, 0, 0),'#FF0000']
        color=askcolor((255, 0, 0))
        self.CWrongAnsColor.config(bg=color[1])
        if color[1]!=None:
            customize.Wcolor=color[1]
    def textColor(self):
        color=[(255, 255, 255),'#FFFFFF']
        color=askcolor((255, 255, 255))
        self.CTextColor.config(bg=color[1])
        if color[1]!=None:
           customize.Tcolor=color[1]
    def scoretextColor(self):
        color=[(255, 255, 255),'#FFFFFF']
        color=askcolor((255, 255, 255))
        self.CSTextColor.config(bg=color[1])
        if color[1]!=None:
           customize.STcolor=color[1]
class addNew:
    def __init__(self,win,no):
     self.no=no
     self.win=win
     self.newoption=[StringVar()]
     Menubar.noOfQns=Menubar.noOfQns+no
     newqnAns=[['' for i in range(Menubar.noOfOptions+1)]for j in range (self.no)]
     newQns=[[self.createEntry(a) for a in range (Menubar.noOfOptions)] for i in range (self.no)]
     newLabel=[[self.createLabel(a,i) for a in range (Menubar.noOfOptions)] for i in range (self.no)]
     newAns=[[self.createRadio(R,r) for r in range(Menubar.noOfOptions-1)] for R in range (self.no)]
     newEntryVar=[[StringVar() for i in range(Menubar.noOfOptions)] for j in range(self.no)]
     self.newoption[no-1].set(MainProg.Values[0])
     MainProg.qnAns.extend(newqnAns)
     MainProg.qnEntry.extend(newQns)
     MainProg.qnLabel.extend(newLabel)
     MainProg.correct.extend(newAns)
     MainProg.option.extend(self.newoption)
     MainProg.qnEntryVar.extend(newEntryVar)
     print(len(MainProg.qnEntry))
     for j in range (Menubar.noOfOptions):
            newLabel[self.no-1][j].grid(row=MainProg.k,column=0,sticky="E")
            newQns[self.no-1][j].grid(row=MainProg.k,column=1,sticky="W")
            if j!=0:
                newAns[self.no-1][j-1].grid(row=MainProg.k,column=3,sticky="W")
            MainProg.k=MainProg.k+1                
     MainProg.htmlbutton.grid(row=MainProg.k,column=1)
    def createEntry(self,a):
            if a==0:
              return Text(MainProg.Swind,width=50,height=3,bd=4)
            else:
              return Entry(MainProg.Swind,width=40)
    def createLabel(self,a,i):
            if a==0:
              lab=MainProg.labele[0]+str(Menubar.noOfQns)
              return Label(MainProg.Swind,text=lab)
            else:
              return Label(MainProg.Swind,text=MainProg.labele[a])
            
    def createRadio(self,R,r):
                
                return Radiobutton(MainProg.Swind,text="Correct Ans",variable=self.newoption[self.no-1],value=MainProg.Values[r])
            
                
   
           


        
x=Menubar(masterwin)
y=customize(masterwin)
masterwin.mainloop()

        
        
