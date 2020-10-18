# Created by wintana at 10/10/20
Feature:  Test Scenario for items in cart
  # Enter feature description here

  Scenario: Verify number of items in cart
    Given open amazon website
    When input teddy bear into search field
    And click on the product
    And click on add to cart
    Then verify number of items