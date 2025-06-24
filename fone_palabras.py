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

def procesar_fonetica(cadena: str):
    cont_vocales: int
    cont_consonantes: int
    palabra:str
    palabras: list
    fonemas: list
    vocales: str
    fonema: int
    
   
    fonemas = []
    vocales = "aeiouAEIOU"
    palabras = cadena.split()
    for palabra in palabras:
        cont_vocales = cont_consonantes = 0
        for letra in palabra:
            if letra != "h":
                if letra in vocales:
                    cont_vocales = cont_vocales + 1
                else:
                    cont_consonantes = cont_consonantes + 1   
                    
                     
        fonema = cont_vocales * 5 + cont_consonantes* 2
        fonemas.append(f"{palabra}: {fonema}")
            
    print(f"La fonetica es: {fonemas}")
    
    
    #Prog Prin
frase: str 
frase = leer_texto()
procesar_fonetica(frase)  
