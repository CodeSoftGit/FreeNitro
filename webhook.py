import requests
from dotenv import load_dotenv
load_dotenv()
import os

url = os.getenv("webhookURL")

querystring = {"wait":"true"}
def send(content):
    payload = {
        "content": f"{content}",
        "embeds": None,
        "attachments": []
    }
    headers = {
        "authority": "discord.com",
        "accept": "application/json",
        "accept-language": "en",
        "content-type": "application/json",
        "origin": "https://discohook.org",
        "referer": "https://discohook.org/",
        "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "sec-gpc": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

    return response.text