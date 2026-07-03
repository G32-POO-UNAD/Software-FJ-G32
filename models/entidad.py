"""Clase abstracta base para todas las entidades del sistema."""
from abc import ABC, abstractmethod


class Entidad(ABC):

    """Clase abstracta que representa una entidad general del sistema."""

    def __init__(self, codigo: str):
        self.__codigo = codigo


    # Encapsulación

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, nuevo_codigo):
        self.__codigo = nuevo_codigo

    
    # Métodos abstractos

    @abstractmethod
    def mostrar_informacion(self):
        
        """Cada clase hija deberá implementar este método."""
        pass

    @abstractmethod
    def validar(self):
        
        """Cada clase hija implementará sus propias validaciones."""
        pass