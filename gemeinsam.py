from Gaste import Gast
from reservierung import Reservierung
from Zimmern import Zimmer
import random
class Gemeinsam:
    def __init__(self):
        self.zimmern=list()
        self.gaste=list()
        self.reservierungs=list()

    def addguest(self,Vorname,Nachname):
        id=random.randint(100000000,999999999)
        self.gaste.append(Gast(Vorname,Nachname,id))
    def addzimmer(self,nummer,anzahl,preis,farbe,meerblick):
        self.zimmern.append(Zimmer(nummer,anzahl,preis,farbe,meerblick))#vezi ca idul ii lista

    def addreservierung(self,gasten,zeitraum,idliste):
        self.reservierungs.append(Reservierung(gasten,zeitraum,idliste))  # vezi ca idul ii lista
    def addreservierungself(self,zeitraum,nummer,ID):
        self.reservierungs.append(Reservierung(nummer,zeitraum,ID))#vezi ca id ii lista

        # scapa de i.id cu getID
    def deleteguest(self,nr):
        l = list()
        l.append(self.gaste[nr].ID)
        for i in self.zimmern:
           if l in i.ID:
               i.ID.clear()
        del self.gaste[nr]
    def deletezimmer(self, nr):
        del self.zimmern[nr]
    def printGuestList(self):
        for i in self.gaste:
            i.printself()
    def printZimmerList(self):
        for i in self.zimmern:
            i.printself()
    def printGuestDeletionList(self):
        for i in range(0,len(self.gaste)):
            print(i+1,' ',end='')
            self.gaste[i].printself()
    def printZimmerDeletionList(self):
        for i in range(0,len(self.zimmern)):
            print(i+1,' ',end='')
            self.zimmern[i].printself()
    def actualiseGuest(self,l,Nachname):
        self.gaste[l].change_name(Nachname)
    def actualiseZimmer(self,l,Preis):
        self.zimmern[l].adjust_preis(Preis)
    def addidtozimmer(self,zimmer,idliste):
            zimmer.ID.append(idliste)
    def gastenMitReservierung(self):
        for i in self.gaste:
            id=i.ID
            for j in self.reservierungs:
                if id in j.ID:
                    i.printself()
    def freeZimmer(self):
        for i in self.zimmern:
            if len(i.ID) == 0:
                i.printself()
    def mitMeerblick(self,preis,mitohne):
        for i in self.zimmern:
            if i.get_preis()<=preis and i.get_meerblick()==mitohne:
                i.printself()
#functie de afisat guest care au rezervari
#functie de aratat camerele libere
#functie de aratat camerele filtrate