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

@TC_PP_01
Scenario: Verify that user update the name successfully 
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I edits the full name field with Test User01 and clicks Save Changes
    Then   I verify home page navigation
    And    I verify updated name should be reflected on the profile
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_02
Scenario: Verify empty name field 
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I clear name field
    Then   I verify error message Please enter valid full name should be displayed
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_03
Scenario: Validate invalid characters in name field 
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I enter invalid characters in name field
    Then   I verify error message Please enter valid full name should be displayed
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_06
Scenario: update email address
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I edits email address and clicks Save Changes
    Then   I verify home page navigation
    And    I verify updated email address should be reflected on the profile
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_07
Scenario: Validate incorrect email format
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I enter incorrect email format in email field
    Then   I verify error message enter valid email address should be displayed
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_08
Scenario: update date of birth successfully
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I selects a new valid date of birth and clicks Save Changes
    Then   I verify home page navigation
    And    I verify updated date of birth should be reflected on the profile
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_09
Scenario: validate future date of birth selection is not allowed
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I enter a future date in the date of birth field
    Then   I verify user are unable to select future Date of birth
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_10
Scenario: Verify Change Picture link opens photo upload
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I click change picture link
    Then   I verify upload pop up opens with file selection option
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_11
Scenario: Verify that the Save button is disabled when any mandatory field is empty.
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I clear name field
    Then   I verify the Save button should be disabled
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_12
Scenario: Verify Toggle color blind mode on/off
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I switch toggle on/off and observe UI
    Then   I verify Color scheme updates to accessible version page should be displayed
        

@TC_PP_13
Scenario: Verify color blind preference saved
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I switch toggle to make color blind mode on and reload page
    Then   I verify preference retained after refresh
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_15
Scenario: Verify changes not get saved after refreshing page 
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I make changes and refresh browser
    Then   I verify page reloads with old saved data
        |appURL|
        |https://www.uat.mcdapp.co|



@TC_PP_16
Scenario: Verify field icons are displayed correctly
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I Check icon presence near each field
    Then   I verify the Correct icons for name, phone, email, DOB
        |appURL|
        |https://www.uat.mcdapp.co|


@TC_Address_Login_01
Scenario: Verify Trigger login when clicking “Add Address” as guest
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on any item to add into a cart
    Then   I verify items details pop up opened successfully
    When   I click on next
    And    I click on Add to cart option
    Then   I verify selected item get added into a cart
    When   I click on add address
    Then   I verify user redirected to login/signup prompt
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_Address_Login_02
Scenario: Verify Successful login redirects to “Add Address” screen
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on add address
    Then   I verify user redirected to login/signup prompt
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    Then   I verify home page navigation
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_Address_Login_03
Scenario: Verify Cancel login from “checkout” page
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on add address
    Then   I verify user redirected to login/signup prompt
    When   I click on cancel button from login/signup pop up
    Then   I verify Login cancelled anduser returned to checkout page
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_Address_Login_04
Scenario: Verify Incorrect login from “Add Address” screen
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on add address
    Then   I verify user redirected to login/signup prompt
    When   I enter incorrect number in mobile number field and click verify
    Then   I verify error message
        |appURL|
        |https://www.uat.mcdapp.co|