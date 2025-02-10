import boto3

from src.utils.logger import logger


class BucketS3Client:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.client = boto3.client("s3")

    def upload(self, file_name, content):
        logger.info(f"Uploading file {file_name} to bucket {self.bucket_name}")
        self.client.put_object(Bucket=self.bucket_name, Key=file_name, Body=content)

    def download(self, file_name, local_file_path):
        logger.info(f"Downloading file {file_name} from bucket {self.bucket_name}")
        self.client.download_file(self.bucket_name, file_name, local_file_path)
        return local_file_path