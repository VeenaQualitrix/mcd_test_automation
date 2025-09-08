@McdMobileRegression
Feature: McD App Functionality

@TC_Android_Login_001 @sanitymobile
Scenario Outline: Verify login with valid Mobile Number and OTP
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    Then  I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button

@TC_Android_LOGIN_002 @sanitymobile
Scenario Outline: Verify referral code input
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I click on referral link
    And   I enter referral code 
    #Then  I verify referral code accepted without error

@TC_Android_LOGIN_003 @sanitymobile
Scenario Outline: Validate empty mobile number
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I leave mobile field empty 
    Then  I confirm 'verify mobile' button is disabled

@TC_Android_LOGIN_004 @sanitymobile
Scenario Outline: Validate short mobile number
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I enter a mobile number with less than 10 digits
    Then  I confirm 'verify mobile' button is disabled

@TC_Android_LOGIN_005 @sanitymobile
Scenario Outline: Validate alphabetic input in mobile field
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I enter alphabets in mobile number field
    Then  I confirm 'verify mobile' button is disabled

@TC_Android_LOGIN_006 @sanitymobile
Scenario Outline: Verify referral code without entering mobile number
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I click on referral link
    And   I enter referral code and click verify
    Then  I verify error message

@TC_Android_LOGIN_007 @sanitymobile
Scenario Outline: Verify mobile number with spaces
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I enter mobile number with spaces and click verify
    Then  I confirm 'verify mobile' button is disabled

@TC_Android_LOGIN_008 @sanitymobile
Scenario Outline: Verify mobile number with special characters
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I enter mobile number with special characters and click verify
    Then  I confirm 'verify mobile' button is disabled
   
@TC_Android_LOGIN_009 @sanitymobile01
Scenario Outline: Verify UI alignment and presence of elements
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I visually inspect the mobile number field
    And   I visually inspect the referral link section
    And   I visually inspect the verify button
    And   I visually inspect the footer links
    Then  I verify all elements should be visible, correctly aligned, and not overlapping

@TC_Android_LOGIN_010 @sanitymobile
Scenario Outline: Verify referral link is clickable
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I click on referral link
    Then  I verify referral textfield is displayed

@TC_Android_LOGIN_011 @sanitymobile
Scenario Outline: Validate "Verify Mobile" button is disabled initially
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    And   I confirm 'verify mobile' button is disabled

@TC_Android_LOGIN_012 @sanitymobile
Scenario Outline: Verify navigation after successfully entetered a valid mobile number
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I enter a valid mobile number and click mobile verify
    Then  I verify OTP screen navigation

@TC_Android_LOGIN_013 @Fridaynew
Scenario Outline: Verify terms and conditions link
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I click terms and conditions link
    Then  I verify user is redirected to terms and conditions page

@TC_Android_LOGIN_014 @sanitymobile
Scenario Outline: Enter exactly 10 digit valid mobile number
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I enter a valid mobile number and click mobile verify
    Then  I verify mobile number accepted and redirected to next page

@TC_Android_LOGIN_015 @sanitymobile
Scenario Outline: Enter 11 digits mobile number and verify
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I enter 11 digits mobile number
    Then  I verify field should restrict to 10 digits
    
@TC_Android_LOGIN_016 @sanitymobile
Scenario Outline: Verify clipboard paste into mobile field
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I copied a mobile number
    When  I paste the number with Ctrl V and click verify
    Then  I verify number pasted correctly and accepted

@TC_Android_LOGIN_017 @sanitymobile
Scenario Outline: Verify mobile field input limit
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I enter more than 10 digits mobile number
    Then  I verify field should restrict to 10 digits

@TC_Android_PP_01
Scenario: Verify that user update the name successfully 
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    Then  I verify profile screen navigation
    When  I edits the full name field with Test User01 and clicks Save Changes
    Then  I verify home screen navigation
    And   I verify updated name should be reflected on the profile
    And   I click on Log out button

@TC_Android_PP_02  @newtestrun
Scenario: Verify empty name field 
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    Then  I verify profile screen navigation
    When  I clear name field
    Then  I verify error message Please enter valid full name should be displayed
    When  I edits the full name field with Test User01 and clicks Save Changes
    Then  I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button

@TC_Android_PP_03  @newtestrun
Scenario: Validate invalid characters in name field 
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    Then  I verify profile screen navigation
    When  I enter invalid characters in name field
    Then  I verify error message Please enter valid full name should be displayed
    When  I edits the full name field with Test User01 and clicks Save Changes
    Then  I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button
    

@TC_Android_PP_06
Scenario: update email address
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    Then  I verify profile screen navigation
    When  I edits email address and clicks Save Changes
    Then  I verify home screen navigation
    And   I verify updated email address should be reflected on the profile
    And   I click on Log out button


