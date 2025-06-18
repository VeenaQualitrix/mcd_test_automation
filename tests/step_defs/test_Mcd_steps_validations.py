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

@when("I click save changes on profile details page")
@allure.step("When I eclick save changes on profile details page")
def lick_save_changes_on_profile_page(setup_platform):
    print("click save changes on profile details page")
    ProfilePage(setup_platform).Click_save_changes_on_profile_details_page()

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
@allure.step("When I verify page reloads with old saved data")
def step_verify_old_data_loaded_after_refresh(setup_platform, user_data_store):
    print("Verifying page reloads with old saved data")
    ProfilePage(setup_platform).verify_data_is_not_saved_after_refresh(user_data_store)
    

@when("I click on any item to add into a cart")
@allure.step("When I click on any item to add into a cart")
def step_click_add_item(setup_platform):
    AddressPage(setup_platform).add_item_in_cart()

@then("I verify items details pop up opened successfully")
@allure.step("When I verify items details pop up opened successfully")
def step_verify_item_popup(setup_platform):
    assert AddressPage(setup_platform).verify_items_details_popup(), "Item detail popup not displayed"

@when("I click on next")
@allure.step("When I click on next")
def step_click_next(setup_platform):
    AddressPage(setup_platform).click_next_button()

@when("I click on Add to cart option")
@allure.step("When I click on Add to cart option")
def step_click_add_to_cart(setup_platform):
    AddressPage(setup_platform).click_add_to_cart()

@then("I verify selected item get added into a cart")
@allure.step("When I verify selected item get added into a cart")
def step_verify_cart(setup_platform):
    AddressPage(setup_platform).verify_item_added_in_cart()

@when("I click on add address in home page")
@allure.step("When I click on add address in home page")
def click_on_add_address_in_home_page(setup_platform):
    print("Clicking On Add Address In Home Page")
    HomePage(setup_platform).click_on_add_address()

@then("I verify user redirected to login/signup prompt")
@allure.step("When I verify user redirected to login/signup prompt")
def step_verify_login_prompt(setup_platform):
    assert AddressPage(setup_platform).verify_redirect_to_login_or_signup_page(), "Login prompt not displayed"

@when("I click on login/signup prompt")
@allure.step("When I click on login/signup prompt")
def click_login_prompt(setup_platform):
    AddressPage(setup_platform).Click_login_prompt()

@when("I click on login/signup prompt from checkout")
@allure.step("When I click on login/signup prompt from checkout")
def click_login_prompt_from_checkout(setup_platform):
    AddressPage(setup_platform).Click_login_prompt_from_checkout()

@then("I verify login page navigation from checkout page")
@allure.step("When I verify login page navigation from checkout page")
def verify_login_page_navigation_from_checkout(setup_platform):
    assert AddressPage(setup_platform).verify_login_page_navigation_from_checkout(), "Login page not navigated from checkout page"

@when("I click on cancel button from login/signup pop up")
@allure.step("When I click on cancel button from login/signup pop up")
def click_cancel_from_login_prompt(setup_platform):
    AddressPage(setup_platform).click_cancel_to_login_or_signup_page()

@then("I verify Login cancelled and user returned to checkout page")
@allure.step("When I verify Login cancelled and user returned to checkout page")
def verify_login_cancelled_and_redirect_to_checkout(setup_platform):
    assert AddressPage(setup_platform).verify_redirect_to_checkout_page(), "Checkout page not displayed"

@when("I enter incorrect number in mobile number field and click verify")
@allure.step("When I enter incorrect number in mobile number field and click verify")
def enter_incorrect_mobile_number(setup_platform):
    AddressPage(setup_platform).enter_incorrect_mobile_number()

@when("I click on add address from checkout page")
@allure.step("When I click on add address from checkout page")
def click_add_address_from_checkout(setup_platform):
    AddressPage(setup_platform).click_add_address_from_checkout()

@when("I click on add new button and search for location")
@allure.step("When I click on add new button and search for location")
def click_on_add_new_button_and_search_for_location(setup_platform):
    print("Searching For Location To Add new Location")
    AddressPage(setup_platform).search_for_new_address()


