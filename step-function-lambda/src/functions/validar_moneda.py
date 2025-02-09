import json

from src.utils.logger import logger

def handler(event, context):
    logger.info(f"ValidarMoneda.handler - Event incoming: {event}")

    return {
        'statusCode': 200,
        'body': json.dumps({'status': 'Success'})
    }