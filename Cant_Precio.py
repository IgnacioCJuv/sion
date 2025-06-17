noValido = True
while noValido:
    try:
        cPrecios= int(input("Cantidad de precios: "))
        if cPrecios > 0:
            noValido = False
        else:
            print("Cantidad fuera de rango")
    except:
        print("Entrada no valida")
precios = []
for indice in range(cPrecios):
    noValido = True
while noValido:
    try:
        precio = int(input(f"Ingrese precio {indice}:"))
        if precio > 0:
            precios.append(precio)
            noValido = False
        else:
            print("Precio fuera de rango")
    except:
        print("Entrada no valida")
precios.sort()
precioMenor = precios[0]
precioMayor = precios[len(precios)- 1]
print("Precio mayor:", precioMayor)
print("Precio menor:", precioMenor)
