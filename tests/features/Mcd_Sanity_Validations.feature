@McDAppValidations
Feature: McD App User Functionality

@TC_01 @TC_02
Scenario: Verify login with valid Mobile Number and OTP
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    Then   I verify profile page navigation


@TC_03
Scenario: Verify that profile page is incomplete after login
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    Then   I verify profile page navigation
    Then   I verify profile page is incomplete


@TC_04
Scenario: Verify that user able to land on Home page after succefully completed profile page 
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    Then   I verify profile page navigation
    Then   I verify profile page is incomplete
    When   I add the profile details
    Then   I verify home page navigation


@TC_05 @TC_06
Scenario: Verify that user able to add one address
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    Then   I verify profile page navigation
    Then   I verify profile page is incomplete
    When   I add the profile details
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I click on add new button and search for location
    And    I select address from search results
    Then   I verify address is added and selected
    When   I click on restaurants nearby in home page
    Then   I verify nearby restaurants are diplayed


@TC_07 @TC_08
Scenario: Verify that user able to add multiple product with customization and coke convergence
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    Then   I verify profile page navigation
    Then   I verify profile page is incomplete
    When   I add the profile details
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I click on add new button and search for location
    And    I select address from search results
    Then   I verify address is added and selected
    When   I add multiple product with customization and coke convergence
    Then   I verify the product added in cart
    When   I click on view cart button
    Then   I verify product is visible on cart page with price without GST


