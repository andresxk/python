# Definir funcion para cambiar nombre a capitalize
def nombre_propio():
    nombre = input("Ingrese su nombre: ")
    return nombre.isupper()

resultado = nombre_propio()
print(resultado)