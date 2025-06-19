def leer_numero()-> int:
    noValido = bool
    numero : int
    
    noValido = True
    while noValido:
        try:
            numero = int(input("Ingrese un numero entero positivo mayor a 0: "))
            if numero > 0:
                noValido = False
            else:
                print("Error. Numero Invalido")
        except:
            print("Error. Dato incorrecto")
    return numero 

def dibujar_trian_rec(n: int): 
    for i in range (1, n, 2):
        linea = ""
        for k in range (i, 0, -2):
            linea = linea + str (k) + " "
        print (linea)
        
        
h: int
h = leer_numero()
dibujar_trian_rec(h)              
