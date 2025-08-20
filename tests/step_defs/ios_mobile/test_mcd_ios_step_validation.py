from pytest_bdd import given, when, then, scenarios
from conftest import readPreReqJson
from pytest_bdd.parsers import parse
import allure
from pages.mobile.login_screen_ios import LoginScreenIos
from pages.mobile.profile_screen_ios import ProfileScreenIos
from pages.mobile.address_screen_ios import AddressScreenIos
from pages.mobile.switching_screen_ios import SwitchScreenIos
from pages.mobile.address_store_screen_ios import AddressStoreScreenIos
import pyperclip

scenarios('../../features/IOS_Mobile/Mcd_ios_Testcases.feature')


@given("I launch the mobile application")
@allure.step("Given I launch the mobile application")
def launch_mobile_application(setup_platform):
    driver = setup_platform
    if driver is None:
        assert False, "Driver not initialized."

    app_package = "com.il.mcd"
    assert driver.is_app_installed(app_package), f"App {app_package} is not installed."
    print(f"App {app_package} is installed and ready.")


@then("I verify the app home screen is displayed")
@allure.step("Then I verify the app home screen is displayed")
def verify_app_home_screen(setup_platform):
    is_displayed = LoginScreenIos(setup_platform).verify_bottom_tab_my_mcd_is_displayed()
    assert is_displayed, "'My McD' bottom tab is not displayed on home screen."


@when("I tap on the My McD bottom tab")
@allure.step("When I tap on the My McD bottom tab")
def tap_on_my_mcd_tab(setup_platform):
    LoginScreenIos(setup_platform).click_bottom_tab_my_mcd()


@then("I verify the Login Sign Up screen appears")
@allure.step("Then I verify the Login Sign Up screen appears")
def verify_login_signup_appears(setup_platform):
    is_displayed = LoginScreenIos(setup_platform).verify_login_signup_text()
    assert is_displayed, "'Login/Sign Up' text is not displayed."


@when("I tap on the Login Sign Up Button")
@allure.step("When I tap on the Login Sign Up button")
def tap_login_signup(setup_platform):
    LoginScreenIos(setup_platform).click_login_signup_button()


@when("I enter a valid mobile number click on verify")
@allure.step("When I enter a valid mobile number")
def enter_mobile_number(setup_platform):
    screen = LoginScreenIos(setup_platform)
    screen.enter_mobile_number("7777777777")
    LoginScreenIos(setup_platform).click_verify_mobile()


@when("I enter a valid mobile number")
@allure.step("When I enter a valid mobile number")
def enter_mobile_number(setup_platform):
    screen = LoginScreenIos(setup_platform)
    screen.enter_mobile_number("9876543210")


@when("I tap on Verify Mobile")
@allure.step("When I tap on Verify Mobile")
def tap_verify_mobile(setup_platform):
    LoginScreenIos(setup_platform).click_verify_mobile()


# @when("I enter the OTP and click verify")
# @allure.step("When I enter the OTP and click verify")
# def enter_the_otp_and_click_verify(setup_platform):
#     otp = readPreReqJson("test_data", "OTP")
#     print("Entering OTP")
#     LoginScreenIos(setup_platform).enter_otp(otp)


@then("I verify OTP screen navigation")
@allure.step("Then I verify OTP screen navigation")
def verify_otp_page_navigation(setup_platform):
    print("Verify otp screen navigation")
    Otp_page_navigation = LoginScreenIos(setup_platform).verify_otp_screen_is_displayed()
    assert Otp_page_navigation, "otp page Is Not navigated successfully As Expected"


@when("I click save changes on profile details page")
@allure.step("When I click save changes on profile details page")
def click_save_button_on_profile_screen(setup_platform):
    print("click save changes on profile details page")
    LoginScreenIos(setup_platform).Click_save_button_on_profile_details_screen()


