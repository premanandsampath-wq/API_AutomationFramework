Feature: login
  @api
  Scenario: Successful login with valid credentials
    Given I have valid login credentials
    When I call the login API
    Then the response status code should be 200
    And the response should contain a valid token