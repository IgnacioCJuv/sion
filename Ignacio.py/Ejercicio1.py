activado = True
while(activado):
    try:
        
        numero = int(input("Ingrese un numero multiplo de 7: "))
        if numero > 0:
            if (numero % 7 == 0):
                print("Numero valido.")
                activado = False
            else:
                print("Error, el numero ingresado no es multiplo de 7")
        else: 
            print("Error, ingrese un numero positivo.")        
    except:
            print("Error inesperado en el sistema")    