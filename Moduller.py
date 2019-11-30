import os
# import random
# import time
# import sys
# import math
# import datetime
# import subprocess
# import webbrowser
# import subprocess as sp

# print(os.getcwd())
# print(os.sep)
# import datetime as dt
# x =  dt.datetime.now()

# yil = str(x.year)
# ay = str(x.month)
# gun = str(x.day)
# saat = str(x.hour)
# dakika = str(x.minute)
# liste = [yil,ay,gun,saat,dakika]
# sonuc = ""
# for item in liste:
#     try:
#         os.mkdir(item)
#         os.chdir(os.curdir+os.sep+item)
#     except:
#         os.chdir(os.curdir+os.sep+item)
# print(os.getcwd())
# os.chdir(r"D:\bayram")
# print(os.getcwd())
# os.chdir("..")
# print(os.getcwd())
# yurudum = os.walk(r"D:\video")
# for a,b,c in yurudum:
#     print(a,b,c,sep="\t")
# import platform
# print(platform.version())



# import random as rnd
# rnd.randint(1,10)
# from random import randint as rint,seed as sd,sample as smp
# rnd.seed(0)
# print(rnd.random())
# print(rnd.random())
# print(rnd.random())
# print(rnd.random())
# print(rnd.random())
# print(rnd.random())

# import sys
# print(sys.argv)
# if sys.argv[1] == "benfero":
#     print("Hava Kapalı")
# elif sys.argv[1] == "normender":
#     print("sabah yaptım krep")
# else:
#     print("Uyhulaaar")

import sys
print(*sys.path,sep="\n")
sys.path.append(r"D:\Video")
import moduller.Jamiryo as jm
jm.rastgele(jm.liste)
print(*sys.path,sep="\n")


