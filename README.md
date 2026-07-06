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
        