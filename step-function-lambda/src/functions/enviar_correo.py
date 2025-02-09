import json

from src.utils import logger

def handler(event, context):
    logger.info(f"EnviarCorreo.handler - Event incoming: {event}")

    return {
        'statusCode': 200,
        'body': json.dumps({'status': 'Success'})
    }