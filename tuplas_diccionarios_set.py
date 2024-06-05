nombres = []
for nombre in range(3):
    nombre = input ("Ingrese un nombre ")
    nombres.append(nombre)
    nombre_largo=max(nombres, key=len)
print(nombres)
print ("El nombre más largo es: ", nombre_largo)