from modulos import saludos
print(saludos.saludar("Carlos"))
print(saludos.despedir("Pepe"))

def precio_final(precio:float , descuento: int)->float:
    desc = descuento / 100
    resultado = precio - (precio * desc)
    return resultado

print(precio_final(100,20))
