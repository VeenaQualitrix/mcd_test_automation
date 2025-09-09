@McdRegression
Feature: McD App Functionality

@TC_Login_001 @sanityweb1
Scenario Outline: Verify login with valid Mobile Number and OTP
    Given I open the Chrome browser
    When  I hit the URL
    Then  I verify website opened successfully
    When  I click on view icon
    Then  I verify view page navigation
    When  I click on login or signup button
    Then  I verify login page navigation
    When  I enter a valid mobile number and click verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    Then  I verify home page navigation
    When  I click on user profile icon
    Then  I verify profile page navigation
    And   I click on Logout button
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_LOGIN_002 @sanityweb1
Scenario Outline: Verify referral code input
    Given  I open the Chrome browser
    When   I hit the URL
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



@TC_LOGIN_003 @sanityweb1
Scenario Outline: Validate empty mobile number
    Given  I open the Chrome browser
    When   I hit the URL
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



@TC_LOGIN_004 @sanityweb1
Scenario Outline: Validate short mobile number
    Given  I open the Chrome browser
    When   I hit the URL
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

@TC_LOGIN_005 @sanityweb1
Scenario Outline: Validate alphabetic input in mobile field
    Given  I open the Chrome browser
    When   I hit the URL
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

@TC_LOGIN_006 @sanityweb1
Scenario Outline: Verify referral code without entering mobile number
    Given  I open the Chrome browser
    When   I hit the URL
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

@TC_LOGIN_007 @sanityweb1
Scenario Outline: Verify mobile number with spaces
    Given  I open the Chrome browser
    When   I hit the URL
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

@TC_LOGIN_008 @sanityweb1
Scenario Outline: Verify mobile number with special characters
    Given  I open the Chrome browser
    When   I hit the URL
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

@TC_LOGIN_009 @sanityweb
Scenario Outline: Verify UI alignment and presence of elements
    Given  I open the Chrome browser
    When   I hit the URL
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

@TC_LOGIN_010 @sanityweb
Scenario Outline: Verify referral link is clickable
    Given  I open the Chrome browser
    When   I hit the URL
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

@TC_LOGIN_011 @sanityweb
Scenario Outline: Validate "Verify Mobile" button is disabled initially
    Given  I open the Chrome browser
    When   I hit the URL
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

@TC_LOGIN_012 @sanityweb
Scenario Outline: Verify navigation after successfully entetered a valid mobile number
    Given  I open the Chrome browser
    When   I hit the URL
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

@TC_LOGIN_013 @sanityweb1
Scenario Outline: Verify terms and conditions link
    Given  I open the Chrome browser
    When   I hit the URL
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

@TC_LOGIN_014 @sanityweb
Scenario Outline: Enter exactly 10 digit valid mobile number
    Given  I open the Chrome browser
    When   I hit the URL
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

@TC_LOGIN_015 @sanityweb
Scenario Outline: Enter 11 digits mobile number and verify
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter 11 digits mobile number and click verify
    Then   I verify field should restrict to 10 digits
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_LOGIN_016 @sanityweb
Scenario Outline: Verify clipboard paste into mobile field
    Given I open the Chrome browser
    When I hit the URL
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

@TC_LOGIN_017 @sanityweb
Scenario Outline: Verify mobile field input limit
    Given  I open the Chrome browser
    When   I hit the URL
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

@TC_PP_01 @sanityweb
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
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation 
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I edits the full name field with Test User01 and clicks Save Changes
    Then   I verify home page navigation
    And    I verify updated name should be reflected on the profile
    And    I click on Logout button
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_02 @sanityweb
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
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation 
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I clear name field
    Then   I verify error message Please enter valid full name should be displayed
    When   I click McDelivery icon
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I click on Logout button
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_03 @sanityweb
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
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I enter invalid characters in name field
    Then   I verify error message Please enter valid full name should be displayed
    When   I click McDelivery icon
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I click on Logout button
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_06 @sanityweb
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
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I edits email address and clicks Save Changes
    Then   I verify home page navigation
    And    I verify updated email address should be reflected on the profile
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I clear email field
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I click on Logout button
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_07  @sanityweb
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
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I enter incorrect email format in email field
    Then   I verify error message enter valid email address should be displayed
    When   I click McDelivery icon
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I click on Logout button
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_08 @sanityweb
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
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I selects a new valid date of birth and clicks Save Changes
    Then   I verify updated date of birth should be reflected on the profile
    And    I click on Logout button
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_09 @sanityweb
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
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    And    I verify user are unable to select future Date of birth
    When   I click McDelivery icon
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I click on Logout button
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_10 @sanityweb
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
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I click change picture link
    Then   I verify upload pop up opens with file selection option
    When   I click McDelivery icon
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I click on Logout button
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_11 @sanityweb
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
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I clear name field
    Then   I verify the Save button should be disabled
    When   I click McDelivery icon
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I click on Logout button
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_12 @sanityweb
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
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I switch toggle on/off and observe UI
    Then   I verify Color scheme updates to accessible version page should be displayed
    When   I click McDelivery icon
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I click on Logout button
        

