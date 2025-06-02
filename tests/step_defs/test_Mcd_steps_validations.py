from pytest_bdd.parsers import parse
from pytest_bdd import given, when, then, scenarios
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.view_page import ViewPage
from pages.profile_page import ProfilePage
from pages.address_page import AddressPage
from pages.view_cart_page import ViewCartPage
from pages.juspay_page import JuspayPage
from conftest import readPreReqJson
from selenium.webdriver.common.keys import Keys
import pyperclip
import allure

scenarios('../features/Mcd_Test_Cases.feature')


@given("I open the Chrome browser")
@allure.step('Given I open the Chrome browser')
def open_the_chrome_browser(setup_platform):
    print("Launch Chrome Browser")


@when(parse("I launch {appURL}"))
@allure.step('When I launch {appURL}')
def i_lanuch_appurl(setup_platform, appURL):
    BasePage(setup_platform).launch_application(appURL)

@when("I hit the URL")
@allure.step('When I hit the URL')
def hit_the_url(setup_platform):
    BasePage(setup_platform).open_mcd_website()


@then("I verify website opened successfully")
@allure.step("Then I verify website opened successfully")
def verify_website_oopened_successfully(setup_platform):
    print("Verifying McD Website")
    Is_Website_Opened = HomePage(setup_platform).verify_website_header_banner()
    assert Is_Website_Opened, "Web Application Is Not Opened As Expected"


@when("I click on view icon")
@allure.step("When I click on view icon")
def click_on_view_icon(setup_platform):
    print("Clicking on view Icon")
    HomePage(setup_platform).click_on_view_icon()


@then("I verify view page navigation")
@allure.step("Then I verify view page navigation")
def verify_view_page_navigation(setup_platform):
    print("Verifying View Page")
    View_Page = ViewPage(setup_platform).verify_view_page_is_reached()
    assert View_Page, "View Page Is Not Reached After Clicking On View Icon In Home Page"


@when("I click on login or signup button")
@allure.step("When I click on login or signup button")
def click_on_login_or_sign_up_button(setup_platform):
    print("Clicking on Login/Sign Up Button")
    ViewPage(setup_platform).click_on_login_or_sign_up_button()


@then("I verify login page navigation")
@allure.step("Then I verify login page navigation")
def verify_login_page_navigation(setup_platform):
    print("Verifying Login Page Navigation")
    Login_Page = LoginPage(setup_platform).verify_login_page_reached()
    assert Login_Page, "Login Page Is Not Reached After Clicking On Login Button In View Page"


@when("I enter a valid mobile number and click verify")
@allure.step("When I enter a valid mobile number and click verify")
def enter_a_valid_mobile_number_and_click_verify(setup_platform):
    mobile_number = readPreReqJson("test_data", "mobile_number")
    print("Entering Mobie Number")
    LoginPage(setup_platform).enter_mobile_number(mobile_number)


@when("I enter the OTP and click verify")
@allure.step("When I enter the OTP and click verify")
def enter_the_otp_and_click_verify(setup_platform):
    otp = readPreReqJson("test_data", "OTP")
    print("Entering OTP")
    LoginPage(setup_platform).enter_otp(otp)

@then('I verify home page navigation')
@allure.step("Then I verify home page navigation")
def verify_home_page_navigation(setup_platform):
    print("Verifying Home Page Navigation")
    Home_Page = HomePage(setup_platform).verify_website_header_banner()
    assert Home_Page, "Home Page Is Not Reached After Logged In"

@when("I leave mobile field empty and click verify")
@allure.step("When I leave mobile field empty and click verify")
def leave_mobile_field_empty_and_click_verify(setup_platform):
    print("Please enter Mobile number")
    LoginPage(setup_platform).leave_mobile_field_empty()

