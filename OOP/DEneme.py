from OOP.OOP5 import DosyaTool
defter2 = DosyaTool("Banka",ALANLAR=["Hesap","TUR","TUTAR","BANKA"])
logdosya = DosyaTool("BankaLog",ALANLAR=["Hesap","TUR","TUTAR","BANKA","İşlem","Zaman"])

class Banka():
    def ParaYatır(self):
        logdosya.kayitYaz()
        defter2.kayitGüncelle
