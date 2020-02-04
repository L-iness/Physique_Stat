# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:49:15 2020

@authors: Inès & Alexia
"""

import matplotlib.pyplot as plt
import numpy as np

#%% Bloc 1 Q1
Tab=[[0,0]]
n= 100 #Nb pas

for i in range(n) :
    x= 2*np.random.rand(1)-1 #Valeur random entre -1 et 1
    y= 2*np.random.rand(1)-1
    if np.sqrt(x**2+y**2) <= 1 : #Vérif norme <= 1
        x+=Tab[-1][-2] #Récup dernière valeur de x
        y+=Tab[-1][-1] #Récup dernière valeur de y
        Tab.append([x,y])


nTab = np.array(Tab)
plt.plot(nTab[:,0],nTab[:,1])
plt.plot(nTab[0,0],"ro")
plt.show()

#%% Bloc 1 Q2

Tab=[[0,0]]
n= 1000


for i in range(n) :
    angle=2*np.pi*np.random.rand(1)
    x=np.cos(angle)+Tab[-1][-2]
    y=np.sin(angle)+Tab[-1][-1]
    Tab.append([x,y])


nTab = np.array(Tab)
plt.plot(nTab[:,0],nTab[:,1])
plt.plot(nTab[0,0],"ro")
plt.show()

#%% Bloc 2

Tab=[[0,0]]
n= 1000


for i in range(n) :
    angle= np.random.choice([np.pi/4,3*np.pi/4,-np.pi/4,-3*np.pi/4])
    x=np.cos(angle)+Tab[-1][-2]
    y=np.sin(angle)+Tab[-1][-1]

    Tab.append([x,y])


nTab = np.array(Tab)
plt.plot(nTab[:,0],nTab[:,1])
plt.plot(nTab[0,0],"ro")
plt.show()


#%% Bloc 3

Tab=[[0,0]]
Tab_NM = [[0,0]]
n= 1000

for j in range(100) : #100 marcheurs
    for i in range(n) :
        angle= np.random.choice([np.pi/4,3*np.pi/4,-np.pi/4,-3*np.pi/4])
        x=np.cos(angle)+Tab[-1][-2]
        y=np.sin(angle)+Tab[-1][-1]
        Tab.append([x,y])
    Tab_NM.append([Tab[-1][-2],Tab[-1][-1]])

nTab_NM = np.array(Tab_NM)
plt.scatter(nTab_NM[:,0],nTab_NM[:,1])
plt.show()

for j in range(1000) : #1000 marcheurs
    for i in range(n) :
        angle= np.random.choice([np.pi/4,3*np.pi/4,-np.pi/4,-3*np.pi/4])
        x=np.cos(angle)+Tab[-1][-2]
        y=np.sin(angle)+Tab[-1][-1]
        Tab.append([x,y])
    Tab_NM.append([Tab[-1][-2],Tab[-1][-1]])

nTab_NM = np.array(Tab_NM)
plt.scatter(nTab_NM[:,0],nTab_NM[:,1])
plt.show()

for j in range(10000) : #10000 marcheurs
    for i in range(n) :
        angle= np.random.choice([np.pi/4,3*np.pi/4,-np.pi/4,-3*np.pi/4])
        x=np.cos(angle)+Tab[-1][-2]
        y=np.sin(angle)+Tab[-1][-1]
        Tab.append([x,y])
    Tab_NM.append([Tab[-1][-2],Tab[-1][-1]])

nTab_NM = np.array(Tab_NM)
plt.scatter(nTab_NM[:,0],nTab_NM[:,1])
plt.show()


#%% Bloc 4

l_NM = [0]
n = 1000
NM = 100 #100 marcheurs

l = 2*np.random.randint(0,2, size=(n,NM))-1
l_NM=np.sum(l, axis = 0)

nl_NM = np.array(l_NM)
plt.hist(nl_NM, align = 'mid')
plt.xlabel('Distance')
plt.ylabel('Nombre de marcheurs')
plt.title('Histogramme des positions finales de 100 marcheurs de 1000 pas sur un réseau à 1D.')
plt.show()

moy = np.mean(l_NM)
ecart = np.std(l_NM)
print("Ecart-type =",ecart,"\nMoyenne =", moy)



l_NM = [0]
n = 1000
NM = 1000 #1000 marcheurs

l = 2*np.random.randint(0,2, size=(n,NM))-1
l_NM=np.sum(l, axis = 0)


nl_NM = np.array(l_NM)
plt.hist(nl_NM, align = 'mid')
plt.xlabel('Distance')
plt.ylabel('Nombre de marcheurs')
plt.title('Histogramme des positions finales de 1000 marcheurs de 1000 pas sur un réseau à 1D.')
plt.show()

moy = np.mean(l_NM)
ecart = np.std(l_NM)
print("Ecart-type =",ecart,"\nMoyenne =", moy)




l_NM = [0]
n = 1000
NM = 10000 #10000 marcheurs

l = 2*np.random.randint(0,2, size=(n,NM))-1
l_NM=np.sum(l, axis = 0)


nl_NM = np.array(l_NM)
plt.hist(nl_NM, align = 'mid')
plt.xlabel('Distance')
plt.ylabel('Nombre de marcheurs')
plt.title('Histogramme des positions finales de 10000 marcheurs de 1000 pas sur un réseau à 1D.')
plt.show()

moy = np.mean(l_NM)
ecart = np.std(l_NM)
print("Ecart-type =",ecart,"\nMoyenne =", moy)



#%% Bloc 5














