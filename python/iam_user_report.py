# iam_user_report.py
import boto3
import csv

iam = boto3.client('iam')
users = iam.list_users()['Users']

with open('iam_users.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['UserName', 'CreateDate', 'PasswordLastUsed'])
    for user in users:
        writer.writerow([user['UserName'], user['CreateDate'], user.get('PasswordLastUsed')])