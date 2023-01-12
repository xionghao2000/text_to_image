import json
import uuid
from http import HTTPStatus
from urllib.parse import urlparse

import boto3
import requests


def get_client(region: str, aws_access_key_id: str, aws_secret_access_key: str, endpoint_url: str = None):
    # create s3 client
    s3 = boto3.resource('s3', region_name=region)
    client = boto3.client('s3', region_name=region, aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key, endpoint_url=endpoint_url)
    return client


def get_image_key(bucket_folder: str=None):
    # use uuid as filename
    filename = str(uuid.uuid4()) + '.png'
    key = bucket_folder + '/' + filename if bucket_folder is not None else filename
    return key


def get_image_url(client, key: str, imageContent: bytes, bucketname: str, download_endpoint: str):
    # upload image to s3
    client.put_object(Body=imageContent, Bucket=bucketname,
                      Key=key, ContentType='image/png')
    # get url
    url = download_endpoint + "/" + bucketname + "/" + key
    return url


def text_to_image(img_url, token, prompt, negative_prompt="",
                  width=512, height=512,
                  ):
    url = img_url + '/api/dev/dev_text_to_image'
    data = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "width": width,
        "height": height,

        "number_of_image": 1,
        "random_seed": True,

        "token": token
    }

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    res = requests.post(url, data=json.dumps(data), headers=headers)
    if res.status_code == HTTPStatus.OK:
        resObj = json.loads(res.text)

        if 'success' in resObj and resObj['success'] == True:
            for urlPath in resObj['data']['list_image']:
                computing_second = resObj['data']['computing_second']

                imageUrl = img_url + urlPath
                reqImage = requests.get(imageUrl)
                if reqImage.status_code == 200:
                    urlParse = urlparse(imageUrl)
                    return reqImage.content

    return None, "", 0
