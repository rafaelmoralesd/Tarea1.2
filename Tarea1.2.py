import pandas as pd

# Rafael Ernesto Morales Díaz
# 20202001873
# TAREA 1.2 IA

# EJERCICIO 1
df_ventas = pd.read_csv("ventas.csv")

print(df_ventas.head())


# Calcule la cantidad total de productos vendidos por categoría
df_productos_por_categoria = df_ventas.groupby("Producto")["Cantidad"].sum().reset_index()

print("Cantidad total de productos vendidos por categoría:")
print(df_productos_por_categoria)


#EJERCICIO 2



