# import random
# liste = []
# for i in range(0,int(input("Satır Gir"))):
#     kayit="{};{};{}\n".format(random.randint(0,100),random.randint(0,100),random.randint(0,100))
#     liste.append(kayit)
# dosya = open("deneme22.csv","w+",encoding="UTF-8")
# dosya.writelines(liste)
# dosya.close()

# mesaj = input("mesajı giriniz").upper()
# sifre = ""
# for kar in mesaj:
#     sayi = ord(kar) + 1
#     if ord('Z') < sayi:
#         sayi= ord('A')
#     sifre += chr(sayi)
# print(sifre)

# desifre = ""
# for kar in sifre:
#     sayi = ord(kar) - 1
#     if ord('A') > sayi:
#         sayi = ord('Z')
#     desifre += chr(sayi)
# print(desifre)

iban = "TR47 0000 1001 0000 0350 9300 01".replace(" ","")
# iban[2] = "5" yapamazsın çünkü immutable variable
iban = iban[4:] + iban[0:4]
"0000100100000350930001TR47"
iban2 = "" 
for kar in iban:
    if not kar.isdigit():
        iban2 += str(ord(kar) - 55)
    else:
        iban2 +=kar
# print(iban2)
# ilk = str(int(iban2[0:9])%97)
# ikinci = ilk + iban2[9:]
# print(int(ikinci[:11])%97)
# # print(int(iban2[0:9])%97)
# # print(int( iban2[9:]))
a = iban2[:9]
b = str(int(a)%97) + iban2[9:18]
c = str(int(b)%97) + iban2[18:]
sonuc = int(c)%97
if sonuc == 1:
    print("IBAN DOĞRU")
else:
    print("YANLIS")
