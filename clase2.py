contrasena = "mimamememima"
longitud_maxima = 20
longitud_minima = 8

if len(contrasena) < longitud_minima:
    print("Muy corta")
elif len(contrasena) > longitud_maxima:
    print("Muy larga")
else:
    print("aceptada")

# Convierte la lista numeros en un set llamado unicos y muestra cuántos números distintos hay.
numeros = [1, 2, 2, 3, 3, 3, 4]
unicos = set(numeros)
print(len(unicos))

# Con if/elif/else clasifica el vehículo y muestra el resultado:
# · Camión de más de 5000 kg → Vehículo pesado
# · Coche de más de 2000 kg → Vehículo pesadito
# · Coche entre 1000 y 2000 kg (incluidos) → Vehículo mediano
# · En cualquier otro caso → Vehículo ligero
tipo = "Coche"
peso = 1500

if tipo and peso >= 2000:
    print("Vehiculo pesadito")
elif tipo and peso > 5000:
    print("Vehiculo pesado")
elif tipo and peso >= 1000 and peso <= 2000:
    print("Vehiculo mediano")
else:
    print("Vehiculo ligero")

colores = ["rojo", "verde", "azul", "amarillo"]
for color in colores:
    print(color)
# Usando un bucle for (sin sum()), guarda en total la suma de todos los números de la lista.
numeros = [4, 8, 15, 16, 23, 42]
total = 0
for suma in numeros:
    total += suma

# Recorre gente con un for y crea la lista cortos con los nombres que tienen exactamente 4 letras.
gente = [
    {"nombre": "Jamiro", "edad": 45},
    {"nombre": "Juan", "edad": 35},
    {"nombre": "Paco", "edad": 34},
    {"nombre": "Pepe", "edad": 14},
    {"nombre": "Pilar", "edad": 24},
    {"nombre": "Laura", "edad": 24},
    {"nombre": "Jenny", "edad": 10},
]
cortos = []
for persona in gente:
    nombre = persona["nombre"]
    if len(nombre) == 4:
        cortos.append(persona)

# Recorre numeros con un for e imprime cada elemento multiplicado por factor, uno por línea. No necesitas una función.
factor = 3
numeros = [2, 5, -1, 0]
for multiplicacion in numeros:
    multiplicacion *= factor
    print(multiplicacion)

# Cuenta del 7 al 11 usando el bucle while:
cuenta = 7
while cuenta < 12:
    print(cuenta)
    cuenta += 1


# Con un bucle while, muestra los números del 5 al 1 (uno por línea) y al final ¡Despegue!
contador = 5
while contador > 0:
    print(contador)
    contador -=1


# Recorre frase usando un índice y un while con len(frase). 
# En cada vuelta imprime Índice: {i}, Letra: {frase[i]}. 
# Si el carácter es un espacio, imprime además ¡Espacio encontrado! en otra línea.
frase = "Python es divertido"
i = 0
while len(frase) > i:
    if frase[i] == " ":
        print("¡Espacio encontrado!")
    else: 
        print(f"Indice: {i}, Letra: {frase[i]}")
    i += 1


# Con bucles while, muestra este patrón (sin líneas en blanco):
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# Pista: puedes ir construyendo cada línea en un texto con f-strings.
print("_____________")
contador = 5
while  contador > 0:
    inner = contador
    txt = ""
    while inner > 0:
        txt += f"{inner}"
        inner -= 1
    print(txt)
    contador -= 1

# Muestra por consola el nombre de cada producto usando el bucle for.
# Muestra por consola el nombre de los primeros 3 productos usando el bucle while.
# Muestra por consola el nombre de cada producto cuyo precio es mayor a 100.
# Muestra por consola el nombre de los productos cuyo stock es menor o igual a 25
productos = [
    {"nombre": "Laptop", "categoria": "Electrónica", "precio": 799.99, "stock": 25},
    {"nombre": "Auriculares Bluetooth", "categoria": "Accesorios", "precio": 59.99, "stock": 50},
    {"nombre": "Cámara Digital", "categoria": "Fotografía", "precio": 399.99, "stock": 10},
    {"nombre": "Smartwatch", "categoria": "Relojes", "precio": 149.99, "stock": 75},
    {"nombre": "Teclado Mecánico", "categoria": "Accesorios", "precio": 89.99, "stock": 30}
]
for producto in productos:
    print(producto["nombre"])

