Feature: Add cart page
  Add/remove products, handle shipping in swag application.

  Background:
    Given user launch browser

  Scenario Outline: Validate the product page, when we log in as the standard user
    When I fill the username : <username>  and password : <password> on the login page
    And I click login button on the loginpage
    Then I navigate to product page
    And I wil check that the product is visible on the product page.

    Examples:
      | username      | password     |
      | standard_user | secret_sauce |

  Scenario Outline: validate whether the user can place an order with random product
    When I fill the username : <username>  and password : <password> on the login page
    And I click login button on the loginpage
    And I navigate to product page
    And I click on random product
    And I processed to cart with random product
    Then I validate the product as successful ordered.

    Examples:
      | username      | password     |
      | standard_user | secret_sauce |

  Scenario Outline: Validate the least product price and order the product
    When I fill the username : <username>  and password : <password> on the login page
    And I click login button on the loginpage
    And I navigate to product page
    Then I validate the least product price on the product page
    And I processed to cart with random product
    And I validate the product as successful ordered.


    Examples:
      | username      | password     |
      | standard_user | secret_sauce |