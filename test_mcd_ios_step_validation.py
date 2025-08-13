from pytest_bdd import given, when, then, scenarios
from conftest import readPreReqJson
from pytest_bdd.parsers import parse
import allure
from pages.mobile.login_screen_ios import LoginScreenIos
from pages.mobile.profile_screen_ios import ProfileScreenIos
from pages.mobile.address_screen_ios import AddressScreenIos
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



@when('I visually inspect the mobile number field')
@allure.step("When I visually inspect the mobile number field")
def inspect_mobile_field(setup_platform):
    print("Visually inspect the mobile number field")
    Login_Page = LoginScreenIos(setup_platform).inspect_mobile_field()
    assert Login_Page, "Mobile number field not visible"


@when('I visually inspect the referral link section')
@allure.step("When I visually inspect the referral link section")
def inspect_referral_link(setup_platform):
    print("Visually inspect the mobile number field")
    Login_Page = LoginScreenIos(setup_platform).inspect_referral_link()
    assert Login_Page, "Referral link not visible"


@when('I visually inspect the verify button')
@allure.step("When I visually inspect the verify button")
def inspect_verify_button(setup_platform):
    print("Visually inspect the mobile number field")
    Login_Page = LoginScreenIos(setup_platform).inspect_verify_button()
    assert Login_Page, "Verify button not visible"


@when('I visually inspect the footer links')
@allure.step("When I visually inspect the footer links")
def inspect_footer_link(setup_platform):
    print("Visually inspect the mobile number field")
    Login_Page = LoginScreenIos(setup_platform).inspect_footer_link()
    assert Login_Page, "Footer links not visible"

@then("I verify all elements should be visible, correctly aligned, and not overlapping")
@allure.step("Then I verify all elements should be visible, correctly aligned, and not overlapping")
def step_validate_alignment(setup_platform):
    print("Validating visibility, alignment, and non-overlapping of UI elements")

    login_page = LoginScreenIos(setup_platform)

    # Fetching elements using your page object
    mobile_field = login_page.inspect_mobile_field()
    referral_link = login_page.inspect_referral_link()
    verify_button = login_page.inspect_verify_button()
    footer_links = login_page.inspect_footer_link()

    elements = [mobile_field, referral_link, verify_button, footer_links]

    # Check that all elements are visible
    for el in elements:
        assert el.is_displayed(), f"Element not visible: {el}"

    # Check that elements are not overlapping
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            overlapping = is_overlapping_js(setup_platform, elements[i], elements[j])
            if overlapping:
            # Capture screenshot before assertion fails
                screenshot_name = f"overlap_{i}_{j}.png"
                setup_platform.save_screenshot(screenshot_name)
                allure.attach.file(screenshot_name, name=f"Overlapping Elements {i}-{j}", attachment_type=allure.attachment_type.PNG)
                assert not overlapping, f"❌ Elements at index {i} and {j} are overlapping"






@then("I verify the Terms and Conditions web view or page is displayed")
@allure.step("Then I verify the Terms and Conditions web view or page is displayed")
def verify_terms_and_conditions_page(setup_platform):
    LoginScreenIos(setup_platform).verify_terms_and_conditions_page_displayed()

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
    ProfileScreenIos(setup_platform).click_business_model_dropdown()    

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


