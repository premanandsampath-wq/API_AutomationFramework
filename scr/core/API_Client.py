import logging
import time
import requests
from scr.config.config import BASE_URL, USERNAME, PASSWORD, AUTH_ENDPOINT, TOKEN_VALIDATION_ENDPOINT

class APIClient:
    def __init__(self, baseurl=BASE_URL, endpoint=AUTH_ENDPOINT, retries=3, delay=2):
        self.baseurl = baseurl
        self.endpoint = endpoint
        self.retries = retries
        self.delay = delay
        logging.info(f"APIClient initialized with base URL: {self.baseurl} and endpoint: {self.endpoint}")

    def retry_request(self, method, url, **kwargs):
        for attempt in range(self.retries + 1):
            response = requests.request(method, url, **kwargs)
            if response.status_code == 200:
                return response
            logging.warning(f"Request failed with status code {response.status_code} on attempt {attempt + 1}")
            if attempt < self.retries:
                logging.info(f"Retrying in {self.delay} seconds...")
                time.sleep(self.delay)
            else:
                logging.error("All retry attempts failed.")
                response.raise_for_status()
        return response

    def get(self, headers=None):
        url = self.baseurl + self.endpoint
        logging.info(f"Making GET request to URL: {url}")
        return self.retry_request("GET", url, headers=headers)

    def post(self, data=None):
        url = self.baseurl + self.endpoint
        logging.info(f"Making POST request to URL: {url} with data: {data}")
        return self.retry_request("POST", url, json=data)