@TC_PP_13 @sanityweb
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
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I switch toggle to make color blind mode on and reload page
    Then   I verify preference retained after refresh
    When   I click McDelivery icon
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I click on Logout button
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_15 @sanityweb
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
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I make changes and refresh browser
    Then   I verify page reloads with old saved data
    When   I click McDelivery icon
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I click on Logout button
        |appURL|
        |https://www.uat.mcdapp.co|



@TC_PP_16 @sanityweb
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
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I click on edit profile icon
    Then   I verify user is on the profile edit page
    When   I Check icon presence near each field
    Then   I verify the Correct icons for name, phone, email, DOB
    When   I click McDelivery icon
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I click on Logout button
        |appURL|
        |https://www.uat.mcdapp.co|


@TC_Address_Login_01 @sanityweb
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

@TC_Address_Login_02 @sanityweb
Scenario: Verify Successful login redirects to “Add Address” screen
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on add address in home page
    Then   I verify user redirected to login/signup prompt
    When   I click on login/signup prompt
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on user profile icon
    Then   I click on Logout button
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_Address_Login_03 @sanityweb
Scenario: Verify Cancel login from “checkout” page
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I browse the menu and return to the homepage
    And    I navigate to the cart
    When   I click on login/signup prompt from checkout
    Then   I verify login page navigation from checkout page
    When   I click on cancel button from login/signup pop up
    Then   I verify Login cancelled and user returned to checkout page
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_Address_Login_04 @sanityweb
Scenario: Verify Incorrect login from “Add Address” screen
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on add address in home page
    Then   I verify user redirected to login/signup prompt
    When   I click on login/signup prompt
    Then   I verify login page navigation
    When   I enter incorrect number in mobile number field and click verify
    Then   I verify error message
        |appURL|
        |https://www.uat.mcdapp.co|


@TC_Address_Login_06 @sanityweb
Scenario: Add new delivery address during checkout
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I browse the menu and return to the homepage
    And    I navigate to the cart
    When   I click on add address from checkout page
    And    I click on add new button and search for location
    And    I select address from search results
    Then   I verify address is added and selected
    And    I verify the address should appear as the selected delivery address
        |appURL|
        |https://www.uat.mcdapp.co|


@TC_Address_Login_07 @sanityweb
Scenario: verify adding address with missing mandatory fields
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on add address in home page
    Then   I verify user redirected to login/signup prompt
    When   I click on login/signup prompt
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I click on add new button and click confirm location
    When   I leave mandatory field empty and click save address
    Then   I verify that the address not saved and validation error should be displayed
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_Address_Login_09 @sanityweb
Scenario: verify adding address with special characters
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on add address in home page
    Then   I verify user redirected to login/signup prompt
    When   I click on login/signup prompt
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I click on add new button and click confirm location
    When   I enter special character in house/flat field and click save address
    Then   I verify field accept characters and address will get saved
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_Address_Login_11 @sanityweb
Scenario: verify clicking cancel button before saving address
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on add address in home page
    Then   I verify user redirected to login/signup prompt
    When   I click on login/signup prompt
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    And    I verify saved delivery address
    When   I click on add address in home page
    And    I click on add new button and click confirm location
    When   I enter text in house/flat field and click back button without saving
    Then   I verify address will not get saved
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_Address_Login_15 @sanityweb
Scenario: verify adding duplicate address
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on add address in home page
    Then   I verify user redirected to login/signup prompt
    When   I click on login/signup prompt
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I click on add new button and click confirm location
    When   I enter text in house/flat field and click save address
    And    I click on add address in home page
    Then   I verify System allows address duplication based on business logic
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_001 @sanityweb
Scenario: Verify dropdown displays all business models
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click the business model dropdown
    Then   I verify Dropdown shows: McDelivery, Dine-In, On the Go, Take Away
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_002 @sanityweb
Scenario: Validate user can select “McDelivery” and proceed
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click the business model dropdown
    And    I select the McDelivery option from dropdown
    Then   I verify User is taken to the McDelivery ordering flow
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_003 @sanityweb
Scenario: Validate user can select “Dine-In” and proceed
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click the business model dropdown
    And    I select Dine-In option from dropdown
    Then   I verify User navigates to Dine-In selection/location flow
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_004 @sanityweb
Scenario: Validate user can select “On the Go” and proceed
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click the business model dropdown
    And    I select on the go option from dropdown
    Then   I verify User is prompted to choose pick-up location
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_005 @sanityweb
Scenario: Validate user can select “Take Away” and proceed
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click the business model dropdown
    And    I select Take Away option from dropdown
    Then   I verify User proceeds to place an order for take away
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_006 @sanityweb
Scenario: Ensure selected model persists during session
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click the business model dropdown
    And    I select Dine-In option from dropdown
    And    I search the address from serchbar abd select the address
    And    I browse the menu and return to the homepage
    Then   I verify Dine-In remains the selected option until manually changed
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_013 @sanityweb
Scenario: Check location permission prompt for “On the Go” or “Dine-In”
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click the business model dropdown
    And    I select Dine-In option from dropdown
    Then   I verify a prompt should appear requesting location permission
    When   I click the business model dropdown
    And    I select Take Away option from dropdown
    Then   I verify a prompt should appear requesting location permission
        |appURL|
        |https://www.uat.mcdapp.co|