@when("I enter a mobile number with less than 10 digits and click verify")
@allure.step("When I enter a mobile number with less than 10 digits and click verify")
def enter_a_invalid_mobile_number_and_click_verify(setup_platform):
    invalid_mobile_number = readPreReqJson("test_data", "invalid_mobile_number")
    print("Entering invalid Mobile Number")
    LoginPage(setup_platform).enter_invalid_mobile_number(invalid_mobile_number)

@then('I verify error message')
@allure.step("Then I verify error message")
def verify_error_message(setup_platform):
    print("Verifying error message")
    Login_Page = LoginPage(setup_platform).mobile_field_empty_error()
    assert Login_Page, "Please enter valid mobile number"

@when("I enter alphabets in mobile number field and click verify")
@allure.step("When I enter alphabets in mobile number field and click verify")
def enter_alphabets_in_mobile_number_field_and_click_verify(setup_platform):
    alphabets_in_mobile_number = readPreReqJson("test_data", "alphabets_in_mobile_number")
    print("Entering alphabets in Mobie Number field")
    LoginPage(setup_platform).enter_alphabets_in_mobile_text_field(alphabets_in_mobile_number)

@when("I enter mobile number with spaces and click verify")
@allure.step("When I enter mobile number with spaces and click verify")
def enter_mobile_number_with_space_and_click_verify(setup_platform):
    mobile_number_with_space = readPreReqJson("test_data", "mobile_number_with_space")
    print("Entering mobile number with spaces")
    LoginPage(setup_platform).enter_mobile_number_with_space(mobile_number_with_space)

@when("I enter mobile number with spacial characters and click verify")
@allure.step("When I enter mobile number with spacial characters and click verify")
def enter_mobile_number_with_special_char_and_click_verify(setup_platform):
    special_characters_in_mobile_field = readPreReqJson("test_data", "special_characters_in_mobile_field")
    print("Entering mobile number with special characters")
    LoginPage(setup_platform).enter_mobile_number_with_space(special_characters_in_mobile_field)

@when("I click on referral link")
@allure.step("When I click on referral link")
def click_on_referral_link(setup_platform):
    print("Clicking on referral link")
    LoginPage(setup_platform).click_referral_code_link()

@then('I verify referral link is clickable')
@allure.step("Then I verify referral link is clickable")
def verify_referral_link_clickable(setup_platform):
    print("Verifying referral link is clickable")
    Is_referral_link_clickable = LoginPage(setup_platform).verify_referral_text_field_is_displayed()
    assert Is_referral_link_clickable, "Referral link is not opened as expected"

@when("I enter referral code")
@allure.step("When I enter referral code")
def enter_referral_code(setup_platform):
    Referral_code = readPreReqJson("test_data", "Referral_code")
    print(f"Entering referral code: {Referral_code}")
    LoginPage(setup_platform).enter_referral_code(Referral_code)

@when("I enter referral code and click verify")
@allure.step("When I enter referral code and click verify")
def enter_referral_code_and_verify(setup_platform):
    Referral_code = readPreReqJson("test_data", "Referral_code")
    print(f"Entering referral code: {Referral_code}")
    LoginPage(setup_platform).enter_referral_code_click_verify(Referral_code)

@then('I verify referral code accepted without error')
@allure.step("Then I verify referral code accepted without error")
def verify_referral_code_accepted(setup_platform):
    print("Verifying that the referral code was accepted")
    result = LoginPage(setup_platform).is_referral_code_accepted()
    assert result, "Referral code was not accepted or an error appeared"

@when("I click on verify mobile button without mobile number entered")
@allure.step("When I click on verify mobile button without mobile number entered")
def click_on_verify_mobile_initially_disabled(setup_platform):
    print("Validate verify mobile is disabled initially ")
    LoginPage(setup_platform).click_verify_mobile_button_without_entering_mobile_number()

@then("I verify OTP page navigation")
@allure.step("Then I verify OTP page navigation")
def verify_otp_page_navigation(setup_platform):
    print("Verify otp page navigation")
    Otp_page_navigation = LoginPage(setup_platform).verify_otp_page_is_displayed()
    assert Otp_page_navigation, "otp page Is Not navigated successfully As Expected"

