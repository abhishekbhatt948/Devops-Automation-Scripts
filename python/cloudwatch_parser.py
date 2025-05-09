# cloudwatch_parser.py
import boto3
import time

group = '/aws/lambda/my-function'
log = boto3.client('logs')
streams = log.describe_log_streams(logGroupName=group, orderBy='LastEventTime', descending=True)['logStreams']

for stream in streams:
    events = log.get_log_events(logGroupName=group, logStreamName=stream['logStreamName'])
    for event in events['events']:
        if 'ERROR' in event['message']:
            print(event['message'])