Feature: Add cart page
  Add/remove products, handle shipping in swag application.

  Background:
    Given user launch browser and user enter swag labs url
    And I navigated to the swagLabs login_page is displayed


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
    And I navigate to the cart_page
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
    And I navigate to the cart_page
    And I processed to cart with random product
    And I validate the product as successful ordered.


    Examples:
      | username      | password     |
      | standard_user | secret_sauce |

  Scenario Outline: Validate whether user is able to add multiple items to cart
    When I fill the username : <username>  and password : <password> on the login page
    And I click login button on the loginpage
    And I navigate to product page
    And I add multiple_items to cart
    And I navigate to the cart_page
    And I processed to cart with multiple products
    Then I validate the product as successful ordered.

    Examples:
      | username      | password     |
      | standard_user | secret_sauce |

  Scenario Outline: Validate whether user is able to continue shopping, when selected items are available in cart page
    When I fill the username : <username>  and password : <password> on the login page
    And I click login button on the loginpage
    And I add multiple_items to cart
    And I navigate to the cart_page
    And I click continue_shopping on the cart_page
    Then I validate the product page

    Examples:
      | username      | password     |
      | standard_user | secret_sauce |


  Scenario Outline: Validate whether user is able to remove particular items from cart page
    When I fill the username : <username>  and password : <password> on the login page
    And I click login button on the loginpage
    And I add multiple_items to cart
    And I navigate to the cart_page
    Then I validate particular item remove from cart

    Examples:
      | username      | password     |
      | standard_user | secret_sauce |

  Scenario Outline: Validate whether user is able to remove all items from cart page
    When I fill the username : <username>  and password : <password> on the login page
    And I click login button on the loginpage
    And I add multiple_items to cart
    And I navigate to the cart_page
    And I remove all items from cart
    Then I validate the empty cart_page

    Examples:
      | username      | password     |
      | standard_user | secret_sauce |