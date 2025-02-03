Feature: Home Screen
  launch Home Screen and Verify Few Things
  Scenario: Sections Check
    Given Launch Home screen
    Then Verify Scrolling Ad
    And verify category Text
    And Verify Brand Text
    And verify feature Text



  Scenario: Subscription section
    Given Launch Home Screen
    Then Scroll down to bottom of page
    And Verify Subscription Text

  Scenario: Add to cart a product
    Given Launch Home screen
    Then click view product
    And Verify Product URL open
    And Verify Product title


