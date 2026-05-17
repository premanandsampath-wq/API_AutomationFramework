import pytest
#from scr.config.Service import settings
from scr.core.http_client import HttpClient
from scr.config.Service.auth_service import AuthService

@pytest.fixture(scope="session")
def http_client():
    return HttpClient(settings["base_url"])

@pytest.fixture(scope="session")
def auth_service(http_client):
    return AuthService(http_client, settings)

@pytest.fixture(scope="session")
def token(auth_service):
    return auth_service.login()
