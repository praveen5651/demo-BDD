Feature: New User SignUp
  A user can able to signup
  Scenario: Login with fresh account
    Given Launch Home screen
    Then click signup up
    And enter name and mail in new user section
    When Validate Enter account Information text
    Then Enter mandatory feilds
    And  click Create Account
    And Verify Account Created MSG

