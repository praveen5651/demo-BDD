Feature: Search Functionality

  Scenario: Search for existing products
    Given Launch Home screen
    When Click on products
    And Search for men
    And Click Search icon
    Then Validate results

@Praveen
 Scenario Outline: Checking mutiple things
    Given Launch Home screen
    When Click on products
    And Search for <product>
    And Click Search icon
    Then Validate results

    Examples:
      |product |
      |kids    |
      |men     |
      |women   |
      |polo    |
      |H&M     |
      |BIBA    |
