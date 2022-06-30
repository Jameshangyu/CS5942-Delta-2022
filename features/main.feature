Feature: main
""" 
Confirm that we can browse the index page
"""

Scenario: Access index page
    Given I navigate to the index page
    When The page opens
    Then I should see the details for the form

