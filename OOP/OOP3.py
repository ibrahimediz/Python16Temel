from OOP2 import Deadpool,Hulk,IronMan,KaraMurat
from random import choice
import time
liste = [Deadpool,Hulk,IronMan,KaraMurat]

p1 = choice(liste)()
p2 = choice(liste)()


while p1.saglik >0 and p2.saglik >0:
    p1.haraketSec()(p2.haraketSec2()())
    p2.haraketSec()(p1.haraketSec2()())
    print("{}-{}".format(p1.Durum(),p2.Durum()))
    time.sleep(1)
else:
    if p1.saglik>p2.saglik:
        print(p1.adi,"Kazandı")
    elif p1.saglik<p2.saglik:
        print(p2.adi,"Kazandı")   
    else:
        print("Berabere") 