@when("I click on referral link")
@allure.step("When I click on referral link")
def click_on_referral_link(setup_platform):
    print("Clicking on referral link")
    LoginScreenIos(setup_platform).click_referral_code_link()


@then('I verify referral textfield is displayed')
@allure.step("Then I verify referral textfield is displayed")
def verify_referral_textfield_is_displayed(setup_platform):
    print("Verifying referral textfield is displayed")
    LoginScreenIos(setup_platform).verify_referral_text_field_is_displayed()


@when("I enter referral code")
@allure.step("When I enter referral code")
def enter_referral_code(setup_platform):
    Referral_code = readPreReqJson("test_data", "Referral_code")
    print(f"Entering referral code: {Referral_code}")
    LoginScreenIos(setup_platform).enter_referral_code(Referral_code)


@when("I enter referral code and click verify")
@allure.step("When I enter referral code and click verify")
def enter_referral_code_and_verify(setup_platform):
    Referral_code = readPreReqJson("test_data", "Referral_code")
    print(f"Entering referral code: {Referral_code}")
    LoginScreenIos(setup_platform).enter_referral_code_click_verify(Referral_code)


@then('I verify error message')
@allure.step("Then I verify error message")
def verify_error_message(setup_platform):
    print("Verifying error message")
    Login_Page = LoginScreenIos(setup_platform).mobile_field_empty_error()
    assert Login_Page, "Please enter valid mobile number"


@then('I verify referral code accepted without error')
@allure.step("Then I verify referral code accepted without error")
def verify_referral_code_accepted(setup_platform):
    print("Verifying that the referral code was accepted")
    result = LoginScreenIos(setup_platform).verify_referral_code_accepted_without_error()
    assert result, "Referral code was not accepted or an error appeared"


@when("I leave mobile field empty")
@allure.step("When I leave mobile field empty")
def leave_mobile_field_empty(setup_platform):
    print("leave mobile field empty")
    LoginScreenIos(setup_platform).leave_mobile_field_empty()


@when("I enter a mobile number with less than 10 digits")
@allure.step("When I enter a mobile number with less than 10 digits")
def enter_a_invalid_mobile_number(setup_platform):
    invalid_mobile_number = readPreReqJson("test_data", "invalid_mobile_number")
    print("Entering invalid Mobile Number")
    LoginScreenIos(setup_platform).enter_invalid_mobile_number(invalid_mobile_number)


@then("I confirm 'verify mobile' button is disabled")
@allure.step("Then I confirm 'verify mobile' button is disabled")
def verify_error_message(setup_platform):
    print("Confirming 'verify mobile' button is disabled")
    LoginScreenIos(setup_platform).verify_mobile_button_is_disabled()


@when("I enter alphabets in mobile number field")
@allure.step("When I enter alphabets in mobile number field")
def enter_alphabets_in_mobile_number_field(setup_platform):
    alphabets_in_mobile_number = readPreReqJson("test_data", "alphabets_in_mobile_number")
    print("Entering alphabets in Mobie Number field")
    LoginScreenIos(setup_platform).enter_alphabets_in_mobile_text_field(alphabets_in_mobile_number)


@when("I enter mobile number with spaces and click verify")
@allure.step("When I enter mobile number with spaces and click verify")
def enter_mobile_number_with_space_and_click_verify(setup_platform):
    mobile_number_with_space = readPreReqJson("test_data", "mobile_number_with_space")
    print("Entering mobile number with spaces")
    LoginScreenIos(setup_platform).enter_mobile_number_with_space(mobile_number_with_space)


@when("I enter mobile number with special characters and click verify")
@allure.step("When I enter mobile number with special characters and click verify")
def enter_mobile_number_with_special_char_and_click_verify(setup_platform):
    special_characters_in_mobile_field = readPreReqJson("test_data", "special_characters_in_mobile_field")
    print("Entering mobile number with special characters")
    LoginScreenIos(setup_platform).enter_mobile_number_with_special_char(special_characters_in_mobile_field)