@when("I select address from search results")
@allure.step("When I select address from search results")
def select_address_from_search_results(setup_platform):
    print("Selecting Address From Search Results")
    AddressPage(setup_platform).select_address_from_search_results()


@then("I verify address is added and selected")
@allure.step("Then I verify address is added and selected")
def verify_address_is_added_and_selected(setup_platform):
    print("Verifying Address Is Added And Selected")
    Address_Added = AddressPage(setup_platform).verify_address_is_added_and_selected()
    assert Address_Added, "Address Is Not Added And Selected From The List Of Addresses"

@then("I verify the address should appear as the selected delivery address")
@allure.step("Then I verify the address should appear as the selected delivery address")
def verify_address_appear_as_selected_delivery_address(setup_platform):
    print("Verifying the address should appear as the selected delivery address")
    AddressPage(setup_platform).verify_address_appear_as_selected_delivery_address()


@when("I click on add new button and click confirm location")
@allure.step("When I click on add new button and click confirm location")
def click_add_new_and_confirm_location(setup_platform):
    print("clicking on add new button and click confirm location")
    AddressPage(setup_platform).Click_add_new_button_and_confirm_location()


@then("I verify user redirected to address fill in details page")
@allure.step("Then I verify user redirected to address fill in details page")
def verify_user_redirected_to_address_filling_page(setup_platform):
    print("Verifying user redirected to address fill in details page")
    Address_Page = AddressPage(setup_platform).verify_redirect_to_address_filling_page()
    assert Address_Page, "Address filling details page is not displayed"

@when("I leave mandatory field empty and click save address")
@allure.step("When I leave mandatory field empty and click save address")
def click_add_new_and_confirm_location(setup_platform):
    print("leave mandatory field empty and click save address")
    AddressPage(setup_platform).verify_leave_address_mandatory_field_empty()


@then("I verify that the address not saved and validation error should be displayed")
@allure.step("Then I verify that the address not saved and validation error should be displayed")
def verify_user_redirected_to_address_filling_page(setup_platform):
    print("Verifying that the address not saved and validation error should be displayed")
    Address_validation_error = AddressPage(setup_platform).verify_address_mandatory_field_empty_error()
    assert Address_validation_error, "Address validation error is not displayed"

@when("I enter special character in house/flat field and click save address")
@allure.step("When I enter special character in house/flat field and click save address")
def enter_special_char_in_house_field_and_saved(setup_platform):
    print("enter special character in house/flat field and click save address")
    AddressPage(setup_platform).enter_special_char_in_house_field()


@then("I verify field accept characters and address will get saved")
@allure.step("Then I verify field accept characters and address will get saved")
def verify_user_redirected_to_address_filling_page(setup_platform):
    print("Verifying field accept characters and address will get saved")
    Address_accept_special_char = AddressPage(setup_platform).verify_field_accept_special_char_and_address_saved()
    assert Address_accept_special_char, "Address does not accept special char and show validation error"

@then("I verify saved delivery address")
@allure.step("Then I verify saved delivery address")
def verify_saved_delivery_address(setup_platform, user_data_store):
    print("Verifying saved delivery address")
    AddressPage(setup_platform).verify_saved_delivery_address(user_data_store)

@when("I enter text in house/flat field and click back button without saving")
@allure.step("When I enter text in house/flat field and click back button without saving")
def enter_text_in_house_field_and_click_back_button(setup_platform):
    print("enter text in house/flat field and click back button without saving")
    AddressPage(setup_platform).enter_text_in_house_field_and_cancel_before_saving()


@then("I verify address will not get saved")
@allure.step("Then I verify address will not get saved")
def verify_address_not_saved(setup_platform, user_data_store):
    print("Verifying address will not get saved")
    AddressPage(setup_platform).verify_address_is_not_saved_when_click_back_button_without_saving(user_data_store)

@when("I enter text in house/flat field and click save address")
@allure.step("When I enter text in house/flat field and click save address")
def enter_text_in_house_field_and_click_save(setup_platform):
    print("enter text in house/flat field and click save address")
    AddressPage(setup_platform).enter_text_in_house_field_and_click_save()


