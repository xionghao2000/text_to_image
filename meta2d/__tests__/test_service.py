import re
from services.image_service  import get_client,get_image_key,get_url

def test_get_client():
    client = get_client()
    assert client is not None

def test_get_image_key():
    key = get_image_key()
    
    # want to make sure the key follows `b/.*.png` pattern using regex
    reg = re.compile(r'b/.*.png')
    assert reg.match(key) is not None

class MokeClient:
    def put_object(self, Body, Bucket, Key, ContentType):
        pass
    
def test_get_url():
    client = MokeClient()
    key = get_image_key()
    imageContent = b'123'
    url = get_url(client, key, imageContent)
    reg = re.compile(r'https://s3..*.amazonaws.com/.*/b/.*.png')
    assert reg.match(url) is not None