@when("I enter an 11-digit mobile number and click mobile verify")
@allure.step("When I enter 11 digits mobile number and click verify")
def enter_11_digits_mobile_number(setup_platform):
    Mobile_number_11_digits = readPreReqJson("test_data", "mobile_number_11_digits")
    print(f"Typing mobile number: {Mobile_number_11_digits} one digit at a time")
    LoginScreenIos(setup_platform).enter_mobile_number_one_by_one(Mobile_number_11_digits)    

@when('I tap on the Terms and Conditions link')
@allure.step("When I tap on the Terms and Conditions link")
def tap_on_terms_and_conditions_link(setup_platform):
    LoginScreenIos(setup_platform).tap_terms_and_conditions_link()


@when("I enter a mobile number with more than 10 digits")
@allure.step("When I enter a mobile number with more than 10 digits")
def enter_mobile_number_with_more_than_10_digits(setup_platform):
    LoginScreenIos(setup_platform).enter_invalid_mobile_number("98765432101")

@when("I copied a mobile number")
@allure.step("When I copied a mobile number")
def copy_mobile_number(setup_platform):
    Copied_number = readPreReqJson("test_data", "mobile_number")
    print("verify mobile number copied")
    LoginScreenIos(setup_platform).copy_mobile_number_to_clipboard(Copied_number)


@when("I paste the number with Ctrl V and click verify")
@allure.step("When I paste the number with Ctrl V and click verify")
def paste_copied_mobile_number(setup_platform):
    print("Pasting mobile number using Ctrl+V")
    LoginScreenIos(setup_platform).paste_mobile_number_using_clipboard()


@then("I verify number pasted correctly and accepted")
@allure.step("Then I verify number pasted correctly and accepted")
def verify_number_pasted_correctly(setup_platform):
    print("Verifying that the pasted number was accepted correctly")

    expected_number = readPreReqJson("test_data", "mobile_number")
    actual_number = LoginScreenIos(setup_platform).get_pasted_mobile_number()

    print(f"Expected Mobile Number: {expected_number}")
    print(f"Actual Mobile Number in Field: {actual_number}")

    assert actual_number == expected_number, "Pasted mobile number does not match or was not accepted"


@then("I verify the Terms and Conditions web view or page is displayed")
@allure.step("Then I verify the Terms and Conditions web view or page is displayed")
def verify_terms_and_conditions_page(setup_platform):
    LoginScreenIos(setup_platform).verify_terms_and_conditions_page_displayed()

@when("I verify the mobile number input field is present")
@allure.step("Then I verify the mobile number input field is present and properly aligned")
def verify_mobile_number_field_alignment(setup_platform):
    print("Verifying presence and alignment of mobile number input field")
    LoginScreenIos(setup_platform).validate_mobile_field()

@when("I verify the referral link field is present")
@allure.step("Then I verify the referral link field is present")
def verify_referral_link_field(setup_platform):
    print("Verifying presence of the referral link field")
    LoginScreenIos(setup_platform).verify_referral_link()

@when("I verify the Verify button is visible")
@allure.step("Then I verify the Verify button is visible")
def verify_verify_button_is_visible(setup_platform):
    print("Verifying visibility of the Verify button")
    LoginScreenIos(setup_platform).verify_verify_button_is_visible()

@then("I verify the footer links are displayed at the bottom of the screen")
@allure.step("Then I verify the footer links are displayed at the bottom of the screen")
def verify_footer_links_displayed(setup_platform):
    print("Verifying footer links are displayed at the bottom of the screen")
    LoginScreenIos(setup_platform).verify_footer_links_position()


@when("I enter the OTP and click verify")
@allure.step("When I enter the OTP and click verify")
def enter_the_otp_and_click_verify(setup_platform):
    otp = readPreReqJson("test_data", "OTP")
    print("Entering OTP")
    ProfileScreenIos(setup_platform).enter_otp(otp)