@TC_BM_012 @sanityweb
Scenario: Verify default business model on first visit
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    And    I verify “McDelivery” should be selected by default
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_014 @sanityweb
Scenario: Validate no restaurant available for selected model
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click the business model dropdown
    And    I select a business model in an unsupported region
    Then   I should see the message: “Sorry, we do not serve this location yet”
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_015 @sanityweb
Scenario: Ensure no multiple model selection at once
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click the business model dropdown
    And    I select the first model
    And    I select the second model
    Then   I verify only one model should remain active at a time
        |appURL|
        |https://www.uat.mcdapp.co|


@TC_BM_019 @sanityweb
Scenario: Verify model selection persists across tabs (same session)
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click the business model dropdown
    And    I select Take Away option from dropdown
    And    I open a new tab in the same session
    Then   I verify the same business model should remain selected
    When   I click on user profile icon
    Then   I click on Logout button
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_020 @sanityweb
Scenario: Test visual feedback on hover on desktop
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click the business model dropdown
    And    I hover over each business model option
    Then   I verify the icons and text should respond visually
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_021 @sanityweb
Scenario: Verify Switching models does not alter profile information
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    And    I verify the user notes their current profile information
    When   I click the business model dropdown
    And    I verify user switches from one model to another
    And    I verify user navigates to the profile page
    Then   I verify the profile information should remain unchanged
    And    I click on Logout button
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_022 @sanityweb
Scenario: Verify Switching between models updates the UI layout appropriately
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click the business model dropdown
    And    I select the first model
    Then   I verify the page layout or menu should adapt to match the first model
    When   I select the second model
    Then   I verify the page layout or menu should adapt to match the second model
    When   I select the third model
    Then   I verify the page layout or menu should adapt to match the third model
    When   I select the fourth model
    Then   I verify the page layout or menu should adapt to match the fourth model
    When   I click on user profile icon
    Then   I click on Logout button
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_AD_001 @sanityweb
Scenario: verify selecting existing delivery address
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I user click on a listed address
    Then   I verify the address is selected and restaurant list should update accordingly
    When   I click on user profile icon
    Then   I click on Logout button
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_AD_002 @sanityweb
Scenario: Verify adding a new delivery address
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I click on add new button and search for location
    And    I select address from search results
    Then   I verify address is added and selected
    And    I verify restaurant list should be refreshed accordingly
    When   I click on user profile icon
    Then   I click on Logout button
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_AD_003 @sanityweb
Scenario: Verify editing an existing address
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I click the edit icon next to an address
    And    I modifies the address details and click save button
    Then   I verify updated address is shown in the address list
    When   I click on user profile icon
    Then   I click on Logout button
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_AD_004 @sanityweb
Scenario: Verify deleting an existing address
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I verify address list shown
    And    I click the delete icon next to an address
    Then   I verify address removed from list
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_AD_005 @sanityweb
Scenario: Ensure address selection updates nearby restaurant list
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I selects the first address from the address list
    Then   I verify restaurant list should update based on the first address location
    When   I click on add address in home page
    And    I selects the second address from the address list
    Then   I verify restaurant list should update based on the second address location
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_AD_006 @sanityweb
Scenario: Validate empty address cannot be saved
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I click on add new button and click confirm location
    Then   I verify user redirected to address fill in details page
    When   I leave mandatory field empty and click save address
    Then   I verify that the address not saved and validation error should be displayed
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_AD_007 @sanityweb
Scenario: Verify "Near" location shown under each address
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I verify address list displayed
    Then   I verify each address should display a Near label with its location description
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_AD_008 @sanityweb
Scenario: Ensure scroll functionality works if many addresses are saved
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I verify address list displayed
    And    I scrolls through the address list
    Then   I verify all saved addresses should be accessible via scrolling
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_AD_010 @sanityweb
Scenario: Verify error handling for invalid or undeliverable address
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I enters an undeliverable pin code or area manually
    Then   I verify an error message should be displayed saying Delivery not available at this address
        |appURL|
        |https://www.uat.mcdapp.co|


@TC_AD_011  @sanityweb
Scenario: Default address selection on login
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    Then   I verify the most recently used address should be auto-selected
        |appURL|
        |https://www.uat.mcdapp.co|


@TC_AD_012 @sanityweb
Scenario: Ensure “Add New” opens address entry popup or page
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I click on add new button and click confirm location
    Then   I verify address entry popup or page should be displayed
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_AD_013
Scenario: Ensure Address list remains consistent after logout and login
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I verify address list before logout of the application
    When   I click on user profile icon
    Then   I verify profile page navigation
    When   I logs out of the application
    And    I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on add address in home page
    Then   I verify previously saved addresses should be retained and visible
        |appURL|
        |https://www.uat.mcdapp.co|


