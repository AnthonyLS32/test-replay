# test_replay_page.py

import requests
from bs4 import BeautifulSoup

url = (
    "https://www.afl.com.au/video/1362116/"
    "match-replay-gold-coast-v-collingwood"
    "?videoId=1362116&modal=true"
    "&type=video&publishFrom=1752258600001"
    "&limit=50"
    "&tagNames=ProgramCategory%3AMatch%20Replays"
    "&references=AFL_COMPSEASON%3A73%2CAFL_ROUND%3A1164"
)

resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
print("Status Code:", resp.status_code)

bs = BeautifulSoup(resp.text, "html.parser")
video_tag = bs.find("video")
print("Video tag found:", bool(video_tag))

for src in bs.find_all("source"):
    print(" Source src= ", src.get("src"))