@when("I edit the full name field")
@allure.step("Edit the full name field")
def edit_full_name_field(setup_platform):
    profile = ProfileScreenIos(setup_platform)
    profile.enter_full_name("John Doe")  # You can parameterize if needed

@when("I clear the full name field")
@allure.step("Clear the full name field")
def clear_full_name_field(setup_platform):
    profile = ProfileScreenIos(setup_platform)
    profile.clear_full_name()
 

@when('I click on Save Changes')
@allure.step("Click on Save Changes button")
def click_save_changes(setup_platform):
    profile = ProfileScreenIos(setup_platform)
    profile.click_save_changes()

@when('I click on Save button')
@allure.step("Click on Save Changes button")
def click_save_changes(setup_platform):
    profile = ProfileScreenIos(setup_platform)
    profile.click_save()

@then("I enter invalid characters in the full name field")
@allure.step("Enter invalid characters in the full name field")
def step_enter_invalid_characters_in_name(setup_platform):
    profile = ProfileScreenIos(setup_platform)
    profile.invalid_character("John@123")  # or any invalid input

@when("I tap on the Edit icon")
@allure.step("Tap on the Edit icon")
def tap_edit_icon(setup_platform):
    profile = ProfileScreenIos(setup_platform)
    profile.tap_edit_icon()

@when("I enter a validate phone number")
@allure.step("I enter a valid phone number")
def enter_valid_number(setup_platform):
    profile = ProfileScreenIos(setup_platform)
    profile.verify_the_number("7777777777")

@when("I enter a valid email address")
@allure.step("I enter a valid email address")
def step_enter_vaild_email(setup_platform):
    profile = ProfileScreenIos(setup_platform)
    profile.enter_email("john.doe@example.com")  

@when("I enter an invalid email address")
@allure.step("I enter an invalid email address")
def step_enter_invaild_email(setup_platform):
    profile = ProfileScreenIos(setup_platform)
    profile.enter_invalid_email_address("john.doe.com")

@when("I update the Date of Birth")
@allure.step("I update the Date of Birth")
def step_update_dob(setup_platform):
    print("click on select button in DOB")
    ProfileScreenIos(setup_platform).click_DOB()


@when("I click on select button in DOB")
@allure.step("I click on select button in DOB")
def tap_dob_save_button(setup_platform):
    print("click on select button in DOB")
    ProfileScreenIos(setup_platform).save_button_on_DOB()

@when("I enter a validate future date")
@allure.step("I enter a validate future date")
def tap_dob_save_button(setup_platform):
    print("validate future date")
    ProfileScreenIos(setup_platform).validate_future_dates()

@when("erify the change pictures link")
@allure.step("erify the change pictures link")
def tap_dob_save_button(setup_platform):
    print("validate future date")
    ProfileScreenIos(setup_platform).validate_future_dates()        

@when("I tap on the Change Picture link")
@allure.step("verify the change pictures link")
def verify_change_pictures_link(setup_platform):
    print("I tap on change pictures link")
    ProfileScreenIos(setup_platform).click_change_pictures_link()    

@then("I verify the profile picture field")
@allure.step("Verify the profile picture field is displayed")
def verify_profile_picture_field(setup_platform):
    print("Verifying profile picture field")
    ProfileScreenIos(setup_platform).verify_profile_picture_field()    

@when('I verify the save button disabled')
@allure.step("I verify the save button disabled")
def verify_the_save_button_disable(setup_platform):
    profile = ProfileScreenIos(setup_platform)
    profile.verify_save_button_disabled()    

@then("I click on color blinded friendly toggle")
@allure.step("Click on color blinded friendly toggle")
def click_color_blind_toggle(setup_platform):
    print("Clicking on color blinded friendly toggle")
    ProfileScreenIos(setup_platform).click_color_blinded_toggle()    

@then("I verify the field icons are displayed correctly")
@allure.step("Verify the field icons are displayed correctly")
def verify_field_icons_displayed(setup_platform):
    print("Verifying field icons are displayed correctly")
    ProfileScreenIos(setup_platform).verify_field_icons()

