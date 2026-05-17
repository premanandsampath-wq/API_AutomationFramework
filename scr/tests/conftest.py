import os
import datetime
import pytest
from scr.services.product_services import ProductServices 
from scr.services.Authorisation import Authorisation
import logging
import playwright.sync_api as syncplaywrite

@pytest.fixture(scope="module")
def product_services():
    return ProductServices()

@pytest.fixture(scope="session")
def  AuthServices():
     return Authorisation()  



@pytest.fixture(scope = "session")
def auth_token(AuthServices):
    auth_response = AuthServices.auth_login(AuthServices.username, AuthServices.password)
    if not auth_response:
        return None
    auth_json = auth_response.json()
    return auth_json.get("token") or auth_json.get("accessToken")

@pytest.fixture(scope="session")
def token_validation_outcome(AuthServices, auth_token):
    return AuthServices.test_getme_token(auth_token)


def pytest_configure(config):
    if not hasattr(config.option, "htmlpath"):
        return

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_dir = os.path.join(config.rootpath, "reports")
    os.makedirs(report_dir, exist_ok=True)
    config.option.htmlpath = os.path.join(report_dir, f"report_{timestamp}.html")
#====================Logger ========================
# Create logs directory if not exists
    log_dir = os.path.join("scr", "logs")
    os.makedirs(log_dir, exist_ok=True)

    # Generate timestamped filename
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = os.path.join(log_dir, f"test_run_{timestamp}.log")

    # Configure logging
    logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s")
    # Tell pytest where to write log
    config.option.log_file = log_file 

    #=================================================================
    @pytest.fixture(scope="session") 
    def browser():
        with syncplaywrite() as p:
            browser = p.chromium.launch(headless=False)
            yield browser
            browser.close() 

    @pytest.fixture(scope="session")
    def page(browser):
     context = browser.new_context()
     page = context.new_page()
     yield page
     context.close()