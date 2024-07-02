import csv

def registrar_trabajador (lista, nombre_apellido = '', cargo = '', sueldo_bruto = 0):
    lista.append ([nombre_apellido, cargo, sueldo_bruto])
    return lista

def lista_trabajadores (nombre_apellido = '', cargo = '', sueldo_bruto = 0):
    with open ('registro.csv', 'r', newline='') as archivo_csv:
        reader = csv.reader(archivo_csv)
        for fila in reader:
            if (fila[0] == nombre_apellido and fila [1] == cargo and fila [2] == sueldo_bruto):
                return 'Datos del trabajador: ' + fila [0], fila [1], fila [2]
        return 'Sin datos'
    
datos = []

while True:
    option = int(input("Elija una opción: \n 1) Registrar trabajador \n 2) Listar a todos los trabajadores \n 3) Imprimir planilla de sueldos \n 4) Salir del programa \n"))
    if option == 1:
        nombre_apellido = input("Ingrese nombre y apellido: ")
        cargo = input ("Ingrese su cargo: ")
        sueldo_bruto = int(input("Ingrese su sueldo bruto: "))
        datos = registrar_trabajador (datos, nombre_apellido=nombre_apellido, cargo=cargo, sueldo_bruto=sueldo_bruto)
        with open ('registro.csv', 'w', newline= '') as archivo_csv:
                writer = csv.writer(archivo_csv)
                writer.writerow(datos)
    elif option == 2:
        lista_trabajadores()