@when("I click terms and conditions link")
@allure.step("When I click terms and conditions link")
def click_terms_and_conditions_link(setup_platform):
    print("Verify terms and conditions link is clickable ")
    LoginPage(setup_platform).click_terms_and_conditions_link()

@then("I verify user is redirected to terms and conditions page")
@allure.step("Then I verify user is redirected to terms and conditions page")
def verify_terms_and_conditions_navigation(setup_platform):
    print("Verify user is redirected to terms and conditions page")
    Terms_and_conditions_navigation = LoginPage(setup_platform).verify_terms_and_conditions_header()
    assert Terms_and_conditions_navigation, "terms and conditions Is Not navigated successfully As Expected"

@then("I verify mobile number accepted and redirected to next page")
@allure.step("Then I verify mobile number accepted and redirected to next page")
def verify_next_page_navigation(setup_platform):
    print("verify mobile number accepted and redirected to next page")
    Next_page_navigation = LoginPage(setup_platform).verify_otp_page_is_displayed()
    assert Next_page_navigation, "Next page is Not navigated successfully As Expected"

@when("I enter 11 digits mobile number and click verify")
@allure.step("When I enter 11 digits mobile number and click verify")
def enter_11_digits_mobile_number(setup_platform):
    Mobile_number_11_digits = readPreReqJson("test_data", "mobile_number_11_digits")
    print(f"Typing mobile number: {Mobile_number_11_digits} one digit at a time")
    LoginPage(setup_platform).enter_mobile_number_one_by_one(Mobile_number_11_digits)

@when("I enter more than 10 digits mobile number and click verify")
@allure.step("When I enter more than 10 digits mobile number and click verify")
def enter_more_than_10_digits_mobile_number(setup_platform):
    Mobile_number_more_than_10_digits = readPreReqJson("test_data", "mobile_number_11_digits")
    print(f"Typing mobile number: {Mobile_number_more_than_10_digits} one digit at a time")
    LoginPage(setup_platform).enter_mobile_number_one_by_one(Mobile_number_more_than_10_digits)

@then("I verify field should restrict to 10 digits")
@allure.step("Then I verify field should restrict to 10 digits")
def verify_field_restricts_to_10_digits(setup_platform):
    print("Verifying that the mobile number input field restricts to 10 digits")
    login_page = LoginPage(setup_platform)
    entered_number = login_page.get_entered_mobile_number()
    print(f"Fetched number from input field: '{entered_number}'")
    assert len(entered_number) == 10, f"Expected 10 digits, but got '{entered_number}' with length {len(entered_number)}"


@when("I copied a mobile number")
@allure.step("When I copied a mobile number")
def copy_mobile_number(setup_platform):
     Copied_number = readPreReqJson("test_data", "mobile_number")
     print("verify mobile number copied")
     LoginPage(setup_platform).copy_mobile_number_to_clipboard(Copied_number)

@when("I paste the number with Ctrl V and click verify")
@allure.step("When I paste the number with Ctrl V and click verify")
def paste_copied_mobile_number(setup_platform):
    print("Pasting mobile number using Ctrl+V")
    LoginPage(setup_platform).paste_mobile_number_using_ctrl_v()

@then("I verify number pasted correctly and accepted")
@allure.step("Then I verify number pasted correctly and accepted")
def verify_number_pasted_correctly(setup_platform):
    print("Verifying that the pasted number was accepted correctly")

    expected_number = readPreReqJson("test_data", "mobile_number")
    actual_number = LoginPage(setup_platform).get_pasted_mobile_number()

    print(f"Expected Mobile Number: {expected_number}")
    print(f"Actual Mobile Number in Field: {actual_number}")

    assert actual_number == expected_number, "Pasted mobile number does not match or was not accepted"

