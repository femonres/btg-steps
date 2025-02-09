import json

from src.utils import logger


def handler(event, context):
    logger.info(f"ValidarFechas.handler - Event incoming: {event}")
    # Obtener el mensaje JSON
    message = json.loads(event['Records'][0]['body'])
    client_id = message['client_id']
    logger.info(f"ValidarFechas.handler - client_id: {client_id}")

    # Validar si las fechas son correctas
    if message['fecha_inicio'] > message['fecha_fin']:
        return {
            'statusCode': 400,
            'body': json.dumps({'ErrorCode': 'INVALID_DATES', 'description': 'Fecha de inicio mayor a fecha de fin'})
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps({'status': 'Success'})
    }

