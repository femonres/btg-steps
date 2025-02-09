import boto3

from src.utils import logger


class BucketS3Client:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.client = boto3.client("s3")

    def upload(self, file, key):
        logger.info(f"Uploading file {file} to bucket {self.bucket_name} with key {key}")
        self.client.put_object(Bucket=self.bucket_name, Key=key, Body=file)