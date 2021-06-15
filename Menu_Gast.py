from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image
from Gaste import Gast


class myWindow():
    def __init__(self,master,title,background,label):
        #Frame.__init__(self,master,title,background)
        self.master=master
        self.title=title
        self.background=background


        #sh=root.winfo_screenwidht()
        #sw=root.winfo_screenmmwidht()
        #self.master.geometry("%dx%d"%(sh,sw))
        #self.master.configure(bg="blue")
        #self.label=Label(master,text="Menu Gast")
        #self.label.place()
        # buttons for the function addguest deleteguest show guests change last name\
    def btn(self,text, command, relx, rely,height, width):
        self.button = Button(master, text=text, command=command)
        self.button.place(relx=0.5, rely=0.7, anchor="center")

        self.MenuGast=Menu_Gast()
        self.btn=Button(self,text="Open",command=self.MenuGast.win).place()
    def ADDguest(self):
        #self.addgeust_button=Button(master,text="Fuge ein Gast hin",command=Gast.addguest())
        #self.addgeust_button.place(relx=0.3,rely=0.5)
        print("epic time")
    
    #def Open(self):
    def editcanvas(self,x,y,image,anchor):
        self.canvas.create_image(x, y, image=self.image, anchor=anchor)
        self.canvas.place(relx=x, rely=y, anchor=anchor)




root = Tk()
app = Menu_Gast(root)
root.mainloop()
