import boto3
import json


from lamlib import hello


def handler(event, context):
    bucket_name = event.get("s3Bucket")
    s3_key = event.get("s3Key")

    _h = hello()
    h = {"hello": _h}

    s3.put_object(Bucket=bucket_name, Key=f"{s3_key}.json", Body=json.dumps(h))
