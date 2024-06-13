pares = []
impares = []
def valida_numeros (list):
        for num in list:
            try:
                int(num)
            except:
                 print ("Ingresó valor no valido")
                 return "No valido"
            return ("Valido")

validador = "No valido"
while validador == "No valido":
     nums = input("Ingresa una lista de números separados por espacio ")
     nums_list = nums.split()

     validador = valida_numeros(nums_list)
     print ("moshi")

def par_o_impar(nums_list):
    for num in nums_list:
        numero=int(num)
        numero = numero%2
        if numero == 0:
            pares.append(num)
        else:
            impares.append(num)

par_o_impar(nums_list)
print ("Los números pares son: ", pares)
print ("Los números impares son: ", impares)
