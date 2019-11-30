
def table(liste):
    for i in range(0,9,3):
        print("+-------"*3,"+",sep="")
        print("|       "*4)
        print("|   {}   |   {}   |   {}   |".format(liste[i],liste[i+1],liste[i+2]))
        print("|       "*4)
    print("+-------"*3,"+",sep="")


def Comp(liste):
    import random as rnd
    secim = rnd.choice(liste)
    while liste[secim-1] in ("O","X"):
        secim = rnd.choice(liste)
    else:
        liste[secim-1] = "X"
    table(liste)


def User(liste):
    user = int(input("Seçim Yap"))
    while liste[user-1] in ("O","X"):
        user = int(input("Yeni bir yer seçimi Yap"))
    else:
        liste[user-1] = "O"
    table(liste)
liste =[i for i in range(1,10)]

while True:
    table(liste)
    Comp(liste)
    User(liste)


0,4,8
2,4,6
for k in range(0,3):
    if liste[k] == liste[k+3] == liste[k+6]:
            break
    for i in range(k,9,3):
        if liste[i] == liste[i+1] == liste[i+2]:
            break
    


0,1,2
3,4,5
6,7,8

0,3,6
1,4,7
2,5,8

# sozluk = {i:str(i+1) for i in range(0,9)}
# def yansit(sozluk):
#     for i in range(0,9,3):
#         print("+-------"*3,"+",sep="")
#         print("|       "*4)
#         print("|   {}   |   {}   |   {}   |".format(sozluk[i],sozluk[i+1],sozluk[i+2]))
#         print("|       "*4)
#     print("+-------"*3,"+",sep="")



# yansit(sozluk)