@TC_AD_018
Scenario: Verify user can tag an address as "Home", "Work", etc.
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I adds an address and select a tag
    And    I click on add address in home page
    Then   I verify the tag should be displayed next to the address name after adding address
    When   I edits an address and select a tag
    And    I click on add address in home page
    Then   I verify the tag should be displayed next to the address name after editing address
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_AD_017
Scenario: Verify behavior when all addresses are deleted
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I delete all addresses
    Then   I verify the address list should be empty and the Add Address prompt should be visible
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_ORDER_003 @testmcd1
Scenario: Check customization option availability
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on 'Add +' for the customizable item
    Then   I verify the customization options should appear before adding the item to the cart
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_ORDER_004 @testmcd1
Scenario: Add multiple items to cart
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I add 2 to 3 different available items to the cart
    And    I navigate to the cart
    Then   I verify all added items should be listed in the cart with correct price and quantities
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_ORDER_006 @testmcd1
Scenario: Ensure menu item prices are correctly displayed and reflected in cart
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I user views the price of a menu item
    And    I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the item price should be correctly displayed in the cart
    And    I verify the price in the cart should match the menu price
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_ORDER_007 @testmcd1
Scenario: Prevent adding items marked as sold out
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I selects the second address from the address list
    And    I Click back button from select location page
    And    I user is on the menu page and sees an item marked as 'Sold out'
    Then   I verify the item should not be clickable and unable to add to cart
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_ORDER_010 
Scenario: View 3Pc Meals
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I selects the address from the address list
    And    I Click back button from select location page
    And    I selects the '3Pc Meals' category under menu
    Then   I verify all items under the '3Pc Meals' category should be displayed
    When   I select any product from the '3Pc Meals' category and click on Add to cart 
    Then   I verify the product added in cart
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_ORDER_016 @testmcd1
Scenario: Customize burger before adding to cart
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on 'Add +' for the customizable item
    And    I click on next
    And    I click on Add to cart option
    Then   I verify selected item get added into a cart
    When   I clicks on the 'Customize' button
    And    I selects or removes items from the customization options
    Then   I verify the customized item should be added to the cart with selected preferences
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_ORDER_024 @testmcd1
Scenario: Remove item from the cart
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I add 2 to 3 different available items to the cart
    And    I navigate to the cart
    Then   I verify the added items in cart
    When   I clicks the 'Remove' button for an item
    Then   I verify the selected item should be removed from the cart
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_ORDER_025 @testmcd1
Scenario: Update item quantity in cart
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    When   I clicks the 'Add' button for an item
    And    I clicks the 'Add' button for an item
    And    I clicks the 'Remove' button for an item
    Then   I verify the Quantity updates correctly
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_ORDER_026 @testmcd1
Scenario: Check total price calculation
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I add 2 to 3 different available items to the cart
    And    I navigate to the cart
    Then   I verify the total payable amount should be displayed
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_ORDER_029 @testmcd1
Scenario: Validate cart icon does not appear on the homepage if the cart is empty
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    And    I verify the cart icon doesn not appear on the homepage if the cart is empty
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_002 @testmcd1
Scenario: Update item quantity
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    And    I verify total payable amount
    When   I clicks the 'Add' button for an item
    And    I clicks the 'Add' button for an item
    And    I clicks the 'Remove' button for an item
    Then   I verify the Quantity updates correctly
    And    I verify total price recalculates
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_003 @testmcd1
Scenario: Verify clear cart when items are already in cart
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    When   I click on the 'Clear All' button
    Then   I verify home page navigation
    And    I verify the cart icon doesn not appear on the homepage if the cart is empty
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_009 @testmcd1
Scenario: Prompt user to log in before proceeding with order
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on any item to add into a cart
    Then   I verify items details pop up opened successfully
    When   I click on next
    And    I click on Add to cart option
    Then   I verify selected item get added into a cart
    When   I click on login/signup prompt from checkout
    Then   I verify login page navigation from checkout page
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_015 @testmcd1
Scenario: Redirect user to login when attempting checkout without being logged in
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on any item to add into a cart
    Then   I verify items details pop up opened successfully
    When   I click on next
    And    I click on Add to cart option
    Then   I verify selected item get added into a cart
    When   I click on login/signup prompt from checkout
    Then   I verify login page navigation from checkout page
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_016 @testmcd1
Scenario: Remove item from cart by decreasing quantity to zero
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    When   I click the '-' button beside the item until the quantity becomes 0
    Then   I verify the item should be removed from the cart and pop up appears
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_020 @testmcd1
Scenario: Verify cart persists after browser refresh
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I add the random item to the cart
    And    I refresh the page
    Then   I verify the cart should retain the previously added items
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_010 @testmcd1
Scenario: Verify 'Know More' for charity donation
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on any item to add into a cart
    Then   I verify items details pop up opened successfully
    When   I click on next
    And    I click on Add to cart option
    Then   I verify selected item get added into a cart
    And    I verify checkbox and link visible
    When   I click on 'Know More' link
    Then   I verify Info opens about the charity
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_011 @testmcd1
Scenario: Select charity donation checkbox
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on any item to add into a cart
    Then   I verify items details pop up opened successfully
    When   I click on next
    And    I click on Add to cart option
    Then   I verify selected item get added into a cart
    And    I verify checkbox and link visible
    When   I clicks the charity donation checkbox to opt-in
    Then   I verify ₹3 should be added to the total payable amount
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_012 @testmcd1
Scenario: Uncheck charity donation checkbox
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on any item to add into a cart
    Then   I verify items details pop up opened successfully
    When   I click on next
    And    I click on Add to cart option
    Then   I verify selected item get added into a cart
    And    I verify checkbox and link visible
    When   I clicks the charity donation checkbox to opt-in
    Then   I verify the charity donation option is visible and selected
    When   I unchecks the charity donation checkbox
    Then   I verify ₹3 should be removed from the total payable amount
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_013 @testmcd1
Scenario: View all available offers
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on any item to add into a cart
    Then   I verify items details pop up opened successfully
    When   I click on next
    And    I click on Add to cart option
    Then   I verify selected item get added into a cart
    And    I verify 'View All' link visible
    When   I click on 'View All' link
    Then   I verify the user should be redirected to a page displaying all available offers
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_014 @testmcd1
Scenario: Ensure currency symbol is correctly shown for all price components
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on any item to add into a cart
    Then   I verify items details pop up opened successfully
    When   I click on next
    And    I click on Add to cart option
    Then   I verify selected item get added into a cart
    When   I reviews all prices in the order summary
    Then   I verify each price should be prefixed with the ₹ symbol
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_005 @testmcd1
Scenario: Validate total price breakdown in order summary
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on any item to add into a cart
    Then   I verify items details pop up opened successfully
    When   I click on next
    And    I click on Add to cart option
    Then   I verify selected item get added into a cart
    When   I checks the price breakdown on the right side of the page
    Then   I verify the subtotal, handling charges, CGST, and SGST should be displayed and match the total payable amount
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_025 @testmcd1
Scenario: Validate behavior with an expired promo code
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on any item to add into a cart
    Then   I verify items details pop up opened successfully
    When   I click on next
    And    I click on Add to cart option
    Then   I verify selected item get added into a cart
    When   I click on 'View All' link
    Then   I verify the user should be redirected to a page displaying all available offers
    When   I enter the expired promo code and click search
    And    I click on offer Apply button and select button
    Then   I verify a message should be displayed indicating that the code is invalid or expired
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_028 @testmcd1
Scenario: Ensure guest checkout not allowed
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on any item to add into a cart
    Then   I verify items details pop up opened successfully
    When   I click on next
    And    I click on Add to cart option
    Then   I verify selected item get added into a cart
    When   I click on login/signup prompt from checkout
    Then   I verify login page navigation from checkout page
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_001 @testmcd1
Scenario: Validate cart contains correct item details
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    And    I verify item name in cart
    And    I verify total payable amount
    And    I verify the Quantity updates correctly
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_006 @testmcd1
Scenario: Add Delivery Instructions on Checkout Page
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on any item to add into a cart
    Then   I verify items details pop up opened successfully
    When   I click on next
    And    I click on Add to cart option
    Then   I verify selected item get added into a cart
    When   I click on 'Add Delivery Instructions'
    And    I enters special notes in the instructions field
    Then   I verify the instructions field should accept the input
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_029 @testmcd1
Scenario: Add special characters in delivery instruction
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on any item to add into a cart
    Then   I verify items details pop up opened successfully
    When   I click on next
    And    I click on Add to cart option
    Then   I verify selected item get added into a cart
    When   I click on 'Add Delivery Instructions'
    And    I enters special characters in the instructions field
    Then   I verify the special characters should accepted in instructions field
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_022 @testmcd1
Scenario: Update quantity for multiple items in cart
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I add 2 to 3 different available items to the cart
    And    I navigate to the cart
    Then   I verify all added items should be listed in the cart with correct price and quantities
    And    I verify total payable amount
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_007 @newtestmcd1
Scenario: Validate subtotal after all additions
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    And    I verify subtotal for a single added item
    When   I add item from recommendation
    Then   I verify subtotal for all added items
    When   I click on the 'Clear All' button
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_008 @testmcd1
Scenario: Validate tax calculation in cart
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on any item to add into a cart
    Then   I verify items details pop up opened successfully
    When   I click on next
    And    I click on Add to cart option
    Then   I verify selected item get added into a cart
    When   I Check CGST and SGST breakdown
    Then   I verify tax percentage should be calculated accurately
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_019 @testmcd1
Scenario: Validate estimated delivery time visibility
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I selects the address from the listed addres
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    And    I verify the estimated delivery time displayed below the delivery address
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_021 @newtestmcd1
Scenario: Apply Multiple Promo Codes
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on any item to add into a cart
    Then   I verify items details pop up opened successfully
    When   I click on next
    And    I click on Add to cart option
    Then   I verify selected item get added into a cart
    When   I click on 'View All' link
    Then   I verify the user should be redirected to a page displaying all available offers
    When   I apply the first promo code
    Then   I verify that the offer is applied and click on 'Change Offer'
    When   I apply the second promo code
    Then   I verify that the first offer is removed and the second offer is displayed
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_023 @newtestmcd1
Scenario: Display applied offer discount in the order summary
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    And    I verify total amount from order summary
    When   I click on 'View All' link
    Then   I verify the user should be redirected to a page displaying all available offers
    When   I apply the first promo code
    Then   I verify the discount should be clearly shown and deducted in the order summary
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_CO_026 @newtestmcd1
Scenario: Check total with delivery charges added
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    And    I verify sub total includes delivery charge
    When   I click on the 'Clear All' button
        |appURL|
        |https://www.uat.mcdapp.co|


