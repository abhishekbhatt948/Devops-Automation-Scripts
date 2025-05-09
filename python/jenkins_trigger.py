# jenkins_trigger.py
import requests

JENKINS_URL = 'https://jenkins.example.com/job/myjob/build'
API_TOKEN = 'your_token'
USER = 'admin'

r = requests.post(JENKINS_URL, auth=(USER, API_TOKEN))
print(f"Triggered Jenkins job: {r.status_code}")