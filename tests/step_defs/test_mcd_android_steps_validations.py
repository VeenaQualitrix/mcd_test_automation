from pytest_bdd.parsers import parse
from pytest_bdd import given, when, then, scenarios
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from pages.base_page import BasePage
from pages.android_home_screen import AndroidHomeScreen
from pages.android_login_screen import AndroidLoginScreen
from pages.android_profile_screen import AndroidProfileScreen
from pages.android_view_screen import AndroidViewScreen
from pages.android_search_menu_screen import AndroidSearchMenuScreen
from pages.android_address_screen import AndroidAddressScreen
from pages.android_view_cart_screen import AndroidViewCartScreen
from pages.android_menu_screen import AndroidMenuScreen
from pages.android_offer_screen import AndroidOfferPage
from conftest import readPreReqJson
import allure
import time

scenarios('../features/Mcd_Android_Test_Cases.feature')


@given("I launch the native app") 
@allure.step('I launch the native appL') 
def launch_native_app(setup_platform): 
    BasePage(setup_platform).launch_application()
'''
def wait_for_activity(driver, expected_activity, timeout=10):
    for _ in range(timeout):
        if expected_activity in driver.current_activity:
            return True
        time.sleep(1)
    return False

@then("I verify the app should be launched")
@allure.step('I verify the app should be launched')
def verify_app_launch(setup_platform):
    if not wait_for_activity(setup_platform, "MainActivity", timeout=15):
        raise AssertionError(f"App did not launch properly. Current activity: {setup_platform.current_activity}")
    print(f" App launched. Current activity: {setup_platform.current_activity}")
    '''

@then("I verify the app should be launched")
@allure.step("I verify the app should be launched")
def verify_app_launch(setup_platform):
    valid_activities = ["LauncherActivity", "MainActivity", "SplashActivity"]
    max_wait_time = 20  # seconds
    poll_interval = 1   # seconds

    for second in range(max_wait_time):
        current_activity = setup_platform.current_activity
        print(f"[{second+1}s] Current activity: {current_activity}")
        if any(activity in current_activity for activity in valid_activities):
            print(f" App launched. Current activity: {current_activity}")
            break
        time.sleep(poll_interval)
    else:
        raise AssertionError(f"App did not launch properly. Current activity: {current_activity}")  

@then("I quit the driver")
@allure.step('I quit the driver')
def close_app(setup_platform):
    BasePage(setup_platform).quit_driver()
    print("driver ended")  

@then('I verify home screen navigation')
@allure.step("Then I verify home screen navigation")
def verify_home_screen_navigation(setup_platform):
    print("verify home screen navigation")
    Home_Screen = AndroidHomeScreen(setup_platform).verify_home_screen_navigation()
    assert Home_Screen, "Home screen Is Not Reached After Logged In"

@then('I click on Log out button')
@allure.step("Then I click on Log out button")
def click_on_log_out_button(setup_platform):
    print("click on Log out button")
    AndroidViewScreen(setup_platform).Click_log_out_button()

@when("I click on MyMcD hamburger icon")
@allure.step("When I click on MyMcD hamburger icon")
def click_on_mymcd_hamburger_icon(setup_platform):
    print("clicked on MyMcD hamburger icon")
    AndroidHomeScreen(setup_platform).click_on_MyMcD_hamburger_icon()


@then("I verify view screen navigation")
@allure.step("Then I verify view screen navigation")
def verify_view_screen_navigation(setup_platform):
    print("verify view screen navigation")
    View_Screen = AndroidViewScreen(setup_platform).verify_view_screen_navigation()
    assert View_Screen, "View screen Is Not Reached After Clicking On hamnburger Icon In Home Page"


@when("I click on login or signup button")
@allure.step("When I click on login or signup button")
def click_on_login_or_sign_up_button(setup_platform):
    print("Clicking on Login/Sign Up Button")
    AndroidViewScreen(setup_platform).click_on_login_or_sign_up_button()


@then("I verify login screen navigation")
@allure.step("Then I verify login screen navigation")
def verify_login_screen_navigation(setup_platform):
    print("verify login screen navigation")
    Login_Screen = AndroidLoginScreen(setup_platform).verify_login_screen_navigation()
    assert Login_Screen, "Login screen Is Not Reached After Clicking On Login Button In View Page"


@when("I enter a valid mobile number and click mobile verify")
@allure.step("When I enter a valid mobile number and click mobile verify")
def enter_a_valid_mobile_number_and_click_verify(setup_platform):
    mobile_number = readPreReqJson("test_data", "mobile_number")
    print("Entering Mobie Number")
    AndroidLoginScreen(setup_platform).enter_mobile_number(mobile_number)


@when("I enter the OTP and click verify")
@allure.step("When I enter the OTP and click verify")
def enter_the_otp_and_click_verify(setup_platform):
    otp = readPreReqJson("test_data", "OTP")
    print("Entering OTP")
    AndroidLoginScreen(setup_platform).enter_otp(otp)

@then("I verify OTP screen navigation")
@allure.step("Then I verify OTP screen navigation")
def verify_otp_page_navigation(setup_platform):
    print("Verify otp screen navigation")
    Otp_page_navigation = AndroidLoginScreen(setup_platform).verify_otp_screen_is_displayed()
    assert Otp_page_navigation, "otp page Is Not navigated successfully As Expected"

@when("I click save changes on profile details page")
@allure.step("When I click save changes on profile details page")
def click_save_button_on_profile_screen(setup_platform):
    print("click save changes on profile details page")
    AndroidProfileScreen(setup_platform).Click_save_button_on_profile_details_screen()

@when("I click on referral link")
@allure.step("When I click on referral link")
def click_on_referral_link(setup_platform):
    print("Clicking on referral link")
    AndroidLoginScreen(setup_platform).click_referral_code_link()


@then('I verify referral textfield is displayed')
@allure.step("Then I verify referral textfield is displayed")
def verify_referral_textfield_is_displayed(setup_platform):
    print("Verifying referral textfield is displayed")
    AndroidLoginScreen(setup_platform).verify_referral_text_field_is_displayed()

@when("I enter referral code")
@allure.step("When I enter referral code")
def enter_referral_code(setup_platform):
    Referral_code = readPreReqJson("test_data", "Referral_code")
    print(f"Entering referral code: {Referral_code}")
    AndroidLoginScreen(setup_platform).enter_referral_code(Referral_code)

@when("I enter referral code and click verify")
@allure.step("When I enter referral code and click verify")
def enter_referral_code_and_verify(setup_platform):
    Referral_code = readPreReqJson("test_data", "Referral_code")
    print(f"Entering referral code: {Referral_code}")
    AndroidLoginScreen(setup_platform).enter_referral_code_click_verify(Referral_code)

@then('I verify error message')
@allure.step("Then I verify error message")
def verify_error_message(setup_platform):
    print("Verifying error message")
    Login_Page = AndroidLoginScreen(setup_platform).mobile_field_empty_error()
    assert Login_Page, "Please enter valid mobile number"

@then('I verify referral code accepted without error')
@allure.step("Then I verify referral code accepted without error")
def verify_referral_code_accepted(setup_platform):
    print("Verifying that the referral code was accepted")
    result = AndroidLoginScreen(setup_platform).verify_referral_code_accepted_without_error()
    assert result, "Referral code was not accepted or an error appeared"

@when("I leave mobile field empty")
@allure.step("When I leave mobile field empty")
def leave_mobile_field_empty(setup_platform):
    print("leave mobile field empty")
    AndroidLoginScreen(setup_platform).leave_mobile_field_empty()

@when("I enter a mobile number with less than 10 digits")
@allure.step("When I enter a mobile number with less than 10 digits")
def enter_a_invalid_mobile_number(setup_platform):
    invalid_mobile_number = readPreReqJson("test_data", "invalid_mobile_number")
    print("Entering invalid Mobile Number")
    AndroidLoginScreen(setup_platform).enter_invalid_mobile_number(invalid_mobile_number)

@then("I confirm 'verify mobile' button is disabled")
@allure.step("Then I confirm 'verify mobile' button is disabled")
def verify_error_message(setup_platform):
    print("Confirming 'verify mobile' button is disabled")
    AndroidLoginScreen(setup_platform).verify_mobile_button_is_disabled()

@when("I enter alphabets in mobile number field")
@allure.step("When I enter alphabets in mobile number field")
def enter_alphabets_in_mobile_number_field(setup_platform):
    alphabets_in_mobile_number = readPreReqJson("test_data", "alphabets_in_mobile_number")
    print("Entering alphabets in Mobie Number field")
    AndroidLoginScreen(setup_platform).enter_alphabets_in_mobile_text_field(alphabets_in_mobile_number)

@when("I enter mobile number with spaces and click verify")
@allure.step("When I enter mobile number with spaces and click verify")
def enter_mobile_number_with_space_and_click_verify(setup_platform):
    mobile_number_with_space = readPreReqJson("test_data", "mobile_number_with_space")
    print("Entering mobile number with spaces")
    AndroidLoginScreen(setup_platform).enter_mobile_number_with_space(mobile_number_with_space)

