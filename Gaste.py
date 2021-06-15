from gasten_functions import *

class  Gast:
    def __init__(self, Vorname, Nachname,ID,nummer=None):
        if ID == None:
            self.Vorname=Nachname
            self.Vorname=Vorname
            self.nummer=nummer
        else:
            self.Vorname=Vorname
            self.Nachname=Nachname
            self.ID=ID
            self.nummer=nummer
    def change_name(self, Nachname):
        self.Nachname=Nachname
    def get_Vorname(self):
        return self.Vorname
    def set_Vorname(self,neu_Vorname):
        self.Vorname=neu_Vorname
        return self.Vorname


    def get_Nachname(self):
        return self.Nachname


    def set_Nachname(self,neu_Nachname):
        return self.Nachname


    def printself(self):
        if len(self.Vorname)>0:
            print(self.Vorname,self.Nachname)

    def getID(self):
        return int(self.ID)
    def setID(self,neu_ID):
        self.ID=neu_ID
        return self.ID
