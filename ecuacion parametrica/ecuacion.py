import matplotlib.pyplot as plt
import numpy as np

# Definir los parámetros
t = np.linspace(0, 2*np.pi, 100)  # Rango del parámetro

# Definir las ecuaciones paramétricas
x = np.cos(t)
y = np.sin(t)

# Graficar la curva paramétrica
#plt.plot(x, y)
#plt.axis('equal')
#plt.xlabel('X')
#plt.ylabel('Y')
#plt.title('Curva Paramétrica')
#plt.show()

import matplotlib.pyplot as plt

# Coordenadas de los puntos de inicio y fin de la línea
x0, y0 = 1, 2
x1, y1 = 5, 6

# Calcular las coordenadas de la línea mediante la ecuación paramétrica
x_coords = []
y_coords = []
for t in range(101):
    t /= 100.0  # Normalizar t al rango [0, 1]
    x = x0 + t * (x1 - x0)
    y = y0 + t * (y1 - y0)
    x_coords.append(x)
    y_coords.append(y)
    print(f"t = {t:.2f}: (x, y) = ({x:.2f}, {y:.2f})")

# Configurar el gráfico
plt.plot(x_coords, y_coords, color='blue')
plt.scatter(x_coords, y_coords, color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Ecuación Paramétrica de una Línea')
plt.grid(True)

# Mostrar el gráfico resultante
plt.show()