@TC_Android_PP_07 @newtestrun
Scenario: Validate incorrect email format
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    Then  I verify profile screen navigation
    When  I enter incorrect email format in email field
    Then  I verify error message enter valid email address should be displayed
    When  I clear email address and clicks Save Changes
    Then  I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button

@TC_Android_PP_08 @sanitymobile01
Scenario: update date of birth successfully
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    Then  I verify profile screen navigation
    When  I selects a new valid date of birth and clicks Save Changes
    Then  I verify updated date of birth should be reflected on the profile
    When  I click save changes on profile details page
    Then  I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button

@TC_Android_PP_09 @newtestrun
Scenario: validate future date of birth selection is not allowed
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    Then  I verify profile screen navigation
    And   I verify user are unable to select future Date of birth
    #When  I click calender close icon and click save button
    #And   I click save changes on profile details page
    #Then  I verify home screen navigation
    #When  I click on MyMcD hamburger icon
    #Then  I click on Log out button
    

@TC_Android_PP_10 @newtestrun
Scenario: Verify Change Picture link opens photo upload
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    Then  I verify profile screen navigation
    When  I click change picture link
    Then  I verify upload pop up opens with file selection option
    When  I click save changes on profile details page
    Then  I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button


@TC_Android_PP_11 @newtestrun
Scenario: Verify that the Save button is disabled when any mandatory field is empty.
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    Then  I verify profile screen navigation
    When  I clear name field
    Then  I verify the Save button should be disabled
    When  I edits the full name field with Test User01 and clicks Save Changes
    Then  I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button


@TC_Android_PP_12 @newtestrun
Scenario: Verify Toggle color blind mode on/off
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    Then  I verify profile screen navigation
    When  I switch toggle on/off and observe UI
    Then  I verify Color scheme updates to accessible version page should be displayed
    When  I click save changes on profile details page
    Then  I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button

@TC_Android_PP_16
Scenario: Verify field icons are displayed correctly
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    Then  I verify profile screen navigation
    When  I Check icon presence near each field
    Then  I verify the Correct icons for name, phone, email, DOB
    When  I click save changes on profile details page
    Then  I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button


@TC_Android_Address_Login_01
Scenario: Verify Trigger login when clicking “Add Address” as guest
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on search icon in home screen
    Then  I verify search menu screen navigation
    When  I click on search textfield
    And   I enter burger name and click search icon
    Then  I verify item displayed
    When  I click on add+ button
    And   I click on Add to cart option
    And   I click on view cart option
    And   I click on add address in home screen
    Then  I verify user redirected to login/signup prompt
   
@TC_Android_Address_Login_02 @newtestrun
Scenario: Verify Successful login redirects to “Add Address” screen
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on add address in home screen
    Then  I verify user redirected to login/signup prompt
    When  I click on login/signup prompt
    Then  I verify login screen navigation
    When  I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    Then  I verify 'Add new' button is displayed to add address
    And   I click back button from select address screen
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button
   

@TC_Android_Address_Login_03
Scenario: Verify Cancel login from “checkout” page
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on search icon in home screen
    Then  I verify search menu screen navigation
    When  I click on search textfield
    And   I enter burger name and click search icon
    Then  I verify item displayed
    When  I click on add+ button
    And   I click on Add to cart option
    And   I click on view cart option
    And   I click on login/signup prompt from checkout
    Then  I verify login screen navigation
    When  I click on cancel button from login/signup pop up
    Then  I verify Login cancelled and user returned to checkout page
  

@TC_Android_Address_Login_04
Scenario: Verify Incorrect login from “Add Address” screen
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on add address in home screen
    Then  I verify user redirected to login/signup prompt
    When  I click on login/signup prompt
    Then  I verify login screen navigation
    When  I enter incorrect mobile number
    Then  I confirm 'verify mobile' button is disabled

@TC_Android_Address_Login_06 @newtestrun
Scenario: Add new delivery address during checkout
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on search icon in home screen
    And   I browse the menu and return to the homepage
    And   I click on add address in home screen
    Then  I verify user redirected to login/signup prompt
    When  I click on login/signup prompt
    When  I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    Then  I verify 'Add new' button is displayed to add address
    When  I click on add new button and click confirm location
    Then  I verify user redirected to address fill in details page
    When  I add new delivery address
    Then  I verify address is added and selected
    #When  I click on view cart option
    #And   I click on clear all to empty the cart
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button


@TC_Android_Address_Login_07 @newtestrun
Scenario: verify adding address with missing mandatory fields
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    Then  I verify 'Add new' button is displayed to add address
    When  I click on add new button and click confirm location
    And   I leave mandatory field empty and click save address
    Then  I verify that the address not saved and validation error should be displayed
    Then  I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button
   

@TC_Android_Address_Login_09 @sanitymobile01
Scenario: verify adding address with special characters
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    Then  I verify 'Add new' button is displayed to add address
    When  I click on add new button and click confirm location
    And   I enter special character in house/flat field and click save address
    Then  I verify field accept characters and address will get saved
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button
   

