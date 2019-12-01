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
class Sınıf():
    sinif_degiskeni = 2 #class attribute
    def __init__(self):
        self.ornek_nitelik = 1 #instance attribute
    def ornek_metod(self): #instance method
        pass

ornek = Sınıf() # instance
ornek2 = Sınıf() #instance
##################################################


# 1. Encapsulation (Kapsülleme)
# 2. Polymorphism (Çokbiçimlilik)
# 3. Inharitance (Miraslama)
# 4. Abstraction (Soyutlama)

class Sekil:
    tip = "Çokgen" #Sınıf Nitelik
    def __init__(self,x,y):
        self.x = x
        self.y = y # Örnek Nitelik
        self.tanim = "Bu şekil henüz tanımlanmadı"
        self.sahip = "Henüz sahip yok"
    
    def alan(self):
        return self.x*self.y

    def Buyut(self,oran):
        self.x = self.x*oran
        self.y = self.y*oran

    def Tanim(self,text):
        self.tanim = text

    @classmethod
    def tipDegistir(cls,param):
        cls.tip = param


kare = Sekil(20,20)
# kare.Tanim("KARE")
# print(kare.tanim)
dikdörtgen = Sekil(20,30)
# dikdörtgen.Tanim("DİKDÖRTGEN")
# print(dikdörtgen.tanim)
print("kare.x",kare.x)
print("dikdörtgen.x",dikdörtgen.x)
kare.x = 30
print("kare.x",kare.x)
print("dikdörtgen.x",dikdörtgen.x)


print("kare.tip",kare.tip)
print("dikdörtgen.tip",dikdörtgen.tip)
kare.tipDegistir("Herhangi")
dikdörtgen.tipDegistir("deneme")
Sekil.tipDegistir("Herhangi 2")
print("kare.tip",kare.tip)
print("dikdörtgen.tip",dikdörtgen.tip)