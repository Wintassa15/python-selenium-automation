# Created by wintana at 10/31/20
Feature: open amazon applications from Terms of Conditions


  Scenario: User can open and close Amazon Applications
     Given Open Amazon T&C page
     When Store original windows
     And Click on Amazon applications link
     And Switch to the newly opened window
     Then Amazon app page is opened
    And User can close new window and switch back to original


