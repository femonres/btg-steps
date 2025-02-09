import json
import boto3

from .auth_interface import IAuthenticator
from ..utils.config import settings


class TokenAutenticator(IAuthenticator):
    def __init__(self):
        self.token = None

    def _load_secret(self, secret_name: str) -> dict:
        client = boto3.client("secretsmanager", region_name=settings.region_name)
        secret_value = client.get_secret_value(SecretId=secret_name)
        secret = json.loads(secret_value["SecretString"])
        return secret

    def authenticate(self, username: str, password: str) -> bool:
        if username == "user" and password == "password":
            self.token = "valid_token"
            return True
        return False
    
    def get_token(self) -> str:
        return self.token
    
    def clear_token(self) -> None:
        self.token = ""
        return None