@TC_Android_Address_Login_11 @sanitymobile01
Scenario: verify clicking cancel button before saving address
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    Then  I verify login screen navigation
    When  I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    Then  I verify 'Add new' button is displayed to add address
    When  I click on add new button and click confirm location
    Then  I verify user redirected to address fill in details page
    When  I enter text in house/flat field and click back button without saving
    And   I click on add address in home screen
    Then  I verify address will not get saved
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button

@TC_Android_Address_Login_13 @sanitymobile01
Scenario: Verify max character limit for address fields
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify view screen navigation
    When  I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    And   I click on add new button and click confirm location
    And   I enter text exceeding the max character limit in address fields and click save address
    Then  I verify address accept max characters and get saved
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button

@TC_Android_Address_Login_15 @sanitymobile01
Scenario: verify adding duplicate address
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    And   I click on add new button and click confirm location
    Then  I verify user redirected to address fill in details page
    When  I add new delivery address
    Then  I verify address is added and selected
    When  I click on add address in home screen
    Then  I verify System allows address duplication based on business logic
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button


@TC_Android_BM_001
Scenario: Verify dropdown displays all business models
    Given  I launch the native app
    Then   I verify the app should be launched
    And    I verify home screen navigation
    Then   I verify displays of McDelivery, Dine-In, On the Go, Take Away at the top of the screen

@TC_Android_BM_002
Scenario: Validate user can select “McDelivery” and proceed
    Given  I launch the native app
    Then   I verify the app should be launched
    And    I verify home screen navigation
    When   I select the McDelivery option
    Then   I verify User is taken to the McDelivery ordering flow

@TC_Android_BM_003
Scenario: Validate user can select “Dine-In” and proceed
    Given  I launch the native app
    Then   I verify the app should be launched
    And    I verify home screen navigation
    When   I select Dine-In option
    Then   I verify User navigates to Dine-In selection/location flow

@TC_Android_BM_004
Scenario: Validate user can select “On the Go” and proceed
    Given  I launch the native app
    Then   I verify the app should be launched
    And    I verify home screen navigation
    When   I select on the go option
    Then   I verify User is prompted to choose pick-up location

@TC_Android_BM_005
Scenario: Validate user can select “Take Away” and proceed
    Given  I launch the native app
    Then   I verify the app should be launched
    And    I verify home screen navigation
    When   I select Take Away option
    Then   I verify User proceeds to place an order for take away

@TC_Android_BM_006  @newtestrun
Scenario: Ensure selected model persists during session
    Given  I launch the native app
    Then   I verify the app should be launched
    And    I verify home screen navigation
    When   I select Dine-In option
    And    I search the address from searchbar and select the address
    And    I click on search icon in home screen
    And    I browse the menu and return to the homepage
    Then   I verify Dine-In remains the selected option until manually changed
    And    I verify selected 'Kasturba Road' address is displayed for Dine-In model

@TC_Android_BM_009
Scenario: Ensure mobile responsiveness on selecting business model
    Given  I launch the native app
    Then   I verify the app should be launched
    And    I verify home screen navigation
    Then   I verify displays of McDelivery, Dine-In, On the Go, Take Away at the top of the screen
    When   I select the McDelivery option
    Then   I verify User is taken to the McDelivery ordering flow
    When   I select Dine-In option
    Then   I verify User navigates to Dine-In selection/location flow
    When   I select on the go option
    Then   I verify User is prompted to choose pick-up location
    When   I select Take Away option
    Then   I verify User proceeds to place an order for take away

@TC_Android_BM_012   @FridayScripts
Scenario: Verify default business model on first visit
    Given  I launch the native app
    Then   I verify the app should be launched
    And    I verify home screen navigation
    And    I verify 'McDelivery' should be selected by default

@TC_Android_BM_013  @FridayScripts
Scenario: Check location permission prompt for “On the Go” or “Dine-In”
    Given  I launch the native app
    Then   I verify the app should be launched
    And    I verify home screen navigation
    When   I select 'Dine-In' without granting location access
    Then   I verify a prompt should appear requesting location permission
    When   I select 'On the Go' without granting location access
    Then   I verify a prompt should appear requesting location permission

@TC_Android_BM_014  @FridayScripts
Scenario: Validate no restaurant available for selected model
    Given  I launch the native app
    Then   I verify the app should be launched
    And    I verify home screen navigation
    When   I select Dine-In option
    And    I search the address from searchbar after selecting BM model
    Then   I should see the message: “Sorry, we do not serve this location yet”

@TC_Android_BM_015
Scenario: Ensure no multiple model selection at once
    Given  I launch the native app
    Then   I verify the app should be launched
    And    I verify home screen navigation
    When   I select Dine-In option
    And    I select Take Away option
    Then   I verify only one model should remain active at a time

