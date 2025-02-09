import json

from src.utils.logger import logger
from src.utils.config import settings
from src.services.database import Database

def handler(event, context):
    logger.info(f"Event incoming: {event}")
    # Obtener el mensaje JSON
    try:
        message = json.loads(event['Message'])
        client_id = message['client_id']
        logger.info(f"client_id: {client_id}")
    except Exception as e:
        logger.error(f"Error al obtener el mensaje: {e}")
        return {
            'statusCode': 400,
            'detail': json.dumps({'ErrorCode': 'INVALID_JSON', 'description': 'Error al obtener el mensaje'})
        }

    # Conectar a la base de datos
    db = Database(settings.secret_name)

    # Validar si el cliente existe
    try:
        db.connect()
        cliente = db.query("SELECT * FROM tbl_clientes WHERE id = %s", (client_id,))
        if not cliente:
            logger.error(f"Cliente no encontrado: {client_id}")
            return {
                "statusCode": 404,
                "errors": json.dumps([{'ErrorCode': 'BUSINES_VALIDATIONS', 'description': 'Cliente no encontrado'}]),
                "Message": event['Message']
            }
    except Exception as e:
        logger.error(f"Error al validar el cliente: {e}")
        return {
            'statusCode': 500,
            'detail': json.dumps({'ErrorCode': 'INTERNAL_ERROR', 'description': 'Error interno'})
        }
    finally:
        db.disconnect()

    logger.info(f"Cliente encontrado: {client_id}")
    return {
        'statusCode': 200,
        'Message': event['Message']
    }