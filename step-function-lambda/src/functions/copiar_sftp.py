import json

from src.utils.logger import logger


def handler(event, context):
    logger.info(f"CopiarSFTP.handler - Event incoming: {event}")

    # Detalles del archivo desde el evento S3

    # Descargar el archivo desde S3

    # Configuración de conexión FTP

    # Conectar y subir archivo al servidor FTP