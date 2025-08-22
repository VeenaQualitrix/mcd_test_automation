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
    And  I verify the mobile number input field is present
    And  I verify the referral link field is present 
    And  I verify the Verify button is visible  
    Then I verify the footer links are displayed at the bottom of the screen 

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


@TC_IOS_Address_Mobile_00014
Scenario: Add a new delivery address during checkout
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Add Address button
    Then I should be redirected to the login screen 
    When I tap on the login continue
    When  I enter a valid mobile number click on verify
    Then  I verify OTP screen navigation
    When  I enter the OTP and click verify 
    And   I click on Save button
    When I click the Add Address button
    And I tap on Add New Address
    And I click on confirm location
    And I enter valid address details
    Then I tap on the Save Address

@TC_IOS_Address_Mobile_00015
Scenario: Add address with missing mandatory fields
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Add Address button
    And I tap on Add New Address
    And I click on confirm location
    And I leave mandatory address fields empty
    Then I verify save is disabled
   

@TC_IOS_Address_Mobile_00016
Scenario: Add address with special characters in fields
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Add Address button
    And I tap on Add New Address
    And I click on confirm location
    And I enter special characters in address fields
    Then I tap on the Save Address
    

@TC_IOS_Address_Mobile_00017
Scenario: Cancel address entry mid-way
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Add Address button
    And I tap on Add New Address
    And I click on confirm location
    Then I start entering address and cancel before saving
    
@TC_IOS_Address_Mobile_00018
Scenario: Verify max character limit for address fields
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Add Address button
    And I tap on Add New Address
    And I click on confirm location
    And I enter text exceeding the max character limit in address fields
    Then I tap on the Save Address    

@TC_IOS_Address_Mobile_00019
Scenario: Add duplicate address
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Add Address button
    And I tap on Add New Address
    And I click on confirm location
    And I enter an address identical to an existing one
    Then I tap on the Save Address
    When I click the Add Address button
    And I tap on Add New Address
    And I click on confirm location
    And I enter an address identical to an existing one
    Then I tap on the Save Address
    When I click the Add Address button
    And I verify that the duplicate address is saved

@TC_IOS_Address_Mobile_00020
Scenario: Add Use Current Location
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Add Address button
    And I tap on Add New Address
    And I click on confirm location
    And I enter valid address details
    Then I tap on the Save Address

    
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

@TC_IOS_Switching_Mobile_00006
Scenario: Dine-In option remains selected until manually changed
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    And I select the Dine In option
    Then I verify that Dine-In remains the selected option

@TC_IOS_Switching_Mobile_00007
Scenario: Ensure mobile responsiveness of dropdown and tappable
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Business Model dropdown  

@TC_IOS_Switching_Mobile_00008
Scenario: Verify default business model on first visit
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    And I verify that the default business model is set to McDelivery

@TC_IOS_Switching_Mobile_00009
Scenario: Location permission prompt appears when selecting "On the Go" or "Dine-In" without location access
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    And I select the On the Go option
    Then I verify that the location permission prompt is displayed

 
@TC_IOS_Switching_Mobile_00010
Scenario: Display service unavailability message for unsupported region
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Add Address button
    And I tap on Add New Address
    And I click on confirm location
    And I enter unsupported address details
    Then I tap on the Save Address
    Then I verify that the message Service not available in your area is displayed
    # need to off the location -19/25

@TC_IOS_Switching_Mobile_00011
Scenario: Ensure only one business model can be active at a time
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    And I select the Dine In option
    And I select the On the Go option
    Then I verify that the location permission prompt is displayed

@TC_IOS_Switching_Mobile_00012
Scenario: Verify model selection updates restaurant listing
    Given I launch the mobile application  
    Then I verify the app home screen is displayed  
    And I select the Dine In option 
    Then I verify that only restaurants with Dine-In availability are displayed

@TC_IOS_Switching_Mobile_00013
Scenario: Test visual feedback on tap for business model options on mobile
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Business Model dropdown
    Then I verify that each option provides visual feedback highlight, underline, or bold

