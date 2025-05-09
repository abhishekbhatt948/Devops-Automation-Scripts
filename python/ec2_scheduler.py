# ec2_scheduler.py
import boto3
from datetime import datetime

INSTANCE_ID = 'i-0123456789abcdef0'
REGION = 'us-east-1'

ec2 = boto3.client('ec2', region_name=REGION)
current_hour = datetime.now().hour

if 9 <= current_hour < 18:
    print("Starting EC2 instance")
    ec2.start_instances(InstanceIds=[INSTANCE_ID])
else:
    print("Stopping EC2 instance")
    ec2.stop_instances(InstanceIds=[INSTANCE_ID])