@TC_Android_BM_020
Scenario: Test visual feedback on tap for mobile
    Given  I launch the native app
    Then   I verify the app should be launched
    And    I verify home screen navigation
    When   I hover over each business model option
    Then   I verify the icons and text should respond visually

@TC_Android_BM_021 @newtestrun
Scenario: Verify Switching models does not alter profile information
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    Then  I verify home screen navigation
    When  I click on MyMcD hamburger icon
    Then  I verify the user notes their current profile information
    When  I verify user switches from one model to another
    And   I click on MyMcD hamburger icon
    Then  I verify the profile information should remain unchanged
    And   I click on Log out button

@TC_Android_BM_022 @sanitymobile01
Scenario: Verify Switching between models updates the UI layout appropriately
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    Then  I verify home screen navigation
    When  I select the McDelivery option
    Then  I verify the page layout or menu should adapt to match the McDelivery model
    When  I select Dine-In option
    Then  I verify the page layout or menu should adapt to match the Dine-In model
    When  I select on the go option
    Then  I verify the page layout or menu should adapt to match the on the go model
    When  I select Take Away option
    Then  I verify the page layout or menu should adapt to match the Take Away model
    When  I select the McDelivery option
    And   I click on MyMcD hamburger icon
    Then  I click on Log out button

@TC_Android_AD_002 @sanitymobile01
Scenario: Verify adding a new delivery address
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    Then  I verify 'Add new' button is displayed to add address
    When  I click on add new button and click confirm location
    Then  I verify user redirected to address fill in details page
    When  I add new delivery address
    Then  I verify address is added and selected
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button

@TC_Android_AD_001 @sanitymobile01
Scenario: verify selecting existing delivery address
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    And   I user click on a listed address
    Then  I verify the address is selected and restaurant list should update accordingly
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button


@TC_Android_AD_003 @sanitymobile01
Scenario: Verify editing an existing address
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    And   I click the edit icon next to an address
    And   I modifies the address details and click save button
    And   I click on add address in home screen
    Then  I verify updated address is shown in the address list
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button

@TC_Android_AD_004 @sanitymobile01
Scenario: Verify deleting an existing address
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    And   I verify address list shown
    And   I click the delete icon next to an address
    Then  I verify address removed from list
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button

@TC_Android_AD_005  @sanitymobile01
Scenario: Ensure address selection updates nearby restaurant list
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    And   I selects the first address from the address list
    Then  I verify restaurant list should update based on the first address location
    When  I click on add address in home screen
    And   I selects the second address from the address list
    Then  I verify restaurant list should update based on the second address location
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button

@TC_Android_AD_006  @sanitymobile01
Scenario: Validate empty address cannot be saved
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    Then  I verify 'Add new' button is displayed to add address
    When  I click on add new button and click confirm location
    And   I leave mandatory field empty and click save address
    Then  I verify that the address not saved and validation error should be displayed
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button

@TC_Android_AD_007  @sanitymobile01
Scenario: Verify "Near" location shown under each address
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    And   I verify address list displayed
    Then  I verify each address should display a Near label with its location description
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button

@TC_Android_AD_008   @sanitymobile01
Scenario: Ensure scroll functionality works if many addresses are saved
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    And   I verify address list displayed
    Then  I verify all saved addresses should be accessible via scrolling
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button

@TC_Android_AD_010  
Scenario: Verify error handling for invalid or undeliverable address
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    And   I enters an undeliverable pin code or area manually
    Then  I verify an error message should be displayed saying Delivery not available at this address
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button


@TC_Android_AD_011   
Scenario: Default address selection on login
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    Then  I verify the most recently used address should be auto-selected
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button


@TC_Android_AD_012  @Fridaynew
Scenario: Ensure “Add New” opens address entry popup or page
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    Then  I verify 'Add new' button is displayed to add address
    When  I click on add new button and click confirm location
    Then  I verify user redirected to address fill in details page
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button

@TC_Android_AD_013  @newtestrun
Scenario: Ensure Address list remains consistent after logout and login
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    And   I verify address list before logout of the application
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button
    When  I click on add address in home screen
    Then  I verify user redirected to login/signup prompt
    When  I click on login/signup prompt
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    Then  I verify previously saved addresses should be retained and visible
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button


@TC_Android_AD_018  @FridayScripts
Scenario: Verify user can tag an address as "Home", "Work", etc.
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    And   I adds an address and select a tag
    And   I click on add address in home screen
    Then  I verify the tag should be displayed next to the address name after adding address
    When  I edits an address and select a tag
    And   I click on add address in home screen
    Then  I verify the tag should be displayed next to the address name after editing address
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button


