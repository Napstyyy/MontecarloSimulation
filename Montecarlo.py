import random
import numpy as np
import matplotlib.pyplot as plt

def simulacionMonteCarlo(distribucionProbabilidades, numObservaciones):
    ganancias = []
    for _ in range(numObservaciones):
        licenciasVendidas = random.choices(*zip(*distribucionProbabilidades))[0]
        costoLicencia = 75
        precioVenta = 100
        ganancia = (precioVenta - costoLicencia) * licenciasVendidas
        ganancias.append(ganancia)
    return ganancias

distribucionProbabilidades = [(100, 0.30), (150, 0.20), (200, 0.30), (250, 0.15), (300, 0.05)]

observaciones1000 = simulacionMonteCarlo(distribucionProbabilidades, 1000)
observaciones2000 = simulacionMonteCarlo(distribucionProbabilidades, 2000)
observaciones5000 = simulacionMonteCarlo(distribucionProbabilidades, 5000)

promedio1000 = np.mean(observaciones1000)
promedio2000 = np.mean(observaciones2000)
promedio5000 = np.mean(observaciones5000)

varianza1000 = np.var(observaciones1000)
varianza2000 = np.var(observaciones2000)
varianza5000 = np.var(observaciones5000)
desviacion1000 = np.sqrt(varianza1000)
desviacion2000 = np.sqrt(varianza2000)
desviacion5000 = np.sqrt(varianza5000)

cv1000 = (desviacion1000 / promedio1000) * 100
cv2000 = (desviacion2000 / promedio2000) * 100
cv5000 = (desviacion5000 / promedio5000) * 100

plt.hist(observaciones1000, bins=30, label='1000 Observaciones', alpha=0.5)
plt.hist(observaciones2000, bins=30, label='2000 Observaciones', alpha=0.5)
plt.hist(observaciones5000, bins=30, label='5000 Observaciones', alpha=0.5)

ventas, probabilidades = zip(*distribucionProbabilidades)
plt.bar(ventas, [p * 100 for p in probabilidades], width=25, label='Distribución Teórica', alpha=0.5)

plt.xlabel('Ganancias')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()
