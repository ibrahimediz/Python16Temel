
var1 = "Al kazık çak karaya kayarak kaç kızakla"
var2 = "Aç raporunu koy okunur o parça"
def palindromCheck(text):
    text = text.lower().replace(" ","")
    orta = int((len(text)/2))
    text1 = text[:orta]
    print(text1)
    text2 = text[orta+1:][::-1]
    print(text2)
    if text1 == text2:
        return True
    else:
        return False

print(palindromCheck(var1))

    