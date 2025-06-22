import pandas as pd

# Rafael Ernesto Morales Díaz
# 20202001873
# TAREA 1.2 IA

# EJERCICIO 1
df_ventas = pd.read_csv("ventas.csv")

print(df_ventas.head())



df_productos_por_categoria = df_ventas.groupby("Producto")["Cantidad"].sum().reset_index()

print("Cantidad total de productos vendidos por categoría:")
print(df_productos_por_categoria)


#EJERCICIO 2


clima = pd.read_csv('clima.csv')

print(clima.head())

temperatura_promedio = clima.groupby('Ciudad')['Temperatura'].mean()

print("Temperatura promedio de cada ciudad :",temperatura_promedio)

temperatura_alta = clima.loc[clima['Temperatura'].idxmax()]
temperatura_baja = clima.loc[clima['Temperatura'].idxmin()]

print("Temperatura mas alta registrada del dataset:", temperatura_alta)
print("Temperatura mas baja registrada del dataset:", temperatura_baja)


ciudad_mas_alta = temperatura_alta['Ciudad']
ciudad_mas_baja = temperatura_baja['Ciudad']

print(f"Ciudad con temperatura mas alta registrada del dataset: {ciudad_mas_alta}")
print(f"Ciudad con temperatura mas baja registrada del  dataset: {ciudad_mas_baja}")

calor_mayor_30= clima[clima['Temperatura'] > 30]

print(f"Cantidad  de veces con temperatura mayor 30°C registrados: {len(calor_mayor_30)}")

dias_por_ciudad = clima['Ciudad'].value_counts()

print(dias_por_ciudad)



