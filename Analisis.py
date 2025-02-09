import pandas as pd

# Especifica el archivo CSV a analizar (cámbialo por el que subiste a Zenodo)
csv_file = "circle.csv"

try:
    # Cargar el dataset
    df = pd.read_csv(csv_file)

    # Mostrar las primeras filas
    print("Primeras filas del dataset:")
    print(df.head())

    # Información general del dataset
    print("\nInformación del dataset:")
    print(df.info())

    # Estadísticas descriptivas
    print("\nEstadísticas descriptivas:")
    print(df.describe())

except FileNotFoundError:
    print(f"Error: No se encontró el archivo {csv_file}. Asegúrate de colocarlo en el mismo directorio.")
