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
        