@then("I verify System allows address duplication based on business logic")
@allure.step("Then I verify System allows address duplication based on business logic")
def verify_address_not_saved(setup_platform):
    print("Verifying  System allows address duplication based on business logic")
    AddressPage(setup_platform).verify_duplicate_address_saved()

@when("I click the business model dropdown")
@allure.step("When I click the business model dropdown")
def click_business_model_dropdown(setup_platform):
    print("click the business model dropdown")
    HomePage(setup_platform).Click_business_model_dropdown()


@then("I verify Dropdown shows: McDelivery, Dine-In, On the Go, Take Away")
@allure.step("Then I verify Dropdown shows: McDelivery, Dine-In, On the Go, Take Away")
def verify_dropdown_displays_all_business_model(setup_platform):
    print("Verifying Dropdown shows: McDelivery, Dine-In, On the Go, Take Away")
    HomePage(setup_platform).verify_dropdown_displays_all_business_model()

@when("I select the McDelivery option from dropdown")
@allure.step("When I select the McDelivery option from dropdown")
def select_McDelivery_from_dropdown(setup_platform):
    print("select the McDelivery option from dropdown")
    HomePage(setup_platform).verify_Selection_of_McDelivery_option_from_dropdown()


@then("I verify User is taken to the McDelivery ordering flow")
@allure.step("Then I verify User is taken to the McDelivery ordering flow")
def verify_redirection_to_McDelivery_ordering_flow(setup_platform):
    print("Verifying User is taken to the McDelivery ordering flow")
    HomePage(setup_platform).verify_user_redirect_to_McDelivery_ordering_flow()

@when("I select Dine-In option from dropdown")
@allure.step("When I select Dine-In option from dropdown")
def select_Dine_in_from_dropdown(setup_platform):
    print("select Dine-In option from dropdown")
    HomePage(setup_platform).verify_Selection_of_Dine_In_option_from_dropdown()


@then("I verify User navigates to Dine-In selection/location flow")
@allure.step("Then I verify User navigates to Dine-In selection/location flow")
def verify_redirection_to_Dine_in_location_flow(setup_platform):
    print("Verifying User navigates to Dine-In selection/location flow")
    HomePage(setup_platform).verify_user_redirect_to_Dine_In_location_flow()

@when("I select on the go option from dropdown")
@allure.step("When I select on the go option from dropdown")
def select_On_the_go_from_dropdown(setup_platform):
    print("select on the go option from dropdown")
    HomePage(setup_platform).verify_Selection_of_On_the_go_option_from_dropdown()


@then("I verify User is prompted to choose pick-up location")
@allure.step("Then I verify User is prompted to choose pick-up location")
def verify_redirection_to_On_the_go_pick_up_location_flow(setup_platform):
    print("Verifying User is prompted to choose pick-up location")
    HomePage(setup_platform).verify_user_redirect_to_On_the_go_pick_up_location_flow()

@when("I select Take Away option from dropdown")
@allure.step("When I select Take Away option from dropdown")
def select_take_away_from_dropdown(setup_platform):
    print("select Take Away option from dropdown")
    HomePage(setup_platform).verify_Selection_of_take_away_option_from_dropdown()


@then("I verify User proceeds to place an order for take away")
@allure.step("Then I verify User proceeds to place an order for take away")
def verify_redirection_to_take_away_location_flow(setup_platform):
    print("Verifying User proceeds to place an order for take away")
    HomePage(setup_platform).verify_user_redirect_to_take_away_location_flow()

@then("I verify “McDelivery” should be selected by default")
@allure.step("When I verify “McDelivery” should be selected by default")
def select_take_away_from_dropdown(setup_platform):
    print("Verify McDelivery should be selected by default")
    HomePage(setup_platform).verify_McDelivery_selected_by_default()

@when("I select a business model in an unsupported region")
@allure.step("When I select a business model in an unsupported region")
def select_business_model_in_unsupported_region(setup_platform):
    print("select a business model in an unsupported region")
    HomePage(setup_platform).verify_Selection_of_Dine_In_option_from_dropdown()


