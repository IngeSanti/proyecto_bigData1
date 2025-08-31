import pandas as pd

df = pd.read_csv('carpeta/online_retail_II_limpio.csv')

print(df.head(10))
print(df.tail(10))

print(df.isnull().mean()*100)
print(df.isnull().sum())
print(df.info())

print(df.describe())