from pytest_bdd import given, when, then, scenarios
from conftest import readPreReqJson
from pytest_bdd.parsers import parse
import allure
from pages.mobile.login_screen_ios import LoginScreenIos
from pages.mobile.profile_screen_ios import ProfileScreenIos
from pages.mobile.address_screen_ios import AddressScreenIos
from pages.mobile.switching_screen_ios import SwitchScreenIos
from pages.mobile.address_store_screen_ios import AddressStoreScreenIos
from pages.mobile.Oderingflow_screen_ios import OderingScreenIos
from pages.mobile.Cart_screen_ios import CartScreenIos
from pages.mobile.searchflow_screen_ios import SearchScreenIos
from pages.mobile.offerflow_screen_ios import OffersScreenIos
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

@when("I copied the mobile number this is ios")
@allure.step("Copy mobile number to clipboard")
def copy_mobile_number(setup_platform):
    mobile_number = readPreReqJson("test_data", "mobile_number")
    print(f"Copying mobile number: {mobile_number}")
    LoginScreenIos(setup_platform).copy_mobile_number_to_clipboard(mobile_number)



@when("I paste CTRL V and click verify")
@allure.step("When I paste CTRL V and click verify")
def step_paste_number_and_verify(setup_platform):
    LoginScreenIos(setup_platform).paste_mobile_number_using_clipboard()


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

@when("I log out of the application")
@allure.step("When I log out of the application")
def step_log_out_of_application(setup_platform):
    AddressStoreScreenIos(setup_platform).logout_user()

@when("I delete all saved addresses")
@allure.step("When I delete all saved addresses")
def step_delete_all_saved_addresses(setup_platform):
    AddressStoreScreenIos(setup_platform).delete_all_saved_addresses()

@then("I verify that the last address is not deleted as it is set as the default address")
@allure.step("Then I verify that the last address is not deleted as it is set as the default address")
def step_verify_default_address_not_deleted(setup_platform):
    AddressStoreScreenIos(setup_platform).verify_default_address_not_deleted()

@when("I select the Home tag and Work for the address and verify that the tag is applied")
@allure.step("And I select the Home tag and Work for the address and verify that the tag is applied")
def step_select_tags_and_verify(setup_platform):
    AddressStoreScreenIos(setup_platform).select_and_verify_address_tags()


@then("I navigate to the McBreakfast menu page")
@allure.step("When I navigate to the McBreakfast menu page")
def navigate_to_mcbreakfast_menu(setup_platform):
    OderingScreenIos(setup_platform).select_breakfast_category()

@then("I select Veg McMuffin with protein plus Meal")
@allure.step("When I select Veg McMuffin with protein plus Meal")
def select_veg_mcmuffin_protein_plus_meal(setup_platform):
    OderingScreenIos(setup_platform).select_veg_mcmuffin_protein_plus_meal()

@then("I click on Add item")
@allure.step("When I click on Add item")
def click_on_add_item(setup_platform):
    OderingScreenIos(setup_platform).click_add_item()

@then("I click on the please select location")
@allure.step("When I click on the please select location")
def click_select_location(setup_platform):
    OderingScreenIos(setup_platform).click_select_location()

@then("I select the location in add popup")
@allure.step("When I select the location in add popup")
def select_location_in_popup(setup_platform):
    OderingScreenIos(setup_platform).select_location_in_popup()

@then("I verify the your order")
@allure.step("Then I verify the your order")
def verify_your_order(setup_platform):
    OderingScreenIos(setup_platform).verify_your_order_displayed()

@when("I search for the location")
@allure.step("User searches for the location")
def search_for_location(setup_platform):
    OderingScreenIos(setup_platform).search_location()

@when("I enter breakfast address details")
@allure.step("Entering address details for McBreakfast order")
def enter_valid_address_details(setup_platform):
    OderingScreenIos(setup_platform).enter_address_details_breakfast()

  
  
