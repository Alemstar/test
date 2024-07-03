lista = []

def registrar_trabajador (nombre, cargo, sueldo_bruto):
    dcto_salud = int(sueldo_bruto*0.07)
    dcto_afp = int(sueldo_bruto*0.12)
    sueldo_liq = sueldo_bruto-dcto_salud-dcto_afp
    lista.append ([nombre, cargo, sueldo_bruto, dcto_salud, dcto_afp, sueldo_liq])

def lista_trabajadores():
    with open ('lista_trabajadores.txt', 'w', newline='') as lista_trabajadores:
        lista_trabajadores.write("nombre / cargo / sueldo bruto / descuento salud / descuento afp /sueldo líquido  \n")
        for trabajador in lista:
            lista_trabajadores.write(f"{trabajador} \n")
    archivo = open ('lista_trabajadores.txt', 'r')
    contenido = archivo.read()
    print (contenido)
    archivo.close



while True:
    option = int(input("Elija una opción: \n 1) Registrar trabajador  \n 2) Listar todos los trabajadores  \n 3) Imprimir planilla de sueldos  \n 4) Salir del programa \n"))
    if option == 1:
        nombre = input("Ingrese el nombre del trabajador: ")
        cargo = input("Ingrese su cargo: ")
        sueldo_bruto = int(input("Ingrese su sueldo bruto: "))
        registrar_trabajador(nombre, cargo, sueldo_bruto)
    if option == 2:
        lista_trabajadores()