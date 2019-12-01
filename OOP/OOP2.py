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

    def Durum(self):
        return "Durum:Adı:{}-Sağlık:{}".format(self.adi,self.saglik)

    @classmethod
    def HeroList(cls):
        print(*cls.heroList,sep="\n")


    def __del__(self):  #DECONSTRUCTOR
        print(self.adi,"Hastala Vista Baby")
    
class Deadpool(MarvelHero):
    def __init__(self):
        super().__init__("Deadpool",2000,200)

    def DarbeAl(self,guc):
        self.saglik -= guc//2

class Hulk(MarvelHero):
    def __init__(self):
        super().__init__("Hulk",2000,100)

    def Vurus(self):
        return self.guc*2

class IronMan(MarvelHero):
    def __init__(self):
        super().__init__("IronMan",1000,100)

class KaraMurat(MarvelHero):
    def __init__(self):
        super().__init__("KaraMurat",3000,100)  
    


