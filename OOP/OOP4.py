# from OOP1 import Sekil
# nesne = Sekil()
# nesne.__degisken


class Sekil:
    tip = "Çokgen" #Sınıf Nitelik
    def __init__(self,x=5,y=5):
        self.x = x
        self.y = y # Örnek Nitelik
        self.tanim = "Bu şekil henüz tanımlanmadı"
        self.sahip = "Henüz sahip yok"

    def alan(self):
        return self.x*self.y

    def Buyut(self,oran):
        self.x = self.x*oran
        self.y = self.y*oran

    def __del__(self):
        print("Hastala Vista")

   
    @classmethod
    def tipDegistir(cls,param):
        cls.tip = param


class Polygon():
    def __init__(self,no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    

    def inputSides(self):
        self.sides = [float(input("Enter side"+str(i+1)+":")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

    def Yaz(self):
        print("Uyhulaar")
    

class Triangle(Polygon,Sekil):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a,b,c = self.sides
        s = (a+b+c) / 2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        print(f"Üçgenin Alanı {area}")
        print("Üçgenin Alanı %0.2f"%area)
        print("Üçgenin Alanı {}".format(area))
 
    def Yaz(self):  #PolyMorphism  # override
        print("Sabah Yaptım Krep")
t = Triangle()





# t.inputSides()
# t.dispSides()
# t.findArea()

class A:
    def __init__(self):
        print("A")

    def yaz2(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")

    def yaz(self):
        print("B")

class C(B):
    def __init__(self):
        super().__init__()
        print("C")
        super().yaz2()
    


c = C()


# from abc import ABCMeta,abstractmethod,ABC


# class Animal(ABC):
#     __metaclass__ = ABCMeta

#     @abstractmethod
#     def biseysoyle(self):
#         return "Merhaba"


#     def devam(self):
#         pass

# class Cat(Animal):
#     def biseysoyle(self):
#         s = super(Cat,self).biseysoyle()
#         return s,"Miyav"



# c = Cat()
# print(c.biseysoyle())