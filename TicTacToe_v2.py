
def table(liste):
    for i in range(0,9,3):
        print("+-------"*3,"+",sep="")
        print("|       "*4)
        print("|   {}   |   {}   |   {}   |".format(liste[i],liste[i+1],liste[i+2]))
        print("|       "*4)
    print("+-------"*3,"+",sep="")

def kimKazandi(k):
    if liste[k] == "X":
        print("Bilgisayar Kazandı")
    else:
        print("Kazandınız")

def Kontrol(liste):
    if (liste[0] == liste[4] == liste[8]):
        kimKazandi(0)
        return False
    if (liste[2] == liste[4] == liste[6]):
        kimKazandi(2)
        return False
    for k in range(0,3):
        if liste[k] == liste[k+3] == liste[k+6]:
            kimKazandi(k)
            return False
        if liste[k] == liste[k+1] == liste[k+2]:
            kimKazandi(k)
            return False
    return True
    
    
        
        
    

def Comp(liste):
    import random as rnd
    secim = rnd.randint(1,9)
    while str(liste[secim-1]) in ("O","X"):
        secim = rnd.randint(1,9)
    else:
        liste[secim-1] = "X"
 


def User(liste):
    user = int(input("Seçim Yap"))
    while str(liste[user-1]) in ("O","X"):
        user = int(input("Yeni bir yer seçimi Yap"))
    else:
        liste[user-1] = "O"


liste =[i for i in range(1,10)]
while True:
    table(liste)
    Comp(liste)
    if not Kontrol(liste):
        break
    User(liste)
    if not Kontrol(liste):
        break


    









# sozluk = {i:str(i+1) for i in range(0,9)}
# def yansit(sozluk):
#     for i in range(0,9,3):
#         print("+-------"*3,"+",sep="")
#         print("|       "*4)
#         print("|   {}   |   {}   |   {}   |".format(sozluk[i],sozluk[i+1],sozluk[i+2]))
#         print("|       "*4)
#     print("+-------"*3,"+",sep="")



# yansit(sozluk)

