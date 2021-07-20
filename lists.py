lista = [1, 2, True, 4, 5, ["hola", 1]]
colors = ['red', 'green', 'blue']

# Constructor
numlist = list((1,2,3,4))
print(numlist)

print("")
print(" Range")
r = list(range(1,10))
print(r)

print(lista[4]) # Buscar un elemento en la lista por posicion

print('green' in colors) # Saber si existe un elemento en la lista

print(colors)
colors[1] = 'yellow' # Cambiar un elemento por otro
print(colors)

colors.append('violet') # Agregar un elemento a la lista
colors.extend(['violet', 'yellow']) # Agregar varios elementos a la lista
colors.insert(1, 'black') # Insertar un elemento en la posicion deseada
colors.insert(len(colors), 'pink') # Insertar elemento al final
colors.pop() # Elimina el ultimo elemento
colors.remove('green') # Eliminar un elemento en especifico
colors.clear() # Limpiar la lista
print(colors)
colors.sort() # Ordenar lista A-Z
print(colors)
colors.sort(reverse=True) # Ordenar lista de la Z-A
print(colors.index('blue')) # Indice de un elemento de la lista
print(colors.count('blue')) # Contar elementos que se repiten en la lista


