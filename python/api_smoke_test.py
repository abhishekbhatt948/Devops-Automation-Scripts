# api_smoke_test.py
import requests

URLS = ['https://example.com/health', 'https://example.com/api/status']

for url in URLS:
    try:
        r = requests.get(url)
        if r.status_code == 200:
            print(f"OK: {url}")
        else:
            print(f"FAIL: {url} - {r.status_code}")
    except Exception as e:
        print(f"ERROR: {url} - {e}")