@TC_SM_001 @newtestmcd1
Scenario Outline: Search for an existing menu item
    Given I open the Chrome browser
    When I launch <appURL>
    Then I verify website opened successfully
    When I click on homepage search icon
    Then I verify search menu page navigation
    When I enters 'Fries' in the search bar
    Then I verify the search results should display items matching 'Fries'
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_SM_002 @newtestmcd1
Scenario Outline: Search for an non-existing menu item
    Given I open the Chrome browser
    When I launch <appURL>
    Then I verify website opened successfully
    When I click on homepage search icon
    Then I verify search menu page navigation
    When I enters '$%^#' in the search bar
    Then I verify 'No matching items found' message is displayed
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|


@TC_SM_003 @newtestmcd1
Scenario Outline: User attempts to search with empty input
    Given I open the Chrome browser
    When I launch <appURL>
    Then I verify website opened successfully
    When I click on homepage search icon
    Then I verify search menu page navigation
    When I clicks the search button without typing anything
    Then I verify no action should be taken and prompt is displayed
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_SM_004 @newtestmcd1
Scenario Outline: Filter menu items by Veg option
    Given I open the Chrome browser
    When I launch <appURL>
    Then I verify website opened successfully
    When I click on homepage search icon
    Then I verify search menu page navigation
    When I clicks the 'Veg' filter button
    Then I verify only Veg items should be displayed in the menu
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_SM_005 @newtestmcd1
Scenario Outline: Filter menu items by Non-Veg option
    Given I open the Chrome browser
    When I launch <appURL>
    Then I verify website opened successfully
    When I click on homepage search icon
    Then I verify search menu page navigation
    When I clicks the 'Non-Veg' filter button
    Then I verify only Non-Veg items should be displayed in the menu
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_SM_006 @newtestmcd1
Scenario Outline: Search Burger while Veg filter is active
    Given I open the Chrome browser
    When I launch <appURL>
    Then I verify website opened successfully
    When I click on homepage search icon
    Then I verify search menu page navigation
    When I clicks the 'Veg' filter button
    And  I search for 'Burger'
    Then I verify only Veg Burger items should be displayed in the menu
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_SM_007 @newtestmcd1
Scenario Outline: Clear search and reset filters
    Given I open the Chrome browser
    When I launch <appURL>
    Then I verify website opened successfully
    When I click on homepage search icon
    Then I verify search menu page navigation
    When I enters 'Fries' in the search bar
    Then I verify the search results should display items matching 'Fries'
    When I clears the search input
    Then I verify Default view restored and no filters should be applied
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_SM_008 @newtestmcd1
Scenario Outline: Add item to cart from search result
    Given  I open the Chrome browser
    When   I launch <appURL>
    Then   I verify website opened successfully
    When   I click on homepage search icon
    Then   I verify search menu page navigation
    When   I search for 'Burger'
    And    I add a 'Burger' item to the cart
    And    I navigate to the cart
    Then   I verify item added to the cart and quantity updated
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_SM_009 @newtestmcd1
Scenario Outline: Search term and results persist after adding an item to the cart
    Given I open the Chrome browser
    When I launch <appURL>
    Then I verify website opened successfully
    When I click on homepage search icon
    Then I verify search menu page navigation
    When I search for 'Burger'
    And  I add a 'Burger' item to the cart
    Then I verify the search results for 'Burger' should still be displayed
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|


