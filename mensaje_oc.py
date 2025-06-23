def leer_texto(texto: str)->  int:
    noValido: bool
    txt : str
    
    noValido = True
    while noValido:
        try:
            txt = str(input("Ingrese el texto: "))
            if txt.split([0],[0]) == 0:
                txt.pop(0)
            else:
                noValido = False    
        except: print("Texto invalido")
    return txt 

   
def oculto(txt: list): 
    t: str       
    for t in range(len[txt]):                
                 
                 
