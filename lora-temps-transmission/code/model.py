
import matplotlib.pyplot as plt
import numpy as np
import csv

li=[]
ly=[]
toa=[]
with open('../../code/Donnee.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        li.append(';'.join(row))
for i in range(len(li)):
    ly.append(li[i].split(';'))
for i in range(1,len(ly)):
    a=int(ly[i][8])
    toa.append(a)


def ComputeMean():
    mean = 0
    for i in range(1,len(ly)-1):

        mean+=toa[i]
    mean=mean/(len(ly)-1)
    mean=round(mean,2)
    return (mean)

def ComputeMedian():

    toa.sort()
    a=len(toa) // 2

    median=toa[a]

    return (median)

def courbeed():
    x=[]
    y=[]
    z=[]
    for i in range(1,len(ly)):

        b=int(ly[i][5])
        b=b*99/1000
        a=int(ly[i][11])
        print(a)


        y.append(b)


        x.append(a)


    plt.bar(x, y, align='center', facecolor='red', alpha=1)
    plt.title("temp d'envoie en fonction de la taille des données")
    plt.xlabel('taille des données ')
    plt.ylabel("temps d'envoie en seconde")
    plt.plot(x, y, 'r--', linewidth=0)




    return(plt.show())

def courbe():
    x=[]
    y=[]
    z=[]
    e=[]
    f=[]
    g=[]
    h=[]
    k=[]
    j=[]
    e2=[]
    f2=[]
    g2=[]
    h2=[]
    j2=[]
    k2=[]
    for i in range(1,len(ly)):

        b=int(ly[i][5])
        b=b*99/1000
        a=int(ly[i][11])
        c=int(ly[i][8])




        y.append(b)



        if c==10:
            g.append(a)
            g2.append(b)
        elif c==11:
            f.append(a)
            f2.append(b)
        elif c==7:
            e.append(a)
            e2.append(b)
        elif c==8:
            h.append(a)
            h2.append(b)
        elif c==9:
            k.append(a)
            k2.append(b)
        elif c==12:
            j.append(a)
            j2.append(b)

        x.append(a)
    print(x)
    plt.bar(k, k2, align='center', facecolor='black', alpha=1)
    plt.bar(j, j2, align='center', facecolor='pink', alpha=1)
    plt.bar(f, f2, align='center', facecolor='blue', alpha=1)
    plt.bar(g, g2, align='center', facecolor='yellow', alpha=1)
    plt.bar(h, h2, align='center', facecolor='green', alpha=1)
    plt.bar(e, e2, align='center', facecolor='red', alpha=1)



    plt.title("temp d'envoie en fonction de la taille des données")
    plt.xlabel('taille des données ')
    plt.ylabel("temps d'envoie en seconde")
    plt.plot(x, y, 'r--', linewidth=0)




    return(plt.show())

print(courbe())

