# # class Araba:
# #     pass

# class Araba:
#     tip = "binek"
#     motor = 1.6
#     renk = "kırmızı"
#     def calistir():
#         print(motor,"çalıştı")

# benimAraba = Araba()


# class Araba:

#     def __init__(self):
#         self.motor = 1.6
#         self.adi = "Chawe"

################################################
class Sınıf:
    sinif_degiskeni = 2 #class attribute
    def __init__(self):
        self.ornek_nitelik = 1 #instance attribute
    def ornek_metod(self): #instance method
        return self.ornek_nitelik
    def __del__(self):
        pass

    @classmethod
    def sinif_metod(cls):
        return cls.sinif_degiskeni


ornek = Sınıf() # instance
ornek2 = Sınıf() #instance
##################################################



# 1. Encapsulation (Kapsülleme)
# 2. Polymorphism (Çokbiçimlilik)
# 3. Inharitance (Miraslama)
# 4. Abstraction (Soyutlama)

class Sekil:
    tip = "Çokgen" #Sınıf Nitelik
    __gizli = "çok gizli"
    def __init__(self,x=5,y=5):
        self.x = x
        self.y = y # Örnek Nitelik
        self.tanim = "Bu şekil henüz tanımlanmadı"
        self.sahip = "Henüz sahip yok"
        self.__degisken = ""
    
    def gizliGetter(self):
        return Sekil.__gizli

    def gizliSetter(self,param=""):
        if param.isdigit():
            Sekil.__gizli = param
        else:
            print("Değişmez")


    def alan(self):
        return self.x*self.y

    def Buyut(self,oran):
        self.x = self.x*oran
        self.y = self.y*oran

    def __del__(self):
        print("Hastala Vista")

   
    @classmethod
    def tipDegistir(cls,param):
        cls.tip = param



# kare = Sekil(20,20)

# # kare.Tanim("KARE")
# # print(kare.tanim)

# # dikdörtgen.Tanim("DİKDÖRTGEN")
# # print(dikdörtgen.tanim)

# kare = Sekil(20,20)
# print(kare.x)
# dikdörtgen = Sekil(20,30)