@TC_IOS_Switching_Mobile_00014
Scenario: Ensure model selection doesn't affect account/profile data
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    And I open the Profile section and note the profile details
    And I click on the homepage
    And I select the Dine In option
    And I select the MCDelivery
    Then I verify that the profile details remain unchanged

@TC_IOS_Switching_Mobile_00015
Scenario: Validate different UI layouts for each business model    
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Business Model dropdown  

@TC_IOS_Address_Store_Mobile_0001
Scenario: Select an existing delivery address
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Add Address button
    And I select an existing address from the saved list
    Then I verify that the selected address is applied

@TC_IOS_Address_Store_Mobile_0002
Scenario: Add a new delivery address
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Add Address button
    And I tap on Add New Address
    And I click on confirm location
    And I enter valid address details
    Then I tap on the Save Address
    Then I verify that the selected address is applied
    
@TC_IOS_Address_Store_Mobile_0003
Scenario: Edit an existing delivery address
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Add Address button
    And I tap on Add New Address
    And I click on confirm location
    And I enter valid address details
    Then I tap on the Save Address
    When I click the Add Address button
    And I click the edit icon for the selected address
    And I modify the address details
    Then I tap on the Save Address
    Then I verify that the updated address appears in the list

@TC_IOS_Address_Store_Mobile_0004
Scenario: Delete an existing delivery address
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Add Address button
    And I click the delete icon for the selected address
    
@TC_IOS_Address_Store_Mobile_0005
Scenario: Ensure address selection updates nearby restaurant list
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    And I select the Dine In option
    And I select an near by restaurant first times
    And I select the MCDelivery
    And I select the Dine In option
    And I select an near by restaurant second times

@TC_IOS_Address_Store_Mobile_0006   
Scenario: Validate empty address cannot be saved
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Add Address button
    And I tap on Add New Address
    And I click on confirm location
    And I leave the address fields blank
    Then I verify that the error message Address fields required is displayed

@TC_IOS_Address_Store_Mobile_0007
Scenario: Verify "Near" location is shown under each address
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    And I select the Dine In option
    Then I verify that the Near label is displayed under each address

@TC_IOS_Address_Store_Mobile_0008
Scenario: Ensure scroll functionality works if many addresses are saved
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    And I select the Dine In option
    When I scroll through the address list
    Then I verify that all addresses are accessible via scrolling

@TC_IOS_Address_Store_Mobile_0009
Scenario: Verify error message for undeliverable address
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Add Address button
    And I tap on Add New Address
    And I click on confirm location
    And I enter unsupported address details
    Then I tap on the Save Address
    Then I verify that the message Service not available in your area is displayed
    # need to off the location -21/25

@TC_IOS_Address_Store_Mobile_0010
Scenario: Select an existing delivery address
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Add Address button
    And I select an existing address from the saved list
    Then I verify that the selected address is applied

@TC_IOS_Address_Store_Mobile_0011
Scenario: Ensure “Add New” opens address entry popup or page
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Add Address button
    And I tap on Add New Address
    And I click on confirm location
    And I enter valid address details

@TC_IOS_Address_Store_Mobile_0012
Scenario: Ensure address list remains consistent across sessions
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Add Address button
    And I select an existing address from the saved list
    When I tap on the My McD bottom tab
    And I log out of the application
    When I tap on the My McD bottom tab
    Then I verify the Login Sign Up screen appears
    When I tap on the Login Sign Up Button
    And I enter a valid mobile number click on verify
    Then  I verify OTP screen navigation
    When  I enter the OTP and click verify
    And   I click on Save button
    When I click the Add Address button
    Then I verify that the selected address is applied

@TC_IOS_Address_Store_Mobile_0013
Scenario: Verify behavior when all addresses are deleted
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Add Address button
    When I delete all saved addresses
    Then I verify that the last address is not deleted as it is set as the default address

@TC_IOS_Address_Store_Mobile_0014  
Scenario: Test address tagging (“Home”, “Work”) feature
    Given I launch the mobile application
    Then I verify the app home screen is displayed
    When I click the Add Address button
    And I click the edit icon for the selected address
    And I select the Home tag and Work for the address and verify that the tag is applied
    Then I tap on the Save Address


