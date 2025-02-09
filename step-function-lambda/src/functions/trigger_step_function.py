import os
import json
import boto3

from src.utils import logger


# Cliente de Step Functions
stepfunctions_client = boto3.client(
    "stepfunctions", endpoint_url=os.getenv("LOCALSTACK_ENDPOINT")
)

def handler(event, context):
    logger.info("Evento recibido: %s", event)

    # Obtener el mensaje de la cola SQS
    try:
        message = event["Records"][0]["body"]
        input_data = json.loads(message)
    except (KeyError, json.JSONDecodeError) as e:
        logger.error("Error al procesar el evento: %s", e)
        return {"statusCode": 400, "body": "Evento inválido"}

    # Iniciar la ejecución de la Step Function
    try:
        response = stepfunctions_client.start_execution(
            stateMachineArn=os.getenv("STEP_FUNCTION_ARN"),
            input=json.dumps(input_data),
        )
        logger.info("Step Function iniciada: %s", response["executionArn"])
    except Exception as e:
        logger.error("Error al iniciar la Step Function: %s", e)
        return {"statusCode": 500, "body": "Error al iniciar la Step Function"}

    return {"statusCode": 200, "body": "Step Function iniciada correctamente"}