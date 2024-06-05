nombres = []
apellidos = []

for i in range (3):
    nombre = input ("Ingrese un nombre ")
    nombres.append(nombre)
for x in range (3):
    apellido = input ("Ingrese el apellido ")
    apellidos.append(apellido)

for j in range(3):
    print(nombres[j], apellidos[j])