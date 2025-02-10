import os
import json
import paramiko

from src.utils.logger import logger
from src.utils.config import settings
from src.services.secrets import get_secrets
from src.services.bucket_s3 import BucketS3Client


def handler(event, context):
    logger.info(f"Event incoming: {event}")

    # Detalles del archivo desde el evento S3
    #bucket_name = event['Records'][0]['s3']['bucket']['name']
    #file_name = event['Records'][0]['s3']['object']['key']
    bucket_name = settings.bucket_name
    file_name = event['file_name']

    # Descargar el archivo desde S3
    local_file_path = f"/tmp/{os.path.basename(file_name)}"

    s3 = BucketS3Client(bucket_name)
    try:
        s3.download(file_name, local_file_path)
        logger.info(f"File downloaded: {file_name}")

    except Exception as e:
        logger.error(f"Error downloading file from S3: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'status': 'Error downloading file from S3'})
        }

    # Enviar el archivo al servidor SFTP
    try:
        send_to_sftp(local_file_path, file_name)
        logger.info(f"File {file_name} sent to SFTP")

    except Exception as e:
        logger.error(f"Error sending file to SFTP: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'status': 'Error sending file to SFTP'})
        }

    return {
        'statusCode': 200,
        'body': json.dumps({'status': 'Success', 'message': f'File {file_name} copied to SFTP'})
    }

def send_to_sftp(local_file_path, file_name):
    credentals = get_secrets(settings.sftp_credentials)
    logger.info(f"Credentials: {credentals}")
    
    transport = paramiko.Transport((credentals['host'], credentals['port']))
    transport.connect(username=credentals['username'], password=credentals['password'])
    sftp = paramiko.SFTPClient.from_transport(transport)
    logger.info(f"Connected to SFTP server: {credentals['host']}")
    
    try:
        remotepath = f"{credentals['path']}/{file_name}"
        sftp.put(local_file_path, remotepath)
        logger.info(f"File {file_name} sent to SFTP")

    except Exception as e:
        logger.error(f"Error sending file to SFTP: {e}")
        raise e

    finally:
        sftp.close()
        transport.close()
        logger.info("Connection to SFTP server closed")