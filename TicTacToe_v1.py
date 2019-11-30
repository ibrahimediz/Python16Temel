#tictactoe
import random
l=[i for i in range(1,10)]
l2=[0 for x in range(9)] #X control
l3=[0 for x in range(9)] #O control
l4=[4 for x in range(20)]+l #%72.41
def table():
    for i in range(0,9,3):
        print("+-------"*3,"+",sep="")
        print("|       "*4)
        print("|   {}   |   {}   |   {}   |".format(l[i],l[i+1],l[i+2]))
        print("|       "*4)
    print("+-------"*3,"+",sep="")
table()

def choose():
    where=int(input("\nWhich Number Will You Put '{}' ?: ".format(whostart)))
    while l[int(where)-1]=="X" or l[int(where)-1]=="O":
        print("Wrong Choose")
        where=int(input("Which Number Will You Put 'X' ?: "))
    l[int(where)-1]=whostart
    if whostart=="X":
        l2[where-1]=5
    elif whostart=="O":
        l3[where-1]=3
    control()

def pcrandom():
    pcchoose=random.choice(l)      
    while pcchoose=="X" or pcchoose=="O":
        pcchoose=random.choice(l)
    if whostart=="X":
        l[pcchoose-1]="O"
        if l[pcchoose-1]=="O":
            l3[pcchoose-1]=3
    elif whostart=="O":
        l[pcchoose-1]="X"
        if l[pcchoose-1]=="X":
            l2[pcchoose-1]=5
def xcheck():
    if (l3[1]+l3[2]==6 and l2[0]!=5 and l3[0]!=3) or (l3[3]+l3[6]==6 and l2[0]!=5 and l3[0]!=3) or (l3[4]+l3[8]==6 and l2[0]!=5 and l3[0]!=3):
        l[0]="O"
        l2[0]=3
    elif (l3[0]+l3[2]==6 and l2[1]!=5 and l3[1]!=3) or (l3[4]+l3[7]==6 and l2[1]!=5 and l3[1]!=3):
        l[1]="O"
        l3[1]=3
    elif (l3[0]+l3[1]==6 and l2[2]!=5 and l3[2]!=3) or (l3[5]+l3[8]==6 and l2[2]!=5 and l3[2]!=3) or (l3[4]+l3[6]==6 and l2[2]!=5 and l3[2]!=3):
        l[2]="O"
        l3[2]=3
    elif (l3[4]+l3[5]==6 and l2[3]!=5 and l3[3]!=3) or (l3[0]+l3[6]==6 and l2[3]!=5 and l3[3]!=3):
        l[3]="O"
        l3[3]=3
    elif (l3[3]+l3[5]==6 and l2[4]!=5 and l3[4]!=3) or (l3[1]+l3[7]==6 and l2[4]!=5 and l3[4]!=3) or (l3[0]+l3[8]==6 and l2[4]!=5 and l3[4]!=3):
        l[4]="O"
        l3[4]=3
    elif (l3[3]+l3[4]==6 and l2[5]!=5 and l3[5]!=3) or (l3[2]+l3[8]==6 and l2[5]!=5 and l3[5]!=3):
        l[5]="O"
        l3[5]=3
    elif (l3[7]+l3[8]==6 and l2[6]!=5 and l3[6]!=3) or (l3[0]+l3[3]==6 and l2[6]!=5 and l3[6]!=3):
        l[6]="O"
        l3[6]=3
    elif (l3[6]+l3[8]==6 and l2[7]!=5 and l3[7]!=3) or (l3[1]+l3[4]==6 and l2[7]!=5 and l3[7]!=3):
        l[7]="O"
        l3[7]=3
    elif (l3[6]+l3[7]==6 and l2[8]!=5 and l3[8]!=3) or (l3[2]+l3[5]==6 and l2[8]!=5 and l3[8]!=3) or (l3[0]+l3[4]==6 and l2[8]!=5 and l3[8]!=3):
        l[8]="O"
        l3[8]=3
