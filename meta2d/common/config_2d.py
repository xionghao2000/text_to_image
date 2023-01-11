from dataclasses import dataclass


@dataclass
class Config2D:
    BUCKET_NAME: str
    TOKEN: str
    IMAGE_URL: str
    REGION: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str