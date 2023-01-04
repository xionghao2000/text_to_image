import os

from dotenv import dotenv_values
_config = dotenv_values(".env")

BUCKET_NAME = _config.get("AWS_BUCKET_NAME", "image-bucket-123")
TOKEN = _config.get("AWS_TOKEN", "123")
IMAGE_URL = _config.get("IMAGE_URL", "http://localhost:5000")
REGION = _config.get("AWS_REGION", "ap-east-1") 