myStr = "hello world julian"
myStr1 = "hello.world.julian"
#print(dir(myStr)) 

print(myStr.title()) # Convertir la primer letra de cada palabra en mayuscula
print(myStr.upper()) # Convertir texto en mayuscula
print(myStr.lower()) # Convertir texto en minuscula
print(myStr.swapcase()) # Convertir la primer letra en mayuscula o minuscula segun el caso
print(myStr.capitalize()) # Convertir la primer letra del texto en mayuscula
print(myStr.replace('hello', 'bye').upper()) #reemplazar una palbara / tambien se puede poner otro metodo
print(myStr.count('l'))  # Contar cuantas veces esta una letra en el texto
print(myStr.startswith('my')) # Saber si el texto empieza con una palabra... False o True (busca por caracteres)

if myStr.startswith('hola') == True:
    print('Si empieza')
else:
    print('no empieza')

print(myStr.endswith('world')) # Saber si el texto termina con una palabra... False o True (busca por caracteres)
print(myStr.split()) # Divide el texto y lo almacena en una lista (separa basado en un espacio)
print(myStr1.split('.')) # Divide el texto a partir de una coma (separa basado en una coma)
print(myStr.find('o')) # Me devuelve la posicion de la letra
print(len(myStr)) # Cuenta los caracteres del texto (longitud)
print(myStr.index('o')) # Saber el indice de la letra(posicion)
print(myStr.isnumeric())
print(myStr.isalpha()) # Saber si las letras de la palabra o frase estan dentro del alfabeto
print(myStr[4])
print(myStr[-1])
print("")
print(" Concatenacion")
s = "Julian"
print("My name is "+s)
print(f"My name is {s}")
print("My name is {0}".format(s))