Feature: Swag lab login page

  Background:
    Given user launch browser and user enter swag labs url
    And I navigated to the swagLabs login_page is displayed

  Scenario: validate the login credentials on the login page
    Then I validate login credentials on the login page

  Scenario Outline: validate the home page for different types of logged users
    When I fill the username <username> and password <password> on login_page
    And I click login button on the loginpage
    Then I validate the home_page with various users.

    Examples:
      | username                | password     |
      | standard_user           | secret_sauce |
      | problem_user         | secret_sauce |
      | performance_glitch_user | secret_sauce |

