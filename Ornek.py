# Hesap makinesi v.1.0
menu = """
Merhaba, hesap makinesine V.1.0'a hoş geldiniz
Toplama için [1]'i
Çıkarma için [2]'yi
Çarpma için  [3]'ü
Bölme için   [4]'ü
Üs alma için [5]'i
Çıkmak için [6]'yı
"""

while True:
    print(menu)
    islem=input("İşlem Seçiniz :")
    if islem == "6":
        break
    if islem not in ["1","2","3","4","5"]:
        print("İşlem Seçmediniz")
        continue
    num1=float(input("1. Rakam giriniz: "))
    num2=float(input("2. Rakam giriniz: "))
    sonuc = 0
    if islem=="1":
        print("Toplama")
        sonuc=(num1+num2)
    elif islem=="2":
        print("Çıkarma")
        sonuc=(num1-num2)
    elif islem=="3":
        print("Çarpma")
        sonuc=(num1*num2)    
    elif islem=="4":
        print("Bölme")
        sonuc=(num1/num2)
    elif islem=="5":
        print("Üssü Alma")
        sonuc=(num1**num2)
    else:
        print("Menude yok")
    print("İşlem Sonucu:",sonuc)


# sonuc1=(num1+num2)
# sonuc2=(num1-num2)
# sonuc3=(num1*num2)
# sonuc4=(num1/num2)
# sonuc5=(num1**num2) 
#  bu kod sebebiyle çarpma işlemi çoklu basamak girildiğinde hata veriyor

# if islem=="1":
#     print("Sonuç: ",[sonuc1])
# elif islem=="2":
#     print("Sonuç: ",[sonuc2])
# elif islem=="3":
#     print("Sonuç: ",[sonuc3])
# elif islem=="4":
#     print("Sonuç: ",[sonuc4])
# elif islem=="5":
#     print("Sonuç: ",[sonuc5])
# else:
#     print("Hatalı Giriş")