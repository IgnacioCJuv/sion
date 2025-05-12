def multiplicar(numero_uno, numero_dos):
    resultado = numero_uno * numero_dos
    return resultado 
    
activado = True
while(activado):
    try:
        
        numero_uno = int(input("Ingrese el primer numero: "))
        numero_dos = int(input("Ingrese el segundo numero: "))
        activado = False
        resultado = multiplicar(numero_uno, numero_dos)
        print("El resultado es: ", resultado)
    except:
        print("Error de sistema. el valor sebe ser numerico")    
        
        