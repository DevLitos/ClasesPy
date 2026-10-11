from modulos import saludos
import app

def testear_saludo():
    assert saludos.saludar("Carlos") == "Hola Carlos"


def testear_precios():
    assert app.precio_final(100, 20) == 80
    assert app.precio_final(100, 0) == 50