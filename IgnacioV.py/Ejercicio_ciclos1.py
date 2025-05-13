def leer_numero_valido()-> int:
    noValido = bool
    numero: int
     
    noValido = True
    while noValido:
        try:      
            numero = int(input("ingresar un numero entero positivo mayor que cero:"))          
            if numero > 0:               
                noValido = False 
            else:
             print("Error. Numero incorrecto!")               
        except:
            print("Error. No es un numero!")
            
    return numero 

def es_par(numero: int)-> bool: 
    resto: intresto = numero % 2       
    if resto == 0:
        return True
    else:
        return False
                
def procesar_numero(numero: int):       
    digito: int     
    suma_par: int     
    suma_impar: int    
    suma_par = 0    
    suma_impar = 0
            
    while numero > 0:
        digito = numero % 10        
        if es_par(digito):          
            suma_par = suma_par + digito
        else:
                        
         suma_impar = suma_impar + digito
                        
         numero = numero // 10
                    
print("Suma par:", suma_par)
            
print("Suma impar:", suma_impar)
            
#Pogo print
num: int
num = leer_numero_valido()
procesar_numero(num)