@then("I should see the message: “Sorry, we do not serve this location yet”")
@allure.step("Then I should see the message: “Sorry, we do not serve this location yet”")
def verify_toast_appear_for_unsupported_location(setup_platform):
    print("Verifying the message: “Sorry, we do not serve this location yet”")
    HomePage(setup_platform).show_toast()

@when("I select the first model")
@allure.step("When I select the first model")
def select_first_model(setup_platform):
    print("select the Dine In model")
    HomePage(setup_platform).step_select_first_model()

@when("I select the second model")
@allure.step("When I select the second model")
def select_second_model(setup_platform):
    print("select the Take away model")
    HomePage(setup_platform).step_select_second_model()


@then("I verify only one model should remain active at a time")
@allure.step("Then I verify only one model should remain active at a time")
def verify_active_model(setup_platform):
    print("Verifying only one model should remain active at a time")
    HomePage(setup_platform).step_check_only_one_active()

@when("I open a new tab in the same session")
@allure.step("When I open a new tab in the same session")
def open_new_tab(setup_platform):
    print("open a new tab in the same session")
    HomePage(setup_platform).open_new_tab()


@then("I verify the same business model should remain selected")
@allure.step("Then I verify the same business model should remain selected")
def verify_take_away_still_selected(setup_platform):
    print("Verifying the same business model should remain selected")
    HomePage(setup_platform).verify_take_away_option_is_still_selected()

@when("I hover over each business model option")
@allure.step("When I hover over each business model option")
def Hover_over_each_business_model(setup_platform):
    print("hover over each business model option")
    HomePage(setup_platform).verify_dropdown_displays_all_business_model()


@then("I verify the icons and text should respond visually")
@allure.step("Then I verify the icons and text should respond visually")
def verify_icons_and_text_repond_visually(setup_platform):
    print("Verifying the icons and text should respond visually")
    HomePage(setup_platform).verify_icons_and_text_display_on_each_business_model()

@then("I verify the user notes their current profile information")
@allure.step("Then I verify the user notes their current profile information")
def verify_current_profile_info(setup_platform, user_data_store):
    print("Verifying the user notes their current profile information")
    ProfilePage(setup_platform).Verify_current_profile_info(user_data_store)

@when("I verify user switches from one model to another")
@allure.step("When I verify user switches from one model to another")
def switch_between_business_model(setup_platform):
    print("Verify user switches from one model to another")
    HomePage(setup_platform).verify_switching_from_one_model_to_another()

@when("I verify user navigates to the profile page")
@allure.step("When I verify user navigates to the profile page")
def verify_user_navigates_to_profile_page(setup_platform):
    print("verify user navigates to the profile page")
    ProfilePage(setup_platform).verify_profile_page_navigation_after_switching_model()

@then("I verify the profile information should remain unchanged")
@allure.step("Then I verify the profile information should remain unchanged")
def verify_icons_and_text_repond_visually(setup_platform, user_data_store):
    print("Verifying the profile information should remain unchanged")
    ProfilePage(setup_platform).Verify_profile_info_remian_unchanged(user_data_store)

@then("I verify the page layout or menu should adapt to match the first model")
@allure.step("Then I verify the page layout or menu should adapt to match the first model")
def verify_layout_of_Dine_In_model(setup_platform):
    print("Verifying the page layout or menu should adapt to match the Dine In model")
    HomePage(setup_platform).verify_user_redirect_to_Dine_In_location_flow()

@then("I verify the page layout or menu should adapt to match the second model")
@allure.step("Then I verify the page layout or menu should adapt to match the second model")
def verify_layout_of_Take_away_model(setup_platform):
    print("Verifying the page layout or menu should adapt to match the Take away model")
    HomePage(setup_platform).verify_user_redirect_to_take_away_location_flow()

@then("I verify the page layout or menu should adapt to match the third model")
@allure.step("Then I verify the page layout or menu should adapt to match the third model")
def verify_layout_of_On_the_go_model(setup_platform):
    print("Verifying the page layout or menu should adapt to match the on the go model")
    HomePage(setup_platform).verify_user_redirect_to_On_the_go_pick_up_location_flow()

