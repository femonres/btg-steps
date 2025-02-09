import json


def handler(event, context):
    print(f"EnviarResultado.handler - Event incoming: {event}")

    return {
        'statusCode': 200,
        'body': json.dumps({'status': 'Success'})
    }