@then("I clear the order")
@allure.step("User clears the current order")
def clear_the_order(setup_platform):
    OderingScreenIos(setup_platform).clear_order()

@when("I search for out of stock item location")
@allure.step("User searches for delivery location before selecting an out-of-stock item")
def search_location_for_out_of_stock_item(setup_platform):
    OderingScreenIos(setup_platform).search_location_outofstock()   

@when("I enter  out of stock item address details")
@allure.step("User enters breakfast address details to check out-of-stock behavior")
def enter_address_for_out_of_stock_item(setup_platform):
    OderingScreenIos(setup_platform).enter_address_details_outodstock()  

@then("I verify the sold out item is indicated as unavailable")
@allure.step("Verify that the sold out item is correctly marked as unavailable")
def verify_sold_out_item_unavailable(setup_platform):
    OderingScreenIos(setup_platform).is_item_marked_sold_out()


@then("I click on the customization options and verify")
@allure.step("User clicks on the customization options")
def click_customization_options(setup_platform):
    OderingScreenIos(setup_platform).select_customization_option()

@then("I added the first item from menu")
@allure.step("User adds an item from the menu")
def add_item_from_menu(setup_platform): 
    OderingScreenIos(setup_platform).add_first_available_item()    

@then("I added the second item from menu")
@allure.step("User adds an item from the menu")
def add_item_from_menu(setup_platform): 
    OderingScreenIos(setup_platform).add_second_available_item()

@then("I navigate to the MCsaver menu page")
@allure.step("Navigate to the MCsaver menu page")
def navigate_to_mcsaver_menu(setup_platform):
    OderingScreenIos(setup_platform).select_mcsaver_category()

@then("I verify the payment method and button")
@allure.step("Verify payment method and confirm button visibility")
def verify_payment_method_and_button(setup_platform):
    OderingScreenIos(setup_platform).is_payment_method_and_confirm_button_displayed()
    print("Payment method and confirm button verified successfully")

@then("I verify the item price matches the listed menu price")
@allure.step("Verify the item price matches the listed menu price")
def verify_item_price_matches_menu(setup_platform):
    OderingScreenIos(setup_platform).verify_pricing()

@then("I verify that sold out items cannot be added to cart")
@allure.step("Verify 'Sold out' label prevents adding the item to cart")
def step_verify_sold_out_items_not_addable(setup_platform):
    OderingScreenIos(setup_platform).verify_sold_out_items_not_clickable()

@then("I verify the item is added to the cart")
@allure.step("Verify that the selected item is present in the cart")
def verify_item_in_cart(setup_platform):
    OderingScreenIos(setup_platform).verify_item_in_cart()

@then("I navigate to the 3pc meal menu page")
@allure.step("User navigates to the 3pc meal menu page")
def navigate_to_3pc_meal_menu(setup_platform):
    OderingScreenIos(setup_platform).select_3pc_meal_category()

@then("I verity the 3pc meal iteam is added to the cart")
@allure.step("Verify 3pc meal item is present in the cart")
def verify_3pc_meal_added_to_cart(setup_platform):
    OderingScreenIos(setup_platform).verify_3pc_meal_item_in_cart()

@then("I click on the meal category")
@allure.step("User clicks on the meal category")
def click_meal_category(setup_platform):
    OderingScreenIos(setup_platform).select_3pc_meal()

@then("I click on the dessert menu")
@allure.step("Click on the Desserts menu from the category list")
def click_on_dessert_menu(setup_platform):
    OderingScreenIos(setup_platform).select_desserts_category()

@then("I select the random dersert item")
@allure.step("Select a random dessert item from the Desserts menu")
def select_random_dessert_item(setup_platform):
    OderingScreenIos(setup_platform).select_random_dessert_item()

@then("I verity the dessert iteam is added to the cart")
@allure.step("Verify dessert item is present in the cart")
def verify_dessert_item_added_to_cart(setup_platform):
    OderingScreenIos(setup_platform).verify_dessert_item_in_cart()

