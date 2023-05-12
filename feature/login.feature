Feature: Swag lab login page

  Background:
    Given user launch browser
    And user enters the swag labs url and is taken to the swag labs web page

  Scenario: validate the login credentials on the login page
    When The user should check their credentials on the login page.
    Then I validate login credentials on the login page

  Scenario Outline: validate home page, when user log with valid credentials
    When I fill the username <username> and password <password> on login page
    And I click login button on the loginpage
    Then I validate the home_page

    Examples:
      | username      | password     |
      | standard_user | secret_sauce |