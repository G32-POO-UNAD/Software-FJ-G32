"""Módulo encargado de registrar eventos y errores del sistema."""


import logging
import os

# Ruta donde se almacenará el archivo de logs
RUTA_LOG = os.path.join("data", "logs.txt")

# Configuración del logger
logging.basicConfig(filename=RUTA_LOG,level=logging.INFO,format="%(asctime)s | %(levelname)s | %(message)s",datefmt="%d/%m/%Y %H:%M:%S",encoding="utf-8")


def registrar_info(mensaje):
    
    """Registra un evento informativo."""
    logging.info(mensaje)


def registrar_error(mensaje):
    
    """Registra un error."""
    logging.error(mensaje)


def registrar_advertencia(mensaje):

    """Registra una advertencia."""
    logging.warning(mensaje)


def registrar_critico(mensaje):
    
    """Registra un error crítico."""
    logging.critical(mensaje)