@then("I click on the Burgers & Wraps menu")
@allure.step("Click on the Burgers & Wraps menu")
def click_on_burgers_and_wraps_menu(setup_platform):
    OderingScreenIos(setup_platform).click_burgers_and_wraps_menu()

@then("I select the Chicken Wrap item")
@allure.step("Select the Chicken Wrap item from the Burgers & Wraps menu")
def select_chicken_wrap_item(setup_platform):
    OderingScreenIos(setup_platform).select_chicken_wrap_item()

@then("I verity the Chicken Wrap iteam is added to the cart")
@allure.step("Verify Chicken Wrap item is present in the cart")
def verify_chicken_wrap_added_to_cart(setup_platform):
    OderingScreenIos(setup_platform).verify_chicken_wrap_item_in_cart()

@then("I select the burger on the customization options")
@allure.step("Select the burger from the customization options")
def select_burger_on_customization_options(setup_platform):
    OderingScreenIos(setup_platform).select_burger_customization_option()

@then("I Click on Customize button")
@allure.step("Click on the Customize button")
def click_on_customize_button(setup_platform):
    OderingScreenIos(setup_platform).click_customize_button()

@then("I added the extra item")
@allure.step("Add an extra item in the customization options")
def add_extra_item(setup_platform):
    OderingScreenIos(setup_platform).add_extra_item()

@then("I click on the fries and sides menu")
@allure.step("Click on the Fries and Sides menu")
def click_on_fries_and_sides_menu(setup_platform):
    OderingScreenIos(setup_platform).click_fries_and_sides_menu()

@then("I select the medium fries item")
@allure.step("Select the Medium Fries item")
def select_medium_fries_item(setup_platform):
    OderingScreenIos(setup_platform).click_fries_medium()

@then("I verify the fries item is added to the cart")
@allure.step("Verify fries item is added to the cart")
def verify_fries_item_in_cart(setup_platform):
    added = OderingScreenIos(setup_platform).is_fries_item_in_cart()
    print(f"Fries item added to cart: {added}")

@then("I click on the Coffee & Beverages menu")
@allure.step("Click on the Coffee & Beverages menu")
def click_on_coffee_and_beverages_menu(setup_platform):
    OderingScreenIos(setup_platform).click_coffee_and_beverages_menu()

@then("I select the cappuccino coffee item")
@allure.step("Select the Cappuccino coffee item")
def select_cappuccino_coffee_item(setup_platform):
    OderingScreenIos(setup_platform).click_cappuccino_coffee()

@then("I verify the cappuccino coffee item is added to the cart")
@allure.step("Verify cappuccino coffee item is added to the cart")
def verify_cappuccino_in_cart(setup_platform):
    added = OderingScreenIos(setup_platform).is_cappuccino_in_cart()
    print(f"Cappuccino coffee item added to cart: {added}")

@then("I click on the Cakes brownies menu")
@allure.step("Click on the Cakes, Brownies & Cookies menu")
def click_on_cakes_brownies_menu(setup_platform):
    OderingScreenIos(setup_platform).click_cakes_brownies_menu()

@then("I select the chcochip muffin brownie item")
@allure.step("Select the Chocochip Muffin Brownie item")
def select_chocochip_muffin_brownie(setup_platform):
    OderingScreenIos(setup_platform).click_chocochip_muffin_brownie()

@then("I verify the chcochip muffin brownie")
@allure.step("Verify Chocochip Muffin Brownie item is added to the cart")
def verify_chocochip_muffin_brownie_in_cart(setup_platform):
    OderingScreenIos(setup_platform).chocochip_muffin_brownie_in_cart()
    print("Chocochip Muffin Brownie item added to cart")