@when("I enter mobile number with special characters and click verify")
@allure.step("When I enter mobile number with special characters and click verify")
def enter_mobile_number_with_special_char_and_click_verify(setup_platform):
    special_characters_in_mobile_field = readPreReqJson("test_data", "special_characters_in_mobile_field")
    print("Entering mobile number with special characters")
    AndroidLoginScreen(setup_platform).enter_mobile_number_with_special_char(special_characters_in_mobile_field)

@when("I click terms and conditions link")
@allure.step("When I click terms and conditions link")
def click_terms_and_conditions_link(setup_platform):
    print("Verify terms and conditions link is clickable ")
    AndroidLoginScreen(setup_platform).click_terms_and_conditions_link()

@then("I verify user is redirected to terms and conditions page")
@allure.step("Then I verify user is redirected to terms and conditions page")
def verify_terms_and_conditions_navigation(setup_platform):
    print("Verify user is redirected to terms and conditions page")
    Terms_and_conditions_navigation = AndroidLoginScreen(setup_platform).verify_terms_and_conditions_header()
    assert Terms_and_conditions_navigation, "terms and conditions Is Not navigated successfully As Expected"

@then("I verify mobile number accepted and redirected to next page")
@allure.step("Then I verify mobile number accepted and redirected to next page")
def verify_next_page_navigation(setup_platform):
    print("verify mobile number accepted and redirected to next page")
    Next_page_navigation = AndroidLoginScreen(setup_platform).verify_otp_screen_is_displayed()
    assert Next_page_navigation, "Next page is Not navigated successfully As Expected"

@when("I enter 11 digits mobile number")
@allure.step("When I enter 11 digits mobile number")
def enter_11_digits_mobile_number(setup_platform):
    Mobile_number_11_digits = readPreReqJson("test_data", "mobile_number_11_digits")
    print(f"Typing mobile number: {Mobile_number_11_digits} one digit at a time")
    AndroidLoginScreen(setup_platform).enter_mobile_number_one_by_one(Mobile_number_11_digits)

@when("I enter more than 10 digits mobile number")
@allure.step("When I enter more than 10 digits mobile number")
def enter_more_than_10_digits_mobile_number(setup_platform):
    Mobile_number_more_than_10_digits = readPreReqJson("test_data", "mobile_number_11_digits")
    print(f"Typing mobile number: {Mobile_number_more_than_10_digits} one digit at a time")
    AndroidLoginScreen(setup_platform).enter_mobile_number_one_by_one(Mobile_number_more_than_10_digits)

@then("I verify field should restrict to 10 digits")
@allure.step("Then I verify field should restrict to 10 digits")
def verify_field_restricts_to_10_digits(setup_platform):
    print("Verifying that the mobile number input field restricts to 10 digits")
    login_page = AndroidLoginScreen(setup_platform)
    entered_number = login_page.get_entered_mobile_number()
    print(f"Fetched number from input field: '{entered_number}'")
    assert len(entered_number) == 10, f"Expected 10 digits, but got '{entered_number}' with length {len(entered_number)}"


@when("I copied a mobile number")
@allure.step("When I copied a mobile number")
def copy_mobile_number(setup_platform):
     Copied_number = readPreReqJson("test_data", "mobile_number")
     print("verify mobile number copied")
     AndroidLoginScreen(setup_platform).copy_mobile_number_to_clipboard(Copied_number)

@when("I paste the number with Ctrl V and click verify")
@allure.step("When I paste the number with Ctrl V and click verify")
def paste_copied_mobile_number(setup_platform):
    print("Pasting mobile number using Ctrl+V")
    AndroidLoginScreen(setup_platform).paste_mobile_number_using_clipboard()

@then("I verify number pasted correctly and accepted")
@allure.step("Then I verify number pasted correctly and accepted")
def verify_number_pasted_correctly(setup_platform):
    print("Verifying that the pasted number was accepted correctly")

    expected_number = readPreReqJson("test_data", "mobile_number")
    actual_number = AndroidLoginScreen(setup_platform).get_pasted_mobile_number()

    print(f"Expected Mobile Number: {expected_number}")
    print(f"Actual Mobile Number in Field: {actual_number}")

    assert actual_number == expected_number, "Pasted mobile number does not match or was not accepted"

@when('I visually inspect the mobile number field')
@allure.step("When I visually inspect the mobile number field")
def inspect_mobile_field(setup_platform):
    print("Visually inspect the mobile number field")
    Login_Page = AndroidLoginScreen(setup_platform).inspect_mobile_field()
    assert Login_Page, "Mobile number field not visible"

@when('I visually inspect the referral link section')
@allure.step("When I visually inspect the referral link section")
def inspect_referral_link(setup_platform):
    print("Visually inspect the mobile number field")
    Login_Page = AndroidLoginScreen(setup_platform).inspect_referral_link()
    assert Login_Page, "Referral link not visible"

@when('I visually inspect the verify button')
@allure.step("When I visually inspect the verify button")
def inspect_verify_button(setup_platform):
    print("Visually inspect the mobile number field")
    Login_Page = AndroidLoginScreen(setup_platform).inspect_verify_button()
    assert Login_Page, "Verify button not visible"

@when('I visually inspect the footer links')
@allure.step("When I visually inspect the footer links")
def inspect_footer_link(setup_platform):
    print("Visually inspect the mobile number field")
    Login_Page = AndroidLoginScreen(setup_platform).inspect_footer_link()
    assert Login_Page, "Footer links not visible"

@then("I verify all elements should be visible, correctly aligned, and not overlapping")
@allure.step("Then I verify all elements should be visible, correctly aligned, and not overlapping")
def step_validate_alignment(setup_platform):
    print("Validating visibility, alignment, and non-overlapping of UI elements")
    AndroidLoginScreen(setup_platform).validate_login_screen_ui()

@when("I click on user profile icon")
@allure.step("When I click on user profile icon")
def click_on_profile_icon(setup_platform):
    print("Clicking on user profile icon")
    AndroidProfileScreen(setup_platform).click_user_profile_icon()

@then('I verify profile screen navigation')
@allure.step("Then I verify profile screen navigation")
def verify_profile_page_navigation(setup_platform):
    print("Verifying Profile screen Navigation")
    Profile_Screen = AndroidProfileScreen(setup_platform).verify_profile_screen_reached()
    assert Profile_Screen, "Profile screen Is Not navigated"

@when("I click on edit profile icon")
@allure.step("When I click on edit profile icon")
def click_on_edit_profile_icon(setup_platform):
    print("Clicking on edit profile icon")
    AndroidProfileScreen(setup_platform).click_edit_profile_icon()

@then("I verify user is on the profile edit page")
@allure.step("Then I verify user is on the profile edit page")
def profile_edit_page(setup_platform):
    print("verify user is on the profile edit page")
    Profile_Screen = AndroidProfileScreen(setup_platform).verify_profile_edit_page()
    assert Profile_Screen, "The user is not navigated to profile edit page"

@when("I edits the full name field with Test User01 and clicks Save Changes")
@allure.step("When I edits the full name field with Test User01 and clicks Save Changes")
def edit_name_and_click_save(setup_platform):
    print("verify edits the full name field with Test User01 and clicks Save Changes")
    AndroidProfileScreen(setup_platform).edit_profile_name()

@then("I verify updated name should be reflected on the profile")
@allure.step("Then I verify updated name should be reflected on the profile")
def profile_updated_name_display(setup_platform):
    updated_name = AndroidProfileScreen(setup_platform).updated_profile_name()
    print(f"Updated name found: {updated_name}")
    assert updated_name == "Test User01", f"The updated name was expected to be 'Test User01', but got '{updated_name}'"

@when("I click back button on profile details page")
@allure.step("When I click back button on profile details page")
def Clear_name_field(setup_platform):
    print("click back button on profile details page")
    AndroidProfileScreen(setup_platform).click_back_button_on_profile_screen()

@when("I clear name field")
@allure.step("When I clear name field")
def Clear_name_field(setup_platform):
    print("verify clearing the name field")
    AndroidProfileScreen(setup_platform).clear_profile_name_field()

@then('I verify error message Please enter valid full name should be displayed')
@allure.step("Then I verify error message Please enter valid full name should be displayed")
def verify_profile_name_field_error_message(setup_platform):
    print("Verifying error message Please enter valid full name should be displayed")
    AndroidProfileScreen(setup_platform).profile_name_field_empty_error()

@when("I enter invalid characters in name field")
@allure.step("When I enter invalid characters in name field")
def enter_invalid_char_in_name_field(setup_platform):
    print("verify entering invalid characters in name field")
    AndroidProfileScreen(setup_platform).enter_invalid_char_in_name_field()

@when("I clear email address and clicks Save Changes")
@allure.step("When I clear email address and clicks Save Changes")
def edit_email_address_and_click_save(setup_platform):
    print("clear email address and clicks Save Changes")
    AndroidProfileScreen(setup_platform).clear_email_field()


@when("I edits email address and clicks Save Changes")
@allure.step("When I edits email address and clicks Save Changes")
def edit_email_address_and_click_save(setup_platform):
    print("verify edits email address and clicks Save Changes")
    AndroidProfileScreen(setup_platform).edit_email_address()

@then("I verify updated email address should be reflected on the profile")
@allure.step("Then I verify updated email address should be reflected on the profile")
def profile_updated_email_display(setup_platform):
    updated_email = AndroidProfileScreen(setup_platform).updated_email_address()
    print(f"Updated name found: {updated_email}")
    assert updated_email == "testuser11@gmail.com", f"The updated email was expected to be 'testuser11@gmail.com', but got '{updated_email}'"