@when("I click the Business Model dropdown")
@allure.step("Click the Business Model dropdown")
def click_business_model_dropdown(setup_platform):
    print("Clicking the Business Model dropdown")
    SwitchScreenIos(setup_platform).click_business_model_dropdown()    

@when("I proceed to the checkout screen")
@allure.step("Proceed to the checkout screen")
def step_proceed_to_checkout_screen(setup_platform):
    print("Proceeding to the checkout screen")
    AddressScreenIos(setup_platform).navigate_to_checkout()

@when("I click the Add Address button")
@allure.step("Click the Add Address button")
def step_click_add_address_button(setup_platform):
    print("Clicking the Add Address button")
    AddressScreenIos(setup_platform).click_add_address()

@then("I should be redirected to the login screen")
@allure.step("Verify redirection to login/signup screen")
def step_verify_login_signup_redirection(setup_platform):
    print("Verifying redirection to login/signup screen")
    AddressScreenIos(setup_platform).verify_login_signup_screen()


@when("I tap on the login continue")
@allure.step("Tap on the login continue button")
def step_tap_login_continue(setup_platform):
    print("Tapping on the login continue button")
    AddressScreenIos(setup_platform).tap_continue_button()

@then("I click on the Menu option")
@allure.step("Click on the Menu option")
def step_click_on_menu_option(setup_platform):
    print("Clicking on the Menu option")
    AddressScreenIos(setup_platform).click_menu_option()

@then("I click on an item to Add")
@allure.step("Click on an item to Add")
def step_click_on_item_to_add(setup_platform):
    print("Clicking on an item to Add")
    AddressScreenIos(setup_platform).click_add_on_item()

@then("I click on the Next button")
@allure.step("Click on the Next button")
def step_click_next_button(setup_platform):
    print("Clicking on the Next button")
    AddressScreenIos(setup_platform).click_next_button()

@then("I click on Add to Cart")
@allure.step("Click on Add to Cart")
def step_click_add_to_cart(setup_platform):
    print("Clicking on Add to Cart")
    AddressScreenIos(setup_platform).click_add_to_cart()

@then("I click on View Cart")
@allure.step("Click on View Cart")
def step_click_view_cart(setup_platform):
    print("Clicking on View Cart")
    AddressScreenIos(setup_platform).click_view_cart()

@then("I tap on the login continue button")
@allure.step("Tap on the login continue button")
def step_tap_login_continue_button(setup_platform):
    print("Tapping on the login continue button")
    AddressScreenIos(setup_platform).login_continue_button()

@then("I close the login screen")
@allure.step("Close the login screen")
def step_close_login_screen(setup_platform):
    print("Closing the login screen")
    AddressScreenIos(setup_platform).close_login_screen()

@then("I should be redirected back to the cart or checkout screen")
@allure.step("Verify redirection to the cart or checkout screen")
def step_verify_redirection_to_cart_or_checkout(setup_platform):
    print("Verifying redirection to the cart or checkout screen")
    AddressScreenIos(setup_platform).verify_cart_or_checkout_screen_displayed()

@when("I tap on Add New Address")
@allure.step("When I tap on Add New Address")
def tap_on_add_new_address(setup_platform):
    print("Tapping on 'Add New Address'")
    AddressScreenIos(setup_platform).tap_add_new_address()

@when("I click on confirm location")
@allure.step("When I click on confirm location")
def click_on_confirm_location(setup_platform):
    print("Clicking on 'Confirm Location' button")
    AddressScreenIos(setup_platform).click_confirm_location()

@when("I enter valid address details")
@allure.step("When I enter valid address details")
def enter_valid_address_details(setup_platform):
    print("Entering valid address details")
    AddressScreenIos(setup_platform).enter_address_details()