@TC_Android_ORDER_001  @FridayScripts
Scenario: Place an order with available breakfast item
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I add breakfast item
    And   I click on view cart option
    Then  I verify the item is added to the cart
    When  I click on clear all to empty the cart

@TC_Android_ORDER_002  @FridayScripts
Scenario: Attempt to order an out-of-stock item
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    And   I selects the Mumbai address from the address list
    And   I click on Menu icon
    And   I click 'Sold out' items from McBreakfast category
    Then  I very User is unable to add item and Sold out popup shown
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button

@TC_Android_ORDER_003 @FridayScripts
Scenario: Check customization option availability
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I click on 'Add +' for the customizable item
    Then  I verify the customization options should appear before adding the item to the cart

@TC_Android_ORDER_004 @FridayScripts
Scenario: Add multiple items to cart
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I add multiple items to cart
    And   I click on view cart option
    Then  I verify all added items should be listed in the cart with correct price and quantities
    When  I click on clear all to empty the cart


@TC_Android_ORDER_005 @FridayScripts
Scenario: Place an order with only 1 item
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I add breakfast item
    And   I click on view cart option
    Then  I verify the item is added to the cart
    When  I click on clear all to empty the cart

@TC_Android_ORDER_006 @FridayScripts
Scenario: Ensure menu item prices are correctly displayed and reflected in cart
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I user adds the item to the cart
    And   I click on view cart option
    Then  I verify the price in the cart should match the menu price
    When  I click on clear all to empty the cart

@TC_Android_ORDER_007   @FridayScripts
Scenario: Verify out-of-stock label prevents adding item
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    And   I selects the Mumbai address from the address list
    And   I click on Menu icon
    And   I click 'Sold out' items from McBreakfast category
    Then  I very User is unable to add item and Sold out popup shown
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button


@TC_Android_ORDER_008 @FridayScripts
Scenario: Add a McBreakfast item to cart
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I add breakfast item
    And   I click on view cart option
    Then  I verify the item is added to the cart
    When  I click on clear all to empty the cart

@TC_Android_ORDER_009   @FridayScripts
Scenario: Add a sold-out McBreakfast item
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    And   I selects the Mumbai address from the address list
    And   I click on Menu icon
    And   I click 'Sold out' items from McBreakfast category
    Then  I very User is unable to add item and Sold out popup shown
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button

@TC_Android_ORDER_010 @newtestrun
Scenario: View 3Pc Meals
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I selects the '3Pc Meals' category under menu
    And   I select McChicken meal from the '3Pc Meals' category and click on Add to cart 
    And   I click on view cart option
    Then  I verify the 3Pc meal added in cart
    When  I click on clear all to empty the cart

@TC_Android_ORDER_011  @sanitymobile01
Scenario: Choose any product from Desserts category
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I selects the 'Desserts' category under menu
    And   I select any product from desserts and click on Add to cart 
    And   I click on view cart option
    Then  I verify the Desserts product added in cart
    When  I click on clear all to empty the cart

@TC_Android_ORDER_015  @FridayScripts
Scenario: Add burger/wrap from Burgers & Wraps
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I selects the 'Burgers & Wraps' category under menu
    And   I select chicken wrap and Add to cart 
    And   I click on view cart option
    Then  I verify the Burgers & Wraps product added in cart
    When  I click on clear all to empty the cart

@TC_Android_ORDER_016   @Fridaynew
Scenario: Customize burger before adding to cart
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I click on 'Add +' for the customizable item
    When  I clicks on the 'Customize' button
    And   I selects or removes items from the customization options
    And   I click on view cart option
    Then  I verify the customized item should be added to the cart with selected preferences
    When  I click on clear all to empty the cart

@TC_Android_ORDER_017   @FridayScripts
Scenario: Add fries to cart
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I click on 'Fries & Sides' menu option
    And   I add 'Medium Fries' to the cart
    And   I click on view cart option
    Then  I verify fries should be added to the cart 
    When  I click on clear all to empty the cart

@TC_Android_ORDER_018   @FridayScripts
Scenario: Add cold coffee to cart
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I click on 'Coffee & Beverages' menu option
    And   I add 'cold coffee' to the cart
    And   I click on view cart option
    Then  I verify cold coffee should be added to the cart 
    When  I click on clear all to empty the cart

@TC_Android_ORDER_019   @FridayScripts
Scenario: Add Hot Coffee and Cold Coffee separately to cart
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I click on 'Coffee & Beverages' menu option
    And   I add 'Hot coffee' to the cart
    And   I add 'cold coffee' to the cart
    And   I click on view cart option
    Then  I verify cold coffee & hot coffee should be added to the cart 
    When  I click on clear all to empty the cart

@TC_Android_ORDER_020   @FridayScripts
Scenario: Add a brownie to cart
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I click on 'Cakes, Brownies & Cookies' menu option
    And   I add 'Brownie' to the cart
    And   I click on view cart option
    Then  I verify brownie should be added to the cart 
    When  I click on clear all to empty the cart