@when("I enter incorrect email format in email field")
@allure.step("When I enter incorrect email format in email field")
def enter_incorrect_email_in_email_field(setup_platform):
    print("verify entering an incorrect email format in email field")
    AndroidProfileScreen(setup_platform).enter_incorrect_email_format_in_email_field()

@then('I verify error message enter valid email address should be displayed')
@allure.step("Then I verify error message enter valid email address should be displayed")
def verify_incorrect_email_error(setup_platform):
    print("Verifying error message enter valid email address should be displayed")
    AndroidProfileScreen(setup_platform).incorrect_email_error()

@when("I selects a new valid date of birth and clicks Save Changes")
@allure.step("When I selects a new valid date of birth and clicks Save Changes")
def edit_date_of_birth_and_click_save(setup_platform, context):
    print("verify selecting a new valid date of birth and clicks Save Changes")
    profile_screen = AndroidProfileScreen(setup_platform)
    dob = profile_screen.edit_date_of_birth()  # returns formatted DOB string
    context['dob'] = dob  # store dob in context for later steps

@then('I verify updated date of birth should be reflected on the profile')
@allure.step("Then I verify updated date of birth should be reflected on the profile")
def verify__updated_date_of_birth(setup_platform, context):
    dob = context.get('dob')
    assert dob is not None, "DOB was not set in previous step"
    print(f"Verifying date of birth update to today's date: Expected DOB = {dob}")
    profile_screen = AndroidProfileScreen(setup_platform)
    actual_dob = profile_screen.verify_updated_date_of_birth()
    print(f"Actual DOB found on profile: {actual_dob}")
    assert actual_dob == dob, f"Expected '{dob}', but got '{actual_dob}'"


@then('I verify user are unable to select future Date of birth')
@allure.step("Then I verify user are unable to select future Date of birth")
def verify_future_dob_disabled(setup_platform):
    print("Verifying user are unable to select future Date of birth")
    is_selectable = AndroidProfileScreen(setup_platform).verify_future_dob_disabled()
    assert not is_selectable, "future date should not be selectable"

@when("I click calender close icon and click save button")
@allure.step("When I click calender close icon and click save button")
def click_on_calendar_close_button(setup_platform):
    print("click calender close icon and click save button")
    AndroidProfileScreen(setup_platform).click_on_calendar_close_button()

@when("I click change picture link")
@allure.step("When I click change picture link")
def click_change_picture_link(setup_platform):
    print("verify clicking change picture link")
    AndroidProfileScreen(setup_platform).click_change_picture_link()

@then('I verify upload pop up opens with file selection option')
@allure.step("Then I verify upload pop up opens with file selection option")
def verify_upload_file_pop_up(setup_platform):
    print("Verifying upload pop up opens with file selection option")
    AndroidProfileScreen(setup_platform).verify_file_upload_pop_up()

@then('I verify the Save button should be disabled')
@allure.step("Then I verify the Save button should be disabled")
def verify_save_button_disabled(setup_platform):
    print("Verifying the Save button should be disabled")
    is_disabled = AndroidProfileScreen(setup_platform).check_save_changes_button_disabled()
    assert is_disabled, "The save button should be disabled"

@then('I click profile back button')
@allure.step("Then I click profile back button ")
def click_back_button_on_profile_acreen(setup_platform):
    print("click profile back button")
    AndroidProfileScreen(setup_platform).click_back_button_on_profile_acreen()

@when("I Check icon presence near each field")
@allure.step("When I Check icon presence near each field")
def check_icons_presence(setup_platform):
    print("verify Checking icon presence near each field")
    AndroidProfileScreen(setup_platform).check_icon_presence_near_each_field()

@then('I verify the Correct icons for name, phone, email, DOB')
@allure.step("Then I verify the Correct icons for name, phone, email, DOB")
def verify_correct_icons(setup_platform):
    print("Verifying the Correct icons for name, phone, email, DOB")
    AndroidProfileScreen(setup_platform).verify_correct_icons()

@when("I switch toggle on/off and observe UI")
@allure.step("When I switch toggle on/off and observe UI")
def check_switch_toggle(setup_platform):
    print("verify switch toggle on/off and observe UI")
    AndroidProfileScreen(setup_platform).switch_toggle_button()

@then('I verify Color scheme updates to accessible version page should be displayed')
@allure.step("Then I verify Color scheme updates to accessible version page should be displayed")
def verify_color_scheme(setup_platform):
    print("Verifying Color scheme updates to accessible version page should be displayed")
    Profile_screen = AndroidProfileScreen(setup_platform).color_scheme()
    assert Profile_screen, "The color scheme should be displayed"

@when("I switch toggle to make color blind mode on and reload page")
@allure.step("When I switch toggle to make color blind mode on and reload page")
def switch_toggle_to_On_and_reload(setup_platform):
    print("verify switch toggle to make color blind mode on and reload page")
    AndroidProfileScreen(setup_platform).color_blind_mode_On_and_reload_page()

@then('I verify preference retained after refresh')
@allure.step("Then I verify preference retained after refresh")
def verify_preference_retained_after_refresh(setup_platform):
    print("Verifying preference retained after refresh")
    Profile_screen = AndroidProfileScreen(setup_platform).verify_color_blind_preference_retained()
    assert Profile_screen, "The color scheme should not be displayed"

@when("I click on search icon in home screen")
@allure.step("When I click on search icon in home screen")
def click_search_icon(setup_platform):
    AndroidHomeScreen(setup_platform).click_on_search_icon_in_home_screen()

@then("I verify search menu screen navigation")
@allure.step("When I verify search menu screen navigation")
def step_verify_search_menu_navigation(setup_platform):
    AndroidSearchMenuScreen(setup_platform).verify_search_menu_screen_navigation()

@when("I click on search textfield")
@allure.step("When I click on search textfield")
def step_click_search_textfield(setup_platform):
    AndroidSearchMenuScreen(setup_platform).click_on_search_textfield_in_search_menu_screen()

@when("I enter burger name and click search icon")
@allure.step("When I enter burger name and click search icon")
def enter_item_and_click_search(setup_platform):
    AndroidSearchMenuScreen(setup_platform).enter_burger_name_and_click_search()

@then("I verify item displayed")
@allure.step("When I verify item displayed")
def step_verify_item_displays(setup_platform):
    AndroidSearchMenuScreen(setup_platform).verify_item_name_displays()

@when("I click on add+ button")
@allure.step("When I click on add+ button")
def step_click_add_button(setup_platform):
    AndroidSearchMenuScreen(setup_platform).click_on_add_button()

@when("I click on Add to cart option")
@allure.step("When I click on Add to cart option")
def step_click_add_to_cart(setup_platform):
    AndroidSearchMenuScreen(setup_platform).click_on_add_to_cart_button()

@when("I click on view cart option")
@allure.step("When I click on view cart option")
def step_click_view_cart(setup_platform):
    AndroidSearchMenuScreen(setup_platform).click_on_view_cart_button()

@when("I click on add address in home screen")
@allure.step("When I click on add address in home screen")
def click_on_add_address_in_home_screen(setup_platform):
    print("click on add address in home screen")
    AndroidHomeScreen(setup_platform).click_on_add_address_in_home_screen()

@then("I verify user redirected to login/signup prompt")
@allure.step("Then I verify user redirected to login/signup prompt")
def step_verify_login_prompt(setup_platform):
    assert AndroidAddressScreen(setup_platform).verify_redirect_to_login_or_signup_page(), "Login prompt not displayed"

@then("I verify 'Add new' button is displayed to add address")
@allure.step("Then I verify 'Add new' button is displayed to add address")
def step_verify_add_new_button_to_add_address(setup_platform):
    print("verify 'Add new' button is displayed to add address")
    AndroidAddressScreen(setup_platform).verify_add_new_button_to_add_address()

@then("I click back button from select address screen")
@allure.step("Then I click back button from select address screen")
def click_back_button_from_select_address_screen(setup_platform):
    print("clicked back button from select address screen")
    AndroidAddressScreen(setup_platform).click_back_button_from_select_address_screen()

@when("I click on login/signup prompt")
@allure.step("When I click on login/signup prompt")
def click_login_prompt(setup_platform):
    AndroidAddressScreen(setup_platform).click_login_prompt()

@when("I click on login/signup prompt from checkout")
@allure.step("When I click on login/signup prompt from checkout")
def click_login_prompt_from_checkout(setup_platform):
    AndroidViewCartScreen(setup_platform).Click_login_prompt_from_checkout()

@when("I click on cancel button from login/signup pop up")
@allure.step("When I click on cancel button from login/signup pop up")
def click_cancel_from_login_prompt(setup_platform):
    AndroidViewCartScreen(setup_platform).click_cancel_to_login_or_signup_page()

@then("I verify Login cancelled and user returned to checkout page")
@allure.step("When I verify Login cancelled and user returned to checkout page")
def verify_login_cancelled_and_redirect_to_checkout(setup_platform):
    assert AndroidViewCartScreen(setup_platform).verify_redirect_to_checkout_page(), "Checkout page not displayed"