@then("I tap on the Save Address")
@allure.step("Then I tap on the Save Address")
def tap_on_save_address(setup_platform):
    print("Tapping on 'Save Address' button")
    AddressScreenIos(setup_platform).tap_save_address()

@when("I leave mandatory address fields empty")
@allure.step("When I leave mandatory address fields empty")
def leave_mandatory_address_fields_empty(setup_platform):
    print("Leaving mandatory address fields empty")
    AddressScreenIos(setup_platform).leave_mandatory_fields_empty()

@then("I verify save is disabled")
@allure.step("Then I verify save is disabled")
def verify_save_is_disabled(setup_platform):
    print("Verifying that 'Save' button is disabled")
    assert AddressScreenIos(setup_platform).is_save_button_disabled(), "'Save' button should be disabled but it is enabled"

@when("I enter special characters in address fields")
@allure.step("When I enter special characters in address fields")
def enter_special_characters_in_address_fields(setup_platform):
    print("Entering special characters into address fields")
    AddressScreenIos(setup_platform).enter_special_character_address()

@then("I start entering address and cancel before saving")
@allure.step("Then I start entering address and cancel before saving")
def step_cancel_address_entry(setup_platform):
    AddressScreenIos(setup_platform).cancel_address_entry_midway()

@when("I enter text exceeding the max character limit in address fields")
@allure.step("And I enter text exceeding the max character limit in address fields")
def step_enter_text_exceeding_limit(setup_platform):
    AddressScreenIos(setup_platform).enter_text_exceeding_max_limit()


@when("I enter an address identical to an existing one")
@allure.step("And I enter an address identical to an existing one")
def step_enter_duplicate_address(setup_platform):
    AddressScreenIos(setup_platform).enter_duplicate_address()

@when("I verify that the duplicate address is saved")
@allure.step("And I verify that the duplicate address is saved")
def step_verify_duplicate_address_saved(setup_platform):
    AddressScreenIos(setup_platform).verify_duplicate_address_saved()

@then("I select the Dine In option")
@allure.step("When I select the Dine-In option")
def step_select_dine_in_option(setup_platform):
    SwitchScreenIos(setup_platform).select_dine_in()

@then("I verify that Dine-In remains the selected option")
@allure.step("Then I verify that Dine-In remains the selected option")
def step_verify_dine_in_remains_selected(setup_platform):
    SwitchScreenIos(setup_platform).verify_dine_in_selected()    

@then("I verify that the default business model is set to McDelivery")
@allure.step("And I verify that the default business model is set to McDelivery")
def step_verify_default_business_model(setup_platform):
    SwitchScreenIos(setup_platform).verify_default_business_model()

@then("I select the On the Go option")
@allure.step("And I select the On the Go option")
def step_select_on_the_go(setup_platform):
    SwitchScreenIos(setup_platform).select_on_the_go()

@then("I verify that the location permission prompt is displayed")
@allure.step("Then I verify that the location permission prompt is displayed")
def step_verify_location_permission_prompt_displayed(setup_platform):
    SwitchScreenIos(setup_platform).verify_location_permission_prompt()

@when("I enter unsupported address details")
@allure.step("And I enter unsupported address details")
def step_enter_unsupported_address_details(setup_platform):
    SwitchScreenIos(setup_platform).enter_unsupported_address()

@then('I verify that the message Service not available in your area is displayed')
@allure.step('Then I verify that the message "Service not available in your area" is displayed')
def step_verify_service_unavailable_message(setup_platform):
    SwitchScreenIos(setup_platform).verify_service_unavailable_message()

@then("I verify that only restaurants with Dine-In availability are displayed")
@allure.step("Then I verify that only restaurants with Dine-In availability are displayed")
def step_verify_dine_in_restaurants_displayed(setup_platform):
    SwitchScreenIos(setup_platform).verify_dine_in_restaurant_listings()

