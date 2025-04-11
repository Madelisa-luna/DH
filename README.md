# Proyecto de Análisis de Vectores en Espacio DH

Este proyecto está enfocado en el análisis de vectores generados por el modelo de Denavit-Hartenberg (DH), que se utiliza para describir la cinemática de robots, y en la búsqueda eficiente del vector más cercano a partir de un conjunto de consultas. También se incluye visualización del espacio de trabajo y distancias euclidianas.

## 📄 Archivos del proyecto

- **DH.py**: Define el modelo de Denavit-Hartenberg y genera los vectores que representan posiciones del robot.
- **Ejemplo5-19.txt**: Archivo de datos generado por `DH.py`, contiene los ángulos y vectores en el espacio 3D.
- **BuscarVec.py**: Script principal que carga los vectores desde `Ejemplo5-19.txt` y busca los vecinos más cercanos para cada vector en `consultas.txt` usando distancia euclidiana. Los resultados se guardan en `ResulBusqueda.txt`.
- **consultas.txt**: Archivo con los vectores que se desean consultar.
- **ResulBusqueda.txt**: Archivo generado automáticamente por `BuscarVec.py` con todos los resultados y tiempos de ejecución.
- **EspacioTrabajo.py**: Script para graficar todos los vectores de `Ejemplo5-19.txt`, mostrando el espacio de trabajo del robot.
- **GraConsultas.py**: Grafica los vectores de consulta junto con los vecinos más cercanos encontrados.
- **GraEuclidiana.py**: Grafica la distancia euclidiana entre los vectores de consulta y sus respectivos vecinos cercanos.

## ⚙️ Cómo funciona

1. `DH.py` genera el archivo `Ejemplo5-19.txt` con datos en este formato:
   ```
   ['ángulo1', 'ángulo2', 'centimetros']x = valor, y = valor, z = valor
   ```

2. `BuscarVec.py`:
   - Carga esos vectores y los ángulos.
   - Lee los vectores de consulta desde `consultas.txt`.
   - Busca el vector más cercano usando distancia euclidiana.
   - Guarda los resultados en `ResulBusqueda.txt`.

3. `EspacioTrabajo.py`, `GraConsultas.py` y `GraEuclidiana.py` ayudan a visualizar:
   - El espacio de trabajo total del robot.
   - La relación entre las consultas y los resultados.
   - Las distancias entre vectores.

## 📈 Requisitos

- Python 3.12+

## 📦 Librerías utilizadas
🔢 NumPy
 - Uso: Operaciones vectoriales y cálculos matemáticos.

Instalación:
```bash
pip install numpy
```

📐 SymPy
 - Uso: Cálculo simbólico para matrices de Denavit-Hartenberg.
Instalación:
```bash
pip install sympy
```

📊 Matplotlib
 - Uso: Graficación de puntos y distancias.
Instalación:
```bash
pip install matplotlib
```

🧠 tqdm
 - Uso: Barra de progreso durante la búsqueda.
Instalación:
```bash
pip install tqdm
```

📋 Tabulate
 - Uso: Formato de tablas en consola.
Instalación:
```bash
pip install tabulate
```

🔁 itertools (incluida en la biblioteca estándar)
 - Uso: Combinaciones de datos.
Instalación:
No requiere instalación, es parte de la librería estándar de Python.

🧪 re (expresiones regulares)
 - Uso: Extracción de datos desde archivos de texto.
Instalación:
No requiere instalación, es parte de la librería estándar de Python.

⏱ time (control de ejecución)
 - Uso: Medición de tiempos de ejecución.
Instalación:
No requiere instalación, es parte de la librería estándar de Python.

## 🧠 Aplicación

Este sistema es útil para visualizar y comprender cómo se mueve un robot en el espacio según su configuración DH, y también para encontrar rápidamente puntos cercanos en entornos tridimensionales.
