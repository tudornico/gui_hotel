class Zimmer:
    def __init__(self,nummer,anzahl_gasten,preis,farbe,meerblick,Zahl=None):
        self.nummer=nummer
        self.preis=preis
        self.farbe=farbe
        self.meerblick=meerblick
        self.anzahl_gasten=anzahl_gasten
        self.ID=list()
        self.Zahl=Zahl

    def get_nummer(self):
        return self.nummer

    def get_anzhal(self):
        return self.gasten

    def get_preis(self):
        return self.preis

    def get_farbe(self):
        return self.farbe

    def get_meerblick(self):
        return self.meerblick

    def set_preis(self,neu_preis):
        self.preis=neu_preis

    def set_nummer(self,neu_nummer):
        self.nummer=neu_nummer

    def set_farbe(self,neu_farbe):
        self.farbe=neu_farbe

    def set_meerblick(self,neu_meerblick):
        self.meerblick=neu_meerblick

    def set_anzahl_gasten(self,neu_anzahl_gasten):
        self.anzahl_gasten=neu_anzahl_gasten

    def __str__(self):

        return  (self.Nummer,self.anzahl_gasten,self.preis,self.farbe,self.meerblick)
    def __repr__(self):
        print("Nummer ist : ", self.Nummer, '\n',
              "Anzahl von moglichen gasten ist : ", self.anzahl_gasten, '\n',
              "farbe ist : ", self.farbe, '\n')
        if self.meerblick == 0:
            print("Hat meerblick")
        else:
            print("Hat kein meerblick")
    def printself(self):
        print("Number=",self.nummer,"Guest number=",self.anzahl_gasten,"Price=",self.preis,"Colour=",self.farbe,end='')
        if int(self.meerblick)==1:
            print(" Has seaview")
        else:
            print(" Has no seaview")