@then("I verify that each option provides visual feedback highlight, underline, or bold")
@allure.step("Then I verify that each option provides visual feedback highlight, underline, or bold")
def step_verify_visual_feedback_on_model_options(setup_platform):
    SwitchScreenIos(setup_platform).verify_visual_feedback_on_model_options()

@then("I open the Profile section and note the profile details")
@allure.step("When I open the Profile section and note the profile details")
def step_open_profile_and_note_details(setup_platform):
    SwitchScreenIos(setup_platform).note_profile_details()

@then("I click on the homepage")
@allure.step("When I click on the homepage")
def step_click_on_homepage(setup_platform):
    SwitchScreenIos(setup_platform).click_homepage()

@then("I verify that the profile details remain unchanged")
@allure.step("Then I verify that the profile details remain unchanged")
def step_verify_profile_details_unchanged(setup_platform):
    SwitchScreenIos(setup_platform).verify_profile_details_unchanged()

@then("I select the MCDelivery")
@allure.step("And I select the MCDelivery")
def step_select_mc_delivery(setup_platform):
    SwitchScreenIos(setup_platform).select_mc_delivery()

@when("I select an existing address from the saved list")
@allure.step("And I select an existing address from the saved list")
def step_select_existing_address(setup_platform):
    AddressStoreScreenIos(setup_platform).select_existing_address_from_saved_list()

@then("I verify that the selected address is applied")
@allure.step("Then I verify that the selected address is applied")
def step_verify_selected_address_applied(setup_platform):
    AddressStoreScreenIos(setup_platform).verify_selected_address_applied()

@when("I click the edit icon for the selected address")
@allure.step("And I click the edit icon for the selected address")
def step_click_edit_icon_for_address(setup_platform):
    AddressStoreScreenIos(setup_platform).click_edit_icon()

@when("I modify the address details")
@allure.step("And I modify the address details")
def step_modify_address_details(setup_platform):
    AddressStoreScreenIos(setup_platform).modify_address_details()

@then("I verify that the updated address appears in the list")
@allure.step("Then I verify that the updated address appears in the list")
def step_verify_updated_address_in_list(setup_platform):
    AddressStoreScreenIos(setup_platform).verify_updated_address_in_list()

@when("I click the delete icon for the selected address")
@allure.step("And I click the delete icon for the selected address")
def step_click_delete_icon_for_selected_address(setup_platform):
    AddressStoreScreenIos(setup_platform).click_delete_icon()

@then("I select an near by restaurant first times")
@allure.step("And I select a nearby restaurant multiple times")
def step_select_nearby_restaurant_multiple_times(setup_platform):
    AddressStoreScreenIos(setup_platform).select_nearby_restaurant_first_times()

@then("I select an near by restaurant second times")
@allure.step("And I select a nearby restaurant multiple times")
def step_select_nearby_restaurant_multiple_times(setup_platform):
    AddressStoreScreenIos(setup_platform).select_nearby_restaurant_second_times()

@when("I leave the address fields blank")
@allure.step("And I leave the address fields blank")
def step_leave_address_fields_blank(setup_platform):
    AddressStoreScreenIos(setup_platform).leave_address_fields_blank()

@then("I verify that the error message Address fields required is displayed")
@allure.step("Then I verify that the error message Address fields required is displayed")
def step_verify_address_fields_required_error(setup_platform):
    AddressStoreScreenIos(setup_platform).verify_address_fields_required_error()

@then("I verify that the Near label is displayed under each address")
@allure.step("Then I verify that the Near label is displayed under each address")
def step_verify_near_label_under_each_address(setup_platform):
    AddressStoreScreenIos(setup_platform).verify_near_label_under_addresses()

@when("I scroll through the address list")
def step_scroll_through_address_list(setup_platform):
    AddressStoreScreenIos(setup_platform).scroll_to_store_by_name("Orion Mall")

@then("I verify that all addresses are accessible via scrolling")
def step_verify_all_addresses_accessible(setup_platform):
    AddressStoreScreenIos(setup_platform).verify_all_addresses_scrollable()
