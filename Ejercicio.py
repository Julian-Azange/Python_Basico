# Hacer una función que una vez se le pase una frase y una palabra cuente las letras de
# cada una de las palabras de la frase, excepto la palabra que se le paso, esto teniendo en
# cuenta lo siguiente:


def conteo_letras(frase: str, palabra: str):
    lista = [len(l) for l in frase.split() if l != palabra]
    return print(lista)


conteo_letras('el artista miente para mostrar la verdad, el político para ocultarla (V de Vendetta)','el')
conteo_letras('hago lo hago aunque no lo hago','hago')