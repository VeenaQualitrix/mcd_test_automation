@McdIosAppValidations

Feature: McD Mobile App Functionality

@TC_IOS_Login_Mobile_0002
Scenario Outline: Verify login with valid Mobile Number and OTP on Mobile App
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    Then I verify the Login Sign Up screen appears
    When I tap on the Login Sign Up Button
    And I enter a valid mobile number click on verify
    
    
    
@TC_IOS_Login_Mobile_0002
Scenario Outline: Verify referral code input
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    Then I verify the Login Sign Up screen appears
    When I tap on the Login Sign Up Button
    And  I enter a valid mobile number
    And  I click on referral link
    And  I enter referral code
    Then  I verify referral code accepted without error

# @TC_IOS_Login_Mobile_0003
# Feature: Validate Mobile Number Field Input
# Scenario: Validate that alphabets are not accepted in the mobile number field
#     Given I launch the mobile application
#     Then I verify the app home screen is displayed
#     When I tap on the My McD bottom tab
#     Then I verify the Login Sign Up screen appears
#     When I tap on the Login Sign Up button
#     And I enter alphabets in mobile number field
#     Then I confirm 'verify mobile' button is disabled


@TC_IOS_Login_Mobile_00012
Scenario Outline: Validate empty mobile number
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    Then I verify the Login Sign Up screen appears
    When I tap on the Login Sign Up Button
    When  I leave mobile field empty 
    Then  I confirm 'verify mobile' button is disabled
    
    

@TC_IOS_Login_Mobile_0004
Scenario Outline: Validate short mobile number
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    Then I verify the Login Sign Up screen appears
    When I tap on the Login Sign Up Button
    When  I enter a mobile number with less than 10 digits
    Then  I confirm 'verify mobile' button is disabled

@TC_IOS_Login_Mobile_0005
Scenario Outline: Validate alphabetic input in mobile field
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    Then I verify the Login Sign Up screen appears
    When I tap on the Login Sign Up Button
    When  I enter alphabets in mobile number field
    Then  I confirm 'verify mobile' button is disabled

@TC_IOS_Login_Mobile_0006
Scenario Outline: Verify referral code without entering mobile number
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    Then I verify the Login Sign Up screen appears
    When I tap on the Login Sign Up Button
    When  I click on referral link
    And   I enter referral code and click verify
    Then  I verify error message

@TC_IOS_Login_Mobile_0007
Scenario Outline: Verify mobile number with spaces
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    Then I verify the Login Sign Up screen appears
    When I tap on the Login Sign Up Button
    When  I enter mobile number with spaces and click verify
    Then  I confirm 'verify mobile' button is disabled

@TC_IOS_Login_Mobile_0008
Scenario Outline: Verify mobile number with special characters
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    Then I verify the Login Sign Up screen appears
    When I tap on the Login Sign Up Button
    When  I enter mobile number with special characters and click verify
    Then  I confirm 'verify mobile' button is disabled
   
@TC_IOS_Login_Mobile_0009
Scenario Outline: Verify UI alignment and presence of elements
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    Then I verify the Login Sign Up screen appears
    When I tap on the Login Sign Up Button
    When  I visually inspect the mobile number field
    And   I visually inspect the referral link section
    And   I visually inspect the verify button
    And   I visually inspect the footer links
    Then  I verify all elements should be visible, correctly aligned, and not overlapping

@TC_IOS_Login_Mobile_00010
Scenario Outline: Verify referral link is clickable
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    Then I verify the Login Sign Up screen appears
    When I tap on the Login Sign Up Button
    When  I click on referral link
    Then  I verify referral textfield is displayed

@TC_IOS_Login_Mobile_00011
Scenario Outline: Verify "Verify Mobile" button is disabled initially and OTP screen is shown on valid input/10digit valid mobile number
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    Then I verify the Login Sign Up screen appears
    When I tap on the Login Sign Up Button
    Then   I confirm 'verify mobile' button is disabled
    When  I enter a valid mobile number click on verify
    Then  I verify OTP screen navigation


@TC_IOS_Login_Mobile_00015
Scenario: Validate navigation when clicking on “Terms and Conditions” link
    Given I launch the mobile application  
    Then I verify the app home screen is displayed  
    When I tap on the My McD bottom tab  
    Then I verify the Login Sign Up screen appears  
    When I tap on the Login Sign Up Button   
    When I tap on the Terms and Conditions link  
# Then I verify the Terms and Conditions web view or page is displayed


 

@TC_IOS_Login_Mobile_00016
Scenario: Validate error for 11-digit mobile number input
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    Then I verify the Login Sign Up screen appears
    When I tap on the Login Sign Up Button
    And I enter a mobile number with more than 10 digits
#   not able to enter more than 10 digits in mobile field

@TC_IOS_Login_Mobile_00017
Scenario: Verify pasting a mobile number from clipboard into the input field
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    Then I verify the Login Sign Up screen appears
    When I tap on the Login Sign Up Button
    And I copied a mobile number
    When I paste the number with Ctrl V and click verify
    Then I verify number pasted correctly and accepted