@when('I visually inspect the mobile number field')
@allure.step("When I visually inspect the mobile number field")
def inspect_mobile_field(setup_platform):
    print("Visually inspect the mobile number field")
    Login_Page = LoginPage(setup_platform).inspect_mobile_field()
    assert Login_Page, "Mobile number field not visible"

@when('I visually inspect the referral link section')
@allure.step("When I visually inspect the referral link section")
def inspect_referral_link(setup_platform):
    print("Visually inspect the mobile number field")
    Login_Page = LoginPage(setup_platform).inspect_referral_link()
    assert Login_Page, "Referral link not visible"

@when('I visually inspect the verify button')
@allure.step("When I visually inspect the verify button")
def inspect_verify_button(setup_platform):
    print("Visually inspect the mobile number field")
    Login_Page = LoginPage(setup_platform).inspect_verify_button()
    assert Login_Page, "Verify button not visible"

@when('I visually inspect the footer links')
@allure.step("When I visually inspect the footer links")
def inspect_footer_link(setup_platform):
    print("Visually inspect the mobile number field")
    Login_Page = LoginPage(setup_platform).inspect_footer_link()
    assert Login_Page, "Footer links not visible"

def is_overlapping_js(driver, el1, el2):
    script = """
    const r1 = arguments[0].getBoundingClientRect();
    const r2 = arguments[1].getBoundingClientRect();
    return !(r1.right <= r2.left ||
             r1.left >= r2.right ||
             r1.bottom <= r2.top ||
             r1.top >= r2.bottom);
    """
    return driver.execute_script(script, el1, el2)

@then("I verify all elements should be visible, correctly aligned, and not overlapping")
@allure.step("Then I verify all elements should be visible, correctly aligned, and not overlapping")
def step_validate_alignment(setup_platform):
    print("Validating visibility, alignment, and non-overlapping of UI elements")

    login_page = LoginPage(setup_platform)

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

@when("I click on user profile icon")
@allure.step("When I click on user profile icon")
def click_on_profile_icon(setup_platform):
    print("Clicking on user profile icon")
    ProfilePage(setup_platform).click_user_profile_icon()

@then('I verify profile page navigation')
@allure.step("Then I verify profile page navigation")
def verify_profile_page_navigation(setup_platform):
    print("Verifying Profile Page Navigation")
    Profile_Page = ProfilePage(setup_platform).verify_profile_page_navigation()
    assert Profile_Page, "Profile Page Is Not navigated"

@when("I click on edit profile icon")
@allure.step("When I click on edit profile icon")
def click_on_edit_profile_icon(setup_platform):
    print("Clicking on edit profile icon")
    ProfilePage(setup_platform).click_edit_profile_icon()

@then("I verify user is on the profile edit page")
@allure.step("Then I verify user is on the profile edit page")
def profile_edit_page(setup_platform):
    print("verify user is on the profile edit page")
    Profile_Page = ProfilePage(setup_platform).verify_profile_edit_page()
    assert Profile_Page, "The user is not navigated to profile edit page"

@when("I edits the full name field with Test User01 and clicks Save Changes")
@allure.step("When I edits the full name field with Test User01 and clicks Save Changes")
def edit_name_and_click_save(setup_platform):
    print("verify edits the full name field with Test User01 and clicks Save Changes")
    ProfilePage(setup_platform).edit_profile_name()

@then("I verify updated name should be reflected on the profile")
@allure.step("Then I verify updated name should be reflected on the profile")
def profile_updated_name_display(setup_platform):
    updated_name = ProfilePage(setup_platform).updated_profile_name()
    print(f"Updated name found: {updated_name}")
    assert updated_name == "Test User01", f"The updated name was expected to be 'Test User01', but got '{updated_name}'"

@when("I clear name field")
@allure.step("When I clear name field")
def Clear_name_field(setup_platform):
    print("verify clearing the name field")
    ProfilePage(setup_platform).clear_profile_name_field()

