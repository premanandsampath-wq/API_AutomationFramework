
Feature: Authentication

  Scenario: Successful login
    Given I have valid credentials
    When I request a token
    Then I should receive a valid JWT token