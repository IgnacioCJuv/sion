def leer_texto()->  str:
    noValido: bool
    cadena : str
    
    noValido = True
    while noValido:
            cadena = input("Ingrese una cadena: ")
            if len(cadena) > 0 and cadena.replace(" ", "").strip().isalpha():
                noValido = False
            else:
                print("Error. Dato incorrecto")
           
    return cadena.strip()   

def procesar(cadena: str):
    palabras: list
    palabra: str
#>>    nueva_palabra : str
    
#>>    nueva_palabra = ""
# Metodo facil que solo funciona en phyton: <<
    palabras = cadena.split() 
    for palabra in palabras:
        print(palabra[0], end = "") #<<
        
        
        
# Metodo dificil: >>
# >>       nueva_palabra = nueva_palabra + palabra [0]
# >>   print(nueva_palabra)      





#Prog Prin
frase: str 
frase = leer_texto()
procesar(frase)      



#texto0 = "" 
#texto1 = "Esta es una prueba de un texto correcto"
#texto2 = "Esta es una prueba con numeros 1234"
#texto3 = "Esta es otra prueba con simbolos //((&/&()))"
#texto4 = "Esta es otra prueba con //((&/&())) y 98696897"

#print(texto1.replace(" ", "").isalpha())
#print(texto1)


#texto1 = texto1.replace(" ", "")
#print(texto1)
#print(texto1.isalpha())


#print(texto1.isalpha())


# if len(cadena) > 0 and cadena.isalum() and cadena.isnumeric()
#                           .isalum es para letras y numeros