@then('I verify error message Please enter valid full name should be displayed')
@allure.step("Then I verify error message Please enter valid full name should be displayed")
def verify_profile_name_field_error_message(setup_platform):
    print("Verifying error message Please enter valid full name should be displayed")
    Profile_Page = ProfilePage(setup_platform).profile_name_field_empty_error()
    assert Profile_Page, "Please enter valid full name"

@when("I enter invalid characters in name field")
@allure.step("When I enter invalid characters in name field")
def enter_invalid_char_in_name_field(setup_platform):
    print("verify entering invalid characters in name field")
    ProfilePage(setup_platform).enter_invalid_char_in_name_field()


@when("I edits email address and clicks Save Changes")
@allure.step("When I edits email address and clicks Save Changes")
def edit_email_address_and_click_save(setup_platform):
    print("verify edits email address and clicks Save Changes")
    ProfilePage(setup_platform).edit_email_address()

@then("I verify updated email address should be reflected on the profile")
@allure.step("Then I verify updated email address should be reflected on the profile")
def profile_updated_email_display(setup_platform):
    updated_email = ProfilePage(setup_platform).updated_email_address()
    print(f"Updated name found: {updated_email}")
    assert updated_email == "testuser11@gmail.com", f"The updated email was expected to be 'testuser11@gmail.com', but got '{updated_email}'"

@when("I enter incorrect email format in email field")
@allure.step("When I enter incorrect email format in email field")
def enter_incorrect_email_in_email_field(setup_platform):
    print("verify entering an incorrect email format in email field")
    ProfilePage(setup_platform).enter_incorrect_email_format_in_email_field()

@then('I verify error message enter valid email address should be displayed')
@allure.step("Then I verify error message enter valid email address should be displayed")
def verify_incorrect_email_error(setup_platform):
    print("Verifying error message enter valid email address should be displayed")
    Profile_Page = ProfilePage(setup_platform).incorrect_email_error()
    assert Profile_Page, "Please enter valid email address"

@when("I selects a new valid date of birth and clicks Save Changes")
@allure.step("When I selects a new valid date of birth and clicks Save Changes")
def edit_date_of_birth_and_click_save(setup_platform):
    print("verify selecting a new valid date of birth and clicks Save Changes")
    ProfilePage(setup_platform).edit_date_of_birth()

@then('I verify updated date of birth should be reflected on the profile')
@allure.step("Then I verify updated date of birth should be reflected on the profile")
def verify__updated_date_of_birth(setup_platform):
    updated_date_of_birth = ProfilePage(setup_platform).updated_date_of_birth()
    print(f"Updated name found: {updated_date_of_birth}")
    assert updated_date_of_birth == "20/05/2025", f"The updated date of birth was expected to be '20/05/2025', but got '{updated_date_of_birth}'"

@when("I enter a future date in the date of birth field")
@allure.step("When I enter a future date in the date of birth field")
def enter_future_date_of_birth(setup_platform):
    print("verify entering a future date in the date of birth field")
    ProfilePage(setup_platform).enter_future_date_of_birth()

@then('I verify user are unable to select future Date of birth')
@allure.step("Then I verify user are unable to select future Date of birth")
def verify_future_dob_disabled(setup_platform):
    print("Verifying user are unable to select future Date of birth")
    Profile_Page = ProfilePage(setup_platform).verify_future_dob_disabled()
    assert Profile_Page, "future date should not be selectable"

@when("I click change picture link")
@allure.step("When I click change picture link")
def click_change_picture_link(setup_platform):
    print("verify clicking change picture link")
    ProfilePage(setup_platform).click_change_picture_link()

@then('I verify upload pop up opens with file selection option')
@allure.step("Then I verify upload pop up opens with file selection option")
def verify_upload_file_pop_up(setup_platform):
    print("Verifying upload pop up opens with file selection option")
    Profile_Page = ProfilePage(setup_platform).verify_file_upload_pop_up()
    assert Profile_Page, "File upload pop up should not be displayed"

