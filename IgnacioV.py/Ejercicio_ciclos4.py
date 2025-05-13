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
    r: int
    suma_par: int
    suma_impar: int  
    suma_total: int
     
    suma_par = 0
    suma_impar = 0
    while numero > 0: # mientras eso se cumpla * se cumplira
        digito = numero % 10 # *
        r = digito % 2 # sin necesidad de retorno
        if r == 0:
            suma_par = suma_par + digito
        else:
            suma_impar = suma_impar + digito
            
    suma_total = suma_par * 3 + suma_par
    r = suma_total %7
    if r == 0:
        print("Es valido")
    else:
        print("No es valido")
          
# Prog Prin
num: int
num = leer_numero_valido()
procesar_numero(num)
