"""Excepciones personalizadas del sistema."""


# CLIENTES

class ClienteError(Exception):
    """Clase base para errores relacionados con clientes."""
    pass

class NombreInvalidoError(ClienteError):
    """Se genera cuando el nombre del cliente es inválido."""
    pass

class CorreoInvalidoError(ClienteError):
    """Se genera cuando el correo tiene un formato incorrecto."""
    pass

class TelefonoInvalidoError(ClienteError):
    """Se genera cuando el teléfono es inválido."""
    pass

class ClienteDuplicadoError(ClienteError):
    """Se genera cuando el cliente ya existe."""
    pass


# SERVICIOS

class ServicioError(Exception):
    """Clase base para errores relacionados con servicios."""
    pass

class PrecioInvalidoError(ServicioError):
    """Se genera cuando el precio es inválido."""
    pass

class CapacidadInvalidaError(ServicioError):
    """Se genera cuando la capacidad no es válida."""
    pass

class ServicioNoDisponibleError(ServicioError):
    """Se genera cuando el servicio no está disponible."""
    pass


# RESERVAS

class ReservaError(Exception):
    """Clase base para errores relacionados con reservas."""
    pass

class ReservaExistenteError(ReservaError):
    """Se genera cuando la reserva ya existe."""
    pass

class ReservaCanceladaError(ReservaError):
    """Se genera cuando la reserva ya fue cancelada."""
    pass

class ReservaNoEncontradaError(ReservaError):
    """Se genera cuando no se encuentra una reserva."""
    pass


# VALIDACIONES GENERALES

class ValidacionError(Exception):
    """Error general de validación."""
    pass