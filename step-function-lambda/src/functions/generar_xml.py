import json
from datetime import datetime

from src.utils import logger
from src.utils.config import settings
from src.services.bucket_s3 import BucketS3Client


def handler(event, context):
    logger.info(f"GenerarXml.handler - Event incoming: {event}")
    # Obtener el mensaje JSON
    try:
        message = json.loads(event['Records'][0]['body'])
        client_id = message['client_id']
        fecha_procesamiento = message["fecha_procesamiento"]
        logger.info(f"GenerarXml.handler - client_id: {client_id}")
    except Exception as e:
        logger.error(f"GenerarXml.handler - Error al obtener el mensaje: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps({'ErrorCode': 'INVALID_JSON', 'description': 'Error al obtener el mensaje'})
        }

    # Generar el XML
    xml_content = f"""<xml>
    <client_id>{client_id}</client_id>
    <fecha>{fecha_procesamiento}</fecha>
</xml>"""
    logger.info(f"GenerarXml.handler - XML generado: {xml_content}")

    # Subir el XML a S3
    s3 = BucketS3Client(settings.bucket_name)
    file_name = f"{datetime.now().strftime('%Y%m%d')}_logProcesamiento_SETI.xml"
    try:
        s3.upload_file(settings.bucket_name, file_name, xml_content)
        logger.info(f"GenerarXml.handler - XML subido a S3: {client_id}")
    except Exception as e:
        logger.error(f"GenerarXml.handler - Error al subir el XML a S3: {e}")

    return {
        'statusCode': 200,
        'body': json.dumps({'xml': xml_content})
    }