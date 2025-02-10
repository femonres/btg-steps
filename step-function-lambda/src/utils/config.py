import os

class Settings:
    secret_name: str = os.getenv("SECRET_NAME")
    region_name: str = os.getenv("REGION_NAME")
    bucket_name: str = os.getenv("BUCKET_NAME")
    queue_name: str = os.getenv("QUEUE_NAME")
    step_function_arn: str = os.getenv("STEP_FUNCTION_ARN")
    localstack_endpoint: str = os.getenv("LOCALSTACK_ENDPOINT")
    sftp_credentials: str = os.getenv("SFTP_SERVER_SECRET")

settings = Settings()