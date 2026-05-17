from pytest_bdd import scenarios, given, when, then
from scr.services.Authorisation import Authorisation 

scenarios("login.feature")

@given("I have valid login credentials", target_fixture="valid_credentials")
def valid_credentials():
    return {
        "username": "emilys",
        "password": "emilyspass"
    }   

@when("I call the login API", target_fixture="response")
def call_login_api(valid_credentials): 
    auth_service = Authorisation()
    response = auth_service.auth_login(valid_credentials["username"], valid_credentials["password"])
    return response

@then("the response status code should be 200")
def check_status_code(response):
    assert response.status_code == 200

@then("the response should contain a valid token")
def check_valid_token(response):
    json_data = response.json()
    assert "token" in json_data or "accessToken" in json_data