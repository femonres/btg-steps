import json
import boto3
from botocore.exceptions import ClientError


def get_secrets(secret_name) -> dict:
    client = boto3.client("secretsmanager")
    try:
        response = client.get_secret_value(SecretId=secret_name)
        return json.loads(response["SecretString"])
    except ClientError as e:
        raise e