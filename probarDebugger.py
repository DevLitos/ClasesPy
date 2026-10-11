def obtener_nombre_completo(nombre, apellido):
    return nombre + " " + apellido
def main():
    usuarios = [
        {"nombre": "Sofía"},
        {"nombre": "Luis", "apellido": "Martínez"},
    ]
    
    for usuario in usuarios:
        completo = obtener_nombre_completo(usuario["nombre"], usuario["apellido"])
        print(completo)
main()
