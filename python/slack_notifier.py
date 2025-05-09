# slack_notifier.py
import requests

WEBHOOK_URL = 'https://hooks.slack.com/services/XXX/YYY/ZZZ'
message = {"text": "Deployment completed successfully."}

r = requests.post(WEBHOOK_URL, json=message)
print(f"Slack notification status: {r.status_code}")