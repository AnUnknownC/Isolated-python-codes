#Daniel Esteban Sanchez, Daniel Alejandro Parra, Juan Esteban Hernandez, Jeronimo Alejandro Diaz
iva = 0.16
productos = {
    "Estufa" : 8000000,
    "Televisor": 18000000,
    "Nevera" : 37500000
}
productosIva = {
    "Estufa" : productos["Estufa"] + productos["Estufa"] * iva,
    "Televisor": productos["Televisor"] + productos["Televisor"] * iva,
    "Nevera" : productos["Nevera"] + productos["Nevera"] * iva
}

def existe(producto):
    return producto not in productos

def genFac(factura):
    nombre = input("Nombre del comprador: ")
    id = input("Numero de cedula: ")
    cIva = 0
    sIva = 0
    print(f"""
Factura de compra
{nombre}
{id}
    """)
    print("Items                Cantidad  ValorSinIVA  ValorConIVA")
    for i in factura:
        cIva += factura[i]*productos[i]
        sIva +=  factura[i]*int(productosIva[i])
        print(f"{i}                {factura[i]}  ${factura[i]*productos[i]}  ${factura[i]*int(productosIva[i])}")
    print(f"""
Valor sin IVA: {sIva}
Valor con IVA: {cIva}
""")

producto = ["", 0]
factura = {}
while True:
    print("Productos disponibles")
    for i in productos:
        print(i)
    while True:
        producto[0] = input("\n¿Que producto desea comprar?: ").lower().capitalize()
        if existe(producto[0]):
            print("Producto no disponible en estos momentos")
        else:
            break    
    producto[1] = int(input("\nCuantos desea: "))
    factura[producto[0]] = producto[1]
    producto = ["", 0]
    if input("¿Desea seguir comprando?(Si/No): ").lower() == "no":
        break
genFac(factura)