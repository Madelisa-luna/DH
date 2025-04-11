import matplotlib.pyplot as plt
import numpy as np
import re

# Función para cargar los vectores desde el archivo
def cargar_resultados(nombre_archivo):
    vectores_consulta = []
    vectores_cercanos = []

    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            # Buscar el vector consultado
            match_consulta = re.search(r"Vector consultado: \[([^\]]+)\]", linea)
            if match_consulta:
                vector_consulta = np.array([float(x) for x in match_consulta.group(1).split(',')])
                vectores_consulta.append(vector_consulta)

            # Buscar el vector cercano
            match_cercano = re.search(r"Vector cercano: \[([^\]]+)\]", linea)
            if match_cercano:
                vector_cercano = np.array([float(x) for x in match_cercano.group(1).split(',')])
                vectores_cercanos.append(vector_cercano)

    # Convertir las listas en arreglos de numpy
    vectores_consulta = np.array(vectores_consulta)
    vectores_cercanos = np.array(vectores_cercanos)

    return vectores_consulta, vectores_cercanos

# Cargar los vectores desde el archivo
archivo = "ResulBusqueda.txt"
vectores_consulta, vectores_cercanos = cargar_resultados(archivo)

# Concatenar todos los puntos para encontrar la curva principal
datos_totales = np.vstack((vectores_consulta, vectores_cercanos))

# Crear figura 3D
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Graficar los vectores originales
ax.plot(vectores_consulta[:, 0], vectores_consulta[:, 1], vectores_consulta[:, 2], 'bo-', label='Vectores Consultados')
ax.plot(vectores_cercanos[:, 0], vectores_cercanos[:, 1], vectores_cercanos[:, 2], 'ro-', label='Vectores Cercanos')

# Marcar el origen (0,0,0)
ax.scatter(0, 0, 0, color='k', marker='o', s=100, label='Origen (0,0,0)')

# Etiquetas de los ejes
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Representación 3D de Vectores, Consultados y Cercanos")
ax.legend()
plt.show()
