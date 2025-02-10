from src.utils.logger import logger
from src.services.secrets import get_secrets


class Database:
    def __init__(self, secret_name):
        self.secret_name = secret_name

    def connect(self):
        secret = get_secrets(self.secret_name)
        logger.info(f"Los datos obtenidos son: {secret}")

    def query(self, sql, params=None):
        logger.info(f"Query: {sql}")
        logger.info(f"Params: {params}")
        return []

    def disconnect(self):
        logger.info("Disconnecting from database")