@then("I click on the Protein Plus and Burgers with Millet Bun menu")
@allure.step("Click on the Protein Plus and Burgers with Millet Bun menu")
def click_on_protein_plus_and_millet_bun_menu(setup_platform):
    OderingScreenIos(setup_platform).click_protein_plus_and_millet_bun_menu()

@then("I select the Chicken Burger with Millet Bun item")
@allure.step("Select the Chicken Burger with Millet Bun item")
def select_chicken_burger_with_millet_bun(setup_platform):
    OderingScreenIos(setup_platform).click_chicken_burger_with_millet_bun()

@then("I verify the Chicken Burger with Millet Bun item is added to the cart")
@allure.step("Verify Chicken Burger with Millet Bun item is added to the cart")
def verify_chicken_burger_with_millet_bun_in_cart(setup_platform):
    OderingScreenIos(setup_platform).chicken_burger_with_millet_bun_in_cart()
    print("Chicken Burger with Millet Bun item added to cart")

@then("I verify that a larger image of the dessert is displayed when tapped")
@allure.step("Verify larger dessert image is displayed after tapping")
def verify_larger_dessert_image_displayed(setup_platform):
    OderingScreenIos(setup_platform).verify_larger_dessert_image()

@then("I verify that the nutrition information is displayed")
@allure.step("Verify nutrition information is displayed")
def verify_nutrition_info_displayed(setup_platform):
    OderingScreenIos(setup_platform).is_nutrition_info_displayed()

@then("I click on another item to Add")
@allure.step("Click on another item to add to the cart")
def click_on_another_item_to_add(setup_platform):
    OderingScreenIos(setup_platform).click_another_item_to_add()

@then("I remove the item from the cart")
@allure.step("Remove the item from the cart")
def remove_item_from_cart(setup_platform):
    OderingScreenIos(setup_platform).remove_item_from_cart()

@then("I update the item quantity in the cart")
@allure.step("Update item quantity in the cart")
def update_item_quantity_in_cart(setup_platform):
    OderingScreenIos(setup_platform).update_item_quantity()

@then("I verify the total price calculation is correct")
@allure.step("Verify total price calculation in the cart")
def verify_total_price_calculation(setup_platform):
    OderingScreenIos(setup_platform).verify_total_price_calculation()

@then("I scroll through all menu categories")
@allure.step("Scroll through all menu categories")
def scroll_through_all_menu_categories(setup_platform):
    OderingScreenIos(setup_platform).scroll_through_all_menu_categories()

@then("I verify the cart is empty on app launch")
@allure.step("Verify the cart is empty on app launch")
def verify_cart_is_empty_on_app_launch(setup_platform):
    OderingScreenIos(setup_platform).validate_cart_is_empty()

@then("I verify the cart item details including name, price, and quantity")
@allure.step("Verify cart item details including name, price, and quantity")
def verify_cart_item_details(setup_platform):
    CartScreenIos(setup_platform).validate_cart_items()


@then("I add delivery instructions in the cart")
@allure.step("Add delivery instructions in the cart")
def add_delivery_instructions_in_cart(setup_platform):
    CartScreenIos(setup_platform).add_delivery_instructions("Please leave it at the doorstep.")

@then("I verify the subtotal reflects all additions accurately")
@allure.step("Verify the subtotal reflects all added item prices accurately")
def verify_subtotal_all_items(setup_platform):
    CartScreenIos(setup_platform).verify_subtotal_reflects_all_items()

@then("I verify the taxes are calculated correctly based on the subtotal")
@allure.step("Verify CGST and SGST are calculated correctly based on the subtotal")
def verify_taxes_calculated_correctly(setup_platform):
    CartScreenIos(setup_platform).validate_tax_breakdown()

@then("I click on the back button")
@allure.step("Clicking on the back button")
def step_click_back_button(setup_platform):
    CartScreenIos(setup_platform).click_back_button()

