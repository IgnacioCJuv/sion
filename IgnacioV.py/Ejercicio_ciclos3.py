def leer_numero_valido()-> int:
    noValido = bool
    numero: int
     
    noValido = True
    while noValido:
        try:      
            numero = int(input("ingresar un numero a validar:"))          
            if numero > 9:               
                noValido = False 
            else:
             print("Error. Numero incorrecto!")               
        except:
            print("Error. No es un numero!")          
    return numero

def procesar_numero(numero: int):
    digito: int
    cont: int
    r: int   
    cont = 0
    suma = 0
    while numero > 0:
        digito = numero % 10
        cont = cont + 1
        r = cont % 2 # binarios
        if r == 0 : # sin necesidad de retorno
            digito = digito * 2
            if digito > 9:
                digito = digito - 9
        suma = suma + digito    
        numero = numero // 10
    r = suma % 10
    if r == 0:
        print("#Es")
    else:
        print("No es")
        
        print(digito)    
    print(suma)    



# Prog Prin
num: int
num = leer_numero_valido()
procesar_numero(num)