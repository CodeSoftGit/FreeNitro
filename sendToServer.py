from gen import generate
import webhook
from dotenv import load_dotenv
load_dotenv()
import os

maxGen = os.getenv("codes")
i = 1
while i < maxGen+1:
    webhook.send(generate())
    i+=1