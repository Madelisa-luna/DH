import matplotlib.pyplot as plt
import numpy as np
import re


# Función para leer el archivo de texto y extraer los datos

def leer_datos(archivo):
    puntos = []
    patron = re.compile(r'x\s*=\s*([-\d\.e]+),\s*y\s*=\s*([-\d\.e]+),\s*z\s*=\s*([-\d\.e]+)')
    
    with open(archivo, 'r', encoding='utf-8', errors='ignore') as f:
        for linea in f:
            match = patron.search(linea)
            if match:
                try:
                    x, y, z = map(float, match.groups())
                    puntos.append([x, y, z])
                except Exception as e:
                    print(f"Error al procesar línea: {linea.strip()} - {e}")
                    continue
    
    return np.array(puntos) if puntos else np.empty((0, 3))

# Cargar los datos del archivo
datos = leer_datos('Ejemplo5-19.txt')

# Verificar que hay datos antes de graficar
if datos.shape[0] == 0:
    print("No se encontraron puntos válidos en el archivo.")
else:
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    
    # Dibujar los puntos alcanzados por el brazo
    ax.scatter(datos[:, 0], datos[:, 1], datos[:, 2], c='blue', marker='o', alpha=0.6, label='Puntos alcanzados')
    ax.scatter(0, 0, 0, color='k', marker='o', s=100, label='Origen (0,0,0)')
    
    # Configuración de la gráfica
    ax.set_xlabel('X (cm)')
    ax.set_ylabel('Y (cm)')
    ax.set_zlabel('Z (cm)')
    ax.set_title('Espacio de trabajo del brazo esférico')
    ax.legend()
    
    plt.show()