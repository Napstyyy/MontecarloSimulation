# Mateo Giraldo Arboleda 1004720499 
# Anderson Adarve Valencia 1088825359
# Importa las bibliotecas necesarias
import random
import numpy as np
import matplotlib.pyplot as plt

# Define una función para realizar una simulación de Monte Carlo
def simulacionMonteCarlo(distribucionProbabilidades, numObservaciones):
    ganancias = []  # Inicializa una lista para almacenar las ganancias simuladas
    for _ in range(numObservaciones):
        # Genera un número de licencias vendidas basado en la distribución de probabilidades
        licenciasVendidas = random.choices(*zip(*distribucionProbabilidades))[0]
        costoLicencia = 75  # Costo por licencia
        precioVenta = 100  # Precio de venta por licencia
        # Calcula la ganancia como la diferencia entre ingresos y costos
        ganancia = (precioVenta - costoLicencia) * licenciasVendidas
        ganancias.append(ganancia)  # Agrega la ganancia a la lista
    return ganancias  # Devuelve la lista de ganancias simuladas

# Define la distribución de probabilidades de ventas de licencias
distribucionProbabilidades = [(100, 0.30), (150, 0.20), (200, 0.30), (250, 0.15), (300, 0.05)]

# Realiza simulaciones de Monte Carlo con diferentes cantidades de observaciones
observaciones1000 = simulacionMonteCarlo(distribucionProbabilidades, 1000)
observaciones2000 = simulacionMonteCarlo(distribucionProbabilidades, 2000)
observaciones5000 = simulacionMonteCarlo(distribucionProbabilidades, 5000)

# Calcula estadísticas para cada conjunto de observaciones
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

# Definir colores específicos para cada observación
colores = ['b', 'g', 'r']

# Crear un histograma de las ganancias simuladas
plt.hist([observaciones1000, observaciones2000, observaciones5000], bins=30, color=colores, label=['1000 Observaciones', '2000 Observaciones', '5000 Observaciones'], alpha=0.5)

# Crea una barra que muestra la distribución teórica de ventas de licencias
ventas, probabilidades = zip(*distribucionProbabilidades)
plt.bar(ventas, [p * 100 for p in probabilidades], color='c', width=25, label='Distribución Teórica', alpha=0.5)

# Etiqueta los ejes del gráfico y muestra una leyenda
plt.xlabel('Ganancias')
plt.ylabel('Frecuencia')
plt.legend()

# Muestra el gráfico
plt.show()
