import os

import requests
from dotenv import load_dotenv

from utils.logger import get_logger


load_dotenv()


class ReqresClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.logger = get_logger(self.__class__.__name__)
        api_key = os.getenv("REQRES_API_KEY")

        if not api_key:
            raise ValueError(
                "REQRES_API_KEY is required. Configure it in a local .env file "
                "or as a GitHub Actions repository secret."
            )

        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "x-api-key": api_key,
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
