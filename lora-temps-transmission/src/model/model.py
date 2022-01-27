
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






print("Le spreading factor median est de : ",ComputeMedian())
print("Le spreading factor moyen  est de : ",ComputeMean())



