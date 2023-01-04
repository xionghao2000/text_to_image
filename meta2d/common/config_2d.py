from dataclasses import dataclass


@dataclass
class Config2D:
    BUCKET_NAME: str
    TOKEN: str
    IMAGE_URL: str
    REGION: str