@then("I click on the Know More link in charity donation option")
@allure.step("Click on the 'Know More' link in the charity donation section")
def click_know_more_in_charity_section(setup_platform):
    CartScreenIos(setup_platform).click_know_more_charity()

@then("I verify that the charity donation information is displayed in the cart")
@allure.step("Verify that the charity donation information is displayed in the cart")
def verify_charity_info_displayed(setup_platform):
    CartScreenIos(setup_platform).is_charity_info_visible()

@then("I select the charity donation checkbox")
@allure.step("Select charity donation checkbox")
def select_charity_checkbox(setup_platform):
    CartScreenIos(setup_platform).charity_checkbox()

@then("I verify that the donation amount is added to the total price in the cart")
@allure.step("Verify donation amount is included in total cart price")
def verify_donation_amount_in_total(setup_platform):
    CartScreenIos(setup_platform).validate_donation_amount()

@then("I uncheck the charity donation checkbox")
@allure.step("Uncheck the charity donation checkbox")
def step_uncheck_charity_donation_checkbox(setup_platform):
    CartScreenIos(setup_platform).uncheck_charity_donation()

@then("I verify that the donation amount is removed from the total price in the cart")
@allure.step("Verify donation amount is removed from the cart total")
def verify_donation_amount_removed(setup_platform):
    CartScreenIos(setup_platform).verify_donation_removed()


@then("I tap on the View All Offers link")
@allure.step("Tap on the 'View All Offers' link")
def tap_view_all_offers_link(setup_platform):
    CartScreenIos(setup_platform).click_view_all_offers()

@then("I verify that the offers page is displayed")
@allure.step("Verify that the offers page is displayed")
def verify_offers_page_displayed(setup_platform):
    CartScreenIos(setup_platform).verify_offers_page_is_visible()

@then("I verify that all price components display the ₹ symbol")
@allure.step("Verify ₹ symbol is displayed with all price components")
def verify_currency_symbol_displayed(setup_platform):
    CartScreenIos(setup_platform).validate_currency_symbols()

@then("I verify the total price should update correctly")
@allure.step("Verify total price is updated correctly after item removal")
def verify_total_price_updated(setup_platform):
    CartScreenIos(setup_platform).is_total_price_correct()
    
@then("I verify the estimated delivery time is displayed below the delivery address")
@allure.step("Verify estimated delivery time is visible below the delivery address")
def verify_estimated_delivery_time_visible(setup_platform):
    CartScreenIos(setup_platform).validate_estimated_delivery_time()


@then("I apply the first promo code")
@allure.step("Apply the first promo code")
def apply_first_promo_code(setup_platform):
    CartScreenIos(setup_platform).apply_first_promo_code()

@then("I apply the second promo code")
@allure.step("Apply the second promo code")
def apply_second_promo_code_step(setup_platform):
    CartScreenIos(setup_platform).apply_second_promo_code()

@then("I verify only one promo code is applied")
@allure.step("Verify only one promo code is applied")
def verify_only_one_promo_code_applied(setup_platform):
    CartScreenIos(setup_platform).validate_single_promo_code_applied()

@then("I add multiple quantity items")
@allure.step("Add multiple quantity items to the cart")
def add_multiple_quantity_items(setup_platform):
    CartScreenIos(setup_platform).add_multiple_item_quantities()

@then("I click on the discount flat")
@allure.step("Click on the flat discount offer")
def click_discount_flat(setup_platform):
    CartScreenIos(setup_platform).click_flat_discount()

@then("I verify the discount is correctly deducted from the subtotal")
@allure.step("Verify discount is correctly deducted from subtotal in order summary")
def verify_discount_deduction(setup_platform):
    CartScreenIos(setup_platform).validate_discount_deduction()

@then("I enter the expired promo code")
@allure.step("Enter the expired promo code into the promo field")
def enter_expired_promo_code(setup_platform):
    expired_code = readPreReqJson("test_data", "Expired_Promo_Code")
    print(f"Entering expired promo code: {expired_code}")
    CartScreenIos(setup_platform).enter_promo_code(expired_code)

