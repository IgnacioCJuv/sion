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


def procesar_letras(cadena: str):
    letra: str
    letras: str
    otra: str
    veces: int
    unicas: list
    
    unicas = []
    letras = frase.replace(" ", "")
    for letra in letras:
        veces = 0
        for otra in letras:
            if letra == otra:
                veces = veces + 1
        if veces == 1:
            unicas.append(letra)        
                
    print(f"Letras unicas: {unicas}")
    
    
        


#Prog Prin
frase: str 
frase = leer_texto()
procesar_letras(frase)      
