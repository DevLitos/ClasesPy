# Pide dos textos con input(), sin convertirlos a números. Si son exactamente iguales, imprime "Son iguales"; si no, "Son distintos". Mayúsculas y espacios cuentan como diferencias. No muestres otros mensajes con print().
primero = input("Primer texto: ")
segundo = input("Segundo texto: ")
# Compara e imprime el resultado
if primero == segundo:
    print("Son iguales")
else:
    print("Son distintos")

edades = [10, 20, 30, 40, 50]
for edad in edades:
    if edad > 18:
        continue
    elif edad >= 65:
        break


# Recorre numeros y muestra (uno por línea) los que sean divisibles por 5. Si encuentras uno mayor que 150, detén el bucle con break.
numeros = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for num in numeros:
    if num > 165:
        break
    elif num % 5== 0:
        print(num)

# alt mueve linea
# ctrl shift alt selecciona 
# shift alt flecha duplica
# crl l selecciona toda la linea
# ctrl ç comenta/descomenta



# # El siguiente ejercicio debe validar lo que escriba el usuario utilizando un bucle while.
# # Se deben cumplir las siguientes condiciones:
# # El usuario tendrá como máximo 5 intentos para introducir un número válido.
# # En cada iteración, el programa debe pedir al usuario que introduzca un número.
# # Si el usuario escribe algo que no sea un número (por ejemplo, letras o símbolos), se debe mostrar un mensaje de advertencia y volver a pedir el número sin detener el programa.
# # Si el usuario introduce un número válido:
# # Se convierte a entero.
# # Se muestra un mensaje indicando que el número es válido.
# # El bucle finaliza inmediatamente
MAX_INTENTOS: int = 5
while MAX_INTENTOS:
    try:
        num = int(input("Introduce un numero:"))
        print("El numero introducido es valido")
        break
    except:
        MAX_INTENTOS -= 1
        print("Error introduce un entero")


# Pide dos números y muestra el resultado de dividirlos. Usa try/except: si se divide entre cero, muestra No se puede dividir por cero.
num1 = int(input("Num 1: "))
num2 = int(input("Num 2: "))
try: 
    num1 / num2
except:
    if num2 == 0:
            print("No se puede dividir por cero")


# Pide dos números y conviértelos con float() dentro de try. Imprime la división. Si ocurre un error (texto inválido o divisor cero), imprime "No se pudo realizar la división". En finally imprime siempre "Proceso finalizado". Puedes usar except sin especificar el tipo de error, como en el ejemplo de clase.
try:
    nume1 = float(input("Introduce un numero: "))
    nume2 = float(input("Num 2 : "))
    print(nume1 / nume2)
    pass
except:
    if nume1 or nume2 is type(str):
        print("text invalido")
    elif nume1 or nume2 == 0:
        print("por 0")
    pass
finally:
    print("proceso finalizado")
