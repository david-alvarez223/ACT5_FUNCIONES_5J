print("Manejo de funciones")
def hola():
    print("Alguien uso la funcion hola")
def chat(mensa):
    print(mensa)
def escribeNC(nombre,apellido):
    print(nombre,apellido)
    print(f"tu nombre completo es: {nombre} {apellido}")
def suma2numeros(n1, n2):
    s=n1+n2
    return f"la suma de {n1} y {n2} es de: {s} "
# llamando a la funcion
hola()
chat("que bonita estas")
chat("el profe me sorprendio enviando mensajes")
escribeNC("DAVID","ALVAREZ")
print("funciones que regresan valores")
print (suma2numeros(7,3))
print (suma2numeros(15,45))
