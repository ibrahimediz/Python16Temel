"""

T and T ==> T
T and F ==> F
F and T ==> F
F and F ==> F

T or T ==> T
F or T ==> T
T or F ==> T
F or F ==> F

not T ==> F
not F ==> T
"""
a = 6
b = 3
if not a == 5 and b == 3 or a != 7:
    print("Doğru")



liste = [1,2,3,4,5]
if 2 in liste:
    print("Doğru")

# metin = "Real Madrid"
# if "B" in metin:
#     print("Doğru")


Hayat = "acı"
Biber = "acı"

if Hayat is Biber:
    print("Hayat Biberdir")



