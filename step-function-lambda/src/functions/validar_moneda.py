import json

from src.utils.logger import logger

def handler(event, context):
    logger.info(f"ValidarMoneda.handler - Event incoming: {event}")

    return {
        'statusCode': event['statusCode'],
        'errors': event['errors'] if 'errors' in event else json.dumps([]),
        'Message': event['Message'],
    }