Feature: Contact US
  Scenario: Verify Contact US Page
    Given Launch contact us page
    When verify get in touch form
    Then enter name email subject and msg
    And verify success msg
    And click on submit