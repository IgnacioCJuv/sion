#FUNCIONES#

def contar_leds(numero):
    total_leds = 0
    while (numero > 0):
        unidad = numero % 10
        if(unidad == 1): 
            total_leds += 2
        elif(unidad == 2 or unidad == 3 or unidad == 5):
            total_leds += 5
        elif(unidad == 4):
            total_leds +=4     
        elif(unidad == 6 or unidad == 9 or unidad == 0):
            total_leds += 6
        elif(unidad == 7):
            total_leds += 3   
        elif(unidad == 8): 
            total_leds +=7
        numero = numero // 10
    return total_leds
                  

#MAIN#

encendido = True
while(encendido == True):
    try:
        print("INGRESE UN NÚMERO ENTERO POSITIVO: ")   
        numero= int(input())
        if numero > 0:
            encendido = False
            total_leds = contar_leds(numero)
            print(f"EL TOTAL DE LEDS DEL NUMERO: {numero} es {total_leds},")
        else:
            print("ERROR, EL NÚMERO DEBE SER ENTERO.")   
    except: 
        print("ERROR EN EL SISTEMA.")