@TC_SM_013 @newtestmcd1
Scenario Outline: Verify placeholder text in search input
    Given I open the Chrome browser
    When I launch <appURL>
    Then I verify website opened successfully
    When I click on homepage search icon
    Then I verify search menu page navigation
    And  I verify the placeholder text should be displayed as 'Search here'
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_SM_015 @newtestmcd1
Scenario Outline: Toggle Veg filter on and off
    Given I open the Chrome browser
    When I launch <appURL>
    Then I verify website opened successfully
    When I click on homepage search icon
    Then I verify search menu page navigation
    When I clicks the 'Veg' filter button
    And  I clicks the close icon of 'Veg' filter button
    Then I verify the default view should be restored
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_SM_017 @newtestmcd2
Scenario Outline: Search persists after page reload
    Given I open the Chrome browser
    When I launch <appURL>
    Then I verify website opened successfully
    When I click on homepage search icon
    Then I verify search menu page navigation
    When I search for 'Burger'
    And  I refresh the page
    Then I verify the default view should be restored
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_SM_018 
Scenario Outline: Product Search from Excel/CSV Data
    Given I open the Chrome browser
    When I launch <appURL>
    Then I verify website opened successfully
    When I reads the list of product names from the Excel/CSV file
    And  I searches for each product from the file
    Then I verify user should see the complete list of products as expected from the Excel/CSV data
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_OFFER_001 @newtestmcd2
Scenario: Verify offer page input field is visible and functional
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    When   I click on 'View All' link
    Then   I verify the user should be redirected to a page displaying all available offers
    And    I verify the input box for entering the coupon code should be visible and accept text input
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_OFFER_002 @newtestmcd2
Scenario: Validate manual coupon entry and search
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    When   I click on 'View All' link
    Then   I verify the user should be redirected to a page displaying all available offers
    When   I user enters a valid coupon code 'FLAT10' into the input box
    Then   I verify an offer card with the code 'FLAT10' should appear
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_OFFER_003 @newtestmcd2
Scenario: Validate offer cards display correctly
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    When   I click on 'View All' link
    Then   I verify the user should be redirected to a page displaying all available offers
    When   I enters a valid coupon code into the input box
    Then   I verify each offer card should displays code, description, Show More link, and Apply button
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_OFFER_004 @newtestmcd2
Scenario: Verify Apply offer coupon functionality
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    When   I click on 'View All' link
    Then   I verify the user should be redirected to a page displaying all available offers
    When   I enters a valid coupon code and clicks on the Apply button
    Then   I verify selected coupon should be applied to the current cart
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_OFFER_005 @newtestmcd2
Scenario: Validate cart value restrictions
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    When   I click on 'View All' link
    Then   I verify the user should be redirected to a page displaying all available offers
    When   I enters a valid coupon code 'FLAT10' and clicks on the Apply button
    Then   I verify a warning should appear with the message 'Promo not applied'
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_OFFER_006 @newtestmcd2
Scenario: Validate cart value eligibility for coupon application
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    When   I capture the total amount before applying the promo
    When   I click on 'View All' link
    Then   I verify the user should be redirected to a page displaying all available offers
    When   I enters a valid coupon code and clicks on the Apply button
    Then   I verify the discount should be successfully applied
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_OFFER_008 @newtestmcd2
Scenario: Validate one coupon per order policy
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on any item to add into a cart
    Then   I verify items details pop up opened successfully
    When   I click on next
    And    I click on Add to cart option
    Then   I verify selected item get added into a cart
    When   I click on 'View All' link
    Then   I verify the user should be redirected to a page displaying all available offers
    When   I apply the first promo code
    Then   I verify that the offer is applied and click on 'Change Offer'
    When   I apply the second promo code
    Then   I verify new coupon should override the previous one
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_OFFER_009 @newtestmcd2
Scenario: Validate expired or inactive coupon codes
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on any item to add into a cart
    Then   I verify items details pop up opened successfully
    When   I click on next
    And    I click on Add to cart option
    Then   I verify selected item get added into a cart
    When   I click on 'View All' link
    Then   I verify the user should be redirected to a page displaying all available offers
    When   I enter the expired promo code and click search
    And    I click on offer Apply button and select button
    Then   I verify a message should be displayed indicating that the code is invalid or expired
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_OFFER_010 @newtestmcd2
Scenario: Verify applied offer is reflected in order summary

    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    When   I capture the total amount before applying the promo
    When   I click on 'View All' link
    Then   I verify the user should be redirected to a page displaying all available offers
    When   I enters a valid coupon code and clicks on the Apply button
    Then   I verify the discount should be successfully applied
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_OFFER_011 @newtestmcd2
Scenario: Validate UI Responsiveness for Offer Page
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    When   I click on 'View All' link
    And    I window is resized
    Then   I verify the offer layout should adapt responsively to the screen size
    And    I verify all buttons and interactive elements should remain functional
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_OFFER_012 @newtestmcd2
Scenario: Validate Offer Tags on Product Cards
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    When   I click on 'View All' link
    Then   I verify the user should be redirected to a page displaying all available offers
    When   I user enters a valid coupon code 'FLAT10' into the input box
    Then   I verify the offer tags such as 'FLAT 10 OFF' should be clearly visible
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_OFFER_013 @newtestmcd2
Scenario: Verify multiple offers are shown in a scrollable  or paginated if many exists
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    When   I click on 'View All' link
    Then   I verify the user should be redirected to a page displaying all available offers
    And    I verify the offers should appear in a scrollable or paginated format without any visual breakage
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PAY_001 @newtestmcd2
Scenario: Verify redirection to payment page after placing an order
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I selects the address from the listed addres
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    When   I click on pay button in view cart page
    Then   I verify user should be redirected to the payment page successfully
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PAY_002 @newtestmcd2
Scenario: Verify display of order summary
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I selects the address from the listed addres
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    And    I verify gross price and total price are same
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PAY_003 @newtestmcd2
Scenario: Verify available payment methods on the payment page
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    When   I click on add address from checkout page
    And    I selects the address from the listed addres
    And    I click on pay button in view cart page
    Then   I verify user should be redirected to the payment page successfully
    And    I verify all supported payment methods should be listed
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PAY_005 @newtestmcd2
Scenario: Validate incorrect UPI ID
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    When   I click on add address from checkout page
    And    I selects the address from the listed addres
    And    I click on pay button in view cart page
    Then   I verify user should be redirected to the payment page successfully
    When   I selects UPI as the payment method
    And    I enters an invalid UPI ID and clicks the Pay button
    Then   I verify an error message should be displayed saying 'Invalid UPI ID'
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PAY_007 @newtestmcd2
Scenario: Validate card details input with invalid information
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    When   I click on add address from checkout page
    And    I selects the address from the listed addres
    And    I click on pay button in view cart page
    Then   I verify user should be redirected to the payment page successfully
    When   I selects Card as the payment method
    And    I enters an invalid card number and clicks the Pay button
    Then   I verify a validation error message should be displayed 
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PAY_009 @newtestmcd2
Scenario: Select Cash on Delivery Payment Option
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    When   I click on add address from checkout page
    And    I selects the address from the listed addres
    And    I click on pay button in view cart page
    Then   I verify user should be redirected to the payment page successfully
    When   I selects Cash on Delivery as the payment method
    And    I click the 'Proceed To Pay' button
    Then   I verify a confirmation message should be displayed saying 'Pay at Door'
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PAY_011 @newtestmcd2
Scenario: Validate navigation from Payment Page to Cart
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    When   I click on add address from checkout page
    And    I selects the address from the listed addres
    And    I click on pay button in view cart page
    Then   I verify user should be redirected to the payment page successfully
    When   I clicks the 'Back to Cart' button
    Then   I verify the user should be redirected to the cart page
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PAY_013 @newtestmcd2
Scenario: Verify secure payment indicators on payment screen
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    When   I click on add address from checkout page
    And    I selects the address from the listed addres
    And    I click on pay button in view cart page
    Then   I verify user should be redirected to the payment page successfully
    And    I verify security indicators should be visible
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_OH_001 @newtestmcd2
Scenario: Verify that the user is able to view order history
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on view icon
    And    I click on 'My Orders'
    Then   I verify order history should be displayed on the screen
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_OH_002 @newtestmcd2
Scenario: Navigate to Post-Payment Page from Order History
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on view icon
    And    I click on 'My Orders'
    Then   I verify order history should be displayed on the screen
    When   I click on 'Order Tracking'
    Then   I verify the user should be navigated to the post-payment page
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_OH_003 @newtestmcd2
Scenario: Validate that the order status is reflected in each order card
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on view icon
    And    I click on 'My Orders'
    Then   I verify user should be able to see the order status displayed on each order card
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_OH_004 @newtestmcd2
Scenario: Validate that the order status matches in order tracking on the post-payment page
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on view icon
    And    I click on 'My Orders'
    And    I click on 'Order Tracking' for completed order
    Then   I verify the completed order status on the post-payment page should match the status displayed on the order card
    When   I click on 'Order Tracking' for cancelled order
    Then   I verify the cancelled order status on the post-payment page should match the status displayed on the order card
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_OH_005 @newtestmcd2
Scenario: Verify that the user is able to view order history cards with Business model name
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on view icon
    And    I click on 'My Orders'
    Then   I verify each order card should display the respective Business model name
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_OH_006 @newtestmcd2
Scenario: Verify that the page scrolls up and down to display order history
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on view icon
    And    I click on 'My Orders'
    And    I user scrolls down the page
    Then   I verify the page should move down and display additional order history
    When   I user scrolls up the page
    Then   I verify the page should move up and show previous order history
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_OH_007 @newtestmcd2
Scenario: Verify that the Help button is only visible for McDelivery orders
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on view icon
    And    I click on 'My Orders'
    Then   I verify the Help button should be visible only for orders placed via McDelivery
    And    I verify the Help button should not be visible for orders from other business models (BM)
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_OH_008 @newtestmcd2
Scenario: Verify that User is able to submit a complaint or feedback via Help
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I user adds the item to the cart
    And    I navigate to the cart
    Then   I verify the single item in cart
    When   I click on add address from checkout page
    And    I selects the address from the listed addres
    And    I click on pay button in view cart page
    Then   I verify user should be redirected to the payment page successfully
    When   I selects Cash on Delivery as the payment method
    And    I click the 'Proceed To Pay' button
    Then   I verify a confirmation message should be displayed saying 'Pay at Door'
    When   I click on back button on post payment page
    And    I click on view icon
    And    I click on 'My Orders'
    And    I selects a latest order and clicks on 'Help'
    Then   I verify a user should be able to to give feedback and raise a complaint
    And    I verify raise a complaint pop up should be displayed
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_OH_009 @newtestmcd2
Scenario: Verify that User cannot raise a complaint after 2 hours of order
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on view icon
    And    I click on 'My Orders'
    And    I selects an order older than 2 hours and clicks on Help button
    Then   I verify a pop-up message should appear saying 'Order active hours ended'
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_001 @newtestmcd2
Scenario: Verify that User is able to view all purchased products in order details
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on view icon
    And    I click on 'My Orders'
    And    I click on 'Order Tracking' for completed order
    Then   I verify 'Your Order Details' section should be displayed
    And    I verify all products included in the order should be visible to the user
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_002 @newtestmcd2
Scenario: Verify that User is able to download the invoice from order tracking
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on view icon
    And    I click on 'My Orders'
    And    I click on 'Order Tracking' for completed order
    Then   I verify 'Your Order Details' section should be displayed
    When   I clicks on 'Invoice'
    Then   I verify invoice should be downloaded and saved on the device
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_003 @newtestmcd2
Scenario: Verify the presence of an order number on the confirmation page
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on view icon
    And    I click on 'My Orders'
    Then   I verify order number should be displayed
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_004 @newtestmcd2
Scenario: Verify store name are shown correctly
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on view icon
    And    I click on 'My Orders'
    Then   I verify the store name should be visible
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_005 @newtestmcd2
Scenario: Verify that the complete delivery address is shown correctly
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on view icon
    And    I click on 'My Orders'
    And    I click on 'Order Tracking'
    Then   I verify the complete delivery address should be shown
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_PP_006 @newtestmcd2
Scenario: verify the order status progress bar on the order tracking page
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on view icon
    Then   I verify view page navigation
    When   I click on login or signup button
    Then   I verify login page navigation
    When   I enter a valid mobile number and click verify
    And    I enter the OTP and click verify
    And    I click save changes on profile details page
    Then   I verify home page navigation
    When   I click on view icon
    And    I click on 'My Orders'
    And    I click on 'Order Tracking'
    Then   I verify the status bar should be visible
    Examples:
        |appURL|
        |https://www.uat.mcdapp.co|










