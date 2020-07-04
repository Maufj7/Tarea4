# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 17:05:44 2020

@author: Owner
"""


# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 21:07:53 2020

@author: Mauricio Figueroa B72980
"""

import pandas as pd
import matplotlib.pyplot as plt
import scipy as sc
from scipy.stats import norm
import matplotlib.mlab as mlab
import numpy as np
from fitter import Fitter
from scipy.optimize import curve_fit
from scipy import optimize
from scipy import stats
from scipy import signal
from scipy import integrate
from mpl_toolkits.mplot3d import Axes3D#grafica en 3D

#Leemos los datos 
data = pd.read_csv('bits10k.csv', header=None, prefix="data")

f=5000 #frecuencia

T= 1/f #periodo 0.0002

#numero de puntos de muestreo por período

p=50

#Puntos de muestreo para cada período

tp=np.linspace(0, T, p)

#Creacion de la forma de onda

sine=np.sin(2*np.pi*f*tp)

#Visualizar onda
plt.figure()
plt.plot(tp, sine)
plt.xlabel('Tiempo /s')
plt.title('Onda')

#Frecuencia de muestreo

fs=p/T #250000

#Creacion de la linea temporal para tx

t=np.linspace(0,len(data)*T,len(data)* p)

#Inicializar vector de señal

senal= np.zeros(t.shape)

#Señal modulada BPSK

for k,b in enumerate(data['data0']):
    
    if b==1:
        senal[k*p:(k+1)*p]= sine
    else:
        senal[k*p:(k+1)*p]= -sine
        
        
#Visualizacion de los bits ya modulados  
pb=5
plt.figure(2)
plt.plot(senal[0:pb*p])

#Parte 2

Pinst= senal**2

#Potencia Promedio (W)

P=integrate.trapz(Pinst, t)/(len(data)*T)

print('La potencio promedio es:', P,'W' )


SRN1=[-2,-1,0,1,2,3]
BER1=[]




#Parte 3 

for i in range(-2, 4):

    SNR=i
    
    #SNRd=10 log10(P/Pn)
    #Potencia del ruido para SNR
    Pn=P/(10**(SNR/10))
    
    #Desviacion estandar
    sigma=np.sqrt(Pn)
    
    
    #Creamos ruido
    
    ruido= np.random.normal(0,sigma,senal.shape )
    
    #Simular el canal
    
    Rx= senal+ruido
    
    
    # Visualizacion de los primeros bits recibidos
    plt.figure()
    plt.title('SRN=%i' %i)
    plt.plot(Rx[0:pb*p])



#Parte 4 Welch
    
    fw, PSD = signal.welch(senal, fs, nperseg=1024)
    plt.figure()
    plt.semilogy(fw, PSD)
    plt.title('Antes del canal ruidoso')
    plt.xlabel('Frecuencia / Hz')
    plt.ylabel('Densidad espectral de potencia / V**2/Hz')
    plt.show()
    
    # Después del canal ruidoso
    fw, PSD = signal.welch(Rx, fs, nperseg=1024)
    plt.figure()
    plt.semilogy(fw, PSD)
    plt.title('Despues del canal ruidoso')
    plt.xlabel('Frecuencia / Hz')
    plt.ylabel('Densidad espectral de potencia / V**2/Hz')
    plt.show()
    
    
    
    
    
    
    # Parte 5 demodular 
    
    #Energia de la onda origuinal
    
    Es= sum(sine**2)
    
    #Inicializacion de bits recibidos
    
    bitsRx= np.zeros(data['data0'].shape)
    
    
    #Decodificacion de la se;al por deteccion de energia
    
    for k,b in enumerate(data['data0']):
        
        E = np.sum(Rx[k*p:(k+1)*p]*sine) #producto de dos funciones
        
        if E> Es/2:
            bitsRx[k]=1
        else:
            bitsRx[k]=0
            
            
    err=  np.sum(np.abs(data['data0']-bitsRx))
        
    BER= err/len(data)
    
    BER1.append(BER)
    
    print('Hay un total de {} errores en {} bits para una tasa de error de {}.'.format(err, len(data), BER))

    
    
#Parte 6
    
plt.figure()
plt.bar(SRN1, BER1)
plt.xlabel('SRN(dB)')
plt.ylabel('Ber')    
plt.title('BER vs SRN')
    






