import csv
lista = []
def registrar_trabajador (nombre_apellido,cargo,sueldo_bruto):
    desc_salud = 0.07*sueldo_bruto
    desc_afp = 0.12*sueldo_bruto
    sueldo_liquido = sueldo_bruto - desc_salud - desc_afp
    lista.append([nombre_apellido, cargo, sueldo_bruto, desc_salud, desc_afp, sueldo_liquido])
    return lista

def lista_trabajadores (nombre_apellido = '', cargo = '', sueldo_bruto = 0, desc_salud= 0, desc_afp = 0, sueldo_liquido = 0):
    with open ('registro.csv', 'r', newline='') as archivo_csv:
        reader = csv.reader(archivo_csv)
        for fila in reader:
            if (fila[0] == nombre_apellido and fila [1] == cargo and fila [2] == sueldo_bruto): #and fila [3] == desc_salud and fila [4] == desc_afp and fila [5] == sueldo_liquido):
                return 'Datos del trabajador: ' + fila [0], fila [1], fila [2], fila [3]#, fila [4], fila [5]
        return 'Sin datos'
    
datos = []

while True:
    option = int(input("Elija una opción: \n 1) Registrar trabajador \n 2) Listar a todos los trabajadores \n 3) Imprimir planilla de sueldos \n 4) Salir del programa \n"))
    if option == 1:
        nombre_apellido = input("Ingrese nombre y apellido: ")
        cargo = input ("Ingrese su cargo: ")
        sueldo_bruto = int(input("Ingrese su sueldo bruto: "))
        #datos = registrar_trabajador (datos, nombre_apellido=nombre_apellido, cargo=cargo, sueldo_bruto=sueldo_bruto, desc_salud=desc_salud, desc_afp = desc_afp sueldo_liquido = sueldo_liquido)
        #datos = registrar_trabajador (nombre_apellido, cargo, sueldo_bruto)
        #registrar_trabajador (nombre_apellido, cargo, sueldo_bruto)
        with open ('registro.csv', 'w', newline= '') as archivo_csv:
                writer = csv.writer(archivo_csv)
                writer.writerows(datos)
        print (datos)
    elif option == 2:
         print (lista)