import pandas as pd
import glob
import os
import csv
li=[]
ly=[]
toa=[]
Toa=[]
erreur0=0
erreur1=0
erreur2=0
erreur3=0
erreur4=0
erreur5=0
erreur6=0
erreur7=0
erreur8=0
erreur9=0
erreur10=0
erreur11=0
erreuri=[]

with open('Donnee.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        li.append(';'.join(row))
for i in range(len(li)):
    ly.append(li[i].split(';'))
for i in range(1,len(li)):
    if ly[i][0]=='NaN':
        erreur0+=1
    if ly[i][1]=='NaN':
        erreur1+=1
    if ly[i][2] == 'NaN':
        erreur2 += 1
    if ly[i][3] == 'NaN':
        erreur3 += 1
    if ly[i][4] == 'NaN':
        erreur4 += 1
    if ly[i][5]=='0':
        erreur5+=1
    if ly[i][6]>'0':
        erreur6+=1
    if ly[i][7]!='14':
        erreur7+=1
    if ly[i][8]=='0':
        erreur8+=1
    if  ly[i][9]!='125' and ly[i][9]!='250':
            erreur9 += 1
    if ly[i][10]!='4_5'and ly[i][10]!='4_6'and ly[i][10]!='4_7'and ly[i][10]!='4_8':
        erreur10+=1
    if ly[i][11]<'51':
        erreur11+=1
erreur=+erreur1+erreur0+erreur2+erreur3+erreur4+erreur5+erreur6+erreur7+erreur8+erreur9+erreur10+erreur11



erreuri.append(erreur0)
erreuri.append(erreur1)
erreuri.append(erreur2)
erreuri.append(erreur3)
erreuri.append(erreur4)
erreuri.append(erreur5)
erreuri.append(erreur6)
erreuri.append(erreur7)
erreuri.append(erreur8)
erreuri.append(erreur9)
erreuri.append(erreur10)
erreuri.append(erreur11)




for i in range (12):
    err='erreur'+str(i)
    print("le nombre d'erreur pour la colonne {} est de : {}".format(ly[0][i],erreuri[i]))
print("le nombre d'érreur total est de : ",erreur)
erreur=(erreur/(len(li)*11))*100
print("le pourcentage d'erreurs est de :",round(erreur,2))
for i in range(1,len(li)):
    a=int(ly[i][5])
    toa.append(a)
for i in range(0,len(toa)):
    b=(toa[i]*99)/1000
    Toa.append(b)

print( "le temps de transmission  des données est de :",Toa)









