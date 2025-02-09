import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    secret_name: str = os.getenv("SECRET_NAME")
    region_name: str = os.getenv("REGION_NAME")
    bucket_name: str = os.getenv("BUCKET_NAME")
    queue_name: str = os.getenv("QUEUE_NAME")

settings = Settings()