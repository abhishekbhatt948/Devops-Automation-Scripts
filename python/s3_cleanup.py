# s3_cleanup.py
import boto3
from datetime import datetime, timezone, timedelta

BUCKET = 'my-bucket-name'
PREFIX = 'logs/'
DAYS_OLD = 30

s3 = boto3.client('s3')
cutoff = datetime.now(timezone.utc) - timedelta(days=DAYS_OLD)

response = s3.list_objects_v2(Bucket=BUCKET, Prefix=PREFIX)
if 'Contents' in response:
    for obj in response['Contents']:
        if obj['LastModified'] < cutoff:
            print(f"Deleting {obj['Key']}")
            s3.delete_object(Bucket=BUCKET, Key=obj['Key'])