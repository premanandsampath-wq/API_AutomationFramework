import requests 
from scr.core.logger import get_logger

logger = get_logger(__name__)

class HttpClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def _url(self, path):
        return f"{self.base_url}{path}"

    def post(self, path, json=None, headers=None):
        url = self._url(path)
        logger.info(f"POST {url}")
        return requests.post(url, json=json, headers=headers)

    def get(self, path, headers=None):
        url = self._url(path)
        logger.info(f"GET {url}")
        return requests.get(url, headers=headers)

