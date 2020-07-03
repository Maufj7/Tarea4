# Tarea4

## 1. Crear un esquema de modulación BPSK para los bits presentados. Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria) para cada bit y luego una concatenación de todas estas formas de onda.

Para esta parte comenzamos importando ciertas librerias que nos permitiran un manejo de datos mas eficiente y realizar todo lo que se pide. Tenemos una frecuencia de la portadora de 5000 Hz. El codigo usado en la primera parte fue el siguiente. EN el cual creamos el modelo BPSK en base que cuando se presenta un 1 la señal se define como lasel seno posotivo y si es un 0 seria el seno negativo.

```python
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

T= 1/f #periodo

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

```

Como resultado en esta parte, creamos la onda la cual es senoidal en base a la frecuencia que tenemos y tambien la onda modulda para cada bit de entrada asi como se ve en las siguiente imagenes.

<img src="Figure_1.png"> <img src="Figure_2.png">

