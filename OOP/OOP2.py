class MarvelHero:
    tip = "Kahraman"
    heroList = []
    def __init__(self,adi,saglik,guc):   # *args   # **kwargs    # CONTRUCTOR
        self.adi = adi
        self.saglik = saglik
        self.guc = guc
        MarvelHero.heroList.append(adi)

    def DarbeAl(self,guc):
        self.saglik -= guc

    def Vurus(self):
        return self.guc

    def __del__(self):  #DECONSTRUCTOR
        print("Hastala Vista Baby")
    
class Deadpool(MarvelHero):
    def __init__(self):
        super().__init__("Deadpool",2000,200)

    def DarbeAl(self,guc):
        self.saglik -= guc//2

    
    


P1 = Deadpool()
P2 = MarvelHero("Hulk",2000,100)
print(P2.saglik)
P1.DarbeAl(P2.Vurus())
print(P1.saglik)