@then("I verify the page layout or menu should adapt to match the fourth model")
@allure.step("Then I verify the page layout or menu should adapt to match the fourth model")
def verify_layout_of_Mcdelivery_model(setup_platform):
    print("Verifying the page layout or menu should adapt to match the Mcdelivery model")
    HomePage(setup_platform).verify_user_redirect_to_McDelivery_ordering_flow()

@when("I select the third model")
@allure.step("When I select the third model")
def select_first_model(setup_platform):
    print("select the on the go model")
    HomePage(setup_platform).step_select_third_model()

@when("I select the fourth model")
@allure.step("When I select the fourth model")
def select_second_model(setup_platform):
    print("select the Mcdelivery model")
    HomePage(setup_platform).step_select_fourth_model()

@when("I search the address from serchbar abd select the address")
@allure.step("When I search the address from serchbar abd select the address")
def search_address_from_searchbar(setup_platform):
    print("search the address from serchbar abd select the address")
    AddressPage(setup_platform).search_for_address_after_selecting_business_model()

@when("I browse the menu and return to the homepage")
@allure.step("When I browse the menu and return to the homepage")
def verify_browse_menu(setup_platform):
    print("browse the menu and return to the homepage")
    AddressPage(setup_platform).verify_browse_menu()

@then("I verify Dine-In remains the selected option until manually changed")
@allure.step("Then I verify Dine-In remains the selected option until manually changed")
def verify_dine_in_remains_selected(setup_platform):
    print("Verifying Dine-In remains the selected option until manually changed")
    HomePage(setup_platform).verify_Dine_In_selected_until_manually_changed()

@when("I user click on a listed address")
@allure.step("When I user click on a listed address")
def click_on_listed_address(setup_platform):
    print("user click on a listed address")
    AddressPage(setup_platform).Click_from_listed_address()

@then("I verify the address is selected and restaurant list should update accordingly")
@allure.step("Then I verify the address is selected and restaurant list should update accordingly")
def verify_address_selected_restaurant_updated_accordingly(setup_platform):
    print("Verifying the address is selected and restaurant list should update accordingly")
    HomePage(setup_platform).verify_address_selected_and_restaurant_updated_accordingly()

@then("I verify restaurant list should be refreshed accordingly")
@allure.step("Then I verify restaurant list should be refreshed accordingly")
def verify_restaurant_list_refreshed_accordingly(setup_platform):
    print("Verifying restaurant list should be refreshed accordingly")
    HomePage(setup_platform).verify_address_selected_and_restaurant_updated_accordingly()

@when("I click the edit icon next to an address")
@allure.step("When I click the edit icon next to an address")
def click_address_edit_icon(setup_platform):
    print("click the edit icon next to an address")
    AddressPage(setup_platform).click_address_edit_icon()

@when("I modifies the address details and click save button")
@allure.step("When I modifies the address details and click save button")
def modify_existing_address(setup_platform):
    print("modifies the address details and click save button")
    AddressPage(setup_platform).modify_existing_address_and_click_save("123, Marathahalli")

@then("I verify updated address is shown in the address list")
@allure.step("Then I verify updated address is shown in the address list")
def verify__updated_address_display_in_address_list(setup_platform):
    print("Verifying updated address is shown in the address list")
    HomePage(setup_platform).verify_updated_address_display_in_address_list("123, Marathahalli")

@then("I verify restaurant are updated based on the modified address")
@allure.step("Then I verify restaurant are updated based on the modified address")
def verify_restaurant_updated_based_on_modified_address(setup_platform):
    print("Verifying restaurant are updated based on the modified address")
    AddressPage(setup_platform).verify_restaurant_updated_based_on_modified_address()

@when("I verify address list shown")
@allure.step("When I verify address list shown")
def verify_address_list_shown(setup_platform, user_data_store):
    print("verify address list shown")
    AddressPage(setup_platform).Verify_address_shown_in_list_before_deletion(user_data_store)

