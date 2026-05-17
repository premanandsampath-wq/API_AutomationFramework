
from scr.Utils import logger
from scr.config.config import BASE_URL, USERNAME, PASSWORD, AUTH_ENDPOINT, TOKEN_VALIDATION_ENDPOINT
import requests
from  scr.core.API_Client import APIClient
class Authorisation:

    logger.info("Authorisation module imported successfully!")
    def __init__(self):  
        self.auth = APIClient(baseurl=BASE_URL, endpoint=AUTH_ENDPOINT) 
        self.token = APIClient(baseurl=BASE_URL, endpoint=TOKEN_VALIDATION_ENDPOINT)
        self.base_url = BASE_URL
        #self.auth_endpoint = AUTH_ENDPOINT
        #self.token_validation_endpoint = TOKEN_VALIDATION_ENDPOINT
        self.username = USERNAME
        self.password = PASSWORD

    def auth_login(self, username=None, password=None):
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        payload = {
            "username": self.username,
            "password": self.password,
        }
        response = self.auth.post(data=payload)
        logger.info(f"Login response status: {response.status_code}")
        if response.status_code == 200:
                logger.info("Login successful!")
                return response
        elif response.status_code == 400:
                logger.warning("Login failed: Bad Request. Check your credentials.")
                return response
        return response
         
    def test_getme_token(self, auth_token):
        url = self.base_url + self.token_validation_endpoint
        headers = {"Authorization": f"Bearer {auth_token}"}
        response = requests.get(url, headers=headers)
        response_code = response.status_code
        print("Status:", response_code)
        if response_code == 200:
            print("Token is valid!")
            data = response.json()
            print("Response data:", data) 
            logger.info(f"json response: {data}")
            return data
        else:
            print("Token is invalid or expired.")
            logger.warning("Token is invalid or expired.")
            return None
