import os
import json
import boto3
import psycopg2
from botocore.exceptions import ClientError

class Database:
    def __init__(self, secret_name):
        self.secret_name = secret_name
        self.connection = None

    def connect(self):
        secret = self._get_secret()
        self.connection = psycopg2.connect(
            host=secret["host"],
            database=secret["dbname"],
            user=secret["username"],
            password=secret["password"]
        )

    def _get_secret(self):
        client = boto3.client("secretsmanager")
        try:
            response = client.get_secret_value(SecretId=self.secret_name)
            return json.loads(response["SecretString"])
        except ClientError as e:
            raise e

    def query(self, sql, params=None):
        cursor = self.connection.cursor()
        cursor.execute(sql, params or ())
        return cursor.fetchall()

    def disconnect(self):
        if self.connection:
            self.connection.close()