contador=0
while len(productos) < 3:
    print(productos["nombre"])
    contador += 1

for producto in productos:
    if producto["precio"] <= 100:
        print(producto["nombre"])

for porducto in productos:
    if producto["stock"] <= 25:
        print(producto["nombre"])

# Con un índice y un while, suma los valores de numeros en total. 
# Imprime cada valor que sumas. Cuando total sea mayor que 100, imprime Límite superado y no proceses más elementos. 
# Si se acaba la lista antes, termina sin ese mensaje. Puedes controlar ambas condiciones en el while; no necesitas break.
numeros = [40, 35, 25, 1, 50]
total = 0
i = 0

while i < len(numeros) and total <= 100:
    total += numeros[i]
    print(numeros[i])
    i += 1
if total >= 100:
    print("Limite superado")
        

# Crea una función saludar que reciba por parámetro el nombre de una persona y devuelva “Hola” y ese nombre.
# Por ejemplo, si ejecutas print(saludar(“Sofía”) la función debe devolver: “Hola Sofía”
def saludar(nombre):
    #print("hola " + nombre)
    return "Hola" + nombre
resultado = saludar("Carlos")
print(resultado)


def calcular_promedio(numeros):
    total = 0
    for numero in numeros:
        total += numero
    division = total / len(numeros)
    return division

print(calcular_promedio([1,2,4,5,6,7,8]))


# Crea una función llamada cuentaCaracteres que reciba un parámetro de tipo string y devuelva el numero de caracteres que tiene. 
# Si el parámetro recibido no es un texto (str), la función debe devolver el mensaje: 'Debo ser ejecutada con un string'
def cuentaCaracteres(palabra):
    if not isinstance(palabra, str):
        respuesta = print("Necesito un str")
        return respuesta
    else:
        print(len(palabra))
    
cuentaCaracteres("Hola buenas")
cuentaCaracteres(4)

# Crea la función comparar(a, b) que devuelva Son iguales, El primero es mayor o El segundo es mayor.
def comparar(a: int,b: int):
    if a == b:
        print("son iguales")
    elif a > b:
        print("El primero es mayor")
    else:
        print("El segundo es mayor")


# Crea la función contar_letra(texto, letra) que devuelva cuántas veces aparece letra en texto, sin distinguir mayúsculas de minúsculas. Usa un bucle.
def contar_letra(texto, letra):
    contador = 0
    texto_l = texto.lower()
    letra_l = letra.lower()

    for c in texto_l:
        if c == letra_l:
            contador += 1

    return contador

contar_letra("pepe tiene ppeperoni", "p")
print("----------")


def dia_semana(numero):
    match numero:
        case 1:
            print("Lunes")
        case 2:
            print("Martes")
        case 3:
            print("Miércoles")
        case 4:
            print("Jueves")
        case 5:
            print("Viernes")
        case 6:
            print("Sábado")
        case 7:
            print("Domingo")
        case _:
            print("Dia no valido")


# Define cuenta_atras(n) para un entero positivo. Con un while, imprime desde n hasta 1, uno por línea. 
# Si el número es divisible por 4, imprime "Pum!" en su lugar. 
# Al terminar imprime "¡Despegue!". Después llama a cuenta_atras(8) una sola vez.
def cuenta_atras(n):
    while n > 0:
        es_divisible = n % 4 == 0
        
        if es_divisible:
            print("pum!")
        else: 
            print(n)
        n -= 1
    print("despegue")

cuenta_atras(8)
    

# Define venta_online(pedido, fecha_entrega, incidencia=False). Si incidencia es True, devuelve "Contacte con Att. Cliente". Si es False, devuelve Su pedido {pedido} se entregará el {fecha_entrega}. Utiliza el valor por defecto para permitir llamadas con solo dos argumentos.
def venta_online(pedido, fecha_entrega, incidencia=False):
    if incidencia == True:
        print("Contacte con att cliente")
    elif incidencia:
        print(f"su {pedido} se entregara el {fecha_entrega}")


fed = lambda texto : texto[0]

print(fed("pepe"))