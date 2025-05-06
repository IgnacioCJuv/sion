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

def es_mayor_a_5(digito: int) -> bool:
    if digito >= 5:
        return True
    else:
        return False
    
def procesar_codigo(numero: int):
    digito: int
    cont_may: int
    cont_men: int
    
    cont_may = 0
    cont_men = 0
    while numero > 0:
        digito = numero % 10
        if es_mayor_a_5(digito):
            cont_may = cont_may + 1
        else: 
            cont_men = cont_men + 1 
        numero = numero // 10
    print("Alta señal: ", cont_may)
    print("Baja señal: ", cont_men)
  
  
    
    
# Prog Prin
num: int
num = leer_numero_valido()
procesar_codigo(num)