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

def courbe():
    x = []
    y = []

    e = []
    f = []
    g = []
    h = []
    k = []
    j = []
    e2 = []
    f2 = []
    g2 = []
    h2 = []
    j2 = []
    k2 = []
    l = []
    l2 = []
    m = []
    m2 = []
    plt.subplot(311)
    for i in range(1, len(ly)):

        b = int(ly[i][5])
        b = b * 99 / 1000
        a = int(ly[i][11])
        c = int(ly[i][10])

        y.append(b)

        if c == 45:
            g.append(a)
            g2.append(b)
        elif c == 46:
            f.append(a)
            f2.append(b)
        elif c == 47:
            e.append(a)
            e2.append(b)
        elif c == 48:
            h.append(a)
            h2.append(b)

        x.append(a)

    plt.bar(h, h2, align='center', facecolor='green', alpha=1,label='codingRate 4_8')
    plt.bar(e, e2, align='center', facecolor='red', alpha=1,label='codingRate 4_7')
    plt.bar(f, f2, align='center', facecolor='blue', alpha=1,label='codingRate 4_6')
    plt.bar(g, g2, align='center', facecolor='black', alpha=1,label='codingRate 4_5')

    plt.title("temp d'envoie en fonction de la taille des données")
    plt.xlabel('taille des données ')
    plt.ylabel("temps d'envoie en seconde")
    plt.legend()


    plt.plot(x, y, 'r--', linewidth=0)

    plt.subplot(312)
    for i in range(1, len(ly)):

        b = int(ly[i][5])
        b = b * 99 / 1000
        a = int(ly[i][11])
        c = int(ly[i][8])

        y.append(b)

        if c == 10:
            g.append(a)
            g2.append(b)
        elif c == 11:
            f.append(a)
            f2.append(b)
        elif c == 7:
            e.append(a)
            e2.append(b)
        elif c == 8:
            h.append(a)
            h2.append(b)
        elif c == 9:
            k.append(a)
            k2.append(b)
        elif c == 12:
            j.append(a)
            j2.append(b)

        x.append(a)







    plt.bar(h, h2, align='center', facecolor='green', alpha=1, label='spreading factor 8')
    plt.bar(j, j2, align='center', facecolor='pink', alpha=1, label='spreading factor 12')

    plt.bar(e, e2, align='center', facecolor='red', alpha=1, label='spreading factor 7')
    plt.bar(k, k2, align='center', facecolor='cyan', alpha=1, label='spreading factor 9')
    plt.bar(f, f2, align='center', facecolor='blue', alpha=1, label='spreading factor 11')
    plt.bar(g, g2, align='center', facecolor='brown', alpha=1, label='spreading factor 10')
    plt.legend()


    plt.xlabel('taille des données ')
    plt.ylabel("temps d'envoie en seconde")

    plt.plot(x, y, 'r--', linewidth=0)

    plt.subplot(313)



    for i in range(1, len(ly)):

        b = int(ly[i][5])
        b = b * 99 / 1000
        a = int(ly[i][11])
        c = int(ly[i][9])

        y.append(b)


        if c == 125:
            l.append(a)
            l2.append(b)
        elif c == 250:
            m.append(a)
            m2.append(b)

        x.append(a)

    plt.bar(l, l2, align='center', facecolor='pink', alpha=1, label='Bandwith 125')
    plt.bar(m, m2, align='center', facecolor='blue', alpha=1, label='Bandwith 250')
    plt.legend()

    plt.xlabel('taille des données ')
    plt.ylabel("temps d'envoie en seconde")

    plt.plot(x, y, 'r--', linewidth=0)

    return(plt.show())
print(courbe())