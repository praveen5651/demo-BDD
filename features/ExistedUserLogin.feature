Feature: Existed Login User
  Scenario: Login With Existed User
    Given Launch Home screen
    Then click signup up
    And Enter existed "username" and "password"
    And click login
    And Verify Logout button in screen



  Scenario Outline: Checking mutiple things
    Given Launch Home screen
    Then click signup up
    And Enter existed "<username>" and "<password>"
    And click login

    Examples:
    |username|password|
    |pppp22@gmail.com|123456789|
    |p@gmail.com     |125897454|
    |pp@gmail.com    |369852147|