@when("I enter incorrect mobile number")
@allure.step("When I enter incorrect mobile number")
def enter_incorrect_mobile_number(setup_platform):
    invalid_mobile_number = readPreReqJson("test_data", "invalid_mobile_number")
    print("Entering invalid Mobile Number")
    AndroidLoginScreen(setup_platform).enter_invalid_mobile_number(invalid_mobile_number)

@when("I click on add new button and search for location")
@allure.step("When I click on add new button and search for location")
def click_on_add_new_button_and_search_for_location(setup_platform):
    print("Searching For Location To Add new Location")
    AndroidAddressScreen(setup_platform).Click_add_new_button_and_confirm_location()

@when("I add new delivery address")
@allure.step("When I add new delivery address")
def add_new_delivery_address(setup_platform):
    print("add new delivery address")
    AndroidAddressScreen(setup_platform).add_new_delivery_address()

@then("I verify address is added and selected")
@allure.step("Then I verify address is added and selected")
def verify_address_is_added_and_selected(setup_platform):
    print("Verifying Address Is Added And Selected")
    Address_Added = AndroidAddressScreen(setup_platform).verify_address_is_added_and_selected()
    assert Address_Added, "Address Is Not Added And Selected From The List Of Addresses"

@when("I click on add new button and click confirm location")
@allure.step("When I click on add new button and click confirm location")
def click_add_new_and_confirm_location(setup_platform):
    print("clicking on add new button and click confirm location")
    AndroidAddressScreen(setup_platform).Click_add_new_button_and_confirm_location()


@then("I verify user redirected to address fill in details page")
@allure.step("Then I verify user redirected to address fill in details page")
def verify_user_redirected_to_address_filling_page(setup_platform):
    print("Verifying user redirected to address fill in details page")
    Address_Page = AndroidAddressScreen(setup_platform).verify_redirect_to_address_filling_page()
    assert Address_Page, "Address filling details page is not displayed"

@when("I leave mandatory field empty and click save address")
@allure.step("When I leave mandatory field empty and click save address")
def click_add_new_and_confirm_location(setup_platform):
    print("leave mandatory field empty and click save address")
    AndroidAddressScreen(setup_platform).verify_leave_address_mandatory_field_empty()


@then("I verify that the address not saved and validation error should be displayed")
@allure.step("Then I verify that the address not saved and validation error should be displayed")
def verify_user_redirected_to_address_filling_page(setup_platform):
    print("Verifying that the address not saved and validation error should be displayed")
    AndroidAddressScreen(setup_platform).verify_address_mandatory_field_empty_error()

@when("I enter special character in house/flat field and click save address")
@allure.step("When I enter special character in house/flat field and click save address")
def enter_special_char_in_house_field_and_saved(setup_platform):
    print("enter special character in house/flat field and click save address")
    AndroidAddressScreen(setup_platform).enter_special_char_in_house_field()


@then("I verify field accept characters and address will get saved")
@allure.step("Then I verify field accept characters and address will get saved")
def verify_user_redirected_to_address_filling_page(setup_platform):
    print("Verifying field accept characters and address will get saved")
    Address_accept_special_char = AndroidAddressScreen(setup_platform).verify_field_accept_special_char_and_address_saved()
    assert Address_accept_special_char, "Address does not accept special char and show validation error"

@when("I enter text in house/flat field and click back button without saving")
@allure.step("When I enter text in house/flat field and click back button without saving")
def enter_text_in_house_field_and_click_back_button(setup_platform):
    print("enter text in house/flat field and click back button without saving")
    AndroidAddressScreen(setup_platform).enter_text_in_house_field_and_cancel_before_saving()


@then("I verify address will not get saved")
@allure.step("Then I verify address will not get saved")
def verify_address_not_saved(setup_platform):
    print("Verifying address will not get saved")
    AndroidAddressScreen(setup_platform).verify_address_is_not_saved_when_click_back_button_without_saving()


@then("I verify System allows address duplication based on business logic")
@allure.step("Then I verify System allows address duplication based on business logic")
def verify_address_not_saved(setup_platform):
    print("Verifying  System allows address duplication based on business logic")
    AndroidAddressScreen(setup_platform).verify_duplicate_address_saved()


@then("I verify displays of McDelivery, Dine-In, On the Go, Take Away at the top of the screen")
@allure.step("Then I verify displays of McDelivery, Dine-In, On the Go, Take Away at the top of the screen")
def verify_dropdown_displays_all_business_model(setup_platform):
    print("Verifying displays of McDelivery, Dine-In, On the Go, Take Away at the top of the screen")
    AndroidHomeScreen(setup_platform).verify_displays_of_all_business_model()

@when("I select the McDelivery option")
@allure.step("When I select the McDelivery option")
def select_McDelivery_from_dropdown(setup_platform):
    print("select the McDelivery option")
    AndroidHomeScreen(setup_platform).verify_McDelivery_option()


@then("I verify User is taken to the McDelivery ordering flow")
@allure.step("Then I verify User is taken to the McDelivery ordering flow")
def verify_redirection_to_McDelivery_ordering_flow(setup_platform):
    print("Verifying User is taken to the McDelivery ordering flow")
    AndroidHomeScreen(setup_platform).verify_user_redirect_to_McDelivery_ordering_flow()

@when("I select Dine-In option")
@allure.step("When I select Dine-In option")
def select_Dine_in_from_dropdown(setup_platform):
    print("select Dine-In option")
    AndroidHomeScreen(setup_platform).verify_Dine_In_option()


@then("I verify User navigates to Dine-In selection/location flow")
@allure.step("Then I verify User navigates to Dine-In selection/location flow")
def verify_redirection_to_Dine_in_location_flow(setup_platform):
    print("Verifying User navigates to Dine-In selection/location flow")
    AndroidHomeScreen(setup_platform).verify_user_redirect_to_Dine_In_location_flow()

@when("I select on the go option")
@allure.step("When I select on the go option")
def select_On_the_go_from_dropdown(setup_platform):
    print("select on the go option")
    AndroidHomeScreen(setup_platform).verify_On_the_go_option()


@then("I verify User is prompted to choose pick-up location")
@allure.step("Then I verify User is prompted to choose pick-up location")
def verify_redirection_to_On_the_go_pick_up_location_flow(setup_platform):
    print("Verifying User is prompted to choose pick-up location")
    AndroidHomeScreen(setup_platform).verify_user_redirect_to_On_the_go_pick_up_location_flow()

@when("I select Take Away option")
@allure.step("When I select Take Away option")
def select_take_away_from_dropdown(setup_platform):
    print("select Take Away option")
    AndroidHomeScreen(setup_platform).verify_take_away_option()


@then("I verify User proceeds to place an order for take away")
@allure.step("Then I verify User proceeds to place an order for take away")
def verify_redirection_to_take_away_location_flow(setup_platform):
    print("Verifying User proceeds to place an order for take away")
    AndroidHomeScreen(setup_platform).verify_user_redirect_to_take_away_location_flow()

@then("I verify 'McDelivery' should be selected by default")
@allure.step("When I verify 'McDelivery' should be selected by default")
def select_take_away_from_dropdown(setup_platform):
    print("Verify McDelivery should be selected by default")
    AndroidHomeScreen(setup_platform).verify_McDelivery_selected_by_default()

@when("I search the address from searchbar and select the address")
@allure.step("When I search the address from searchbar and select the address")
def search_address_from_searchbar(setup_platform):
    print("search the address from searchbar and select the address")
    AndroidAddressScreen(setup_platform).search_for_address_after_selecting_business_model()

@when("I browse the menu and return to the homepage")
@allure.step("When I browse the menu and return to the homepage")
def verify_browse_menu(setup_platform):
    print("browse the menu and return to the homepage")
    AndroidSearchMenuScreen(setup_platform).verify_browse_menu()

@then("I verify Dine-In remains the selected option until manually changed")
@allure.step("Then I verify Dine-In remains the selected option until manually changed")
def verify_dine_in_remains_selected(setup_platform):
    print("Verifying Dine-In remains the selected option until manually changed")
    AndroidHomeScreen(setup_platform).verify_Dine_In_selected_until_manually_changed()

@then("I verify selected 'Kasturba Road' address is displayed for Dine-In model")
@allure.step("Then I verify selected 'Kasturba Road' address is displayed for Dine-In model")
def verify_dine_in_remains_selected(setup_platform):
    print("verify selected 'Kasturba Road' address is displayed for Dine-In model")
    AndroidAddressScreen(setup_platform).verify_selected_address_is_displayed()

@when("I select 'Dine-In' without granting location access")
@allure.step("When I select 'Dine-In' without granting location access")
def select_dine_in_option(setup_platform):
    print("select 'Dine-In' without granting location access")
    AndroidHomeScreen(setup_platform).verify_Dine_In_option()

@when("I select 'On the Go' without granting location access")
@allure.step("When I select 'On the Go' without granting location access")
def select_on_the_go_option(setup_platform):
    print("select 'On the Go' without granting location access")
    AndroidHomeScreen(setup_platform).verify_On_the_go_option()

@then("I verify a prompt should appear requesting location permission")
@allure.step("Then I verify a prompt should appear requesting location permission")
def verify_location_popup(setup_platform):
    print("verify a prompt should appear requesting location permission")
    AndroidHomeScreen(setup_platform).verify_location_popup()

