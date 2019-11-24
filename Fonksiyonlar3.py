#6.
# import time
# a =  time.perf_counter()
# def fibo(n):
#     if n < 2:
#         return 1
#     return fibo(n-2) + fibo(n-1)
# for i in range(0,100):
#     print("{}. {}".format(i+1,fibo(i)))


# def fibo(terimSay):
#     a = 1
#     b = 1
#     for i in range(0,terimSay):
#         c = a+b
#         print(i,c)
#         a,b = b,c
# fibo(100)
# print("a",a)

# a = 5 # global
# def fonk():
#     global a
#     a=3 #local
#     print(a)
# fonk()
# print(a)
""" Soru:Düzgün Sıralama
liste = ["Ali","Hakkı","Soner","Işınsu","Çiğdem","Berkcan","Efecan","Şirincan"]
liste.sort()
print(liste)
"""
# #1.
# fonk = lambda x : x*x
# print(fonk(2))
# #2.
# metin = "tyz"
# sozluk = {x:metin.index(x) for x in metin}
# print(sozluk)
# #3.
# liste = ["Ali","Hakkı","Soner","Işınsu","Çiğdem","Berkcan","Efecan","Şirincan"]
# listSonuc = sorted(liste,key=____)

# alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
# sozluk = {x:alfabe.index(x) for x in alfabe}
# print(sozluk)
# liste = ["Ali","Hakkı","Soner","Işınsu","Çiğdem","Berkcan","Efecan","Şirincan"]
# fonk = lambda x: sozluk.get(x[0].lower())
# print(fonk("Işınsu"))
# listSonuc = sorted(liste,key=lambda x: sozluk.get(x[0].lower()))
# print(listSonuc)