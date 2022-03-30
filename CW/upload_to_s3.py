import logging
import boto3
from botocore.exceptions import ClientError
import os
from time import time, sleep

#logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

#connecting to boto3 client
s3_client = boto3.client('s3')

def upload_file(file_name, bucket, object_name=None):
    """Uploads a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: Event response if file was uploaded, else raise Exception
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)
        
    
      
    # Upload the file
    try:
          response = s3_client.upload_file(file_name, bucket, object_name)
          logger.info(f'Successfully uploaded {file_name} to S3 bucket {bucket}.')
          return response

    except ClientError:
          logger.exception(f'Failed to upload {file_name} to S3 bucket {bucket}.')
          raise
        
if __name__ == '__main__':
    a_directory = "images/images/"
    bucket_name="buckets1827468"
    if len(os.listdir(a_directory) ) == 0:
      logger.info(f'Directory is empty. No files to upload.')
    else:
      for filename in os.listdir(a_directory):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
          filepath = os.path.join(a_directory, filename)
          logger.info(f'Uploading {filepath} to S3 bucket {bucket_name}...')
          sleep(30)
          upload_file(filepath,bucket_name)
        else:
          logger.error(f'File is not an image')
    
