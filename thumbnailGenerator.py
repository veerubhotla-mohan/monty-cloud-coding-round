# This is the script present in the lambda function
# This script will fetch the image uploaded by the user from an S3 bucket, generates thumbnail for that image
# and uploads the thumbnail to a different S3 bucket

import boto3
import json
import uuid
import os

from pathlib import Path
from urllib.parse import unquote_plus
from PIL import Image

s3_client = boto3.client('s3')


def resize_image(image_path, resized_path):
    print(image_path, resized_path)
    with Image.open(image_path) as image:
        image.thumbnail(tuple(x / 2 for x in image.size))
        image.save(resized_path)


def lambda_handler(event, context):
    for record in event['Records']:
        x = (json.loads(record['body']))
        y = ((x['Records'])[0])
        bucket = y['s3']['bucket']['name']
        key = y['s3']['object']['key']
        key = unquote_plus(key)
        tmpkey = key.replace('/', '')
        download_path = '/tmp/{}'.format(tmpkey)
        upload_path = '/tmp/resized-{}'.format(tmpkey)
        s3_client.download_file(bucket, key, download_path)
        resize_image(download_path, upload_path)

        s3_client.upload_file(upload_path, bucket+'-resized', key)
