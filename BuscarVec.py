import numpy as np
import re
import time
from tqdm import tqdm  # Importar tqdm

def cargar_vectores(nombre_archivo):
    """Cargar los vectores desde un archivo de texto.
    linea por linea para evitar consumo de memoria"""
    vectores =[]
    angulos_cm = []

    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:

            match_angulo_cm = re.search(r"\[\s*'([-?\d.]+)'\s*,\s*'([-?\d.]+)'\s*,\s*'([-?\d.]+)'\s*]", linea)

            match_vector = re.search(r"x\s*=\s*(-?\d+\.?\d*),\s*y\s*=\s*(-?\d+\.?\d*),\s*z\s*=\s*(-?\d+\.?\d*)", linea)
            
            if match_angulo_cm and match_vector:
                angulo = float(match_angulo_cm.group(1))
                centimetros = float(match_angulo_cm.group(2))
                valores_xyz = [float(match_vector.group(i)) for i in range(1, 4)]

                vectores.append(np.array(valores_xyz))
                angulos_cm.append((angulo, centimetros))

    return np.array(vectores), angulos_cm

def distancia_euclidiana(v1, v2):
    return np.linalg.norm(v1 - v2)

def buscar_vecino(vectores, vector_consulta):
    distancias = [distancia_euclidiana(vector_consulta, v) for v in vectores]
    indice_min = np.argmin(distancias)
    return indice_min, vectores[indice_min], distancias[indice_min]

#Nombre del archivo
archivo_datos = "Ejemplo5-19.txt"
archivo_consultas = "consultas.txt"

#Medir tiempo de busqueda
start_time = time.time()
#Cargar los vectores del archivo
vectores, angulos_cm = cargar_vectores(archivo_datos)

#Leer el archivo de consultas
vectores_consulta = []
with open(archivo_consultas, 'r') as archivo:
    for linea in archivo:
        valores = linea.strip().split(",")
        if len(valores) == 3:
            try:
                vector = np.array([float(val) for val in valores])
                vectores_consulta.append(vector)
            except ValueError:
                print(f"Error al procesar la linea: {linea.strip()}")

#Guardar los datos en el archivo sin sobreescribir lo anterior
with open("ResulBusqueda.txt", "a") as archivo_salida:
    archivo_salida.write("\n===== Nueva Búsqueda =====\n")
    start_time = time.time()  # Medir tiempo de ejecución

    # Usar tqdm para la barra de carga
    for vector_consulta in tqdm(vectores_consulta, desc="Procesando consultas", unit="consulta"):
        # Buscar el vecino más cercano
        indice, vecino, distancia = buscar_vecino(vectores, vector_consulta)
        
        # Guardar resultados en archivo
        archivo_salida.write(f"Vector consultado: {vector_consulta.tolist()}\n")
        archivo_salida.write(f"Vector cercano: {vecino.tolist()}\n")
        archivo_salida.write(f"Ángulos: {angulos_cm[indice]}\n")
        archivo_salida.write(f"Centímetros: {angulos_cm[indice][1]}\n")
        archivo_salida.write(f"Distancia euclidiana: {distancia:.4f}\n\n")

    end_time = time.time()  # Medir tiempo total de ejecución
    total_time = end_time - start_time
    archivo_salida.write(f"Tiempo de ejecución: {total_time:.5f} segundos\n")

print("Resultados guardados en el archivo ResulBusqueda.txt")
print(f"Tiempo de ejecución: {total_time:.5f} segundos")
