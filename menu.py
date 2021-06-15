from tkinter import *
import switch
from gemeinsam import Gemeinsam
from reader_Gast import *
from reader_Zimmer import *
def gastHinfugen(object):
    l=input("Please give the First Name and Last Name").split()
    object.addguest(l[0], l[1])
def gastAnzeigen(object):
    object.printGuestList()
def gastLoschung(object):
    object.printGuestDeletionList()
    l=int(input("Who do you want to delete?"))
    object.deleteguest(l-1)
def freezimmern(object):
    object.freeZimmer()
def zimmerLoschung(object):
    object.printZimmerDeletionList()
    l = int(input("Who do you want to delete?"))
    object.deletezimmer(l - 1)
def freereservierung(object):
    object.gastenMitReservierung()
def gastAktualisieren(object):
    object.printGuestDeletionList()
    l=int(input("Who do you want to actualize?"))
    Nachname=input("New name?")
    object.actualiseGuest(l-1,Nachname)
def zimmerHinfugen(object):
    l=input("Please give the number, the maximum number of guests, the price, the colour and whether it has seaview or not: ").split()
    object.addzimmer(l[0],l[1],l[2],l[3],l[4])
def zimmerAnzeigen(object):
    object.printZimmerList()
def zimmerAktualisieren(object):
    object.printZimmerDeletionList()
    l = int(input("Which do you want to actualize?"))
    Preis = input("New price?")
    object.actualiseZimmer(l -1,Preis)
def reservierungMachen(object):
    i = int(input("How many guests?"))
    zeitraum=input("How many days?")
    object.printGuestDeletionList()
    l = input("Dami nr lor").split()
    for k in range(0, len(l)):
        l[k] = int(l[k])
    idliste=list()
    for i in l:
        idliste.append(object.gaste[i-1].ID)
    zimmernummer=-1
    while zimmernummer==-1:
        for k in range(len(object.zimmern)):
            if object.zimmern[k].anzahl_gasten == i and object.zimmern[k].ID == None:
                zimmernummer = k
                break
        i=i+1
        if i>10:
            break
    object.addreservierung(i,zeitraum,idliste)
    object.addidtozimmer(object.zimmern[zimmernummer],idliste)
def filterzimmern(object,preis,meerblick):
    if meerblick == 1 :
        object.mitMeerblick(preis,meerblick)
# am facut listele de gast si zimmer initiale am putea adauga iduri pe cand le citim !!!!!!!
list_gast=list()
list_gast=reader_Gaste(list_gast)
list_zimmer=list()
list_zimmer=reader_Zimmer(list_zimmer)
gastHinfugen(list_gast)
zimmerHinfugen(list_zimmer)
def main():
    object = Gemeinsam()

    while True:
        print("write 'Menu Gast' for the guest menu\n",
              "wirte 'Menu Zimmern' for the guest menu\n", \
              "write 'Menu Gemeinsam' for the togheter menu\n")
        a = str(input("we choose menu: "))
        with switch.Switch(a) as case:
            if case("Menu Gast"):
                print("write 'add guest' to add a new guest to the list \n",
                      "write 'neu nachname' to change the last name of a guest\n",
                      "write 'remove guest' to remove one guest from the list\n",
                      "write 'show guests' to print all guests\n")
                while True:
                    b = str(input("task is: "))
                    with switch.Switch(b) as case:

                        if case("add guest"):
                            gastHinfugen(object)
                        if case("neu nachname"):
                            gastAktualisieren(object)
                        if case("remove guest"):
                            gastLoschung(object)
                        if case("show guests"):
                            gastAnzeigen(object)
                        if case("enough") : break

            if case("Menu Zimmern"):
                print("write 'add zimmer' to add a new room to the list\n",
                      "write 'neu pries' to change the price of a room\n",
                      "write 'remove zimmer' to remove a room from the list\n",
                      "write 'show zimmer' to print all rooms\n")
                while True:
                    b = str(input("task is: "))
                    with switch.Switch(b) as case:
                        if case("add zimmer"):
                            zimmerHinfugen(object)
                        if case("neu preis"):
                            zimmerAktualisieren(object)
                        if case("remove zimmer"):
                            zimmerLoschung(object)
                        if case("show zimmer"):
                            zimmerAnzeigen(object)
                        if case("enough") : break
        if case("Menu Gemeinsam"):
            print("write 'mach reservierung' to make a reservation\n",
                  "write 'Gasten mir reservierung' to see the guests with reservations\n",
                  "write 'filter zimmer' to see the rooms cheaper than x and if they have sea sight\n",
                  "write 'frei zimmer' to see all the free rooms\n")
            while True:
                b = str(input("task is :"))
                with switch.Switch(b) as case:
                    if case("mach reservierung"):
                        reservierungMachen(object)
                    if case("Gasten mit reservierung"):
                        freereservierung(object)
                    if case("filter zimmer"):
                        preis=int(input("Price lower than:"))
                        meer=int(input("Write 1 if you want sea view or 0 for no sea view"))
                        filterzimmern(object,preis,meer)
                    if case("frei zimmer"):
                        freezimmern(object)
                    if case("enough"): break
        if case.default: break

main()