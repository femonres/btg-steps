import json

from src.utils.logger import logger
from src.utils.config import settings
from src.services.database import Database

def handler(event, context):
    logger.info(f"ValidarCliente.handler - Event incoming: {event}")
    # Obtener el mensaje JSON
    try:
        message = json.loads(event['Message'])
        client_id = message['client_id']
        logger.info(f"ValidarCliente.handler - client_id: {client_id}")
    except Exception as e:
        logger.error(f"ValidarCliente.handler - Error al obtener el mensaje: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps({'ErrorCode': 'INVALID_JSON', 'description': 'Error al obtener el mensaje'})
        }

    # Conectar a la base de datos
    db = Database(settings.secret_name)

    # Validar si el cliente existe
    try:
        db.connect()
        cliente = db.query("SELECT * FROM tbl_clientes WHERE id = %s", (client_id,))
        if not cliente:
            logger.error(f"ValidarCliente.handler - Cliente no encontrado: {client_id}")
            return {"statusCode": 404, "body": "Cliente no encontrado"}
    except Exception as e:
        logger.error(f"ValidarCliente.handler - Error al validar el cliente: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'ErrorCode': 'INTERNAL_ERROR', 'description': 'Error interno'})
        }
    finally:
        db.disconnect()

    logger.info(f"ValidarCliente.handler - Cliente encontrado: {client_id}")
    return {
        'statusCode': 200,
        'body': json.dumps({'status': 'Success'})
    }