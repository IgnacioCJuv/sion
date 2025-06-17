def leer_precio(texto: str)-> int:
    num : int
    noValido : bool
    
    noValido = True
    while noValido:
        try:
            num = int(input(f"Ingrese {texto}: "))
            if num > 0:
                noValido = False
            else:
                print("Valor incorrecto.")
        except:
            print("Dato incorrecto.")
    return num 

def llenar(precios: list, cantidad: int):
    i: int
    precio: int
    for i in range(cantidad):
        precio = leer_precio(f"el precio del producto {i+1}")
        precios.append(precio)
    #print(precios)    
    precios.sort()
    print(f"El menor valor es {precios[0]}")
    #print(f"El menor valor es {min(precios)}") # se ordenan automaticamnete 
    #print(f"El mayor valor es {precios[cantidad-1]}")
    print(f"El mayor valor es {precios[len(precios)-1]}") # si no se sabe la cantidad de precios, len(lista)-1 es siempre la ultima posicion
    #print(f"El mayor valor es {max(precios)}") # se ordenan automaticamnete 
    #print(precios) 
    
    
    
       

#Prog Prin
cantidad: int
lista_precios: list

lista_precios = []
cantidad = leer_precio("la cantidad de precios")
llenar(lista_precios, cantidad)
