print("-----------------\n")
print("     ARREGLO - Numpy\n")
print("------------------\n")
print("")

import numpy as np
lista44 = [25,12,15,66,12.5]
vector = np.array(lista44)

print("- vector original")
print(vector)

print("- sumarle 1 a cada elemento del vector:")
print(vector+1)
print("- multiplicar por 5 cada elemento del vector:")
print(vector*5)

print("- suma de los elementos:")
print(np.sum(vector))

print("- promedio (media) de los elementos:")
print(np.mean(vector))

print("- el vector sumado a si mismo:")
print(vector+vector)
print("- suma de vectores vector1 y vector2 (mismo tamaño):")
vector2 = np.array([11,55,1.2,7.4,-8])
print(vector , " + " , vector2)
print(vector+vector2)