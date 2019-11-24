# var2 = input("Cümle gir")
# def palindromCheck(text):
#     return text.lower().replace(" ","")[::-1] == text.lower().replace(" ","")
# print(palindromCheck(var2))
# normal parametre tanımlama
def fonk(a,b):
    pass

#parametre belli ne kadar değer geleceği belli değilse
def fonk2(*args):
    pass

#parametre adı  belli değilse ve ne kadar değer geleceği belli değilse
def fonk3(**kwargs):
    pass
"""
Python ile kullanıcının virgül ile ayırarak 
girdiği sayıları toplayan ve sonucu ekranda gösteren programı yazınız.
"""
# vars = input("Sayıları giriniz")
# sonuc = 0
# liste  = list(vars.replace(",","")) # 1
# print(liste)
# liste2 = vars.split(",") # 2
# print(liste2)
# for item in liste:
#     sonuc += int(item)
# print(sonuc)
#--------------------------
# var3 = vars.replace(",","*")
# print(eval(var3)) #evaluate
# exec("""a=5
# print(a)""") #execution
#--------------------------
# def topluTopla(*args):
#     sonuc = 0
#     for item in args:
#         sonuc += int(item)
#     return sonuc

# vars = input("Sayıları giriniz")
# liste2 = vars.split(",") # 2
# print(topluTopla(1,2,3,4,5,6))

def fonk4(**kwargs):
    result = []
    print(kwargs.items())
    for key,value in kwargs.items():
        if key.lower()=="topla":
            result.append(value[0]+value[1])
        elif key.lower() == "cikar":
            result.append(value[0]-value[1])
    return result,"Yaptım ama kod çok saçma"


print(fonk4(Topla=[1,2],cikar=[2,3]))