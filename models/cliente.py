"""Clase Cliente"""


import re

from models.entidad import Entidad
from utils.excepciones import (NombreInvalidoError,CorreoInvalidoError,TelefonoInvalidoError)
from utils.logger import registrar_info


class Cliente(Entidad):

    def __init__(self, codigo, nombre, correo, telefono):

        super().__init__(codigo)

        self.__nombre = ""
        self.__correo = ""
        self.__telefono = ""

        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

        registrar_info(f"Cliente registrado: {self.__nombre}")

    
    # NOMBRE

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):

        valor = valor.strip()

        if len(valor) < 3:
            raise NombreInvalidoError("El nombre debe tener mínimo 3 caracteres.")

        self.__nombre = valor


    # CORREO

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):

        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(patron, valor):
            raise CorreoInvalidoError("Correo electrónico inválido.")
        
        self.__correo = valor

    
    # TELÉFONO

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):

        if not valor.isdigit():
            raise TelefonoInvalidoError("El teléfono solo debe contener números.")

        if len(valor) != 10:
            raise TelefonoInvalidoError("El teléfono debe tener 10 dígitos.")

        self.__telefono = valor

   
    # MÉTODOS ABSTRACTOS

    def mostrar_informacion(self):

        return (f"Código: {self.codigo}\n"f"Nombre: {self.nombre}\n"f"Correo: {self.correo}\n"f"Teléfono: {self.telefono}")

    def validar(self):
        return True


    # REPRESENTACIÓN

    def __str__(self):

        return (f"{self.codigo} - "f"{self.nombre} - "f"{self.correo}")