import os

import requests
from dotenv import load_dotenv

from utils.logger import get_logger


load_dotenv()


class ReqresClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.logger = get_logger(self.__class__.__name__)
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "x-api-key": os.getenv(
                    "REQRES_API_KEY",
                    "free_user_3EKJqFeUD8Y2tnBD7IoxTE7Cttr",
                ),
            }
        )

    def get_user(self, user_id):
        url = f"{self.base_url}/api/users/{user_id}"
        self.logger.info("GET %s", url)
        return self.session.get(url, timeout=10)

    def create_user(self, payload):
        url = f"{self.base_url}/api/users"
        self.logger.info("POST %s", url)
        return self.session.post(url, json=payload, timeout=10)

    def delete_user(self, user_id):
        url = f"{self.base_url}/api/users/{user_id}"
        self.logger.info("DELETE %s", url)
        return self.session.delete(url, timeout=10)
