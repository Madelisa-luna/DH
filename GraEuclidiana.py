import matplotlib.pyplot as plt
import re

# Función para cargar distancias euclidianas desde el archivo
def cargar_distancias(nombre_archivo):
    distancias = []

    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            # Buscar la distancia euclidiana en el formato 'Distancia euclidiana: X'
            match = re.search(r"Distancia euclidiana: ([\d.]+)", linea)
            if match:
                distancias.append(float(match.group(1)))
    
    return distancias

# Cargar las distancias euclidianas desde el archivo
archivo = "ResulBusqueda.txt"
distancias = cargar_distancias(archivo)

# Crear la gráfica solo con las distancias euclidianas
if len(distancias) > 0:
    # Crear figura
    plt.figure(figsize=(10, 5))
    plt.plot(range(len(distancias)), distancias, 'ro-', label='Distancia Euclidiana')  # Rojo
    plt.xlabel("Número de consulta")
    plt.ylabel("Distancia Euclidiana")
    plt.title("Distancia Euclidiana de las Búsquedas")
    plt.legend()
    plt.grid(True)
    plt.show()
