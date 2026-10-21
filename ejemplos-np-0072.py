import numpy as np 

#lista 
califas = np.array([60,70,90])
print("-------------- ejemplo 1 --------------")
print(califas) # imprime las listas de califas
print(type(califas)) # nuestra el tipo de arreglo
print("-------------- ejemplo 0 dimensiones de un array --------------")
califas=np.array(60)
print(califas)
print("dimencion :",califas.ndim)
print("-------------- ejemplo 1 dimensiones de un array --------------")
califas = np.array([60,70,90])
print(califas)
print("dimencion :",califas.ndim)
print("-------------- ejemplo 2 dimensiones de un array --------------")
califas = np.array([
    [60,70,90]
    [50,80,98]
    ]) #un arreglo de dos dimenciones es como una tabla de excel
print(califas)
print("dimencion :",califas.ndim)