import sys
if "../" not in sys.path:
    sys.path.append("../")
import requests

day = 1

with open("session_id.txt", "r") as f:
    session_id = f.read()

headers = {"user_agent": "AOC Data Fetcher"}

raw_data = requests.get(f"https://adventofcode.com/2024/day/{day}/input", cookies={"session":session_id}, headers=headers)

with open(f"data\\raw\\day_{day}.txt", "w") as f:
    f.write(raw_data.text)