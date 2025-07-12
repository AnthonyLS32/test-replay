# test_listing_json.py

import requests
from bs4 import BeautifulSoup
import json

listing_url = (
    "https://www.afl.com.au/video?"
    "tagNames=ProgramCategory%3AMatch%20Replays&limit=10"
)
resp = requests.get(listing_url, headers={"User-Agent": "Mozilla/5.0"})
print("Listing status:", resp.status_code)

bs = BeautifulSoup(resp.text, "html.parser")
blobs = bs.find_all("script", type="application/json")
print("Found JSON scripts:", len(blobs))

for i, sc in enumerate(blobs):
    try:
        data = json.loads(sc.string)
        print(f"Blob {i} top keys:", list(data.keys())[:10])
    except Exception as e:
        print(f"Blob {i} parse error:", e)
