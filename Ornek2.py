"""
9,852,852

Dokuz Milyon 
Sekiz Yüz Elli Bin 
Sekiz Yüz Elli İki

"""

birler = {
"0":" ",
"1":" Bir",
"2":" İki",
"3":" Üç",
"4":" Dört",
"5":" Beş",
"6":" Altı",
"7":" Yedi",
"8":" Sekiz",
"9":" Dokuz"}

onlar = {
"0":" ",
"1":" On",
"2":" Yirmi",
"3":" Otuz",
"4":" Kırk",
"5":" Elli",
"6":" Altmış",
"7":" Yetmiş",
"8":" Seksen",
"9":" Doksan"}

basamak = {
    0:" ",
    1:" Bin",
    2:" Milyon",
    3:" Milyar",
    4:" Trilyon",
    5:" Katrilyon",
}

while True:
    sayi = input("Sayıyı Giriniz").replace(",","").replace(".","")
    if sayi == "e":
        break
    sayi = str(int(sayi))
    while len(sayi)%3!=0:
        sayi = "0" + sayi
    """
    009852852

    """
    liste = []
    for i in range(0,int(len(sayi)/3)):
        liste.append(sayi[(i*3):(i*3)+3])
    print(liste)
    liste.reverse()
    tumSonuc = ""
    adim = 0
    for item in liste:
        sonuc = ""
        if item != "000":
            if item[0] != "0":
                if item[0] != "1":
                    sonuc = birler[item[0]] +" Yüz "
                else:
                    sonuc = "Yüz"
            sonuc += onlar[item[1]] + birler[item[2]] 
            sonuc += basamak[adim]
        adim+= 1
        tumSonuc = sonuc + tumSonuc
    print(tumSonuc)