@then('I verify the Save button should be disabled')
@allure.step("Then I verify the Save button should be disabled")
def verify_save_button_disabled(setup_platform):
    print("Verifying the Save button should be disabled")
    is_disabled = ProfilePage(setup_platform).check_save_changes_button_disabled()
    assert is_disabled, "The save button should be disabled"

@when("I Check icon presence near each field")
@allure.step("When I Check icon presence near each field")
def check_icons_presence(setup_platform):
    print("verify Checking icon presence near each field")
    ProfilePage(setup_platform).check_icon_presence_near_each_field()

@then('I verify the Correct icons for name, phone, email, DOB')
@allure.step("Then I verify the Correct icons for name, phone, email, DOB")
def verify_correct_icons(setup_platform):
    print("Verifying the Correct icons for name, phone, email, DOB")
    ProfilePage(setup_platform).verify_correct_icons()

@when("I switch toggle on/off and observe UI")
@allure.step("When I switch toggle on/off and observe UI")
def check_switch_toggle(setup_platform):
    print("verify switch toggle on/off and observe UI")
    ProfilePage(setup_platform).switch_toggle_button()

@then('I verify Color scheme updates to accessible version page should be displayed')
@allure.step("Then I verify Color scheme updates to accessible version page should be displayed")
def verify_color_scheme(setup_platform):
    print("Verifying Color scheme updates to accessible version page should be displayed")
    Profile_Page = ProfilePage(setup_platform).color_scheme()
    assert Profile_Page, "The color scheme should be displayed"

@when("I switch toggle to make color blind mode on and reload page")
@allure.step("When I switch toggle to make color blind mode on and reload page")
def switch_toggle_to_On_and_reload(setup_platform):
    print("verify switch toggle to make color blind mode on and reload page")
    ProfilePage(setup_platform).color_blind_mode_On_and_reload_page()

@then('I verify preference retained after refresh')
@allure.step("Then I verify preference retained after refresh")
def verify_preference_retained_after_refresh(setup_platform):
    print("Verifying preference retained after refresh")
    Profile_Page = ProfilePage(setup_platform).verify_color_blind_preference_retained()
    assert Profile_Page, "The color scheme should not be displayed"

@when("I make changes and refresh browser")
@allure.step("When I make changes and refresh browser")
def make_changes_and_refresh_page(setup_platform, user_data_store):
    print("verify make changes and refresh browser")
    ProfilePage(setup_platform).make_changes_and_refresh_page(user_data_store)


@then('I verify page reloads with old saved data')
def step_verify_old_data_loaded_after_refresh(setup_platform, user_data_store):
    print("Verifying page reloads with old saved data")
    ProfilePage(setup_platform).verify_data_is_not_saved_after_refresh(user_data_store)
    

@when("I click on any item to add into a cart")

def step_click_add_item(setup_platform):
    ProfilePage(setup_platform).add_item_in_cart()

@then("I verify items details pop up opened successfully")
def step_verify_item_popup(setup_platform):
    assert ProfilePage(setup_platform).verify_items_details_popup(), "Item detail popup not displayed"


@when("I click on next")
def step_click_next(setup_platform):
    ProfilePage(setup_platform).click_next_button()

@when("I click on Add to cart option")
def step_click_add_to_cart(setup_platform):
    ProfilePage(setup_platform).click_add_to_cart()

@then("I verify selected item get added into a cart")
def step_verify_cart(setup_platform):
    ProfilePage(setup_platform).verify_item_added_in_cart()

@when("I click on add address")
def step_click_add_address(setup_platform):
    ProfilePage(setup_platform).click_add_address_arrow()

@then("I verify user redirected to login/signup prompt")
def step_verify_login_prompt(setup_platform):
    assert ProfilePage(setup_platform).verify_redirect_to_login_or_signup_page(), "Login prompt not displayed"

