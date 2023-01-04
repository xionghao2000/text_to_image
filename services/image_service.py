from fileinput import filename
from http import client
import json
import os
from urllib.parse import urlparse
import uuid
import boto3
import requests
from http import HTTPStatus
from meta2d.common import config


def get_client(region: str = config.REGION):
    # create s3 client
    s3 = boto3.resource('s3', region_name=region)
    client = boto3.client('s3', region_name=region)
    return client


def get_image_key(bucket_folder: str = 'b'):
    # use uuid as filename
    filename = str(uuid.uuid4()) + '.png'
    key = bucket_folder + '/' + filename
    return key


def get_url(client, key: str, imageContent: bytes, bucketname: str = config.BUCKET_NAME, region: str = 'ap-east-1'):
    # upload image to s3
    client.put_object(Body=imageContent, Bucket=bucketname,
                      Key=key, ContentType='image/png')
    # get url
    url = "https://s3." + region + ".amazonaws.com/" + bucketname + "/" + key
    return url


def text_to_image(prompt, negative_prompt="",
                  width=512, height=512,
                  token=config.TOKEN):
    url = config.IMAGE_URL + '/api/dev/dev_text_to_image'
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

                imageUrl = config.IMAGE_URL + urlPath
                reqImage = requests.get(imageUrl)
                if reqImage.status_code == 200:
                    urlParse = urlparse(imageUrl)
                    return reqImage.content

    return None, "", 0