@then("I verify only one model should remain active at a time")
@allure.step("Then I verify only one model should remain active at a time")
def verify_active_model(setup_platform):
    print("Verifying only one model should remain active at a time")
    AndroidHomeScreen(setup_platform).step_check_only_one_active()

@when("I hover over each business model option")
@allure.step("When I hover over each business model option")
def Hover_over_each_business_model(setup_platform):
    print("hover over each business model option")
    AndroidHomeScreen(setup_platform).verify_displays_of_all_business_model()

@then("I verify the icons and text should respond visually")
@allure.step("Then I verify the icons and text should respond visually")
def verify_icons_and_text_repond_visually(setup_platform):
    print("Verifying the icons and text should respond visually")
    AndroidHomeScreen(setup_platform).verify_icons_display_on_each_business_model()

@then("I verify the user notes their current profile information")
@allure.step("Then I verify the user notes their current profile information")
def verify_current_profile_info(setup_platform, user_data_store):
    print("Verifying the user notes their current profile information")
    AndroidViewScreen(setup_platform).Verify_current_profile_info(user_data_store)

@when("I verify user switches from one model to another")
@allure.step("When I verify user switches from one model to another")
def switch_between_business_model(setup_platform):
    print("Verify user switches from one model to another")
    AndroidHomeScreen(setup_platform).verify_switching_from_one_model_to_another()

@then("I verify the profile information should remain unchanged")
@allure.step("Then I verify the profile information should remain unchanged")
def verify_icons_and_text_repond_visually(setup_platform, user_data_store):
    print("Verifying the profile information should remain unchanged")
    AndroidViewScreen(setup_platform).Verify_profile_info_remian_unchanged(user_data_store)

@then("I verify the page layout or menu should adapt to match the McDelivery model")
@allure.step("Then I verify the page layout or menu should adapt to match the McDelivery model")
def verify_layout_of_Dine_In_model(setup_platform):
    print("verify the page layout or menu should adapt to match the McDelivery model")
    AndroidHomeScreen(setup_platform).verify_user_redirect_to_McDelivery_ordering_flow()

@then("I verify the page layout or menu should adapt to match the on the go model")
@allure.step("Then I verify the page layout or menu should adapt to match the on the go model")
def verify_layout_of_Take_away_model(setup_platform):
    print("verify the page layout or menu should adapt to match the on the go model")
    AndroidHomeScreen(setup_platform).verify_user_redirect_to_On_the_go_pick_up_location_flow()

@then("I verify the page layout or menu should adapt to match the Dine-In model")
@allure.step("Then I verify the page layout or menu should adapt to match the Dine-In model")
def verify_layout_of_On_the_go_model(setup_platform):
    print("verify the page layout or menu should adapt to match the Dine-In model")
    AndroidHomeScreen(setup_platform).verify_user_redirect_to_Dine_In_location_flow()

@then("I verify the page layout or menu should adapt to match the Take Away model")
@allure.step("Then I verify the page layout or menu should adapt to match the Take Away model")
def verify_layout_of_Mcdelivery_model(setup_platform):
    print("verify the page layout or menu should adapt to match the Take Away model")
    AndroidHomeScreen(setup_platform).verify_user_redirect_to_take_away_location_flow()

@when("I search the address from searchbar after selecting BM model")
@allure.step("When I search the address from searchbar after selecting BM model")
def search_address_after_selecting_BM_model(setup_platform):
    print("search the address from searchbar after selecting BM model")
    AndroidAddressScreen(setup_platform).search_for_address_after_selecting_Dine_In_model()

@then("I should see the message: “Sorry, we do not serve this location yet”")
@allure.step("Then I should see the message: “Sorry, we do not serve this location yet”")
def verify_toast_appear_for_unsupported_location(setup_platform):
    print("Verifying the message: “Sorry, we do not serve this location yet”")
    AndroidHomeScreen(setup_platform).show_toast()

@when("I user click on a listed address")
@allure.step("When I user click on a listed address")
def click_on_listed_address(setup_platform):
    print("user click on a listed address")
    AndroidAddressScreen(setup_platform).Click_from_listed_address("Marathahalli village, HAL Airport road")

@then("I verify the address is selected and restaurant list should update accordingly")
@allure.step("Then I verify the address is selected and restaurant list should update accordingly")
def verify_address_selected_restaurant_updated_accordingly(setup_platform):
    print("Verifying the address is selected and restaurant list should update accordingly")
    AndroidAddressScreen(setup_platform).verify_address_is_added_and_selected()

@when("I click the edit icon next to an address")
@allure.step("When I click the edit icon next to an address")
def click_address_edit_icon(setup_platform):
    print("click the edit icon next to an address")
    AndroidAddressScreen(setup_platform).click_address_edit_icon()

@when("I modifies the address details and click save button")
@allure.step("When I modifies the address details and click save button")
def modify_existing_address(setup_platform):
    print("modifies the address details and click save button")
    AndroidAddressScreen(setup_platform).modify_existing_address_and_click_save("123, Marathahalli")

@then("I verify updated address is shown in the address list")
@allure.step("Then I verify updated address is shown in the address list")
def verify__updated_address_display_in_address_list(setup_platform):
    print("Verifying updated address is shown in the address list")
    AndroidAddressScreen(setup_platform).verify_updated_address_display_in_address_list("123, Marathahalli,")

@when("I enter text exceeding the max character limit in address fields and click save address")
@allure.step("And I enter text exceeding the max character limit in address fields and click save address")
def step_enter_text_exceeding_limit(setup_platform):
    AndroidAddressScreen(setup_platform).enter_text_exceeding_max_limit()

@then("I verify address accept max characters and get saved")
@allure.step("Then I verify address accept max characters and get saved")
def verify_address_accept_max_char(setup_platform):
    print("verify address accept max characters and get saved")
    Address_accept_max_char = AndroidAddressScreen(setup_platform).verify_field_accept_maximum_char_and_address_saved()
    assert Address_accept_max_char, "Address does not accept maximum char and show validation error"

@when("I verify address list shown")
@allure.step("When I verify address list shown")
def verify_address_list_shown(setup_platform, user_data_store):
    print("verify address list shown")
    AndroidAddressScreen(setup_platform).Verify_address_shown_in_list_before_deletion(user_data_store)

@when("I click the delete icon next to an address")
@allure.step("When I click the delete icon next to an address")
def click_address_delete_icon(setup_platform):
    print("click the delete icon next to an address")
    AndroidAddressScreen(setup_platform).click_address_delete_icon()

@then("I verify address removed from list")
@allure.step("Then I verify address removed from list")
def verify_address_removed_from_list(setup_platform, user_data_store):
    print("Verifying address removed from list")
    AndroidAddressScreen(setup_platform).Verify_address_removed_from_list_after_deletion(user_data_store)

@when("I verify address list displayed")
@allure.step("When I verify address list displayed")
def verify_address_list(setup_platform):
    print("verify address list displayed")
    AndroidAddressScreen(setup_platform).verify_address_list()

@then("I verify each address should display a Near label with its location description")
@allure.step("Then I verify each address should display a Near label with its location description")
def verify_address_removed_from_list(setup_platform):
    print("Verifying each address should display a Near label with its location description")
    AndroidAddressScreen(setup_platform).verify_near_label_visible_in_address_description()


@then("I verify all saved addresses should be accessible via scrolling")
@allure.step("Then I verify all saved addresses should be accessible via scrolling")
def verify__all_saved_address_accessible_via_scroll(setup_platform):
    print("Verifying all saved addresses should be accessible via scrolling")
    AndroidAddressScreen(setup_platform).All_addresses_accessible_via_scrolling()

@when("I selects the first address from the address list")
@allure.step("When I selects the first address from the address list")
def select_first_address_from_list(setup_platform):
    print("selects the first address from the address list")
    AndroidAddressScreen(setup_platform).select_first_address_from_list()

@then("I verify restaurant list should update based on the first address location")
@allure.step("Then I verify restaurant list should update based on the first address location")
def verify_restaurant_list_update_based_on_first_address(setup_platform):
    print("Verifying restaurant list should update based on the first address location")
    AndroidHomeScreen(setup_platform).verify_error_message_for_undeliverable_address()

@when("I selects the second address from the address list")
@allure.step("When I selects the second address from the address list")
def select_second_address_from_list(setup_platform):
    print("selects the second address from the address list")
    AndroidAddressScreen(setup_platform).select_another_address_from_list()

@then("I verify restaurant list should update based on the second address location")
@allure.step("Then I verify restaurant list should update based on the second address location")
def verify_restaurant_list_update_based_on_second_address(setup_platform):
    print("Verifying restaurant list should update based on the second address location")
    AndroidHomeScreen(setup_platform).verify_address_selected_and_restaurant_updated_accordingly()

@when("I enters an undeliverable pin code or area manually")
@allure.step("When I enters an undeliverable pin code or area manually")
def enter_undeliverable_address(setup_platform):
    print("enters an undeliverable pin code or area manually")
    AndroidAddressScreen(setup_platform).enter_an_undeliverable_address()

@then("I verify an error message should be displayed saying Delivery not available at this address")
@allure.step("Then I verify an error message should be displayed saying Delivery not available at this address")
def verify__error_message_for_undeliverable_location(setup_platform):
    print("Verifying an error message should be displayed saying Delivery not available at this address")
    AndroidHomeScreen(setup_platform).verify_error_message_for_undeliverable_address()