@TC_IOS_Profile_Mobile_00001
Scenario: Update name successfully
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    Then I verify the Login Sign Up screen appears
    When I tap on the Login Sign Up Button
    When  I enter a valid mobile number click on verify
    Then  I verify OTP screen navigation
    When  I enter the OTP and click verify
    When I edit the full name field

@TC_IOS_Profile_Mobile_00001
Scenario: Validate empty name field
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    Then I verify the Login Sign Up screen appears
    When I tap on the Login Sign Up Button
    When  I enter a valid mobile number click on verify
    Then  I verify OTP screen navigation
    When  I enter the OTP and click verify
    When I edit the full name field
    When I clear the full name field
    # And  I click on Save Changes

@TC_IOS_Profile_Mobile_00002
Scenario: Verify login with invalid characters
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    When I tap on the Edit icon
    When I edit the full name field
    When I clear the full name field
    Then I enter invalid characters in the full name field

@TC_IOS_Profile_Mobile_00003
Scenario: Verify validate phone number field
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    When I tap on the Edit icon
    And I enter a validate phone number  

@TC_IOS_Profile_Mobile_00004
Scenario: Update email address
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    When I tap on the Edit icon
    And I enter a valid email address

@TC_IOS_Profile_Mobile_00004
Scenario: Validate incorrect email format
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    When I tap on the Edit icon
    And I enter a valid email address
    When I enter an invalid email address


@TC_IOS_Profile_Mobile_00005
Scenario: Update date of birth successfully
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    When I tap on the Edit icon
    And I update the Date of Birth
    And I click on select button in DOB

@TC_IOS_Profile_Mobile_00005
Scenario: User updates Date of Birth and saves the profile successfully
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    When I tap on the Edit icon
    And I update the Date of Birth
    And I click on select button in DOB
    And I enter a validate future date 

@TC_IOS_Profile_Mobile_00006
Scenario: Verify the change pictures link
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    When I tap on the Edit icon
    And I tap on the Change Picture link
    Then I verify the profile picture field

@TC_IOS_Profile_Mobile_00007
Scenario: Verify the save button disabled
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    When I tap on the Edit icon
    When I edit the full name field
    When I clear the full name field

@TC_IOS_Profile_Mobile_00007
Scenario: Toggle color blind mode on/off
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    When I tap on the Edit icon
    When I edit the full name field
    When I clear the full name field
    # Then I click on color blinded friendly toggle 

@TC_IOS_Profile_Mobile_00007
Scenario: Verify color blind preference saved
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    When I tap on the Edit icon
    When I edit the full name field
    When I clear the full name field
    # Then I click on color blinded friendly toggle 
    # Then I verify the color preference saved
    # There is no locators for the toggle
    

@TC_IOS_Profile_Mobile_00008
Scenario: Verify the field icons are displayed correctly
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    And I tap on the Edit icon
    Then I verify the field icons are displayed correctly



@TC_IOS_Switching_Mobile_00001
Scenario: Verify the field icons and business model dropdown options
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Business Model dropdown

@TC_IOS_Switching_Mobile_00002
Scenario: Validate user can select “McDelivery” and proceed
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Business Model dropdown

@TC_IOS_Switching_Mobile_00003
Scenario: Validate user can select “Dine-In” and proceed
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Business Model dropdown  

@TC_IOS_Switching_Mobile_00004
Scenario: Validate user can select “On the Go” and proceed
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Business Model dropdown           

@TC_IOS_Switching_Mobile_00005
Scenario: Validate user can select “Take Away” and proceed
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Business Model dropdown               

        

@TC_IOS_Address_Mobile_00010
Scenario: Trigger login when clicking Add Address as guest
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    And I proceed to the checkout screen
    When I click the Add Address button
    Then I should be redirected to the login screen 


@TC_IOS_Address_Mobile_00011
Scenario: Successful login redirects to Add Address screen
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I tap on the My McD bottom tab
    And I proceed to the checkout screen
    When I click the Add Address button
    Then I should be redirected to the login screen 
    When I tap on the login continue
    When  I enter a valid mobile number click on verify
    Then  I verify OTP screen navigation
    When  I enter the OTP and click verify 


@TC_IOS_Address_Mobile_00011
Scenario: Cancel login from Add Address prompt
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    And I click on the Menu option
    And I click on an item to Add
    And I click on the Next button
    And I click on Add to Cart
    And I click on View Cart
    And I tap on the login continue button
    And I close the login screen
    Then I should be redirected back to the cart or checkout screen    
      
            
@TC_IOS_Address_Mobile_00013
Scenario: Incorrect login from Add Address screen
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    And I click on the Menu option
    And I click on an item to Add
    And I click on the Next button
    And I click on Add to Cart
    And I click on View Cart
    And I tap on the login continue button
    When  I enter mobile number with special characters and click verify    


    
