from pytest_bdd import given, when, then, scenarios
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.view_page import ViewPage
from pages.profile_page import ProfilePage
from pages.address_page import AddressPage
from conftest import readPreReqJson

scenarios('../features/Mcd_Sanity_Validations.feature')


@given("I open the Chrome browser")
def open_the_chrome_browser(setup_platform):
    print("Launch Chrome Browser")


@when("I hit the URL")
def hit_the_url(setup_platform):
    BasePage(setup_platform).open_mcd_website()


@then("I verify website opened successfully")
def verify_website_oopened_successfully(setup_platform):
    print("Verifying McD Website")
    Is_Website_Opened = HomePage(setup_platform).verify_website_header_banner()
    assert Is_Website_Opened, "Web Application Is Not Opened As Expected"


@when("I click on view icon")
def click_on_view_icon(setup_platform):
    print("Clicking on view Icon")
    HomePage(setup_platform).click_on_view_icon()


@then("I verify view page navigation")
def verify_view_page_navigation(setup_platform):
    print("Verifying View Page")
    View_Page = ViewPage(setup_platform).verify_view_page_is_reached()
    assert View_Page, "View Page Is Not Reached After Clicking On View Icon In Home Page"


@when("I click on login or signup button")
def click_on_login_or_sign_up_button(setup_platform):
    print("Clicking on Login/Sign Up Button")
    ViewPage(setup_platform).click_on_login_or_sign_up_button()


@then("I verify login page navigation")
def verify_login_page_navigation(setup_platform):
    print("Verifying Login Page Navigation")
    Login_Page = LoginPage(setup_platform).verify_login_page_reached()
    assert Login_Page, "Login Page Is Not Reached After Clicking On Login Button In View Page"


@when("I enter a valid mobile number and click verify")
def enter_a_valid_mobile_number_and_click_verify(setup_platform):
    mobile_number = readPreReqJson("test_data", "mobile_number")
    print("Entering Mobie Number")
    LoginPage(setup_platform).enter_mobile_number(mobile_number)


@when("I enter the OTP and click verify")
def enter_the_otp_and_click_verify(setup_platform):
    otp = readPreReqJson("test_data", "OTP")
    print("Entering OTP")
    LoginPage(setup_platform).enter_otp(otp)


@then('I verify profile page navigation')
def verify_profile_page_navigation(setup_platform):
    print("Verifying Profile Page Navigation")
    Profile_Page = ProfilePage(setup_platform).verify_profile_page_reached()
    assert Profile_Page, "Profile Page Is Not Reached After Logged In"


@then("I verify profile page is incomplete")
def verify_profile_page_is_incomplete(setup_platform):
    print("Verifying Profile Page Is Incomplete")
    Profile_Page_Incomplete = ProfilePage(setup_platform).verify_profile_page_is_incomplete_after_login()
    assert Profile_Page_Incomplete, "Profile Page Is Not Incomplete After Login"


@when("I add the profile details")
def add_the_profile_details(setup_platform):
    print("Adding Profile Details In Profile Page")
    ProfilePage(setup_platform).add_profile_details()


@then("I verify home page navigation")
def verify_home_page_navigation(setup_platform):
    print("Verifying Home Page")
    Home_page_reached = HomePage(setup_platform).verify_website_header_banner()
    assert Home_page_reached, "Home Page Is Not Reached After Adding Profile Details And Saving The Details"


@when("I click on add address in home page")
def click_on_add_address_in_home_page(setup_platform):
    print("Clicking On Add Address In Home Page")
    HomePage(setup_platform).click_on_add_address()


@when("I click on add new button and search for location")
def click_on_add_new_button_and_search_for_location(setup_platform):
    print("Searching For Location To Add new Location")
    AddressPage(setup_platform).search_for_new_address()


@when("I select address from search results")
def select_address_from_search_results(setup_platform):
    print("Selecting Address From Search Results")
    AddressPage(setup_platform).select_address_from_search_results()


@then("I verify address is added and selected")
def verify_address_is_added_and_selected(setup_platform):
    print("Verifying Address Is Addded And Selected")
    Address_Added = AddressPage(setup_platform).verify_address_is_added_and_selected()
    assert Address_Added, "Address Is Not Added And Selected From The List Of Address"


@when("I click on restaurants nearby in home page")
def click_on_restaurants_nearby_in_home_page(setup_platform):
    print("Clicking On Restaurants Nearby Button In Home Page")
    HomePage(setup_platform).click_on_restaurants_nearby()


@then("I verify nearby restaurants are diplayed")
def verify_nearby_restaurants_are_displayed(setup_platform):
    print("Verifying Address Is Addded And Selected")
    Nearby_Restaurants = HomePage(setup_platform).verify_nearby_restaurants_are_displayed()
    assert Nearby_Restaurants, "Nearby Restaurants Are Not Displayed For Selected Address"


@when("I add multiple product with customization and coke convergence")
def add_multiple_product_with_customization_and_coke_convergence(setup_platform):
    print("Adding Multiple Product With Customization And Coke Convergence")
    HomePage(setup_platform).add_multiple_product_with_customization_and_coke_convergence()


@then("I verify the product added in cart")
def verify_the_product_added_in_cart(setup_platform):
    print("Verifying Product Added In Cart")
    Nearby_Restaurants = HomePage(setup_platform).verify_product_added_in_cart()
    assert Nearby_Restaurants, ""