@then("I verify the most recently used address should be auto-selected")
@allure.step("Then I verify the most recently used address should be auto-selected")
def verify_recently_used_address_is_auto_selected_after_login(setup_platform):
    print("Verifying the most recently used address should be auto-selected")
    AndroidHomeScreen(setup_platform).verify_recently_used_address_is_auto_selected_after_login()

@when("I adds an address and select a tag")
@allure.step("When I adds an address and select a tag")
def add_address_and_select_tag(setup_platform):
    print("adds an address and select a tag")
    AndroidAddressScreen(setup_platform).add_address_and_select_tag()

@then("I verify the tag should be displayed next to the address name after adding address")
@allure.step("Then I verify the tag should be displayed next to the address name after adding address")
def verify_work_tag_display_next_to_address(setup_platform):
    print("Verifying the tag should be displayed next to the address name after adding address")
    AndroidAddressScreen(setup_platform).verify_tag_next_to_address_after_adding_address()

@when("I edits an address and select a tag")
@allure.step("When I edits an address and select a tag")
def edit_address_and_select_tag(setup_platform):
    print("edits an address and select a tag")
    AndroidAddressScreen(setup_platform).edit_address_and_select_tag()

@then("I verify the tag should be displayed next to the address name after editing address")
@allure.step("Then I verify the tag should be displayed next to the address name after editing address")
def verify_home_tag_display_next_to_address(setup_platform):
    print("Verifying the tag should be displayed next to the address name after editing address")
    AndroidAddressScreen(setup_platform).verify_tag_next_to_address_after_editing_address()

@when("I delete all addresses")
@allure.step("When I delete all addresses")
def verify_delete_all_addresses(setup_platform):
    print("delete all addresses")
    AndroidAddressScreen(setup_platform).delete_all_addresses()

@then("I verify the address list should be empty and the Add Address prompt should be visible")
@allure.step("Then I verify the address list should be empty and the Add Address prompt should be visible")
def verify_address_prompt_visible(setup_platform):
    print("Verifying the address list should be empty and the Add Address prompt should be visible")
    AndroidAddressScreen(setup_platform).verify_add_new_address_prompt_visible()

@when("I verify address list before logout of the application")
@allure.step("When I verify address list before logout of the application")
def verify_address_list_before_logout(setup_platform, user_data_store):
    print("verify address list before logout of the application")
    AndroidAddressScreen(setup_platform).verify_address_list_before_logout_the_application(user_data_store)

@then("I verify previously saved addresses should be retained and visible")
@allure.step("Then I verify previously saved addresses should be retained and visible")
def verify_previously_saved_address_should_visible(setup_platform, user_data_store):
    print("Verifying previously saved addresses should be retained and visible")
    AndroidAddressScreen(setup_platform).verify_previously_saved_address_should_visible_after_logs_in(user_data_store)

@when("I scroll to clear all")
@allure.step("When I scroll to clear all")
def Scroll_to_clear_all(setup_platform):
    print("scroll to clear all")
    AndroidViewCartScreen(setup_platform).Scroll_to_clear_all()

@when("I click on clear all to empty the cart")
@allure.step("When I click on clear all to empty the cart")
def Clear_all_cart(setup_platform):
    print("click on clear all to empty the cart")
    AndroidViewCartScreen(setup_platform).Clear_all_cart()

@when("I click on Menu icon")
@allure.step("When I click on Menu icon")
def click_on_Menu_icon(setup_platform):
    print("click on Menu icon")
    AndroidHomeScreen(setup_platform).click_on_Menu_icon()

@when("I add breakfast item")
@allure.step("When I add breakfast item")
def add_breakfast_item(setup_platform):
    print("add breakfast item")
    AndroidMenuScreen(setup_platform).add_breakfast_item("Veg McMuffin with protein plus Meal")

@then("I verify the item is added to the cart")
@allure.step("Then I verify the item is added to the cart")
def verify_breakfast_item_added_to_cart(setup_platform):
    print("verify the item is added to the cart")
    AndroidViewCartScreen(setup_platform).verify_breakfast_item_added_to_cart()

@when("I click on 'Add +' for the customizable item")
@allure.step("When I click on 'Add +' for the customizable item")
def click_add_button(setup_platform):
    print("Add+ button clicked for the customizable item")
    AndroidMenuScreen(setup_platform).click_add_for_customise_item("Mexican Grilled Chicken & Cheese Burger + Fries (M)")

@then("I verify the customization options should appear before adding the item to the cart")
@allure.step("Then I verify the customization options should appear before adding the item to the cart")
def step_verify_customise_option_appear(setup_platform):
    print("Verifying the customization options should appear before adding the item to the cart")
    AndroidMenuScreen(setup_platform).verify_customise_option_appear()

@when("I user adds the item to the cart")
@allure.step("When I user adds the item to the cart")
def Add_single_item_to_the_cart(setup_platform, context):
    print("User adds the item to the cart")
    menu_price = AndroidMenuScreen(setup_platform).add_item_in_cart(
        "Mexican Grilled Chicken & Cheese Burger + Fries (M)")
    context["menu_price"] = menu_price  # Store price for later


@then("I verify the price in the cart should match the menu price")
@allure.step("Then I verify the price in the cart should match the menu price")
def verify_product_price_in_the_cart_match_with_menu_price(setup_platform, context):
    print("Verifying that the price in the cart matches the menu price")
    menu_price = context.get("menu_price")
    AndroidMenuScreen(setup_platform).verify_price_in_cart_matches_menu_price(
        "Mexican Grilled Chicken & Cheese Burger + Fries (M)", menu_price
    )

@when("I clicks on the 'Customize' button")
@allure.step("When I clicks on the 'Customize' button")
def click_customise_option(setup_platform):
    print("clicks on the 'Customize' button")
    AndroidMenuScreen(setup_platform).click_customise_option()

@when("I selects or removes items from the customization options")
@allure.step("When I selects or removes items from the customization options")
def Add_or_remove_items_on_customise_page(setup_platform):
    print("selects or removes items from the customization options")
    AndroidMenuScreen(setup_platform).click_add_and_remove_sign_to_customised_item()

@then("I verify the customized item should be added to the cart with selected preferences")
@allure.step("When I verify the customized item should be added to the cart with selected preferences")
def Verify_customisation_text_after_adding_or_removing_items(setup_platform):
    print("verify the customized item should be added to the cart with selected preferences")
    AndroidViewCartScreen(setup_platform).verify_customised_item_is_displayed_to_cart()

@when("I selects the '3Pc Meals' category under menu")
@allure.step("When I selects the '3Pc Meals' category under menu")
def select_3PC_meal_under_menu(setup_platform):
    print("selects the '3Pc Meals' category under menu")
    AndroidMenuScreen(setup_platform).Select_3PC_meals_menu()

@when("I select McChicken meal from the '3Pc Meals' category and click on Add to cart")
@allure.step("When I select McChicken meal from the '3Pc Meals' category and click on Add to cart")
def select_product_from_3PC_meals_category(setup_platform):
    print("Select McChicken meal from the '3Pc Meals' category and click on Add to cart")
    AndroidMenuScreen(setup_platform).add_McChicken_meal_in_cart()

@then("I verify the 3Pc meal added in cart")
@allure.step("Then I verify the 3Pc meal added in cart")
def verify_3pc_meal_item_added_to_cart(setup_platform):
    print("verify the 3Pc meal added in cart")
    AndroidViewCartScreen(setup_platform).verify_3pc_meal_item_added_to_cart()

@when("I click on 'Fries & Sides' menu option")
@allure.step("When I click on 'Fries & Sides' menu option")
def click_fries_and_sides_menu(setup_platform):
    print("click on 'Fries & Sides' menu option")
    AndroidMenuScreen(setup_platform).click_fries_and_sides_menu()
    
@when("I add 'Medium Fries' to the cart")
@allure.step("When I add 'Medium Fries' to the cart")
def add_fries_in_cart(setup_platform):
    print("add 'Medium Fries' to the cart")
    AndroidMenuScreen(setup_platform).add_fries_in_cart()

@then("I verify fries should be added to the cart")
@allure.step("Then I verify fries should be added to the cart")
def verify_product_added_in_cart(setup_platform):
    print("verify fries should be added to the cart")
    AndroidViewCartScreen(setup_platform).verify_fries_added_to_cart()

@when("I selects the 'Desserts' category under menu")
@allure.step("When I selects the 'Desserts' category under menu")
def Select_Desserts_menu(setup_platform):
    print("selects the 'Desserts' category under menu")
    AndroidMenuScreen(setup_platform).Select_Desserts_menu()

@when("I select any product from desserts and click on Add to cart")
@allure.step("When I select any product from desserts and click on Add to cart")
def add_Desserts_product_in_cart(setup_platform):
    print("select any product from desserts and click on Add to cart")
    AndroidMenuScreen(setup_platform).add_Desserts_product_in_cart()

@then("I verify the Desserts product added in cart")
@allure.step("Then I verify the Desserts product added in cart")
def verify_Desserts_item_added_to_cart(setup_platform):
    print("verify the Desserts product added in cart")
    AndroidViewCartScreen(setup_platform).verify_Desserts_item_added_to_cart()