@TC_Android_ORDER_021   @FridayScripts
Scenario: View thumbnails image of a dessert
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I selects the 'Desserts' category under menu
    Then  I verify thumbnails image of a dessert is clearly displayed

@TC_Android_ORDER_022   @FridayScripts
Scenario: Add millet bun burger to cart
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I click on 'Burgers with Millet Bun' menu option
    And   I add 'millet bun burger' to the cart
    And   I click on view cart option
    Then  I verify millet bun burger should be added to the cart 
    When  I click on clear all to empty the cart

@TC_Android_ORDER_023   @FridayScripts
Scenario: View nutrition description of millet bun
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I click on 'Burgers with Millet Bun' menu option
    And   I click on millet bun burger
    Then  I verify nutritional info is displayed in the description

@TC_Android_ORDER_024   @FridayScripts
Scenario: Remove item from the cart
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I add multiple items to cart
    And   I click on view cart option
    When  I clicks the 'Remove' button for an item
    Then  I verify the selected item should be removed from the cart
    When  I click on clear all to empty the cart

@TC_Android_ORDER_025   @FridayScripts
Scenario: Update item quantity in cart
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I add single item to the cart
    And   I click on view cart option
    Then  I verify the single item in cart
    When  I clicks the 'Add' button for an item
    And   I clicks the 'Add' button for an item
    And   I clicks the 'Remove' button for an item
    Then  I verify the Quantity updates correctly
    When  I click on clear all to empty the cart

@TC_Android_ORDER_026   @FridayScripts
Scenario: Check total price calculation
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I add multiple items to cart
    And   I click on view cart option
    Then  I verify the total payable amount should be displayed
    When  I click on view cart option
    And   I click on clear all to empty the cart

@TC_Android_ORDER_027   @FridayScripts
Scenario: Scroll through all menu categories
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I selects the 'Desserts' category under menu
    Then  I verify the Desserts category is accessible via scrolling
    When  I click on 'Fries & Sides' menu option
    Then  I verify the Fries & Sides category is accessible via scrolling

@TC_Android_ORDER_029  @FridayScripts
Scenario: Validate cart icon does not appear on the homepage if the cart is empty
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    And   I verify the cart icon does not appear on the homepage if the cart is empty

@TC_Android_CO_001 @testmcd1
Scenario: Validate cart contains correct item details
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I add multiple items to cart
    And   I click on view cart option
    Then  I verify all added items should be listed in the cart with correct price and quantities
    When  I click on clear all to empty the cart

@TC_Android_CO_002 @testmcd1
Scenario: Update item quantity
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I add single item to the cart
    And   I click on view cart option
    Then  I verify the single item in cart
    When  I clicks the 'Add' button for an item
    And   I clicks the 'Add' button for an item
    And   I clicks the 'Remove' button for an item
    Then  I verify the Quantity updates correctly
    And   I verify the total payable amount should be displayed
    When  I click on view cart option
    And   I click on clear all to empty the cart

@TC_Android_CO_003 @testmcd1
Scenario: Verify clear cart when items are already in cart
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I add single item to the cart
    And   I click on view cart option
    Then  I verify the single item in cart
    When  I click on clear all to empty the cart
    Then  I verify the cart icon does not appear on the homepage if the cart is empty

@TC_Android_CO_005 @testmcd1
Scenario: Validate total price breakdown in order summary
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I add single item to the cart
    And   I click on view cart option
    Then  I verify the single item in cart
    When  I checks the price breakdown on the right side of the page
    Then  I verify the subtotal, handling charges, CGST, and SGST should be displayed and match the total payable amount
    When  I click on clear all to empty the cart

@TC_Android_CO_006 @testmcd1
Scenario: Add Delivery Instructions on Checkout Page
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I add single item to the cart
    And   I click on view cart option
    Then  I verify the single item in cart
    When  I click on 'Add Delivery Instructions'
    And   I enters special notes in the instructions field
    Then  I verify the instructions field should accept the input
    When  I click on clear all to empty the cart

@TC_Android_CO_007 @Fridaynew
Scenario: Validate subtotal after all additions
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I add single item to the cart
    And   I click on view cart option
    Then  I verify the single item in cart
    And   I verify subtotal for a single added item
    When  I add item from recommendation
    Then  I verify subtotal for all added items
    When  I click on view cart option
    And   I click on clear all to empty the cart

@TC_Android_CO_008 @testmcd1
Scenario: Validate tax calculation in cart
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I add single item to the cart
    And   I click on view cart option
    Then  I verify the single item in cart
    When  I Check CGST and SGST breakdown
    Then  I verify tax percentage should be calculated accurately
    When  I click on view cart option
    And   I click on clear all to empty the cart