def ocheck():
    if (l2[1]+l2[2]==10 and l3[0]!=3) or (l2[3]+l2[6]==10 and l3[0]!=3) or (l2[4]+l2[8]==10 and l3[0]!=3):
        l[0]="X"
        l2[0]=5
    elif (l2[0]+l2[2]==10 and l3[1]!=3) or (l2[4]+l2[7]==10 and l3[1]!=3):
        l[1]="X"
        l2[1]=5
    elif (l2[0]+l2[1]==10 and l3[2]!=3) or (l2[5]+l2[8]==10 and l3[2]!=3) or (l2[2]+l2[6]==10 and l3[4]!=3):
        l[2]="X"
        l2[2]=5
    elif (l2[4]+l2[5]==10 and l3[3]!=3) or (l2[0]+l2[6]==10 and l3[3]!=3):
        l[3]="X"
        l2[3]=5
    elif (l2[3]+l2[5]==10 and l3[4]!=3) or (l2[1]+l2[7]==10 and l3[4]!=3) or (l2[0]+l2[8]==10 and l3[4]!=3):
        l[4]="X"
        l2[4]=5
    elif (l2[3]+l2[4]==10 and l3[5]!=3) or (l2[2]+l2[8]==10 and l3[5]!=3):
        l[5]="X"
        l2[5]=5
    elif (l2[7]+l2[8]==10 and l3[6]!=3) or (l2[0]+l2[3]==10 and l3[6]!=3) or (l2[2]+l2[4]==10 and l3[6]!=3):
        l[6]="X"
        l2[6]=5
    elif (l2[6]+l2[8]==10 and l3[7]!=3) or (l2[1]+l2[4]==10 and l3[7]!=3):
        l[7]="X"
        l2[7]=5
    elif (l2[6]+l2[7]==10 and l3[8]!=3) or (l2[2]+l2[5]==10 and l3[8]!=3) or (l2[0]+l2[4]==10 and l3[8]!=3):
        l[8]="X"
        l2[8]=5

def pc():
    if whostart=="X":
        xcheck()
        control()
        if (l2[1]+l2[2]==10 and l3[0]!=3) or (l2[3]+l2[6]==10 and l3[0]!=3) or (l2[4]+l2[8]==10 and l3[0]!=3):
            l[0]="O"
            l3[0]=3
        elif (l2[0]+l2[2]==10 and l3[1]!=3) or (l2[4]+l2[7]==10 and l3[1]!=3):
            l[1]="O"
            l3[1]=3
        elif (l2[0]+l2[1]==10 and l3[2]!=3) or (l2[5]+l2[8]==10 and l3[2]!=3) or (l2[2]+l2[6]==10 and l3[4]!=3):
            l[2]="O"
            l3[2]=3
        elif (l2[4]+l2[5]==10 and l3[3]!=3) or (l2[0]+l2[6]==10 and l3[3]!=3):
            l[3]="O"
            l3[3]=3
        elif (l2[3]+l2[5]==10 and l3[4]!=3) or (l2[1]+l2[7]==10 and l3[4]!=3) or (l2[0]+l2[8]==10 and l3[4]!=3):
            l[4]="O"
            l3[4]=3
        elif (l2[3]+l2[4]==10 and l3[5]!=3) or (l2[2]+l2[8]==10 and l3[5]!=3):
            l[5]="O"
            l3[5]=3
        elif (l2[7]+l2[8]==10 and l3[6]!=3) or (l2[0]+l2[3]==10 and l3[6]!=3) or (l2[2]+l2[4]==10 and l3[6]!=3):
            l[6]="O"
            l3[6]=3
        elif (l2[6]+l2[8]==10 and l3[7]!=3) or (l2[1]+l2[4]==10 and l3[7]!=3):
            l[7]="O"
            l3[7]=3
        elif (l2[6]+l2[7]==10 and l3[8]!=3) or (l2[2]+l2[5]==10 and l3[8]!=3) or (l2[0]+l2[4]==10 and l3[8]!=3):
            l[8]="O"
            l3[8]=3
        else:
            pcrandom()
    if whostart=="O":
        ocheck()
        control()
        if (l3[1]+l3[2]==6 and l2[0]!=5 and l3[0]!=3) or (l3[3]+l3[6]==6 and l2[0]!=5 and l3[0]!=3) or (l3[4]+l3[8]==6 and l2[0]!=5 and l3[0]!=3):
            l[0]="X"
            l2[0]=5
        elif (l3[0]+l3[2]==6 and l2[1]!=5 and l3[1]!=3) or (l3[4]+l3[7]==6 and l2[1]!=5 and l3[1]!=3):
                l[1]="X"
                l2[1]=5
        elif (l3[0]+l3[1]==6 and l2[2]!=5 and l3[2]!=3) or (l3[5]+l3[8]==6 and l2[2]!=5 and l3[2]!=3) or (l3[4]+l3[6]==6 and l2[2]!=5 and l3[2]!=3):
                l[2]="X"
                l2[2]=5
        elif (l3[4]+l3[5]==6 and l2[3]!=5 and l3[3]!=3) or (l3[0]+l3[6]==6 and l2[3]!=5 and l3[3]!=3):
                l[3]="X"
                l2[3]=5
        elif (l3[3]+l3[5]==6 and l2[4]!=5 and l3[4]!=3) or (l3[1]+l3[7]==6 and l2[4]!=5 and l3[4]!=3) or (l3[0]+l3[8]==6 and l2[4]!=5 and l3[4]!=3):
                l[4]="X"
                l2[4]=5
        elif (l3[3]+l3[4]==6 and l2[5]!=5 and l3[5]!=3) or (l3[2]+l3[8]==6 and l2[5]!=5 and l3[5]!=3):
                l[5]="X"
                l2[5]=5
        elif (l3[7]+l3[8]==6 and l2[6]!=5 and l3[6]!=3) or (l3[0]+l3[3]==6 and l2[6]!=5 and l3[6]!=3):
                l[6]="X"
                l2[6]=5
        elif (l3[6]+l3[8]==6 and l2[7]!=5 and l3[7]!=3) or (l3[1]+l3[4]==6 and l2[7]!=5 and l3[7]!=3):
                l[7]="X"
                l2[7]=5
        elif (l3[6]+l3[7]==6 and l2[8]!=5 and l3[8]!=3) or (l3[2]+l3[5]==6 and l2[8]!=5 and l3[8]!=3) or (l3[0]+l3[4]==6 and l2[8]!=5 and l3[8]!=3):
                l[8]="X"
                l2[8]=5
        elif (l2[1]+l2[2]==10 and l3[0]!=5 and l3[0]!=3) or (l2[3]+l2[6]==10 and l3[0]!=5 and l3[0]!=3) or (l2[4]+l2[8]==10 and l3[0]!=5 and l3[0]!=3):
                l[0]="X"
                l2[0]=5
        elif (l2[0]+l2[2]==10 and l3[1]!=5 and l3[1]!=3) or (l2[4]+l2[7]==10 and l3[1]!=5 and l3[1]!=3):
                l[1]="X"
                l2[1]=5
        elif (l2[0]+l2[1]==10 and l3[2]!=5 and l3[2]!=3) or (l2[5]+l2[8]==10 and l3[2]!=5 and l3[2]!=3) or (l2[4]+l2[6]==10 and l3[2]!=5 and l3[2]!=3):
                l[2]="X"
                l2[2]=5
        elif (l2[4]+l2[5]==10 and l3[3]!=5 and l3[3]!=3) or (l2[0]+l2[6]==10 and l3[3]!=5 and l3[3]!=3):
                l[3]="X"
                l2[3]=5
        elif (l2[3]+l2[5]==10 and l3[4]!=5 and l3[4]!=3) or (l2[1]+l2[7]==10 and l3[4]!=5 and l3[4]!=3) or (l2[0]+l2[8]==10 and l3[4]!=5 and l3[4]!=3):
                l[4]="X"
                l2[4]=5
        elif (l2[3]+l2[4]==10 and l3[5]!=5 and l3[5]!=3) or (l2[2]+l2[8]==10 and l3[5]!=5 and l3[5]!=3):
                l[5]="X"
                l2[5]=5
        elif (l2[7]+l2[8]==10 and l3[6]!=5 and l3[6]!=3) or (l2[0]+l2[3]==10 and l3[6]!=5 and l3[6]!=3):
                l[6]="X"
                l2[6]=5
        elif (l2[6]+l2[8]==10 and l3[7]!=5 and l3[7]!=3) or (l2[1]+l2[4]==10 and l3[7]!=5 and l3[7]!=3):
                l[7]="X"
                l2[7]=5
        elif (l2[6]+l2[7]==10 and l3[8]!=5 and l3[8]!=3) or (l2[2]+l2[5]==10 and l3[8]!=5 and l3[8]!=3) or (l2[0]+l2[4]==10 and l3[8]!=5 and l3[8]!=3):
                l[8]="X"
                l2[8]=5
        else:
            pcrandom()
    control()

