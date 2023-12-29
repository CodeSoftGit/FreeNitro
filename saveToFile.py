from gen import generate
import webhook
import os
from dotenv import load_dotenv
load_dotenv()

maxGen = int(os.getenv("codes"))
i = 1
while i < maxGen+1:
    with open("codes.txt", "a") as file:
        file.write(generate() + "\n")
    i+=1