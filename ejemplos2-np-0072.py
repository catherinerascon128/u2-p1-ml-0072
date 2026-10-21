import numpy as np

print("------llenar matriz de ceros-----")
matriz = np.zeros([6,7]) # 3 seis filas con 7 columnas
print(matriz)

print("-------llenar matriz de unos-----")
matriz = np.ones([6,7])
print(matriz)

print("-------llenar matriz vacios-----")
matriz = np.empty([6,7])
print(matriz)

print("-------llenar listas con rango-----")
# el primer parametro es el valor inicial
# el segundo parametro es el valor final
# el tercer parametro es el incremento
listas = np.arange(0,10,2)
print(listas)

print("-------llenar listas con rango No 2-----")
listas = np.arange(0,10,2)
print(listas)
