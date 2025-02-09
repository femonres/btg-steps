from datetime import datetime
import json

from src.utils.logger import logger


def handler(event, context):
    logger.info(f"Event incoming: {event}")
    # Obtener el mensaje JSON
    message = json.loads(event['Message'])
    errors = json.loads(event['errors']) if 'errors' in event else []
    client_id = message['client_id']
    logger.info(f"client_id: {client_id}")

    # Validar si las fechas son correctas
    if message['fecha_procesamiento'] > datetime.now().strftime('%Y-%m-%d'):
        logger.error(f"Fecha de procesamiento mayor a la fecha actual: {message['fecha_procesamiento']}")
        errors.append({'ErrorCode': 'INVALID_DATE', 'description': 'Fecha de procesamiento mayor a la fecha actual'})
        return {
            'statusCode': 400,
            'errors': json.dumps(errors),
            'Message': event['Message']
        }
    
    return {
        'statusCode': event['statusCode'],
        'errors': json.dumps(errors),
        'Message': event['Message']
    }

