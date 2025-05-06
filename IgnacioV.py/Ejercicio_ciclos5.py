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
             print("Error. Numero invalido!")               
        except:
            print("Error. No es valido!")          
    return numero

def procesar_numero(numero: int):
    digito: int
    r: int
    dec: int
    umi: int
    suma: int
    suma = 0   
    
    while numero > 0:
        digito = numero % 10
        r = digito % 2
        if r == 0:
            digito = digito * 3
        else:
            digito = digito + 1
        if digito > 9:    
            dec = digito // 10
            uni = digito % 10
            digito = dec + uni
        suma = suma + digito
        numero = numero // 10
    r = suma % 7
    if r == 0:
        print("Valido")
    else:
        print("Invalido")                
        
              
# Prog Prin
num: int
num = leer_numero_valido()
procesar_numero(num)