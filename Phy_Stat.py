# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:49:15 2020

@authors: Inès & Alexia
"""

import matplotlib.pyplot as plt
import numpy as np

#%% Bloc 1 Q1
Tab=[[0,0]]
n= 1000 #Nb pas

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
    angle=2*np.pi*np.random.rand(1)#Norme 1
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
sn=[]
l_x=[]

for j in range(100) : #100 marcheurs
    for i in range(n) :
        angle= np.random.choice([np.pi/4,3*np.pi/4,-np.pi/4,-3*np.pi/4]) #Déplacement en diagonale uniquement
        x=np.cos(angle)+Tab[-1][-2]
        y=np.sin(angle)+Tab[-1][-1]
        Tab.append([x,y])
    Tab_NM.append([Tab[-1][-2],Tab[-1][-1]])
    l_x.append(Tab[-1][-2])



sn = [nb*nb for nb in l_x]
rms = np.sqrt(np.sum(sn)/100)
print("RMS :", rms)


#nTab_NM = np.array(Tab_NM)
#plt.scatter(nTab_NM[:,0],nTab_NM[:,1])
#plt.show()

"""

for j in range(1000) : #1000 marcheurs
    for i in range(n) :
        angle= np.random.choice([np.pi/4,3*np.pi/4,-np.pi/4,-3*np.pi/4])
        x=np.cos(angle)+Tab[-1][-2]
        y=np.sin(angle)+Tab[-1][-1]
        Tab.append([x,y])
    Tab_NM.append([Tab[-1][-2],Tab[-1][-1]])
    l_x.append(Tab[-1][-2])
    
for a in range(1000) :
    sn.append(l_x[a]**2)
    
    
rms = np.sqrt(np.sum(sn)/1000**2)
print("RMS :", rms)


#nTab_NM = np.array(Tab_NM)
#plt.scatter(nTab_NM[:,0],nTab_NM[:,1],color='orange')
#plt.show()



for j in range(10000) : #10000 marcheurs
    for i in range(n) :
        angle= np.random.choice([np.pi/4,3*np.pi/4,-np.pi/4,-3*np.pi/4])
        x=np.cos(angle)+Tab[-1][-2]
        y=np.sin(angle)+Tab[-1][-1]
        Tab.append([x,y])
    Tab_NM.append([Tab[-1][-2],Tab[-1][-1]])
    l_x.append(Tab[-1][-2])
    
for a in range(10000) :
    sn.append(l_x[a]**2)
    
    
rms = np.sqrt(np.sum(sn)/10000**2)
print("RMS :", rms)


#nTab_NM = np.array(Tab_NM)
#plt.scatter(nTab_NM[:,0],nTab_NM[:,1],color='purple')
#plt.show()
"""

#%% Bloc 4

l_NM = [0]
n = 1000
NM = 100 #100 marcheurs

l = 2*np.random.randint(0,2, size=(n,NM))-1
l_NM=np.sum(l, axis = 0)

nl_NM = np.array(l_NM)
plt.hist(nl_NM, align = 'mid', bins = 200)
plt.xlabel('Distance')
plt.ylabel('Nombre de marcheurs')
plt.title('Histogramme des positions finales de 100 marcheurs de 1000 pas sur un réseau à 1D')
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
plt.hist(nl_NM, align = 'mid', color = 'orange', bins = 200)
plt.xlabel('Distance')
plt.ylabel('Nombre de marcheurs')
plt.title('Histogramme des positions finales de 1000 marcheurs de 1000 pas sur un réseau à 1D')
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
plt.hist(nl_NM, align = 'mid', color = 'purple', bins = 200)
plt.xlabel('Distance')
plt.ylabel('Nombre de marcheurs')
plt.title('Histogramme des positions finales de 10000 marcheurs de 1000 pas sur un réseau à 1D')
plt.show()

moy = np.mean(l_NM)
ecart = np.std(l_NM)
print("Ecart-type =",ecart,"\nMoyenne =", moy)



#%% Bloc 5

NM= np.zeros((100,10000))
NM[50,0] = 1
Tab_NM = [[]]
p = 0.01

for t in range(1,10000): #Pas de temps
    for i in range(100): #Position
        NM[i,t] = NM[i,t-1] - 2*p*NM[i, t-1]
        if i != 0:
            NM[i,t] = NM[i,t] + p*NM[i-1,t-1]
            if i != 99:
                NM[i,t] = NM[i,t] + p*NM[i+1,t-1]
            else :
                NM[i,t] = NM[i,t] + p*NM[i-1,t-1]
        
   
plt.plot(NM[:,0]/max(NM[:,0]))
plt.plot(NM[:,4999]/max(NM[:,4999]))
plt.plot(NM[:,-1]/max(NM[:,-1]))
plt.show()
