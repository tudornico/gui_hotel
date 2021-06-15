from Zimmern import Zimmer
def reader_Zimmer(list_zimmer):
    f=open("Zimmer.txt","r")
    i=0
    while True:
        for j in f.readline():
            list_zimmer[i].set_nummer(j)
            list_zimmer[i].set_anzahl_gasten(j)
            list_zimmer[i].set_preis(j)
            list_zimmer[i].set_farbe(j)
            list_zimmer[i].set_meerblick(j)
        i+=1
        if not f:
            break
    return list_zimmer