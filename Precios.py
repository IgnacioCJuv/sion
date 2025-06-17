listaCompras = ['manzanas', 'mangos', 'peras', 'platanos']

print(f"Debo comprar los siguientes {len(listaCompras)} elementos:")

for item in listaCompras:
    print(f"*{item}")
print("Pero además, debo comprar limones.")
listaCompras.append('limones')
print("Ahora mi lista de compras ordenada alfabéticamente es:")
listaCompras.sort()

for item in listaCompras:
    print(f"*{item}")
    
print("Ahora lo primero que tengo que comprar es", listaCompras[0])

elementoComprado = listaCompras[0]
listaCompras.pop(0)
print(f"Ya compre {elementoComprado}")

print("Ahora mi lista de compras es")
for item in listaCompras:
    print(f"*{item}")
