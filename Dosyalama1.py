# dosya = open("deneme.csv")
# print("1",dosya.read())
# print(dosya.tell())
# print("2",dosya.readline())
# print("3",dosya.readlines())
# print("4",dosya.read())
# dosya.seek(0)
# print(dosya.read(5))
# print(dosya.tell())
# dosya.read()
# dosya.write("write ile yazıldı\n")

import os
if os.path.exists("deneme.csv"):
    dosya = open("deneme.csv","r+",encoding="UTF-8")
else:
    dosya = open("deneme.csv","w+",encoding="UTF-8")
anahtar = 1    
liste =  dosya.readlines()
while anahtar == 1:
    islem = input("islem ")
    if islem == "1":
        adi = input("Adınız:")
        kayit = "{};{};{}\n".format(adi,"aa","123")
        liste.append(kayit)
    elif islem == "2":
        siraNum = 1
        for item in liste:
            print(siraNum,"-",item)
            siraNum += 1
    elif islem == "3":
        siraNum = 1
        for item in liste:
            print(siraNum,"-",item)
            siraNum += 1
        sira = int(input("Düzenlemek istediğin kayıt:"))
        adi = input("Adınız:")
        kayit = "{};{};{}\n".format(adi,"aa","123")
        liste[sira-1] = kayit
    elif islem == "4":
        anahtar =0
else:
    dosya.seek(0)
    dosya.truncate()
    dosya.writelines(liste)
    dosya.close()




