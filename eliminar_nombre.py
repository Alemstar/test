nombres = []

while True:
    x = input("Desea agregar un nombre? Si/No ")
    if x == "Si":
        nombre = input ("Ingrese un nombre ")
        nombres.append(nombre)
    if x == "No":
        break
dato = min(nombres, key=len)
nombres.remove(dato)
print(nombres)