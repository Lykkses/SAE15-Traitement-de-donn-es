
import matplotlib.pyplot as plt
import numpy as np
import csv

li=[]
ly=[]
toa=[]
Toa=[]
with open('../../code/Donnee.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        li.append(';'.join(row))
for i in range(len(li)):
    ly.append(li[i].split(';'))
for i in range(1,len(ly)):
    a=int(ly[i][8])
    toa.append(a)

for i in range(0, len(toa)):
    b = (toa[i] * 99) / 1000
    Toa.append(b)

def ComputeMean():
    mean7 = 0
    mean8=0
    mean9 = 0
    mean10 = 0
    mean11 = 0
    mean12 = 0
    cont7 = 0
    cont8 = 0
    cont9 = 0
    cont10 = 0
    cont11 = 0
    cont12=0

    for i in range(len(ly)-1):
        if toa[i]==7:
            cont7 += 1
            mean7+=Toa[i]
        if toa[i] == 8:
            mean8 += Toa[i]
            cont8 += 1
        if toa[i]==9:
            cont9 += 1
            mean9+=Toa[i]
        if toa[i]==10:
            cont10 += 1
            mean10+=Toa[i]
        if toa[i]==11:
            cont11 += 1
            mean11+=Toa[i]

        if toa[i]==12:
            cont12+=1
            mean12+=Toa[i]

    mean7 = mean7 / (cont7)
    mean7 = round(mean7, 2)
    mean8 = mean8 / (cont8)
    mean8= round(mean8, 2)
    mean9 = mean9 / (cont9)
    mean9 = round(mean9, 2)
    mean10 = mean10 / (cont10)
    mean10= round(mean10, 2)
    mean11 = mean11 / (cont11)
    mean11 = round(mean11, 2)
    mean12=mean12/(cont12)
    mean12=round(mean12,2)
    print("Le temps d'envoie moyen pour un spreding factor de 7 est de : ",mean7,'secondes')
    print("Le temps d'envoie moyen pour un spreding factor de 8 est de : ", mean8,'secondes')
    print("Le temps d'envoie moyen pour un spreding factor de 9 est de : ", mean9,'secondes')
    print("Le temps d'envoie moyen pour un spreding factor de 10 est de : ", mean10,'secondes')
    print("Le temps d'envoie moyen pour un spreding factor de 11 est de : ", mean11,'secondes')
    print("Le temps d'envoie moyen pour un spreding factor de 12 est de : ", mean12,'secondes')


    return (mean12)

def ComputeMedian():
    med7 = []
    med8 = []
    med9 = []
    med10 = []
    med11 = []
    med12 = []
    cont7 = 0
    cont8 = 0
    cont9 = 0
    cont10 = 0
    cont11 = 0
    cont12 = 0

    for i in range(len(ly) - 1):
        if toa[i] == 7:
            cont7 += 1
            med7.append(Toa[i])
        if toa[i] == 8:
            med8.append(Toa[i])
            cont8 += 1
        if toa[i] == 9:
            cont9 += 1
            med9.append(Toa[i])
        if toa[i] == 10:
            cont10 += 1
            med10.append(Toa[i])
        if toa[i] == 11:
            cont11 += 1
            med11.append(Toa[i])

        if toa[i] == 12:
            cont12 += 1
            med12.append(Toa[i])

    med7.sort()
    med8.sort()
    med9.sort()
    med10.sort()
    med11.sort()
    med12.sort()
    cont7=len(med7)//2
    cont8 = len(med8) // 2
    cont9 = len(med9) // 2
    cont10 = len(med10) // 2
    cont11 = len(med11) // 2
    cont12 = len(med12) // 2

    print("Le temps médian d'envoie avec un spreading factor de 7 est de  ", med7[cont7])
    print("Le temps médian d'envoie avec un spreading factor de 8 est de  ", med8[cont8])
    print("Le temps médian d'envoie avec un spreading factor de 9 est de  ", med9[cont9])
    print("Le temps médian d'envoie avec un spreading factor de 10 est de  ", med10[cont10])
    print("Le temps médian d'envoie avec un spreading factor de 11 est de  ", med11[cont11])
    print("Le temps médian d'envoie avec un spreading factor de 12 est de  ", med12[cont12])


    median=toa[a]

    return (median)






ComputeMedian()

ComputeMean()



