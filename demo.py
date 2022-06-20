from operator import le

# Definicion de dicionario 
diccionario = {}

diccionario["t"] = 0
diccionario["a"] = 1
diccionario["e"] = 2
diccionario["i"] = 3
diccionario["o"] = 4
diccionario["u"] = 5
diccionario["n"] = 6
diccionario["s"] = 7
diccionario["b"] = 8
diccionario["r"] = 9

# invertir diccionario para desencriptar
diccionario_reversado = dict(map(reversed, diccionario.items()))
keys_values = diccionario_reversado.items()
diccionario_reversado = {str(key): str(value) for key, value in keys_values}

# Impresion de Menu
print("Que Operacion desea realizar:")
print("1: Encriptar")
print("2: Desencriptar")
seleccion = input('Operacion: ')


if seleccion == str(1) or seleccion == str(2):
    data = input('Ingrese el mensaje: ')

    # Vamos a encriptar
    if seleccion == str(1):

        mensaje_encriptado = ""

        for element in data:
            if element in diccionario:
                mensaje_encriptado = mensaje_encriptado + str(diccionario[element])
            else:
                mensaje_encriptado = mensaje_encriptado + element
        
        print(mensaje_encriptado)

    # Vamos a desencriptar
    if seleccion == str(2):
        mensaje_desenciptado = ""
        for element in data:
                      
            if element in diccionario_reversado:
                mensaje_desenciptado = mensaje_desenciptado + str(diccionario_reversado[element])
            else:
                mensaje_desenciptado = mensaje_desenciptado + element

        print(mensaje_desenciptado)

else:
    print("Comando no reconocido")


