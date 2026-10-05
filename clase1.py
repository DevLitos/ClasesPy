nombre: str = "Carlos"
apellido: str = "Gutierrez"

print(f"Soy {nombre} y mi apellido es {apellido}")

edad: int = 21
ciudad: str = "Valencia"
tengo_carnet: bool = True
print(f"{nombre.upper()} {apellido.lower()} {len(nombre)}, {apellido[-1]}")

hombres = []
hombre ={
    "nombre":"carlos",
    "edad":12,
    "ciudad": "Valencia",
    "Soltero": False,
}
hombres.append(hombre)
print(hombre["nombre"])

compra = ["pan", "leche", "huevos"]
compra.append("frutas")
compra.insert(2, "verduras")
compra.remove(compra[-1])
print(compra)
peliculas = ["Inception", "The Matrix", "Interstellar"]
peliculas.append("Gladiator")
peliculas.insert(1,"Up")
print(len(peliculas))
numeros = [20, 47, 19, 29, 45, 67, 78, 90]
numeros[5]= 0
print(numeros)
# Cine: inserta, elimina y ordena
# Parte de peliculas. Añade "El Padrino", inserta "Memento" en el índice 2 (tercera posición), elimina "Gladiator" con remove() y guarda la última película usando pop() en ultima. Ordena alfabéticamente, guarda una copia en ordenadas y vacía peliculas con clear(). En un comentario explica cómo usar pop() para otro índice.

culpable: bool = True
if culpable:
    print("Culpable")
else:
    print("No culpable")

gente = [
    {"nombre": "Jamiro", "edad": 45},
    {"nombre": "Juan", "edad": 35},
    {"nombre": "Paco", "edad": 34},
    {"nombre": "Pepe", "edad": 14},
    {"nombre": "Pilar", "edad": 24},
    {"nombre": "Laura", "edad": 24},
    {"nombre": "Jenny", "edad": 10},
]
p= gente[3]
if p["edad"] >= 18:
    print("mayor")
else:
    print("menor")
    