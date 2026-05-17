import requests 
import scr.Utils.logger as logger
from scr.config.config import AUTH_ENDPOINT, BASE_URL, PASSWORD, PRODUCT_ENDPOINT, USERNAME

class ProductServices:

    def __init__(self):
        self.base_url = BASE_URL
        self.username = USERNAME
        self.password = PASSWORD

    def product_details(self):
        URL = self.base_url + PRODUCT_ENDPOINT
        response = requests.get(URL)
        logger.info(f"Product details response status: {response.status_code}")
        return response.json() if response.status_code == 200 else None
            
print("Product Services module imported successfully!", ProductServices())
