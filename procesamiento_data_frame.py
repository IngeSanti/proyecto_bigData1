import pandas as pd
import numpy as np

df = pd.read_csv("carpeta/online_retail_II.csv")


#Datos faltantes:
#en porcentaje
datos_null = df.isnull().mean()*100

print(datos_null)

#para saber en que columna faltan y los suma
suma_datos_faltantes = df.isnull().sum()

print(suma_datos_faltantes)

#hallar moda
moda = df['Description'].mode()[0]
print(f"producto con mayor demanda: {moda}")

#imputar la moda en los datos faltantes
df["Description"] = df["Description"].fillna(moda)

df["Customer ID"] = df["Customer ID"].fillna(00000)

#verificar
nuevos_datos = df.isnull().mean()*100
print(nuevos_datos)

suma_datos_faltantes_2 = df.isnull().sum()
print(suma_datos_faltantes_2)

#guardar dataset con los cambios
#se crea un nuevo archivo no sobreescriber el original
df.to_csv("carpeta/online_retail_II_limpio.csv", index=False)


