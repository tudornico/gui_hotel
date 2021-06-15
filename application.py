from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image
from Menu_Gast import *
from functionsforaplication import *
class Menu:
    def __init__(self, master):
        self.master = master
        self.master.title("Anfang Menu")
        sh=root.winfo_screenheight()
        sw=root.winfo_screenwidth()
        self.master.geometry("%dx%d"%(1.5*sh,1.7*sw))
        self.master.configure(bg='gray')
        """
        self.canvas=Canvas(root,width=sw,height=sh/2)
        self.canvas.pack()
        self.img=ImageTk.PhotoImage(Image.open("TheHotel.jpg"))
        self.canvas.create_image(20,20,anchor=NW,image=self.img)
        """
        self.label = Label(master, text="Menu")
        self.label.place()
        #open=Menu_Gast.Open(self)
        self.Gast_button = Button(master, text="Menu Gast")
        self.Gast_button.place(relx=0.2,rely=0.5,anchor="center")

        self.Zimmer_button=Button(master,text="Menu Zimmer",command=self.addguest())
        self.Zimmer_button.place(relx=0.5,rely=0.5,anchor="center")

        self.Gemeinsam_button=Button(master,text="Menu Gemeinsam")
        self.Gemeinsam_button.place(relx=0.8,rely=0.5,anchor="center")
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.place()


    # we define the MenuGast window
    def MenuGast(self):
        self.newGast=Toplevel()
        """"
        self.newGast.geometry=("%dx%d"%(sh,sw))
        self.Label(newWindow,text="").pack()
        self.label=Label(master,text="")
        self.label.pack(pady=10)
        """

    #def open_menugast(self):
        

root = Tk()
my_gui = Menu(root)
root.mainloop()