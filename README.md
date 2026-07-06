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