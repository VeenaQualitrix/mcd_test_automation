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
    When   I click on add address in home page
    Then   I verify user redirected to login/signup prompt
    When   I click on login/signup prompt
    Then   I verify login page navigation
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
    When   I click on any item to add into a cart
    Then   I verify items details pop up opened successfully
    When   I click on next
    And    I click on Add to cart option
    Then   I verify selected item get added into a cart
    When   I click on login/signup prompt from checkout
    Then   I verify login page navigation from checkout page
    When   I click on cancel button from login/signup pop up
    Then   I verify Login cancelled and user returned to checkout page
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_Address_Login_04
Scenario: Verify Incorrect login from “Add Address” screen
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on add address
    Then   I verify user redirected to login/signup prompt
    When   I click on login/signup prompt
    Then   I verify login page navigation
    When   I enter incorrect number in mobile number field and click verify
    Then   I verify error message
        |appURL|
        |https://www.uat.mcdapp.co|


@TC_Address_Login_06
Scenario: Add new delivery address during checkout
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click on any item to add into a cart
    Then   I verify items details pop up opened successfully
    When   I click on next
    And    I click on Add to cart option
    Then   I verify selected item get added into a cart
    When   I click on add address from checkout page
    And    I click on add new button and search for location
    And    I select address from search results
    Then   I verify address is added and selected
    And    I verify the address should appear as the selected delivery address
        |appURL|
        |https://www.uat.mcdapp.co|


@TC_Address_Login_07
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
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I click on add new button and click confirm location
    Then   I verify user redirected to address fill in details page
    When   I leave mandatory field empty and click save address
    Then   I verify that the address not saved and validation error should be displayed
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_Address_Login_09
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
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I click on add new button and click confirm location
    Then   I verify user redirected to address fill in details page
    When   I enter special character in house/flat field and click save address
    Then   I verify field accept characters and address will get saved
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_Address_Login_11
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
    Then   I verify home page navigation
    And    I verify saved delivery address
    When   I click on add address in home page
    And    I click on add new button and click confirm location
    Then   I verify user redirected to address fill in details page
    When   I enter text in house/flat field and click back button without saving
    Then   I verify address will not get saved
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_Address_Login_15
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
    Then   I verify home page navigation
    When   I click on add address in home page
    And    I click on add new button and click confirm location
    Then   I verify user redirected to address fill in details page
    When   I enter text in house/flat field and click save address
    And    I click on add address in home page
    Then   I verify System allows address duplication based on business logic
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_001
Scenario: Verify dropdown displays all business models
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click the business model dropdown
    Then   I verify Dropdown shows: McDelivery, Dine-In, On the Go, Take Away
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_002
Scenario: Validate user can select “McDelivery” and proceed
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click the business model dropdown
    And    I select the McDelivery option from dropdown
    Then   I verify User is taken to the McDelivery ordering flow
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_003
Scenario: Validate user can select “Dine-In” and proceed
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click the business model dropdown
    And    I select Dine-In option from dropdown
    Then   I verify User navigates to Dine-In selection/location flow
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_004
Scenario: Validate user can select “On the Go” and proceed
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click the business model dropdown
    And    I select on the go option from dropdown
    Then   I verify User is prompted to choose pick-up location
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_005
Scenario: Validate user can select “Take Away” and proceed
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click the business model dropdown
    And    I select Take Away option from dropdown
    Then   I verify User proceeds to place an order for take away
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_006
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


@TC_BM_012
Scenario: Verify default business model on first visit
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    And    I verify “McDelivery” should be selected by default
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_013
Scenario: Check location permission prompt for “On the Go” or “Dine-In”
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click the business model dropdown
    And    I select “On the Go” or “Dine-In” without granting location access
    Then   I verify a prompt should appear requesting location permission
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_014
Scenario: Validate no restaurant available for selected model
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click the business model dropdown
    And    I select a business model in an unsupported region
    Then   I should see the message: “Sorry, we do not serve this location yet”
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_015
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


@TC_BM_019
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
    Then   I verify home page navigation
    When   I click the business model dropdown
    And    I select Take Away option from dropdown
    And    I open a new tab in the same session
    Then   I verify the same business model should remain selected
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_020
Scenario: Test visual feedback on hover on desktop
    Given  I open the Chrome browser
    When   I hit the URL
    Then   I verify website opened successfully
    When   I click the business model dropdown
    And    I hover over each business model option
    Then   I verify the icons and text should respond visually
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_021
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
    Then   I verify home page navigation
    And    I verify the user notes their current profile information
    When   I click the business model dropdown
    And    I verify user switches from one model to another
    And    I verify user navigates to the profile page
    Then   I verify the profile information should remain unchanged
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_BM_022
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
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_AD_001
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
        |appURL|
        |https://www.uat.mcdapp.co|

@TC_AD_002
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
        |https://www.uat.mcdapp.co|

@TC_AD_003
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
    And    I verify restaurant are updated based on the modified address
        |https://www.uat.mcdapp.co|

@TC_AD_004
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
        |https://www.uat.mcdapp.co|

@TC_AD_006
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
        |https://www.uat.mcdapp.co|

@TC_AD_007
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
        |https://www.uat.mcdapp.co|

@TC_AD_008
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
        |https://www.uat.mcdapp.co|

@TC_AD_010
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
        |https://www.uat.mcdapp.co|


@TC_AD_011
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
        |https://www.uat.mcdapp.co|


@TC_AD_012
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
        |https://www.uat.mcdapp.co|


