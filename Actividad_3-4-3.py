
num = input("Ingrese una lista de núymeros separados por espacios ")
lista_de_num = (num.split())

print(lista_de_num)
try:
    x = [int(lista_de_num)]
except ValueError:
    print ("Debe ingresar un valor númerico")
