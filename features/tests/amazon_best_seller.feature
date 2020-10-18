# Created by wintana at 10/16/20
Feature: Test best sellers page
  # Enter feature description here

  Scenario: verify the links of bestsellers
    Given Open Amazon page
    When open Bestsellers
    Then Verify there are 5 links