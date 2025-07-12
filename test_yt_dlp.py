# test_yt_dlp.py

import yt_dlp
import json

url = (
    "https://www.afl.com.au/video/1362116/"
    "match-replay-gold-coast-v-collingwood"
    "?videoId=1362116&modal=true"
    "&type=video&publishFrom=1752258600001"
    "&limit=50"
    "&tagNames=ProgramCategory%3AMatch%20Replays"
    "&references=AFL_COMPSEASON%3A73%2CAFL_ROUND%3A1164"
)

opts = {
    "quiet": False,
    "skip_download": True,
}
with yt_dlp.YoutubeDL(opts) as ydl:
    info = ydl.extract_info(url, download=False)

print(json.dumps(info, indent=2))
