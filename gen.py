import requests
import webhook
import json
import time
import os

def random_hex_string(length=32):
    return os.urandom(length).hex()

url = "https://api.discord.gx.games/v1/direct-fulfillment"

def generate():
    payload = {"partnerUserId": random_hex_string()}
    headers = {
        "authority": "api.discord.gx.games",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://www.opera.com",
        "referer": "https://www.opera.com/",
        "sec-ch-ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    data = json.loads(response.text)
    return f'https://discord.com/billing/partner-promotions/1180231712274387115/{data["token"]}'