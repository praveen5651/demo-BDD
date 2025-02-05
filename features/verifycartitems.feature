Feature: Add To Cart
  Scenario: Verify Items are adding to cart
    Given Launch Home screen
    Given Launch Home screen
    When Click on products
    And Search for men
    And Click Search icon
    Then Validate results
    And add item to cart and validate success msg

