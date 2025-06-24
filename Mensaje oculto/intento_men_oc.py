def leer_texto()->  str:
    noValido: bool
    txt : str
    
    noValido = True
    while noValido:
        try:
            txt = str(input("Ingrese el texto: ").strip())
            if txt.replace(" ", "").isalpha():
                print("El valor es valido")
            else:
                print("El valor ingresado no esta permitido")
                   
        except: print("Error. Texto invalido")
    return txt
   
def oculto(txt: list): 
    txt: str
    mensaje_oculto =  ""       
    for t in range(len[txt[0]]):
        mensaje_oculto +=([t] [0])
    print (mensaje_oculto)
    
    
print(f"El mensaje oculto es")                
                 


#Prog Prin
txt: str
txt =  leer_texto() 
txt(oculto)              