@when("I selects the 'Burgers & Wraps' category under menu")
@allure.step("When I selects the 'Burgers & Wraps' category under menu")
def Select_Burgers_and_wrap_menu(setup_platform):
    print("selects the 'Burgers & Wraps' category under menu")
    AndroidMenuScreen(setup_platform).Select_Burgers_and_wrap_menu()

@when("I select chicken wrap and Add to cart")
@allure.step("When I select chicken wrap and Add to cart")
def add_Chicken_wrap_to_cart(setup_platform):
    print("select chicken wrap and Add to cart")
    AndroidMenuScreen(setup_platform).add_Chicken_wrap_to_cart()

@then("I verify the Burgers & Wraps product added in cart")
@allure.step("Then I verify the Burgers & Wraps product added in cart")
def verify_Wrap_item_added_to_cart(setup_platform):
    print("verify the Burgers & Wraps product added in cart")
    AndroidViewCartScreen(setup_platform).verify_Wrap_item_added_to_cart()

@when("I click on 'Coffee & Beverages' menu option")
@allure.step("When I click on 'Coffee & Beverages' menu option")
def Select_Coffee_and_beverages_menu(setup_platform):
    print("click on 'Coffee & Beverages' menu option")
    AndroidMenuScreen(setup_platform).Select_Coffee_and_beverages_menu()

@when("I add 'cold coffee' to the cart")
@allure.step("When I add 'cold coffee' to the cart")
def add_cold_coffee_to_cart(setup_platform):
    print("add 'cold coffee' to the cart")
    AndroidMenuScreen(setup_platform).add_cold_coffee_to_cart()

@then("I verify cold coffee should be added to the cart")
@allure.step("Then I verify cold coffee should be added to the cart")
def verify_cold_coffee_added_to_cart(setup_platform):
    print("verify cold coffee should be added to the cart")
    AndroidViewCartScreen(setup_platform).verify_cold_coffee_added_to_cart()

@when("I add 'Hot coffee' to the cart")
@allure.step("When I add 'Hot coffee' to the cart")
def add_hot_coffee_to_cart(setup_platform):
    print("add 'Hot coffee' to the cart")
    AndroidMenuScreen(setup_platform).add_hot_coffee_to_cart()

@then("I verify cold coffee & hot coffee should be added to the cart")
@allure.step("Then I verify cold coffee & hot coffee should be added to the cart")
def verify_cold_coffee_and_hot_coffee_added_to_cart(setup_platform):
    print("verify cold coffee & hot coffee should be added to the cart")
    AndroidViewCartScreen(setup_platform).verify_cold_coffee_and_hot_coffee_added_to_cart()

@when("I click on 'Cakes, Brownies & Cookies' menu option")
@allure.step("When I click on 'Cakes, Brownies & Cookies' menu option")
def Select_Cakes_brownies_and_cookies_menu(setup_platform):
    print("click on 'Cakes, Brownies & Cookies' menu option")
    AndroidMenuScreen(setup_platform).Select_Cakes_brownies_and_cookies_menu()

@when("I add 'Brownie' to the cart")
@allure.step("When I add 'Brownie' to the cart")
def add_brownie_to_cart(setup_platform):
    print("add 'Brownie' to the cart")
    AndroidMenuScreen(setup_platform).add_brownie_to_cart()

@then("I verify brownie should be added to the cart")
@allure.step("Then I verify brownie should be added to the cart")
def verify_brownie_added_to_cart(setup_platform):
    print("verify brownie should be added to the cart")
    AndroidViewCartScreen(setup_platform).verify_brownie_added_to_cart()

@then("I verify thumbnails image of a dessert is clearly displayed")
@allure.step("Then I verify thumbnails image of a dessert is clearly displayed")
def verify_Desserts_thumnbnails_image_is_clearly_displayed(setup_platform):
    print("verify thumbnails image of a dessert is clearly displayed")
    AndroidMenuScreen(setup_platform).verify_Desserts_thumnbnails_image_is_clearly_displayed()

@when("I click on 'Burgers with Millet Bun' menu option")
@allure.step("When I click on 'Burgers with Millet Bun' menu option")
def select_millet_bun_menu(setup_platform):
    print("click on 'Burgers with Millet Bun' menu option")
    AndroidMenuScreen(setup_platform).select_millet_bun_menu()

@when("I add 'millet bun burger' to the cart")
@allure.step("When I add 'millet bun burger' to the cart")
def add_millet_bun_to_cart(setup_platform):
    print("add 'millet bun burger' to the cart")
    AndroidMenuScreen(setup_platform).add_millet_bun_to_cart()

@then("I verify millet bun burger should be added to the cart")
@allure.step("Then I verify millet bun burger should be added to the cart")
def verify_millet_bun_added_to_cart(setup_platform):
    print("verify millet bun burger should be added to the cart")
    AndroidViewCartScreen(setup_platform).verify_millet_bun_added_to_cart()

@when("I click on millet bun burger")
@allure.step("When I click on millet bun burger")
def click_on_millet_bun_burger(setup_platform):
    print("click on millet bun burger")
    AndroidMenuScreen(setup_platform).click_on_millet_bun_burger()

@then("I verify nutritional info is displayed in the description")
@allure.step("Then I verify nutritional info is displayed in the description")
def verify_millet_bun_description_is_displayed(setup_platform):
    print("verify nutritional info is displayed in the description")
    AndroidMenuScreen(setup_platform).verify_millet_bun_description_is_displayed()

@when("I selects the Mumbai address from the address list")
@allure.step("When I selects the Mumbai address from the address list")
def select_Mumbai_address_from_list(setup_platform):
    print("I selects the Mumbai address from the address list")
    AndroidAddressScreen(setup_platform).select_Mumbai_address_from_list()

@when("I click 'Sold out' items from McBreakfast category")
@allure.step("When I click 'Sold out' items from McBreakfast category")
def add_sold_out_breakfast_item(setup_platform):
    print("Click 'Sold out' items from McBreakfast category")
    AndroidMenuScreen(setup_platform).add_sold_out_breakfast_item("Veg McMuffin with protein plus Meal")

@then("I very User is unable to add item and Sold out popup shown")
@allure.step("Then I very User is unable to add item and Sold out popup shown")
def verify_millet_bun_description_is_displayed(setup_platform):
    print("very User is unable to add item and Sold out popup shown")
    AndroidMenuScreen(setup_platform).verify_sold_out_option_is_displayed()

@when("I add single item to the cart")
@allure.step("When I add single item to the cart")
def add_single_item_in_cart(setup_platform):
    print("add single item to the cart")
    AndroidMenuScreen(setup_platform).add_single_item_in_cart("Mexican Grilled Chicken & Cheese Burger + Fries (M)")

@when("I add multiple items to cart")
@allure.step("When I add multiple items to cart")
def add_multiple_items_to_the_cart(setup_platform):
    print("add multiple items to cart")
    AndroidMenuScreen(setup_platform).add_multiple_items_to_cart()

@then("I verify all added items should be listed in the cart with correct price and quantities")
@allure.step("Then I verify all added items should be listed in the cart with correct price and quantities")
def verify_all_item_added_with_correct_price(setup_platform):
    print("Verifying all added items should be listed in the cart with correct price and quantities")
    AndroidViewCartScreen(setup_platform).get_all_cart_items()

@when("I clicks the 'Remove' button for an item")
@allure.step("When I clicks the 'Remove' button for an item")
def Click_remove_to_decrease_cart_item(setup_platform):
    print("clicks the 'Remove' button for an item")
    AndroidViewCartScreen(setup_platform).remove_cart_item()

@then("I verify the selected item should be removed from the cart")
@allure.step("Then I verify the selected item should be removed from the cart")
def Verify_selected_items_removed_from_cart(setup_platform):
    print("verify the selected item should be removed from the cart")
    AndroidViewCartScreen(setup_platform).Verify_selected_items_removed_from_cart()

@then("I verify the single item in cart")
@allure.step("Then I verify the single item in cart")
def Verify_single_item_in_cart(setup_platform):
    print("verify the single item in cart")
    AndroidViewCartScreen(setup_platform).Verify_single_item_in_cart()

@when("I clicks the 'Add' button for an item")
@allure.step("When I clicks the 'Add' button for an item")
def Click_add_to_increase_cart_item(setup_platform):
    print("clicks the 'Add' button for an item")
    AndroidViewCartScreen(setup_platform).increase_cart_item()

@then("I verify the Quantity updates correctly")
@allure.step("Then I verify the Quantity updates correctly")
def verify_item_quantity(setup_platform):
    print("Verifying quantity updated correctly")
    AndroidViewCartScreen(setup_platform).verify_item_quantity()

@then("I verify the total payable amount should be displayed")
@allure.step("Then I verify the total payable amount should be displayed")
def Verify_total_payable_amount_is_displayed_in_cart_page(setup_platform):
    print("verify the total payable amount should be displayed")
    AndroidViewCartScreen(setup_platform).Verify_total_payable_amount_is_displayed_in_cart_page()

@then("I verify the Desserts category is accessible via scrolling")
@allure.step("Then I verify the Desserts category is accessible via scrolling")
def verify_Desserts_category_is_accessble_via_scrolling(setup_platform):
    print("verify the Desserts category is accessible via scrolling")
    AndroidMenuScreen(setup_platform).verify_Desserts_category_is_accessble_via_scrolling()

