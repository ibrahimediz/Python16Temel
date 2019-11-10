# buyuksayi = int(input("Kontrol edilecek sayıyı giriniz"))
# adim = 0
# for sayi in range(2,buyuksayi):

#     for i in range(2,sayi):
#         if sayi % i == 0:
#             # print("sayı asal değildir")
#             break
#     else:
#         adim += 1
#         if adim == 10001:
#             print(sayi)
#             break


def is_prime(n):
    if n == 2 or n == 3: 
        return True
    if n < 2 or n%2 == 0: 
        return False
    if n < 9: 
        return True
    if n%3 == 0: 
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        # print('\t',f)
        if n%f == 0: 
            return False
        if n%(f+2) == 0: 
            return False
        f +=6
    return True
# adim = 0
# for i in range(0,200000):
#     if is_prime(i):
#         adim += 1
#         if adim == 10001:
#             print(i)
#             break

# for sayi in  range(1000000,10,-1):
#     sayi = str(sayi)
#     basamak = len(sayi)
#     sonuc =0
#     for i in range(0,len(sayi)):
#         sonuc += int(sayi[i]) ** basamak
#     if int(sayi) == sonuc:
#         print(sayi,"armstrong sayısı")


# for i in  range(1000000,10,-1):
#     giris = str(i)
#     basamak = len(giris)
#     sayi = int(giris)
#     sonuc = 0
#     while sayi > 0:
#         sonuc += ((sayi%10)**basamak)
#         sayi //= 10
#     if int(giris) == sonuc:
#         print(sonuc,"Sayı Armstrong Sayısıdır")

# import random
# while True:
#     sayi = random.randint(1,100)
#     hak = 5
#     while hak>0:
#         tahmin = input("Tahmininizi Giriniz")
#         if tahmin:
#             tahmin = int(tahmin)
#             hak -= 1
#             if tahmin > sayi:
#                 print("Aşağı Kalan Hak {}".format(hak))
#             elif tahmin < sayi:
#                 print("Yukarı Kalan Hak {}".format(hak))
#             elif tahmin == sayi:
#                 print("Tebrikler")
#                 break
#     else:
#         print("Oyun Bitti Tahmin ettiğim sayı:{}".format(sayi))
#     secim = input("Tekrar Oyanamak İster misiniz? (e/h)")
#     if secim.lower() != "e":
#         break
# print("İyi Günler Dileriz")


liste = [i for i in range(0,5)]
sozluk = {i:is_prime(i)  for i in range(1,2000)}
print(liste)
print(sozluk)