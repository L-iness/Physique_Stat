# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:49:15 2020

@author: Inès
"""

import matplotlib.pyplot as plt
import numpy as np

#%% Bloc 1 Q1
Tab=[[0,0]]
n= 100

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
    angle=2*np.pi*np.random.rand(1)
    x=np.cos(angle)+Tab[-1][-2]
    y=np.sin(angle)+Tab[-1][-1]

    Tab.append([x,y])


nTab = np.array(Tab)
plt.plot(nTab[:,0],nTab[:,1])
plt.plot(nTab[0,0],"ro")
plt.show()





