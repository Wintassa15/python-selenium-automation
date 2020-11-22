# Created by wintana at 10/1/20
Feature: Test Scenarios for orders functionality
  # Enter feature description here

  Scenario: Verify Sign in page appears
    Given Open Amazon page
    When select Orders
    Then Sign in page opens

  Scenario: Verify Shopping Cart is Empty
   Given Open Amazon
   When click on Cart
   Then verify shopping cart is empty

  Scenario: Amazon Music has 7 menu items
  Given Open Amazon page
  When Click on hamburger menu
  And Click on Amazon Music menu item
  Then 7 menu items are present

    Scenario: Verify size selection appears
      Given Open Amazon product page
      When Hoover over add to cart button
      Then Verify size selection tooltip appears

      Scenario: User can select and search in a department
        Given Open Amazon Page
        When Select Books Department
        And Search for Faust
        Then Verify books department is selected

        Scenario: User can search and select through baby  department
          Given Open Amazon Page
          When Select Baby Department
          And Search for VTech Pull and Sing Puppy
          Then Verify Baby department is selected

          Scenario:Verify that the user sees the deals in New arrivals.
            Given Open Amazon B074TBCSC8 product item
            When hoover over New arrivals
            Then Verify user sees all the deals

          

