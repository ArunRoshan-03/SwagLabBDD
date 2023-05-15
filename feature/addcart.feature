Feature: Add cart page
  Add/remove products, handle shipping in swag application.

  Background:
    Given user launch browser

  Scenario Outline: Validate the product page, when we log in as the standard user
    When I fill the username : <username>  and password : <password> on the login page
    And I click login button on the loginpage
    And I navigate to home page
    Then I wil check that the product is visible on the product page.

    Examples:
      | username      | password     |
      | standard_user | secret_sauce |

  Scenario Outline: Validate the filter button by clicking the option name (Z to A).
    When I fill the username : <username>  and password : <password> on the login page
    And I click login button on the loginpage
    And I navigate to home page
    And I click the filter button and select "name (Z to A)".
    Then I validate the product list by clicking the filter button.

    Examples:
      | username      | password     |
      | standard_user | secret_sauce |