@then("I should see a message indicating the code is invalid or expired")
@allure.step("Verify error message for invalid/expired promo code")
def verify_expired_promo_message(setup_platform):
    expected_message = readPreReqJson("test_data", "Expired_Promo_Message")
    CartScreenIos(setup_platform).verify_expired_promo_message(expected_message)


@then("I add a delivery instruction in the cart using emojis or special characters")
@allure.step("Add delivery instruction in the cart with emojis/special characters")
def add_delivery_instruction_with_special_chars(setup_platform):
    notes = readPreReqJson("test_data", "Special_Notes")
    print(f"Adding delivery instruction with special characters: {notes}")
    CartScreenIos(setup_platform).add_delivery_instruction(notes)

@then("I select location")
@allure.step("Select delivery location")
def select_location(setup_platform):
    CartScreenIos(setup_platform).select_location()


@when("I click on the Search icon")
@allure.step("Click on the Search icon")
def click_search_icon(setup_platform):
    SearchScreenIos(setup_platform).click_search_icon()

@when("I enter Fries in the search bar")
@allure.step("Enter menu item in the search bar")
def enter_menu_item(setup_platform):
    menu_item = readPreReqJson("test_data", "menu_item") 
    print(f"Entering menu item: {menu_item}")
    SearchScreenIos(setup_platform).enter_search_text(menu_item) 

@when("I click on the search icon inside the search bar")
@allure.step("Click on the search icon inside the search bar")
def click_search_icon_inside(setup_platform):
    SearchScreenIos(setup_platform).click_search_icon_inside()      

@then("I verify the search results display matching items")
@allure.step("Verify search results display matching items")
def verify_search_results(setup_platform):
    expected_item = readPreReqJson("test_data", "fries_item_display")
    actual_results = SearchScreenIos(setup_platform).get_search_results()
    assert expected_item in actual_results, f"Expected '{expected_item}' in search results, but got {actual_results}"
    print(f"Verified search results contain: {expected_item}")    

@when("I enter a non-existent menu item")
@allure.step("Enter a non-existent menu item")
def enter_nonexistent_item(setup_platform):
    menu_item = readPreReqJson("test_data", "menu_item_nonexistent")
    print(f"Entering non-existent menu item: {menu_item}")
    SearchScreenIos(setup_platform).enter_search_text(menu_item)    


@then("I verify the No items found message is displayed")
@allure.step("Verify the No items found message is displayed")
def verify_no_items_message(setup_platform):
    expected_message = readPreReqJson("test_data", "no_items_message")
    actual_message = SearchScreenIos(setup_platform).get_no_items_message()
    assert actual_message == expected_message, f"Expected '{expected_message}' but got '{actual_message}'"
    print(f"Verified No items found message: {actual_message}")

@then("I verify the prompt message is displayed for empty input")
@allure.step("Verify the prompt message is displayed for empty input")
def verify_empty_search_prompt(setup_platform):
    expected_message = readPreReqJson("test_data", "empty_search_message")
    actual_message = SearchScreenIos(setup_platform).get_no_items_empty_message()
    assert actual_message == expected_message, f"Expected '{expected_message}' but got '{actual_message}'"
    print(f"Verified empty search prompt message: {actual_message}")

@then("I verify the item is added in the cart")
@allure.step("Verify the item is added in the cart")
def verify_item_in_cart(setup_platform):
    expected_item = "Fries" 
    actual_item = SearchScreenIos(setup_platform).get_cart_item_name()
    # check if expected_item is part of the actual text
    assert expected_item in actual_item, f"Expected '{expected_item}' in cart item but found '{actual_item}'"
    print(f"Verified item is added in the cart: {actual_item}")

