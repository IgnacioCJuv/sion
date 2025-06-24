def leer_texto()->  str:
    noValido: bool
    cadena : str
    
    noValido = True
    while noValido:
            cadena = input("Ingrese el mensaje: ")
            if len(cadena) > 0 and cadena.replace(" ", "").strip().isalpha():
                noValido = False
            else:
                print("Error. Dato incorrecto")
           
    return cadena.strip()  

def procesar_mensaje(cadena: str):
    palabra = 0
    for p in range(len(cadena.split())- 1):
        if cadena[0]== cadena[len(cadena[p])- 1]:
            palabra += 1
    print(f"Palabras simetricas {palabra}")

#Prog Prin
frase: str 
frase = leer_texto()
procesar_mensaje(frase)      
