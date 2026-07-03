"""Clase Reserva"""

from datetime import datetime

from models.cliente import Cliente
from models.servicio import Servicio
from utils.excepciones import (ReservaError,ReservaCanceladaError,CapacidadInvalidaError)
from utils.constantes import (ESTADO_RESERVA_PENDIENTE,ESTADO_RESERVA_CONFIRMADA,ESTADO_RESERVA_CANCELADA)
from utils.logger import (registrar_info,registrar_error)


class Reserva:

    def __init__(self, codigo, cliente, servicio, duracion):

        if not isinstance(cliente, Cliente):
            raise ReservaError("Debe ingresar un cliente válido.")

        if not isinstance(servicio, Servicio):
            raise ReservaError("Debe ingresar un servicio válido.")

        self.__codigo = codigo
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = ESTADO_RESERVA_PENDIENTE
        self.__fecha = datetime.now()

        self.validar()

        registrar_info(f"Reserva {self.__codigo} creada correctamente.")

   
    # PROPIEDADES

    @property
    def codigo(self):
        return self.__codigo

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    @property
    def fecha(self):
        return self.__fecha

   
    # VALIDACIONES

    def validar(self):

        if self.__duracion <= 0:
            raise CapacidadInvalidaError("La duración debe ser mayor que cero.")

    
    # CONFIRMAR

    def confirmar(self):

        try:

            if self.__estado == ESTADO_RESERVA_CANCELADA:
                raise ReservaCanceladaError("No es posible confirmar una reserva cancelada.")

            self.__estado = ESTADO_RESERVA_CONFIRMADA

        except ReservaCanceladaError as error:

            registrar_error(str(error))
            raise

        else:

            registrar_info(f"Reserva {self.__codigo} confirmada.")

    
    # CANCELAR

    def cancelar(self):

        try:

            if self.__estado == ESTADO_RESERVA_CONFIRMADA:
                raise ReservaError("No se puede cancelar una reserva confirmada.")

            self.__estado = ESTADO_RESERVA_CANCELADA

        except ReservaError as error:

            registrar_error(str(error))
            raise

        else:

            registrar_info(f"Reserva {self.__codigo} cancelada.")

   
    # PROCESAR

    def procesar(self):

        try:

            total = self.__servicio.calcular_costo()

            registrar_info(f"Reserva {self.__codigo} procesada.")

            return total

        except Exception as error:

            registrar_error(str(error))

            raise ReservaError("Error al procesar la reserva.") from error

        finally:

            registrar_info(f"Proceso finalizado para la reserva {self.__codigo}.")


    # INFORMACIÓN

    def mostrar_informacion(self):

        return (f"Código: {self.codigo}\n"f"Cliente: {self.cliente.nombre}\n"f"Servicio: {self.servicio.nombre}\n"f"Duración: {self.duracion}\n"f"Estado: {self.estado}\n"f"Fecha: {self.fecha.strftime('%d/%m/%Y %H:%M')}")

  
    # REPRESENTACIÓN

    def __str__(self):

        return (f"{self.codigo} - "f"{self.cliente.nombre} - "f"{self.servicio.nombre} - "f"{self.estado}")
    