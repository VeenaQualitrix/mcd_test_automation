@McdRegression
Feature: McD App Functionality

@TC_Login_001 @sanity
Scenario Outline: Verify login with valid Mobile Number and OTP
    Given I open the Chrome browser
    When I launch <appURL>
    Then I verify website opened successfully
    When I click on view icon
    Then I verify view page navigation
    When I click on login or signup button
    Then I verify login page navigation
    When I enter a valid mobile number and click verify
    And I enter the OTP and click verify
    Then I verify home page navigation
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_LOGIN_002
Scenario Outline: Verify referral code input
    Given  I open the Chrome browser
    When   I launch <appURL>
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I click on referral link
    And    I enter referral code 
    Then   I verify referral code accepted without error
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|



@TC_LOGIN_003
Scenario Outline: Validate empty mobile number
    Given  I open the Chrome browser
    When   I launch <appURL>
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I leave mobile field empty and click verify
    Then   I verify error message
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|



@TC_LOGIN_004
Scenario Outline: Validate short mobile number
    Given  I open the Chrome browser
    When   I launch <appURL>
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a mobile number with less than 10 digits and click verify
    Then   I verify error message
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_LOGIN_005
Scenario Outline: Validate alphabetic input in mobile field
    Given  I open the Chrome browser
    When   I launch <appURL>
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter alphabets in mobile number field and click verify
    Then   I verify error message
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_LOGIN_006
Scenario Outline: Verify referral code without entering mobile number
    Given  I open the Chrome browser
    When   I launch <appURL>
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I click on referral link
    And    I enter referral code and click verify
    Then   I verify error message
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_LOGIN_007
Scenario Outline: Verify mobile number with spaces
    Given  I open the Chrome browser
    When   I launch <appURL>
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter mobile number with spaces and click verify
    Then   I verify error message
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_LOGIN_008
Scenario Outline: Verify mobile number with special characters
    Given  I open the Chrome browser
    When   I launch <appURL>
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter mobile number with spacial characters and click verify
    Then   I verify error message
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_LOGIN_009
Scenario Outline: Verify UI alignment and presence of elements
    Given  I open the Chrome browser
    When   I launch <appURL>
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I visually inspect the mobile number field
    And    I visually inspect the referral link section
    And    I visually inspect the verify button
    And    I visually inspect the footer links
    Then   I verify all elements should be visible, correctly aligned, and not overlapping
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_LOGIN_010
Scenario Outline: Verify referral link is clickable
    Given  I open the Chrome browser
    When   I launch <appURL>
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I click on referral link
    Then   I verify referral link is clickable
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_LOGIN_011
Scenario Outline: Validate "Verify Mobile" button is disabled initially
    Given  I open the Chrome browser
    When   I launch <appURL>
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I click on verify mobile button without mobile number entered
    Then   I verify error message
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_LOGIN_012
Scenario Outline: Verify navigation after successfully entetered a valid mobile number
    Given  I open the Chrome browser
    When   I launch <appURL>
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    Then   I verify OTP page navigation
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_LOGIN_013
Scenario Outline: Verify terms and conditions link
    Given  I open the Chrome browser
    When   I launch <appURL>
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I click terms and conditions link
    Then   I verify user is redirected to terms and conditions page
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_LOGIN_014
Scenario Outline: Enter exactly 10 digit valid mobile number
    Given  I open the Chrome browser
    When   I launch <appURL>
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    Then   I verify mobile number accepted and redirected to next page
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_LOGIN_015
Scenario Outline: Enter 11 digits mobile number and verify
    Given  I open the Chrome browser
    When   I launch <appURL>
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter 11 digits mobile number
    Then   I verify field should restrict to 10 digits
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_LOGIN_016
Scenario Outline: Verify clipboard paste into mobile field
    Given I open the Chrome browser
    When I launch <appURL>
    Then I verify website opened successfully
    When I click on view icon
    Then I verify view page navigation
    When I click on login or signup button
    Then I verify login page navigation
    When I copied a mobile number
    When I paste the number with Ctrl V and click verify
    Then I verify number pasted correctly and accepted
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_LOGIN_017
Scenario Outline: Verify mobile field input limit
    Given  I open the Chrome browser
    When   I launch <appURL>
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter more than 10 digits mobile number and click verify
    Then   I verify field should restrict to 10 digits
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

