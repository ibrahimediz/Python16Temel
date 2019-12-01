from random import choice
class MarvelHero:
    tip = "Kahraman"
    heroList = []
    def __init__(self,adi,saglik,guc,super=2):   # *args   # **kwargs    # CONTRUCTOR
        self.adi = adi
        self.saglik = saglik
        self.guc = guc
        self.super = super
        MarvelHero.heroList.append(adi)

    def DarbeAl(self,guc):
        self.saglik -= guc

    def Vurus(self):
        return self.guc

    def UltiVurus(self):
        print(self.adi,"SuperVuruş")
        return self.guc*self.super

    def haraketSec(self):
        return choice([self.DarbeAl,self.Savunma])

    def haraketSec2(self):
        return choice([self.UltiVurus,self.Vurus])

    def Savunma(self,guc):
        print(self.adi,"Savunma")
        self.saglik -= guc//2

    def Durum(self):
        return "Durum:Adı:{}-Sağlık:{}".format(self.adi,self.saglik)

    @classmethod
    def HeroList(cls):
        print(*cls.heroList,sep="\n")


    def __del__(self):  #DECONSTRUCTOR
        print(self.adi,"Hastala Vista Baby")
    
class Deadpool(MarvelHero):
    def __init__(self):
        super().__init__("Deadpool",2000,200,2)

    def DarbeAl(self,guc):
        self.saglik -= guc//2

class Hulk(MarvelHero):
    def __init__(self):
        super().__init__("Hulk",2000,100,3)

    def Vurus(self):
        return self.guc*2

class IronMan(MarvelHero):
    def __init__(self):
        super().__init__("IronMan",1000,100,1.5)

class KaraMurat(MarvelHero):
    def __init__(self):
        super().__init__("KaraMurat",3000,100,4)  
    