@TC_Android_CO_009 @testmcd1
Scenario: Prompt user to log in before proceeding with order
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on search icon in home screen
    Then  I verify search menu screen navigation
    When  I click on search textfield
    And   I enter burger name and click search icon
    Then  I verify item displayed
    When  I click on add+ button
    And   I click on Add to cart option
    And   I click on view cart option
    And   I click on add address in home screen
    Then  I verify user redirected to login/signup prompt
    When  I click on login/signup prompt


@TC_Android_CO_010 @testmcd1
Scenario: Verify 'Know More' for charity donation
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I add single item to the cart
    And   I click on view cart option
    Then  I verify the single item in cart
    When  I click on 'Know More' link
    Then  I verify Info opens about the charity
    When  I click on view cart option
    And   I click on clear all to empty the cart

@TC_Android_CO_011 @testmcd1
Scenario: Select charity donation checkbox
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I add single item to the cart
    And   I click on view cart option
    Then  I verify the single item in cart
    When  I clicks the charity donation checkbox to opt-in
    Then  I verify ₹3 should be added to the total payable amount
    When  I click on view cart option
    And   I click on clear all to empty the cart

@TC_Android_CO_012 @testmcd1
Scenario: Uncheck charity donation checkbox
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I add single item to the cart
    And   I click on view cart option
    Then  I verify the single item in cart
    When  I unchecks the charity donation checkbox
    Then  I verify ₹3 should be removed from the total payable amount
    When  I click on view cart option
    And   I click on clear all to empty the cart

@TC_Android_CO_013 @testmcd1
Scenario: View all available offers
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I add single item to the cart
    And   I click on view cart option
    Then  I verify the single item in cart
    When  I click on 'View All' link
    Then  I verify the user should be redirected to a page displaying all available offers
    When  I click on clear all to empty the cart
  
@TC_Android_CO_014 @testmcd1
Scenario: Ensure currency symbol is correctly shown for all price components
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I add single item to the cart
    And   I click on view cart option
    Then  I verify the single item in cart
    When  I reviews all prices in the order summary
    Then  I verify each price should be prefixed with the ₹ symbol
    When  I click on view cart option
    And   I click on clear all to empty the cart

@TC_Android_CO_015 @testmcd1
Scenario: Redirect user to login when attempting checkout without being logged in
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on search icon in home screen
    Then  I verify search menu screen navigation
    When  I click on search textfield
    And   I enter burger name and click search icon
    Then  I verify item displayed
    When  I click on add+ button
    And   I click on Add to cart option
    And   I click on view cart option
    And   I click on add address in home screen
    Then  I verify user redirected to login/signup prompt
   
@TC_Android_CO_016 @testmcd1
Scenario: Remove item from cart by decreasing quantity to zero
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I add multiple items to cart
    And   I click on view cart option
    When  I clicks the 'Remove' button for an item
    Then  I verify the selected item should be removed from the cart
    And   I verify the total payable amount should be displayed
    When  I click on view cart option
    And   I click on clear all to empty the cart

@TC_Android_CO_018 @testmcd1
Scenario: Verify that payment is not allowed to process with a sold-out item.
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    And   I selects the Mumbai address from the address list
    And   I click on Menu icon
    And   I click 'Sold out' items from McBreakfast category
    Then  I very User is unable to add item and Sold out popup shown
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button

@TC_Android_CO_019 @Fridaynew
Scenario: Validate estimated delivery time visibility
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    And   I selects the Mumbai address from the address list
    And   I click on Menu icon
    And   I add single item to the cart
    And   I click on view cart option
    Then  I verify the estimated delivery time displayed below the delivery address
    When  I click on clear all to empty the cart

@TC_Android_CO_020 @testmcd1
Scenario: Verify cart persists after browser refresh
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I add single item to the cart
    And   I click on view cart option
    Then  I verify the single item in cart
    And   I click back button
    When  I click on view cart option
    Then  I verify the cart should retain the previously added items
    When  I click on clear all to empty the cart

@TC_Android_CO_021 @newtestmcd1
Scenario: Apply Multiple Promo Codes
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    When  I click on Menu icon
    And   I add single item to the cart
    And   I click on view cart option
    Then  I verify the single item in cart
    When  I click on 'View All' link
    And   I apply multiple promo codes
    Then  I verify only one code applied at a time
    When  I click on view cart option
    And   I click on clear all to empty the cart

@TC_Android_CO_022 @testmcd1
Scenario: Update quantity for multiple items in cart
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I add multiple items to cart
    And   I click on view cart option
    And   I clicks the 'Add' button for an item
    And   I clicks the 'Remove' button for an item
    Then  I verify the Quantity updates correctly
    And   I verify the total payable amount should be displayed
    When  I click on view cart option
    And   I click on clear all to empty the cart

