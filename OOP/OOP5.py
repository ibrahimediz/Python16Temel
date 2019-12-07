##################################################     1 ##
# import os
# if os.path.exists("deneme.csv"):
#     dosya = open("deneme.csv","r+",encoding="UTF-8")
# else:
#     dosya = open("deneme.csv","w+",encoding="UTF-8")
# anahtar = 1    
# liste =  dosya.readlines()
# while anahtar == 1:
#     islem = input("islem ")
#     if islem == "1":
#         adi = input("Adınız:")
#         kayit = "{};{};{}\n".format(adi,"aa","123")
#         liste.append(kayit)
#     elif islem == "2":
#         siraNum = 1
#         for item in liste:
#             print(siraNum,"-",item)
#             siraNum += 1
#     elif islem == "3":
#         siraNum = 1
#         for item in liste:
#             print(siraNum,"-",item)
#             siraNum += 1
#         sira = int(input("Düzenlemek istediğin kayıt:"))
#         adi = input("Adınız:")
#         kayit = "{};{};{}\n".format(adi,"aa","123")
#         liste[sira-1] = kayit
#     elif islem == "5":
#         anahtar =0
# else:
#     dosya.seek(0)
#     dosya.truncate()
#     dosya.writelines(liste)
#     dosya.close()
##################################################     2 ##

# def dosyaAc(adres = "deneme.csv"):
#     import os
#     if os.path.exists(adres):
#         dosya = open(adres,"r+",encoding="UTF-8")
#     else:
#         dosya = open(adres,"w+",encoding="UTF-8")
#     return dosya

# def KayitEkle(adres,**kwargs):
#     dosya = dosyaAc(adres)
#     liste = dosya.readlines()

#     kayit = ""
#     for key,value in kwargs.items():
#         if key="ALANLAR":
#             for item in value:
#                 kayit +="{};".format(input(item +"giriniz"))
#     kayit = kayit.rstrip(";")+"\n"

#     liste.append(kayit)

#     dosya.seek(0)
#     dosya.truncate()
#     dosya.writelines(liste)
#     dosya.close()



# def KayitDuzenle(adres,**kwargs):
#     dosya = dosyaAc(adres)
#     liste = dosya.readlines()

#     siraNum = 1
#     for item in liste:
#         print(siraNum,"-",item)
#         siraNum += 1
#     sira = int(input("Düzenlemek istediğin kayıt:"))

#     kayit = ""
#     for key,value in kwargs.items():
#         if key="ALANLAR":
#             for item in value:
#                 kayit +="{};".format(input(item +"giriniz"))
#     kayit = kayit.rstrip(";")+"\n"

#     liste[sira-1] = kayit

#     dosya.seek(0)
#     dosya.truncate()
#     dosya.writelines(liste)
#     dosya.close()

# def KayitSilme(adres):
#     dosya = dosyaAc(adres)
#     liste = dosya.readlines()

#     siraNum = 1
#     for item in liste:
#         print(siraNum,"-",item)
#         siraNum += 1
#     sira = int(input("Silmek istediğin kayıt:"))

#     liste.pop(sira-1)

#     dosya.seek(0)
#     dosya.truncate()
#     dosya.writelines(liste)
#     dosya.close()

# def KayitListele(adres):
#     dosya = dosyaAc(adres)
#     liste = dosya.readlines()

#     siraNum = 1
#     for item in liste:
#         print(siraNum,"-",item)
#         siraNum += 1
    
#     dosya.seek(0)
#     dosya.truncate()
#     dosya.writelines(liste)
#     dosya.close()


##################################################     3 OOP ##
import os
class DosyaTool:
    __dosyaUzanti = ".csv"
    
    def __init__(self,adi,**kwargs):
        self.adi = adi
        self.alanlar = None
        for key,value in kwargs.items():
            if key=="ALANLAR":
                self.alanlar = value
        self.adres = os.getcwd() + os.sep + self.adi + DosyaTool.__dosyaUzanti
        self.kayitlar = None
        self.dosya = None
        self.dosyaAc()
    

    def dosyaAc(self):
        if os.path.exists(self.adres):
            dosya = open(self.adres,"r+",encoding="UTF-8")
        else:
            dosya = open(self.adres,"w+",encoding="UTF-8")
        self.dosya = dosya
        self.kayitlar =  self.dosya.readlines()


    def KayitEkle(self):
        kayit = self.kayitAl()
        self.kayitlar.append(kayit)
       

    def kayitAl(self):
        kayit = ""
        for item in self.alanlar:
            kayit +="{};".format(input(item +"giriniz"))
        kayit = kayit.rstrip(";")+"\n"
        return kayit

    def __del__(self):
        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writelines(self.kayitlar)
        self.dosya.close()

    def KayitListele(self):
        siraNum = 1
        for item in self.kayitlar:
            print(siraNum,"-",item)
            siraNum += 1
        

    def KayitDuzenle(self):
        self.KayitListele()
        sira = int(input("Düzenlemek istediğin kayıt:"))
        kayit = self.kayitAl()
        self.kayitlar[sira-1] = kayit

    def KayitSilme(self):
        self.KayitListele()
        sira = int(input("Düzenlemek istediğin kayıt:"))
        self.kayitlar.pop(sira-1)


defter = DosyaTool("teldefter",ALANLAR=["ADI","SOYADI","TEL"])
defter2 = DosyaTool("Banka",ALANLAR=["Hesap","TUR","TUTAR","BANKA"])
