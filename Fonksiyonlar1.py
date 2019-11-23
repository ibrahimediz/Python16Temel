# def fonk():
#     print("Merhaba")
# fonk()
# def fonk(isim="Kilimcinin Köroğlu"):
#     print("Merhaba",isim)
# fonk()

# def fonk(a,b=3): # b=3 sonrasında gelecek tüm parametreler için varsayılan değer tanımı yapılmalıdır
#     print(a+b)
# fonk(b=3,a=2)


def fonk(a,b): 
    """ => None iki sayıyı toplar 
    a interger olmalı
    b integer olmalı b = 4"""
    print(a+b)
fonk(2,3)
print(type(fonk(2,3)))


def topla(a,b):
    return a+b
def cikar(a,b):
    return a-b
def bolme(a,b):
    return a/b
def carpma(a,b):
    return a*b
def calistir(fonk,a,b):
    return fonk(a,b)
print(calistir(topla,2,3))
print(calistir(cikar,2,3))
print(calistir(bolme,2,3))
print(calistir(carpma,2,3))
# sonuc = topla(2,2) + 5 * 2
# print(type(topla(2,3)))

