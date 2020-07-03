# Tarea4

## 1.Crear un esquema de modulación BPSK para los bits presentados. Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria) para cada bit y luego una concatenación de todas estas formas de onda.

Para esta parte comenzamos importando ciertas librerias que nos permitiran un manejo de datos mas eficiente y realizar todo lo que se pide.
'''python
#Frecuencia de operación
f = 1000 # Hz

#Duración del período de cada símbolo (onda)
T = 1/f # 1 ms

#Número de puntos de muestreo por período
p = 50

#Puntos de muestreo para cada período
tp = np.linspace(0, T, p)

#Creación de la forma de onda de la portadora
sinus = np.sin(2*np.pi * f * tp)

#Visualización de la forma de onda de la portadora
plt.plot(tp, sinus)
plt.xlabel('Tiempo / s')
plt.show()

#Frecuencia de muestreo
fs = p/T # 50 kHz

#Creación de la línea temporal para toda la señal Tx
t = np.linspace(0, N*T, N*p)

#Inicializar el vector de la señal modulada Tx
senal = np.zeros(t.shape)

#Creación de la señal modulada OOK
for k, b in enumerate(bits):
    senal[k*p:(k+1)*p] = b * sinus

#Visualización de los primeros bits modulados
pb = 5
plt.figure()
plt.plot(senal[0:pb*p])
plt.show()
...
