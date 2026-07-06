# Software-FJ-G32
# participantes: Robinson Ordoñez, Edilson Ordoñez, Gabriela Ramirez, Jesus Figueroa, Daniel Lopez
from abc import ABC, abstractmethod

class EntidadBase(ABC):
    def __init__(self, id_entidad):
        self._id_entidad = id_entidad

    @property
    def id_entidad(self):
        return self._id_entidad

    @abstractmethod
    def mostrar_info(self):
        pass
class SistemaFJError(Exception):
    """Excepción base del sistema."""
    pass

class ClienteError(SistemaFJError):
    """Errores relacionados con clientes."""
    pass

class ServicioError(SistemaFJError):
    """Errores relacionados con servicios."""
    pass

class ReservaError(SistemaFJError):
    """Errores relacionados con reservas."""
    pass

class ValidacionError(SistemaFJError):
    """Errores de validación de datos."""
    Pass
import re
from entidades import EntidadBase
from excepciones import ClienteError, ValidacionError

class Cliente(EntidadBase):
    def __init__(self, id_entidad, nombre, documento, correo, telefono):
        super().__init__(id_entidad)
        self.nombre = nombre
        self.documento = documento
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or len(valor.strip()) < 3:
            raise ValidacionError("El nombre del cliente debe tener al menos 3 caracteres.")
        self._nombre = valor.strip()

    @property
    def documento(self):
        return self._documento

    @documento.setter
    def documento(self, valor):
        if not str(valor).isdigit():
            raise ValidacionError("El documento debe contener solo números.")
        self._documento = str(valor)

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(patron, valor):
            raise ValidacionError("Correo electrónico no válido.")
        self._correo = valor

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if not str(valor).isdigit() or len(str(valor)) < 7:
            raise ValidacionError("El teléfono debe tener al menos 7 dígitos.")
        self._telefono = str(valor)

    def mostrar_info(self):
        return f"Cliente: {self.nombre} | Documento: {self.documento} | Correo: {self.correo}"
from abc import ABC, abstractmethod
from entidades import EntidadBase
from excepciones import ServicioError, ValidacionError

class Servicio(EntidadBase, ABC):
    def __init__(self, id_entidad, nombre, tarifa_base, disponible=True):
        super().__init__(id_entidad)
        if tarifa_base <= 0:
            raise ValidacionError("La tarifa base debe ser mayor que cero.")
        self._nombre = nombre
        self._tarifa_base = tarifa_base
        self._disponible = disponible

    @property
    def nombre(self):
        return self._nombre

    @property
    def tarifa_base(self):
        return self._tarifa_base

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, valor):
        self._disponible = valor

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        pass

    @abstractmethod
    def mostrar_info(self):
        pass
class ReservaSala(Servicio):
    def __init__(self, id_entidad, nombre, tarifa_base, capacidad):
        super().__init__(id_entidad, nombre, tarifa_base)
        if capacidad <= 0:
            raise ValidacionError("La capacidad de la sala debe ser mayor que cero.")
        self.capacidad = capacidad

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        if duracion <= 0:
            raise ServicioError("La duración de la reserva debe ser mayor que cero.")
        subtotal = self.tarifa_base * duracion
        subtotal -= subtotal * (descuento / 100)
        subtotal += subtotal * (impuesto / 100)
        return subtotal

    def mostrar_info(self):
        return f"Servicio: {self.nombre} | Tipo: Reserva de Sala | Capacidad: {self.capacidad}"
class AlquilerEquipo(Servicio):
    def __init__(self, id_entidad, nombre, tarifa_base, tipo_equipo):
        super().__init__(id_entidad, nombre, tarifa_base)
        self.tipo_equipo = tipo_equipo

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        if duracion <= 0:
            raise ServicioError("La duración del alquiler debe ser mayor que cero.")
        subtotal = self.tarifa_base * duracion
        subtotal -= subtotal * (descuento / 100)
        subtotal += subtotal * (impuesto / 100)
        return subtotal

    def mostrar_info(self):
        return f"Servicio: {self.nombre} | Tipo: Alquiler de Equipo | Equipo: {self.tipo_equipo}"
class AsesoriaEspecializada(Servicio):
    def __init__(self, id_entidad, nombre, tarifa_base, especialidad):
        super().__init__(id_entidad, nombre, tarifa_base)
        self.especialidad = especialidad

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        if duracion <= 0:
            raise ServicioError("La duración de la asesoría debe ser mayor que cero.")
        subtotal = self.tarifa_base * duracion
        subtotal -= subtotal * (descuento / 100)
        subtotal += subtotal * (impuesto / 100)
        return subtotal

    def mostrar_info(self):
        return f"Servicio: {self.nombre} | Tipo: Asesoría | Especialidad: {self.especialidad}"
from excepciones import ReservaError, ValidacionError

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        if cliente is None:
            raise ValidacionError("La reserva debe tener un cliente válido.")
        if servicio is None:
            raise ValidacionError("La reserva debe tener un servicio válido.")
        if duracion <= 0:
            raise ValidacionError("La duración de la reserva debe ser mayor que cero.")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        if not self.servicio.disponible:
            raise ReservaError(f"El servicio '{self.servicio.nombre}' no está disponible.")
        self.estado = "Confirmada"

    def cancelar(self):
        if self.estado == "Cancelada":
            raise ReservaError("La reserva ya estaba cancelada.")
        self.estado = "Cancelada"

    def procesar(self, descuento=0, impuesto=0):
        if self.estado == "Cancelada":
            raise ReservaError("No se puede procesar una reserva cancelada.")
        costo = self.servicio.calcular_costo(self.duracion, descuento, impuesto)
        return costo

    def mostrar_info(self):
        return f"Reserva -> Cliente: {self.cliente.nombre}, Servicio: {self.servicio.nombre}, Estado: {self.estado}"
from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import ClienteError, ServicioError, ReservaError, ValidacionError
from datetime import datetime

class GestorSistema:
    def __init__(self, archivo_log="logs_sistema.txt"):
        self.clientes = []
        self.servicios = []
        self.reservas = []
        self.archivo_log = archivo_log

    def registrar_log(self, mensaje):
        with open(self.archivo_log, "a", encoding="utf-8") as archivo:
            archivo.write(f"[{datetime.now()}] {mensaje}\n")

    def agregar_cliente(self, cliente):
        try:
            if any(c.documento == cliente.documento for c in self.clientes):
                raise ClienteError("Ya existe un cliente con ese documento.")
            self.clientes.append(cliente)
            self.registrar_log(f"Cliente agregado correctamente: {cliente.nombre}")
        except Exception as e:
            self.registrar_log(f"Error al agregar cliente: {e}")
            raise

    def agregar_servicio(self, servicio):
        try:
            self.servicios.append(servicio)
            self.registrar_log(f"Servicio agregado correctamente: {servicio.nombre}")
        except Exception as e:
            self.registrar_log(f"Error al agregar servicio: {e}")
            raise

    def crear_reserva(self, reserva):
        try:
            self.reservas.append(reserva)
            self.registrar_log(f"Reserva creada para cliente {reserva.cliente.nombre} con servicio {reserva.servicio.nombre}")
        except Exception as e:
            self.registrar_log(f"Error al crear reserva: {e}")
            raise

    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente.mostrar_info())

    def listar_servicios(self):
        for servicio in self.servicios:
            print(servicio.mostrar_info())

    def listar_reservas(self):
        for reserva in self.reservas:
            print(reserva.mostrar_info())