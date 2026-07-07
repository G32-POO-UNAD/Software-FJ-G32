# Software-FJ-G32
# participantes: Robinson Ordoñez, Edilson Ordoñez, Gabriela Ramirez, Jesus Figueroa, Daniel Lopez
from abc import ABC, abstractmethod
import re
from datetime import datetime

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
    """Errores relacionados con 
    clientes."""
    pass

class ServicioError(SistemaFJError):
    """Errores relacionados con servicios."""
    pass

class ReservaError(SistemaFJError):
    """Errores relacionados con reservas."""
    pass

class ValidacionError(SistemaFJError):
    """Errores de validación de datos."""
    pass

class Logger:

    @staticmethod
    def registrar_log(mensaje):
        with open("logs_sistema.txt", "a", encoding="utf-8") as archivo:
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            archivo.write(f"[{fecha}] {mensaje}\n")

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
        try:
           if not self.servicio.disponible:
               raise ReservaError(
                  f"El servicio '{self.servicio.nombre}' no está disponible."
               )
           self.estado = "Confirmada" 

        except ReservaError as e:
            Logger.registrar_log(f"ERROR: {e}")
            raise ReservaError("No fue posible confirmar la reserva.") from e

        else:
           Logger.registrar_log(
               f"Reserva confirmada para el cliente {self.cliente.nombre}"
               )

        finally: 
           Logger.registrar_log(
               "Finalizó el proceso de confirmación de la reserva."
           )
            

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
        
class GestorSistema:
    def __init__(self, archivo_log="logs_sistema.txt"):
        self.clientes = []
        self.servicios = []
        self.reservas = []
        self.archivo_log = archivo_log

    def registrar_log(self, mensaje):
        """Guarda un mensaje en el archivo de registro."""
        Logger.registrar_log(mensaje)

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
from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from gestor import GestorSistema
from excepciones import SistemaFJError

def main():
    gestor = GestorSistema()

    print("===== SISTEMA SOFTWARE FJ =====")

    # 1. Cliente válido
    try:
        cliente1 = Cliente(1, "Robinson Ordoñez", "123456789", "robinson@gmail.com", "3001234567")
        gestor.agregar_cliente(cliente1)
        print("Cliente 1 registrado correctamente.")
    except Exception as e:
        print("Error:", e)

    # 2. Cliente inválido (correo incorrecto)
    try:
        cliente2 = Cliente(2, "Ana", "987654321", "correo_invalido", "3009998888")
        gestor.agregar_cliente(cliente2)
    except Exception as e:
        gestor.registrar_log(f"Excepción controlada en cliente inválido: {e}")
        print("Error controlado en cliente 2:", e)

    # 3. Cliente inválido (documento repetido)
    try:
        cliente3 = Cliente(3, "Carlos Pérez", "123456789", "carlos@gmail.com", "3005554444")
        gestor.agregar_cliente(cliente3)
    except Exception as e:
        gestor.registrar_log(f"Excepción por documento repetido: {e}")
        print("Error controlado en cliente 3:", e)

    # 4. Servicio válido - sala
    try:
        sala1 = ReservaSala(101, "Sala Premium", 50000, 20)
        gestor.agregar_servicio(sala1)
        print("Servicio sala registrado correctamente.")
    except Exception as e:
        print("Error:", e)

    # 5. Servicio válido - equipo
    try:
        equipo1 = AlquilerEquipo(102, "Alquiler VideoBeam", 30000, "VideoBeam")
        gestor.agregar_servicio(equipo1)
        print("Servicio equipo registrado correctamente.")
    except Exception as e:
        print("Error:", e)

    # 6. Servicio válido - asesoría
    try:
        asesoria1 = AsesoriaEspecializada(103, "Asesoría en Python", 80000, "Programación")
        gestor.agregar_servicio(asesoria1)
        print("Servicio asesoría registrado correctamente.")
    except Exception as e:
        print("Error:", e)

    # 7. Servicio inválido (tarifa negativa)
    try:
        servicio_invalido = ReservaSala(104, "Sala Económica", -1000, 10)
        gestor.agregar_servicio(servicio_invalido)
    except Exception as e:
        gestor.registrar_log(f"Excepción por servicio inválido: {e}")
        print("Error controlado en servicio inválido:", e)

    # 8. Reserva válida
    try:
        reserva1 = Reserva(cliente1, sala1, 2)
        gestor.crear_reserva(reserva1)
        reserva1.confirmar()
        total = reserva1.procesar(descuento=10, impuesto=19)
        print(f"Reserva 1 procesada correctamente. Total: ${total}")
    except Exception as e:
        gestor.registrar_log(f"Error en reserva 1: {e}")
        print("Error:", e)

    # 9. Reserva inválida (duración negativa)
    try:
        reserva2 = Reserva(cliente1, equipo1, -3)
        gestor.crear_reserva(reserva2)
    except Exception as e:
        gestor.registrar_log(f"Error en reserva inválida: {e}")
        print("Error controlado en reserva 2:", e)

    # 10. Reserva con servicio no disponible
    try:
        asesoria1.disponible = False
        reserva3 = Reserva(cliente1, asesoria1, 1)
        gestor.crear_reserva(reserva3)
        reserva3.confirmar()
    except Exception as e:
        gestor.registrar_log(f"Error por servicio no disponible: {e}")
        print("Error controlado en reserva 3:", e)

    # 11. Cancelar reserva y luego procesarla
    try:
        reserva4 = Reserva(cliente1, equipo1, 2)
        gestor.crear_reserva(reserva4)
        reserva4.cancelar()
        total = reserva4.procesar()
        print(total)
    except Exception as e:
        gestor.registrar_log(f"Error al procesar reserva cancelada: {e}")
        print("Error controlado en reserva 4:", e)

    # 12. Mostrar información final
    print("\n===== CLIENTES REGISTRADOS =====")
    gestor.listar_clientes()

    print("\n===== SERVICIOS REGISTRADOS =====")
    gestor.listar_servicios()

    print("\n===== RESERVAS REGISTRADAS =====")
    gestor.listar_reservas()

if __name__ == "__main__":
    main()
