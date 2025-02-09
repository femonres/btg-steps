import os
import json
import boto3
from botocore.exceptions import ClientError

from src.utils.logger import logger


class Database:
    def __init__(self, secret_name):
        self.secret_name = secret_name

    def connect(self):
        secret = self._get_secret()
        logger.info(f"Los datos obtenidos son: {secret}")

    def _get_secret(self):
        client = boto3.client("secretsmanager")
        try:
            response = client.get_secret_value(SecretId=self.secret_name)
            return json.loads(response["SecretString"])
        except ClientError as e:
            raise e

    def query(self, sql, params=None):
        return []

    def disconnect(self):
        pass