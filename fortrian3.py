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

def dibujar_triangulo(altura: int):
    for i in range(altura):
        print("*" * i)
h: int
h = leer_numero
dibujar_triangulo(h)