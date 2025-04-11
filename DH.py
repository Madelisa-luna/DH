# Importaciones
import numpy as np
from sympy import symbols, cos, sin, Matrix, simplify, pi, N, Symbol
from tabulate import tabulate
import itertools
from tqdm import tqdm

print("----------------------------------------------------")
print("--             Informacion para tabla DH          --")
print("----------------------------------------------------")

# Solicitar el número de eslabones
while True:
    try:
        num_filas = int(input("Ingrese el numero de eslabones(filas): "))
        if num_filas > 0:
            break
        else:
            print("Por favor, ingresa un numero entero positivo y mayor a 0.")
    except ValueError:
        print("Error: ingresa un numero entero positivo")

# Matrices
columnas = ["Eslabon", "bi", "theta_i", "ai", "alpha_i"]
tabla = []
tab_matrices = []
variables = {}

# Pedimos los datos para las filas del eslabon
for i in range(1, num_filas + 1):
    print(f"\nIngrese los valores para el eslabon {i}: ")
    fila = [i]
    for j in range(1, 5):
        valor = input(f"Ingrese el valor para la columna {columnas[j]} (numero o variable): ").strip()
        try:
            if j in [2, 4]:
                valor = float(valor) * (pi / 180)
            else:
                valor = float(valor)
        except ValueError:
            valor = symbols(valor)
            variables[valor] = (None, j in [2, 4])  # (valor, es_angular)
        fila.append(valor)
    tabla.append(fila)

# Mostrar la tabla
print("\nTabla de DH: ")
print(tabulate(tabla, headers=columnas, tablefmt="grid"))

def imprimir_matriz(matriz):
    filas = [[str(valor) for valor in fila] for fila in matriz.tolist()]
    print(tabulate(filas, tablefmt="grid"))

# Crear matrices de transformación
print("----------------------------------------------")
print("--   Matriz de transformación de DH T_i     --")
print("----------------------------------------------")

for fila in tabla:
    eslabon, b_i, theta_i, a_i, alpha_i = fila

    try:
        T_i = Matrix([
            [cos(theta_i), -sin(theta_i)*cos(alpha_i), sin(theta_i)*sin(alpha_i), a_i*cos(theta_i)],
            [sin(theta_i),  cos(theta_i)*cos(alpha_i),-cos(theta_i)*sin(alpha_i), a_i*sin(theta_i)],
            [0,             sin(alpha_i),               cos(alpha_i),              b_i],
            [0,             0,                          0,                         1]
        ])
        tab_matrices.append(T_i)
        print(f"\nMatriz T_{eslabon}: ")
        imprimir_matriz(T_i)
    except Exception as e:
        print(f"Error al crear la matriz T_{eslabon}: {e}")

# Multiplicación de matrices
if tab_matrices:
    print("\nMultiplicación de matrices")
    matriz_res = tab_matrices[0]

    for i in range(1, len(tab_matrices)):
        print(f"\nMultiplicando T_{i} con T_{i+1}...")
        matriz_res = simplify(matriz_res * tab_matrices[i])
        print("\nResultado parcial")
        imprimir_matriz(matriz_res)
        continuar = input("¿Desea continuar con la multiplicación? (s/n): ").strip().lower()
        if continuar != 's':
            print("Multiplicación detenida.")
            break

# Extraer rotación y traslación
matriz_Q = matriz_res[:3, :3]
matriz_Vec = matriz_res[0:3, 3]

print("Matriz de rotación")
imprimir_matriz(matriz_Q)

print("Matriz de traslación")
imprimir_matriz(matriz_Vec)

# Configurar archivo de salida
archivo_salida = "Ejemplo5-19.txt"
with open(archivo_salida, "w") as archivo:
    archivo.write("Evaluación del vector de traslación\n\n")
    archivo.write(f"Vector de traslación simbólico: \n{matriz_Vec}\n\n")

    # Recolección de rangos
    rango_variables = []
    variables_variables = []

    for var in variables:
        valor, es_angular = variables[var]
        tipo = input(f"¿La variable '{var}' es constante o variable? (c/v): ").strip().lower()
        if tipo == 'c':
            val = float(input(f"Ingresa el valor para la constante '{var}': "))
            if es_angular:
                val *= pi / 180
            variables[var] = (val, es_angular)
        else:
            ini = float(input(f"Desde qué valor inicia '{var}': "))
            fin = float(input(f"Hasta qué valor termina '{var}': "))
            paso = float(input(f"¿De cuánto en cuánto deseas el paso para '{var}'?: "))
            if es_angular:
                rango = list(np.arange(ini, fin + paso, paso))  # en grados
            else:
                rango = list(np.arange(ini, fin + paso, paso))
            rango_variables.append(rango)
            variables_variables.append(var)

    # Crear combinaciones
    combinaciones = list(itertools.product(*rango_variables))

    for combinacion in tqdm(combinaciones, desc="Generando archivo", unit="iteración"):
        sustituciones = {}

        # Asignar variables variables
        for i, var in enumerate(variables_variables):
            valor_combinacion = combinacion[i]
            es_angular = variables[var][1]
            if es_angular:
                valor_combinacion = valor_combinacion * (pi / 180)
            sustituciones[var] = valor_combinacion

        # Asignar constantes
        for var, (valor, _) in variables.items():
            if valor is not None:
                sustituciones[var] = valor

        # Evaluar vector
        evaluacion = matriz_Vec.subs(sustituciones)
        evaluacion = evaluacion.applyfunc(lambda x: N(x, 6) if x.is_number else x)
        x, y, z = evaluacion[0], evaluacion[1], evaluacion[2]

        # Mostrar variables en texto
        combinacion_mostrada = []
        for i, var in enumerate(variables_variables):
            original = combinacion[i]
            combinacion_mostrada.append(f"{original}")

        archivo.write(f"{combinacion_mostrada}")
        archivo.write(f"x = {x}, y = {y}, z = {z}\n")

print(f"\n Los resultados se han guardado en '{archivo_salida}' correctamente.")
