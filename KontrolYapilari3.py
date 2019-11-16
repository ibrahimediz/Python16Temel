# for i in range(0,5):
#     print(i)


# for i in range(0,50,2):
#     print(i)

# for i in range(0,50):
#     if i % 2 == 0:
#         print(i)

# sayi = 374
# adim=0
# print(sayi%10*10**adim)
# sayi //= 10
# adim = 1
# print(sayi%10*10**adim)
# sayi //= 10
# adim = 2
# print(sayi%10*10**adim)
# sayi //= 10

sayi = input("Sayıyı Giriniz")
basamak = len(sayi)
sayi = int(sayi)
for i in range(0,basamak):
    print(sayi%10*10**i)
    sayi //= 10

# sayi = int(input("Sayıyı Giriniz"))
# sonuc = 1
# for faruk in range(0,sayi):
#     sonuc *= faruk + 1
# print("sonuc",sonuc)


# sayi = int(input("Sayıyı Giriniz"))
# sonuc = 1
# for faruk in range(1,sayi+1):
#     sonuc *= faruk 
# print("sonuc",sonuc)

# liste = ["Hava","Kapalı","Ama","Akalım","Arabaya"]
# for item in liste:
#     print(item)

# metin = "Tripanazomigambiyetsiz"
# for item in metin:
#     print(item)

# metin = "BEŞİKTAŞ"
# for i in range(0,len(metin)):
#     print(metin[i])
    

sozluk =  {"1":"Bir","2":"İki","3":"üç"}

# for item in sozluk.keys():
#     print(item)
# print(sozluk.items())

for key,value in sozluk.items():
    print(key,value)

# import random
# kolon = int(input("Kaç Kolon Oynamak İstersin"))
# for i in range(0,kolon):
#     liste = []
#     for i in range(0,6):
#         sayi = random.randint(1,49)
#         while sayi in liste:
#             sayi = random.randint(1,49)
#         liste.append(sayi)
#     liste.sort()
#     print(liste)

# sayi = input("Sayıyı Giriniz")
# sayi = int(sayi)
# adim = 0
# while sayi > 0:
#     print(sayi%10*10**adim)
#     sayi //= 10
#     adim +=1
