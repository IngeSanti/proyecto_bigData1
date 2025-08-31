import pandas as pd
import time

inicio = time.time()

df = pd.read_excel('carpeta/online_retail_II.xlsx', sheet_name=0)
df_dos = pd.read_excel('carpeta/online_retail_II.xlsx', sheet_name=1)

df_total = pd.concat([df, df_dos], ignore_index=True)

#Guardar como csv
df_total.to_csv('carpeta/online_retail_II.csv', index=False)


fin = time.time()

tiempo_transcurrido = fin - inicio
print(f"El tiempo de ejecución fue: {tiempo_transcurrido} segundos")


