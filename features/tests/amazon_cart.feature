# Created by wintana at 10/10/20
Feature:  Test Scenario for items in cart
  # Enter feature description here

  Scenario: Verify number of items in cart
    Given open amazon website
    When input teddy bear into search field
    And click on search icon
    Then select an item
    And add to cart
    And verify number of items