def control():
    if l2[0]+l2[1]+l2[2]==15 or l2[3]+l2[4]+l2[5]==15 or l2[6]+l2[7]+l2[8]==15 or l2[0]+l2[3]+l2[6]==15 or l2[1]+l2[4]+l2[7]==15 or l2[2]+l2[5]+l2[8]==15 or l2[2]+l2[4]+l2[6]==15 or l2[0]+l2[4]+l2[8]==15:
        table()
        print("\n'X' WIN\n")
        exit()

    elif l3[0]+l3[1]+l3[2]==9 or l3[3]+l3[4]+l3[5]==9 or l3[6]+l3[7]+l3[8]==9 or l3[0]+l3[3]+l3[6]==9 or l3[1]+l3[4]+l3[7]==9 or l3[2]+l3[5]+l3[8]==9 or l3[2]+l3[4]+l3[6]==9 or l3[0]+l3[4]+l3[8]==9:
        table()
        print("\n'O' WIN\n")
        exit()

    elif sum(l2)+sum(l3)==37:
        table()
        print("\nDRAW\n")
        exit()

whostart=input("\nChoose One (X) or (O): ").upper()
print("\n'X' Start The Game\n")
if whostart=="O":
    l[random.choice(l4)]="X"
    first=l.index("X")
    l2[first]=5
    table()
    
while True:
    if whostart=="X":
        choose()
        pc()
        table()
        
    elif whostart=="O":
        choose()
        pc()
        table()