@then("I verify the Fries & Sides category is accessible via scrolling")
@allure.step("Then I verify the Fries & Sides category is accessible via scrolling")
def verify_Fries_category_is_accessble_via_scrolling(setup_platform):
    print("verify the Fries & Sides category is accessible via scrolling")
    AndroidMenuScreen(setup_platform).verify_Fries_category_is_accessble_via_scrolling()

@then("I verify the cart icon does not appear on the homepage if the cart is empty")
@allure.step("Then I verify the cart icon does not appear on the homepage if the cart is empty")
def verify_cart_icon_does_not_appear_if_cart_is_empty(setup_platform):
    print("verify the cart icon does not appear on the homepage if the cart is empty")
    AndroidHomeScreen(setup_platform).verify_cart_icon_does_not_appear_if_cart_is_empty()

@when("I checks the price breakdown on the right side of the page")
@allure.step("When I checks the price breakdown on the right side of the page")
def verify_prices_breakdown_in_order_summary(setup_platform):
    print("checks the price breakdown on the right side of the page")
    AndroidViewCartScreen(setup_platform).verify_prices_breakdown_in_order_summary()

@then("I verify the subtotal, handling charges, CGST, and SGST should be displayed and match the total payable amount")
@allure.step("Then I verify the subtotal, handling charges, CGST, and SGST should be displayed and match the total payable amount")
def verify_display_of_charges_and_total_amount_in_order_summary(setup_platform):
    print("verify the subtotal, handling charges, CGST, and SGST should be displayed and match the total payable amount")
    AndroidViewCartScreen(setup_platform).verify_display_of_charges_and_total_amount_in_order_summary()

@when("I click on 'Add Delivery Instructions'")
@allure.step("When I click on 'Add Delivery Instructions'")
def click_add_delivery_instructions(setup_platform):
    print("click on 'Add Delivery Instructions'")
    AndroidViewCartScreen(setup_platform).scroll_to_add_delivery_instructions_and_click()

@when("I enters special notes in the instructions field")
@allure.step("When I enters special notes in the instructions field")
def enter_notes_in_instructions_field(setup_platform):
    print("enters special notes in the instructions field")
    AndroidViewCartScreen(setup_platform).enter_notes_in_instructions_field()

@then("I verify the instructions field should accept the input")
@allure.step("Then I verify the instructions field should accept the input")
def verify_instructions_field_input(setup_platform):
    print("verify the instructions field should accept the input")
    AndroidViewCartScreen(setup_platform).verify_instructions_field_input()

@then("I verify subtotal for a single added item")
@allure.step("When I verify subtotal for a single added item")
def verify_sub_total_for_single_added_item(setup_platform):
    print("verify subtotal for a single added item")
    AndroidViewCartScreen(setup_platform).verify_sub_total_for_single_added_item()

@when("I add item from recommendation")
@allure.step("When I add item from recommendation")
def add_item_from_recommendation(setup_platform):
    print("add item from recommendation")
    AndroidViewCartScreen(setup_platform).add_item_from_recommendation()

@then("I verify subtotal for all added items")
@allure.step("When I verify subtotal for all added items")
def verify_sub_total_for_all_added_item(setup_platform):
    print("verify subtotal for all added items")
    AndroidViewCartScreen(setup_platform).verify_sub_total_for_all_added_item()

@when("I Check CGST and SGST breakdown")
@allure.step("When I Check CGST and SGST breakdown")
def verify_cgst_and_sgst_breakdown_in_order_summary(setup_platform):
    print("Check CGST and SGST breakdown")
    AndroidViewCartScreen(setup_platform).verify_cgst_and_sgst_breakdown_in_order_summary()

@then("I verify tax percentage should be calculated accurately")
@allure.step("When I verify tax percentage should be calculated accurately")
def verify_tax_percentage_calculation(setup_platform):
    print("verify tax percentage should be calculated accurately")
    AndroidViewCartScreen(setup_platform).verify_tax_percentage_calculation()

@when("I click on 'Know More' link")
@allure.step("When I click on 'Know More' link")
def click_know_more_link(setup_platform):
    print("click on 'Know More' link")
    AndroidViewCartScreen(setup_platform).click_know_more_link()

@then("I verify Info opens about the charity")
@allure.step("When I verify Info opens about the charity")
def verify_charity_info_pop_up(setup_platform):
    print("verify Info opens about the charity")
    AndroidViewCartScreen(setup_platform).verify_charity_info_pop_up()

@when("I clicks the charity donation checkbox to opt-in")
@allure.step("When I clicks the charity donation checkbox to opt-in")
def click_charity_checkbox(setup_platform):
    print("clicks the charity donation checkbox to opt-in")
    AndroidViewCartScreen(setup_platform).verify_charity_checkbox_is_selected()

@then("I verify ₹3 should be added to the total payable amount")
@allure.step("When I verify ₹3 should be added to the total payable amount")
def verify_Donation_amount_added_in_payable_amount(setup_platform):
    print("verify ₹3 should be added to the total payable amount")
    AndroidViewCartScreen(setup_platform).verify_Donation_amount_added_in_payable_amount()


@when("I unchecks the charity donation checkbox")
@allure.step("When I unchecks the charity donation checkbox")
def uncheck_charity_checkbox(setup_platform):
    print("unchecks the charity donation checkbox")
    AndroidViewCartScreen(setup_platform).uncheck_charity_checkbox()

@then("I verify ₹3 should be removed from the total payable amount")
@allure.step("Then I verify ₹3 should be removed from the total payable amount")
def verify_donation_amount_removed_from_payable_amount(setup_platform):
    print("verify ₹3 should be removed from the total payable amount")
    AndroidViewCartScreen(setup_platform).verify_donation_amount_removed_from_payable_amount()

@when("I click on 'View All' link")
@allure.step("When I click on 'View All' link")
def click_view_all_link(setup_platform):
    print("click on 'View All' link")
    AndroidViewCartScreen(setup_platform).click_view_all_link()

@then("I verify the user should be redirected to a page displaying all available offers")
@allure.step("Then I verify the user should be redirected to a page displaying all available offers")
def verify_user_redirected_to_offers_page(setup_platform):
    print("verify the user should be redirected to a page displaying all available offers")
    AndroidOfferPage(setup_platform).verify_user_redirected_to_offers_page()

@when("I reviews all prices in the order summary")
@allure.step("When I reviews all prices in the order summary")
def review_prices_in_order_summary(setup_platform):
    print("reviews all prices in the order summary")
    AndroidViewCartScreen(setup_platform).verify_prices_breakdown_in_order_summary()

@then("I verify each price should be prefixed with the ₹ symbol")
@allure.step("Then I verify each price should be prefixed with the ₹ symbol")
def verify_all_prices_prefixed_with_currency_symbol(setup_platform):
    print("verify each price should be prefixed with the ₹ symbol")
    AndroidViewCartScreen(setup_platform).verify_all_prices_prefixed_with_currency_symbol()

@then("I verify the estimated delivery time displayed below the delivery address")
@allure.step("Then I verify the estimated delivery time displayed below the delivery address")
def verify_estimated_delivery_time(setup_platform):
    print("verify the estimated delivery time displayed below the delivery address")
    AndroidViewCartScreen(setup_platform).verify_estimated_delivery_time()

@then("I click back button")
@allure.step("Then I click back button")
def Click_back_button(setup_platform):
    print("click back button")
    AndroidViewCartScreen(setup_platform).Click_back_button()

@then("I verify the cart should retain the previously added items")
@allure.step("Then I verify the cart should retain the previously added items")
def cart_retained_the_previously_added_item(setup_platform):
    print("verify the cart should retain the previously added items")
    AndroidViewCartScreen(setup_platform).Verify_single_item_in_cart()

@when("I apply multiple promo codes")
@allure.step("When I apply multiple promo codes")
def verify_coupon_switch(setup_platform):
    print("apply multiple promo codes")
    AndroidOfferPage(setup_platform).verify_coupon_switch()

@then("I verify only one code applied at a time")
@allure.step("Then I verify only one code applied at a time")
def verify_applied_offer_and_click_change_offer(setup_platform):
    print("verify only one code applied at a time")
    AndroidViewCartScreen(setup_platform).verify_first_offer_is_removed_and_the_second_offer_is_displayed()

@when("I apply the second promo code")
@allure.step("When I apply the second promo code")
def Select_second_promo_code(setup_platform):
    print("apply the second promo code")
    AndroidOfferPage(setup_platform).Select_second_promo_code()

@then("I verify that the first offer is removed and the second offer is displayed")
@allure.step("When I verify that the first offer is removed and the second offer is displayed")
def verify_first_offer_is_removed_and_the_second_offer_is_displayed(setup_platform):
    print("verify that the first offer is removed and the second offer is displayed")
    AndroidViewCartScreen(setup_platform).verify_first_offer_is_removed_and_the_second_offer_is_displayed()

@then("I verify the discount should be clearly shown and deducted in the order summary")
@allure.step("When I verify the discount should be clearly shown and deducted in the order summary")
def verify_discount_prices_in_order_summary(setup_platform):
    print("verify the discount should be clearly shown and deducted in the order summary")
    AndroidViewCartScreen(setup_platform).verify_discount_is_applied_correctly()




    





    