@when("I click the delete icon next to an address")
@allure.step("When I click the delete icon next to an address")
def click_address_delete_icon(setup_platform):
    print("click the delete icon next to an address")
    AddressPage(setup_platform).click_address_delete_icon()

@then("I verify address removed from list")
@allure.step("Then I verify address removed from list")
def verify_address_removed_from_list(setup_platform, user_data_store):
    print("Verifying address removed from list")
    AddressPage(setup_platform).Verify_address_removed_from_list_after_deletion(user_data_store)

@then("I verify address entry popup or page should be displayed")
@allure.step("Then I verify address entry popup or page should be displayed")
def verify_user_redirected_to_address_filling_page(setup_platform):
    print("Verifying address entry popup or page should be displayed")
    Address_Page = AddressPage(setup_platform).verify_redirect_to_address_filling_page()
    assert Address_Page, "Address entry popup or page is not displayed"

@when("I verify address list displayed")
@allure.step("When I verify address list displayed")
def verify_address_list(setup_platform):
    print("verify address list displayed")
    AddressPage(setup_platform).verify_address_list()

@then("I verify each address should display a Near label with its location description")
@allure.step("Then I verify each address should display a Near label with its location description")
def verify_address_removed_from_list(setup_platform):
    print("Verifying each address should display a Near label with its location description")
    AddressPage(setup_platform).verify_near_label_visible_in_address_description()

@when("I scrolls through the address list")
@allure.step("When I scrolls through the address list")
def scroll_address_list(setup_platform):
    print("scrolls through the address list")
    AddressPage(setup_platform).scroll_to_bottom_of_element()

@then("I verify all saved addresses should be accessible via scrolling")
@allure.step("Then I verify all saved addresses should be accessible via scrolling")
def verify__all_saved_address_accessible_via_scroll(setup_platform):
    print("Verifying all saved addresses should be accessible via scrolling")
    AddressPage(setup_platform).All_addresses_accessible_via_scrolling()
    

@then("I verify the most recently used address should be auto-selected")
@allure.step("Then I verify the most recently used address should be auto-selected")
def verify_recently_used_address_is_auto_selected_after_login(setup_platform):
    print("Verifying the most recently used address should be auto-selected")
    HomePage(setup_platform).verify_recently_used_address_is_auto_selected_after_login()

@when("I enters an undeliverable pin code or area manually")
@allure.step("When I enters an undeliverable pin code or area manually")
def enter_undeliverable_address(setup_platform):
    print("enters an undeliverable pin code or area manually")
    AddressPage(setup_platform).enter_an_undeliverable_address()

@then("I verify an error message should be displayed saying Delivery not available at this address")
@allure.step("Then I verify an error message should be displayed saying Delivery not available at this address")
def verify__error_message_for_undeliverable_location(setup_platform):
    print("Verifying an error message should be displayed saying Delivery not available at this address")
    HomePage(setup_platform).verify_error_message_for_undeliverable_address()

@when("I adds an address and select a tag")
@allure.step("When I adds an address and select a tag")
def add_address_and_select_tag(setup_platform):
    print("adds an address and select a tag")
    AddressPage(setup_platform).add_address_and_select_tag()

@then("I verify the tag should be displayed next to the address name after adding address")
@allure.step("Then I verify the tag should be displayed next to the address name after adding address")
def verify_work_tag_display_next_to_address(setup_platform):
    print("Verifying the tag should be displayed next to the address name after adding address")
    AddressPage(setup_platform).verify_tag_next_to_address_after_adding_address()

@when("I edits an address and select a tag")
@allure.step("When I edits an address and select a tag")
def edit_address_and_select_tag(setup_platform):
    print("edits an address and select a tag")
    AddressPage(setup_platform).edit_address_and_select_tag()

@then("I verify the tag should be displayed next to the address name after editing address")
@allure.step("Then I verify the tag should be displayed next to the address name after editing address")
def verify_home_tag_display_next_to_address(setup_platform):
    print("Verifying the tag should be displayed next to the address name after editing address")
    AddressPage(setup_platform).verify_tag_next_to_address_after_editing_address()
    
