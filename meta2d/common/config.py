import os

from dotenv import dotenv_values
_config = dotenv_values(".env")

BUCKET_NAME = os.getenv("AWS_BUCKET_NAME", "image-bucket-123")
TOKEN = os.getenv("AWS_TOKEN", "123")
IMAGE_URL = os.getenv("IMAGE_URL", "http://localhost:5000")
REGION = os.getenv("AWS_REGION", "ap-east-1")