def leer_texto()-> str:
    return input("Ingrese la frase: ")

def contar(cadena: str):
    contVocal = contCons = contDig = contEsp = contSim = 0 
    for i in range(len(cadena)):
        caracter = cadena[i]
        if caracter.isdigit():
            contDig = contDig + 1
        elif caracter.isspace():
            contEsp = contEsp + 1
        elif caracter.isalpha():
            vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
            if caracter in vocales: 
                contVocal = contVocal + 1
            else:
                contCons = contCons + 1     
        else:
            contSim = contSim + 1
                      
    print(f"Vocales: {contVocal}\nConsonantes: {contCons}\nDigitos: {contDig}\nEspacios: {contEsp}\nSimbolos: {contSim}")
    

texto = leer_texto()
contar(texto)
