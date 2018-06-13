from tkinter import *

class TkController():
    # Geometry Parameter
    x = 0
    y = 0
    w = 0
    h = 0
    # Control parameter
    Labels = dict()
    ImageData = dict()
    Buttons = dict()
    TextBox =dict()
    commandList=dict()
    Window = None
    icon =""
    title = ""
    #Initialize TkController
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.title = ""
        self.Window = Tk()
        self.Window.title(self.title)
        self.Window.iconbitmap(self.icon)
        self.Window.geometry("%dx%d+%d+%d"%(self.w,self.h,self.x,self.y))
        self.Window.configure(bg='green')
        #self.Window.wm_attributes("-topmost",True)
        #self.Window.wm_attributes("-disabled", True)

        #self.Window.attributes("-alpha", 0.5)
        #self.Window.configure(bg='white')
        print("Ok")
    def AddImageData(self,name,data):
        self.ImageData[name]=PhotoImage(data=data)
    #Add Button to Dictionary
    def AddButton(self,name,x,y):
        self.Buttons[name]= Button(self.Window,text=name,bg='green',fg="yellow")
        self.Buttons[name].place(x=x,y=y)
        #print(self.Buttons)
    #Add Label to Dictionary
    def AddLabel(self,name,x,y):
        self.Labels[name] = Label(self.Window,bg='green',fg="yellow")
        self.Labels[name].place(x=x,y=y)
        #print(self.Labels)
    def AddTextBox(self,name,x,y):
        self.TextBox[name]=Entry(self.Window)
        self.TextBox[name].place(x=x,y=y)
        #print(self.TextBox)
    def GetText(self,name):
        str = self.TextBox[name].get()
        print(str)
        return str
    #Set Icon
    def SetIcon(self,icon):
        self.Window.iconbitmap(icon)
    #Configure Label TextSetting
    def ConfigureLabelText(self,name,str):
        self.Labels[name].configure(text=str)
        #print(self.Labels)
     # Configure Label ImageSet
    def ConfigureLabelsImage(self, name, img):
        self.Labels[name].configure(image=img)
    def GetString(self,name):
        for k in self.TextBox.keys():
            if(k == name):
                str = self.TextBox[name].get()
        print(str)
        return str
    def AddCommandList(self,cName,*args):
        self.commandList[cName]=args
        print(self.commandList)
    def ConfigureButtonCommnad(self,name,cName):
        self.Buttons[name].configure(command=self.commandList[cName]())
        print("Call")

            #print(self.Labels)
    # Set Window Size&Pos
    def SetWindowSize(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.Window.geometry("%dx%d+%d+%d" % (self.w, self.h, self.x, self.y))
        print(self.x,self.y,self.w,self.h)
    def SetWindowTitle(self,title):
        self.title = title
        self.Window.title(self.title)
        print(self.title)

    #Loop
    def Loop(self):
        self.Window.mainloop()
        print("LoopWindow")