@TC_Android_CO_028 @testmcd1
Scenario: Ensure guest checkout not allowed
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on search icon in home screen
    Then  I verify search menu screen navigation
    When  I click on search textfield
    And   I enter burger name and click search icon
    Then  I verify item displayed
    When  I click on add+ button
    And   I click on Add to cart option
    And   I click on view cart option
    And   I click on add address in home screen
    Then  I verify user redirected to login/signup prompt

@TC_Android_CO_023 @newtestmcd1
Scenario: Display applied offer discount in the order summary
    Given  I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    When  I click on Menu icon
    And   I add single item to the cart
    And   I click on view cart option
    Then  I verify the single item in cart
    When  I clicks the 'Add' button multiple times to increase the item quantity
    Then  I verify total amount from order summary
    When  I click on 'View All' link
    And   I apply the discount promo code
    Then  I verify the discount should be clearly shown and deducted in the order summary
    When  I click on view cart option
    And   I click on clear all to empty the cart

@TC_Android_CO_025 @testmcd1
Scenario: Validate behavior with an expired promo code
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    When  I click on Menu icon
    And   I add single item to the cart
    And   I click on view cart option
    Then  I verify the single item in cart
    When  I click on 'View All' link
    When  I enter the expired promo code and click search
    And   I click on offer Apply button and select button
    Then  I verify a message should be displayed indicating that the code is invalid or expired
    When  I click on clear all to empty the cart


@TC_Android_CO_026 @newtestmcd1
Scenario: Check total with delivery charges added
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on Menu icon
    And   I add single item to the cart
    And   I click on view cart option
    Then  I verify the single item in cart
    When  I checks the price breakdown on the right side of the page
    Then  I verify the subtotal, handling charges, CGST, and SGST should be displayed and match the total payable amount
    When  I click on clear all to empty the cart

@TC_Android_SM_001 @newtestmcd1
Scenario Outline: Search for an existing menu item
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on search icon in home screen
    Then  I verify search menu screen navigation
    When  I click on search textfield
    And   I enters 'Fries' in the search bar
    Then  I verify the search results should display items matching 'Fries'

@TC_Android_SM_002 @newtestmcd1
Scenario Outline: Search for an non-existing menu item
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on search icon in home screen
    Then  I verify search menu screen navigation
    When  I click on search textfield
    And   I enters 'Pasta' in the search bar
    Then  I verify 'No matching items found' message is displayed


@TC_Android_SM_003 @newtestmcd1
Scenario Outline: User attempts to search with empty input
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on search icon in home screen
    Then  I verify search menu screen navigation
    When  I clicks the search button without typing anything
    Then  I verify no action should be taken and prompt is displayed

@TC_Android_SM_004 @newtestmcd1
Scenario Outline: Filter menu items by Veg option
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on search icon in home screen
    Then  I verify search menu screen navigation
    When  I clicks the 'Veg' filter button
    Then  I verify only Veg items should be displayed in the menu

@TC_Android_SM_005 @newtestmcd1
Scenario Outline: Filter menu items by Non-Veg option
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on search icon in home screen
    Then  I verify search menu screen navigation
    When  I clicks the 'Non-Veg' filter button
    Then  I verify only Non-Veg items should be displayed in the menu


@TC_Android_SM_006 @newtestmcd1
Scenario Outline: Search Burger while Veg filter is active
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on search icon in home screen
    Then  I verify search menu screen navigation
    When  I clicks the 'Veg' filter button
    And   I enters 'Burger' in the search bar
    Then  I verify only Veg Burger items should be displayed in the menu


@TC_Android_SM_007 @newtestmcd1
Scenario Outline: Clear search and reset filters
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on search icon in home screen
    Then  I verify search menu screen navigation
    When  I click on search textfield
    And   I enters 'Fries' in the search bar
    Then  I verify the search results should display items matching 'Fries'
    When  I clears the search input
    Then  I verify Default view restored and no filters should be applied

@TC_Android_SM_008 @newtestmcd1
Scenario Outline: Add item to cart from search result
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on search icon in home screen
    Then  I verify search menu screen navigation
    When  I click on search textfield
    And   I enter burger name and click search icon
    Then  I verify item displayed
    When  I click on add+ button
    And   I click on Add to cart option
    And   I click on view cart option
    Then  I verify item added to the cart and quantity updated
    When  I click on clear all to empty the cart


@TC_Android_AD_017   @Fridaynew
Scenario: Verify behavior when all addresses are deleted
    Given I launch the native app
    Then  I verify the app should be launched
    And   I verify home screen navigation
    When  I click on MyMcD hamburger icon
    And   I click on login or signup button
    And   I enter a valid mobile number and click mobile verify
    And   I enter the OTP and click verify
    And   I click save changes on profile details page
    And   I click on add address in home screen
    And   I delete all addresses
    Then  I verify the address list should be empty and the Add Address prompt should be visible
    When  I click on MyMcD hamburger icon
    Then  I click on Log out button



    




    