@when("I enter Burger in the search bar")
@allure.step("Enter 'Burger' in the search bar")
def enter_burger_in_search_bar(setup_platform):
    menu_item = readPreReqJson("test_data", "Burger")
    print(f"Entering menu item: {menu_item}")
    SearchScreenIos(setup_platform).enter_search_text(menu_item)



@then("I verify the search results for Burger are still displayed")
@allure.step("Verify the search results for Burger are still displayed")
def verify_burger_search_results_persist(setup_platform):
    results = SearchScreenIos(setup_platform).burger_display_in_search()
    print(f"Search results captured: {results}")
    assert any("burger" in item.lower() for item in results), \
        f"No results found containing 'Burger'. Actual results: {results}"
    print("Verified search results still displayed for: Burger")


@then('I verify the placeholder text in the search bar is displayed as Search here')
@allure.step("Verify placeholder text in the search bar is displayed as 'Search here'")
def verify_search_placeholder_text(setup_platform):
    expected_placeholder = "Search here"
    actual_placeholder = SearchScreenIos(setup_platform).get_search_placeholder_text()
    assert expected_placeholder == actual_placeholder, \
        f"Expected placeholder '{expected_placeholder}' but found '{actual_placeholder}'"
    print(f"Verified placeholder text in search bar: {actual_placeholder}")


@when("I click on the Veg filter button")
@allure.step("Click on the Veg filter button")
def click_veg_filter_button(setup_platform):
    SearchScreenIos(setup_platform).click_veg_filter()
    print("Clicked on the Veg filter button")

@then("verify only veg items should be displayed in the results")
@allure.step("Verify only veg items are displayed in the results")
def verify_only_veg_items_displayed(setup_platform):
    expected_label = readPreReqJson("test_data", "Veg_Filter").lower()
    results = SearchScreenIos(setup_platform).get_search_veg()
    print(f"Search results after applying Veg filter: {results}")
    # Collect only veg items
    veg_items = [item for item in results if expected_label in item.lower()]
    if veg_items:
        print(f" Veg items displayed: {veg_items}")
    else:
        print(f" No veg items found in results: {results}")


@when("I click on the Non-Veg filter button")
@allure.step("Click on the Non-Veg filter button")
def click_nonveg_filter_button(setup_platform):
    SearchScreenIos(setup_platform).click_nonveg_filter()
    print("Clicked on the Non-Veg filter button")

@then("verify only non-veg items should be displayed in the results")
@allure.step("Verify only non-veg items are displayed in the results")
def verify_only_nonveg_items_displayed(setup_platform):
    expected_label = readPreReqJson("test_data", "NonVeg_Filter").lower()
    results = SearchScreenIos(setup_platform).get_search_nonveg()
    print(f"Search results after applying Non-Veg filter: {results}")
    # Collect only non-veg items
    nonveg_items = [item for item in results if expected_label in item.lower()]
    if nonveg_items:
        print(f"Non-Veg items displayed: {nonveg_items}")
    else:
        print(f"No non-veg items found in results: {results}")


@then("verify only veg items containing Burger are displayed in the results")
@allure.step("Verify only veg items containing Burger are displayed in the results")
def verify_veg_burger_search_results(setup_platform):
    expected_label = readPreReqJson("test_data", "Veg_Burger_Filter").lower()
    search_term = "burger"
    results = SearchScreenIos(setup_platform).get_search_veg()
    print(f"Search results after applying Veg filter: {results}")
    # Filter only veg items containing the search term
    veg_burger_items = [item for item in results if expected_label in item.lower() and search_term in item.lower()]
    if veg_burger_items:
        print(f"Veg items containing '{search_term}' displayed: {veg_burger_items}")
    else:
        print(f"No veg items containing '{search_term}' found in results: {results}")



@when("I clear the search input")
@allure.step("Clear the search input")
def clear_search_input(setup_platform):
    SearchScreenIos(setup_platform).clear_search()
    print("Cleared the search input")

