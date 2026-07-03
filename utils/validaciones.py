import re
from utils.excepciones import (ValidacionError)

def validar_nombre(nombre):
    if not nombre.strip():
        raise ValidacionError("El nombre no puede estar vacío.")

    if len(nombre.strip()) < 3:
        raise ValidacionError("Debe tener mínimo 3 caracteres.")


def validar_precio(precio):
    if precio <= 0:
        raise ValidacionError("El precio debe ser mayor que cero.")


def validar_capacidad(capacidad):
    if capacidad <= 0:
        raise ValidacionError("La capacidad debe ser mayor que cero.")


def validar_duracion(duracion):
    if duracion <= 0:
        raise ValidacionError("La duración debe ser mayor que cero.")


def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not re.match(patron, email):
        raise ValidacionError("Correo electrónico inválido.")