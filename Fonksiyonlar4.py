# def dosyaAc(adres ="deneme.csv" ):
#     import os
#     if os.path.exists(adres):
#         dosya = open(adres,"r+",encoding="UTF-8")
#     else:
#         dosya = open(adres,"w+",encoding="UTF-8")
#     return dosya
liste = [i for i in range(1,10)]
liste[4] = 'X'
for i in range(0,9,3):
    print("+-------"*3,"+",sep="")
    print("|       "*4)
    print("|   {}   |   {}   |   {}   |".format(liste[i],liste[i+1],liste[i+2]))
    print("|       "*4)
print("+-------"*3,"+",sep="")
# print("|   {}   |   {}   |   {}   |".format(1,2,3))

# def ayikla(liste):
#     for i in range(0,len(liste)):
#         if liste[i] == 'X' or liste[i] == 'S':
#             liste.pop(i)
#     return liste
# import random

def rastgele(liste):
    import random
    secim = random.choice(liste)
    while secim == 'X' or secim == 'O':
        secim = random.choice(liste)
    return secim
print(rastgele(liste))
    

# liste = [1,'X',2]
# liste2 = ['X']
# liste3 = liste.remove('X')
# print(liste3)