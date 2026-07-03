"""Clase abstracta Servicio y sus clases derivadas."""

from abc import ABC, abstractmethod
from multipledispatch import dispatch

from models.entidad import Entidad
from utils.excepciones import (NombreInvalidoError, PrecioInvalidoError, CapacidadInvalidaError, ValidacionError)
from utils.validaciones import (validar_nombre,validar_precio,validar_capacidad)
from utils.constantes import (SERVICIO_SALA, SERVICIO_ALQUILER, SERVICIO_ASESORIA,)
from utils.logger import registrar_info


class Servicio(Entidad, ABC):

    def __init__(self, codigo, nombre, precio):

        super().__init__(codigo)

        self.__nombre = ""
        self.__precio = 0

        self.nombre = nombre
        self.precio = precio
    

   
    # NOMBRE

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        try:
            validar_nombre(valor)
        except ValidacionError as e:
            raise NombreInvalidoError("Nombre del servicio inválido.") from e

        self.__nombre = valor
   
    # PRECIO

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):

        try:
            validar_precio(valor)
        except ValidacionError as e:
            raise PrecioInvalidoError("Precio del servicio inválido.") from e

        self.__precio = valor

   
    # SOBRECARGA
    
    @dispatch()
    def calcular_costo(self):
        return self.precio

    @dispatch(float)
    def calcular_costo(self, impuesto):
        return self.precio + (self.precio * impuesto)

    @dispatch(float, float)
    def calcular_costo(self, impuesto, descuento):

        subtotal = self.precio + (self.precio * impuesto)

        return subtotal - (subtotal * descuento)

    
    # METODOS ABSTRACTOS

    @abstractmethod
    def descripcion(self):
        pass

    @abstractmethod
    def validar(self):
        pass

    @abstractmethod
    def mostrar_informacion(self):
        pass
    
    # RESERVA DE SALA
    
class ReservaSala(Servicio):

    def __init__(self, codigo, precio, capacidad):

        super().__init__(codigo, SERVICIO_SALA, precio)

        self.capacidad = capacidad

        registrar_info("Servicio Reserva de Sala creado.")

    @dispatch()
    def calcular_costo(self):
        return self.precio

    def descripcion(self):
        return "Reserva de sala empresarial."

    def validar(self):

        try:
            validar_capacidad(self.capacidad)
        except ValidacionError as e:
            raise CapacidadInvalidaError("Capacidad del servicio inválida.") from e

        return True

    def mostrar_informacion(self):

        return (f"Código: {self.codigo}\n"f"Servicio: {self.nombre}\n"f"Precio: ${self.precio:,.0f}\n"f"Capacidad: {self.capacidad}")
    
    # ALQUILER DE EQUIPOS
    
class AlquilerEquipo(Servicio):

    def __init__(self, codigo, precio, cantidad):

        super().__init__(codigo, SERVICIO_ALQUILER, precio)

        self.cantidad = cantidad

        registrar_info("Servicio Alquiler de Equipos creado.")

    @dispatch()
    def calcular_costo(self):
        return self.precio * self.cantidad

    def descripcion(self):
        return "Alquiler de equipos tecnológicos."

    def validar(self):

        try:
            validar_capacidad(self.cantidad)
        except ValidacionError as e:
            raise CapacidadInvalidaError("Cantidad del servicio inválida.") from e

        return True

    def mostrar_informacion(self):

        return (f"Código: {self.codigo}\n"f"Servicio: {self.nombre}\n"f"Precio: ${self.precio:,.0f}\n"f"Cantidad: {self.cantidad}")
    
    # ASESORÍA ESPECIALIZADA
    
class AsesoriaEspecializada(Servicio):

    def __init__(self, codigo, precio, horas):

        super().__init__(codigo, SERVICIO_ASESORIA, precio)

        self.horas = horas

        registrar_info("Servicio Asesoría creado.")

    @dispatch()
    def calcular_costo(self):
        return self.precio * self.horas

    def descripcion(self):
        return "Servicio de asesoría especializada."

    def validar(self):

        try:
            validar_capacidad(self.horas)
        except ValidacionError as e:
            raise CapacidadInvalidaError("Número de horas inválido.") from e

        return True

    def mostrar_informacion(self):

        return (f"Código: {self.codigo}\n"f"Servicio: {self.nombre}\n"f"Precio por hora: ${self.precio:,.0f}\n"f"Horas: {self.horas}")
       