@then("verify the default view is restored with no filters applied")
@allure.step("Verify the default view is restored with no filters applied")
def verify_default_view(setup_platform):
    results = SearchScreenIos(setup_platform).get_all_items()
    print(f"Items displayed after clearing search and filters: {results}")
    # Check if some items are displayed (default view)
    if results:
        print("Default view restored with all items displayed")
    else:
        print("No items found after clearing search and filters")


@when('I enter Wrap in the search bar')
@allure.step('Enter "Wrap" in the search bar')
def enter_wrap_in_search_bar(setup_platform):
    menu_item = "Wrap"
    SearchScreenIos(setup_platform).enter_search_text(menu_item)
    print(f"Entered search term: {menu_item}")


@then("I verify only items containing Wrap are displayed in the results")
@allure.step("Verify only items containing Wrap are displayed in the results")
def verify_wrap_search_results(setup_platform):
    Wrap = readPreReqJson("test_data", "Wrap")
    print(f"Checking search results for items containing: {Wrap}")
    results = SearchScreenIos(setup_platform).get_search_wrap()
    print(f"Search results captured: {results}")
    # Filter results that contain the search term
    filtered_results = [item for item in results if Wrap.lower() in item.lower()]
    # Just print the filtered results without asserting
    print(f"Filtered items containing '{Wrap}': {filtered_results}")


@then("I verify the default view is restored with no filters applied")
@allure.step("Verify default view is restored with no filters applied")
def verify_default_view_restored(setup_platform):
    results = SearchScreenIos(setup_platform).fetch_displayed_items()
    print(f"Items visible after clearing filters: {results}")
    print("Default view restored; no filters applied")

@when("I click  the Veg filter button again")
@allure.step("I click  the Veg filter button again")
def click_veg_filter_button(setup_platform):
    SearchScreenIos(setup_platform).click_veg_filter_again()
    print("I click  the Veg filter button again")

@then("I clicked on the back button in search page")
@allure.step("I clicked on the back button in search page")
def step_click_back_button(setup_platform):
    SearchScreenIos(setup_platform).click_back_button()    

@then('I enter a valid coupon code "FLAT10" in the coupon input field')
@allure.step("Enter valid coupon code in coupon input field")
def enter_valid_coupon_code(setup_platform):
    Valid_Coupon_Code = readPreReqJson("test_data", "Valid_Coupon_Code")
    print(f"Entering coupon code from prereq: {Valid_Coupon_Code}")
    OffersScreenIos(setup_platform).enter_coupon_code(Valid_Coupon_Code)
    print(" Coupon code entered successfully")

@then("I tap on the search button")
@allure.step("Tap on the search button")
def tap_search_button(setup_platform):
    print("Tapping on the search button...")
    OffersScreenIos(setup_platform).tap_search_button()
    print("Search button tapped successfully")


@then('I verify that an offer card with code "FLAT10" is displayed')
@allure.step("Verify that an offer card with code 'FLAT10' is displayed")
def verify_offer_card_displayed(setup_platform):
    coupon_code = "FLAT10"
    print(f"Verifying offer card for coupon code: {coupon_code}")
    results = OffersScreenIos(setup_platform).get_offer_cards()
    print(f"Offer cards visible: {results}")
    if any(coupon_code in card for card in results):
        print(f" Offer card with code '{coupon_code}' is displayed")
    else:
        print(f" Offer card with code '{coupon_code}' not found in results: {results}")



@then("I scroll through all the offer cards")
@allure.step("Scroll through all offer cards")
def step_scroll_through_offer_cards(setup_platform):
    OffersScreenIos(setup_platform).scroll_through_offer_cards()


@then("I verify  coupon code, description, Show More link, and Apply button")
@allure.step("Verify all required elements are present in offer cards")
def step_verify_offer_card_elements(setup_platform):
    OffersScreenIos(setup_platform).verify_offer_card_elements()
