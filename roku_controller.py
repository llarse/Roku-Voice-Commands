import requests
import dotenv
import os
import json

# The rokus IP is stored in the .env file
dotenv.load_dotenv()


class RokuController:
    def __init__(self):
        self.roku_ip = os.getenv("ROKUIP")
        with open('config.json', 'r') as f:
            self.config = json.load(f)

    def send_command(self, command):
        url = f"http://{self.roku_ip}:8060/keypress/{command}"
        try:
            requests.post(url)
            print(f"Sent command: {command}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending command to Roku: {e}")
