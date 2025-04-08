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
import allure

scenarios('../features/Mcd_Sanity_Validations.feature')


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


@then('I verify profile page navigation')
@allure.step("Then I verify profile page navigation")
def verify_profile_page_navigation(setup_platform):
    print("Verifying Profile Page Navigation")
    Profile_Page = ProfilePage(setup_platform).verify_profile_page_reached()
    assert Profile_Page, "Profile Page Is Not Reached After Logged In"


@then("I verify profile page is incomplete")
@allure.step("Then I verify profile page is incomplete")
def verify_profile_page_is_incomplete(setup_platform):
    print("Verifying Profile Page Is Incomplete")
    Profile_Page_Incomplete = ProfilePage(setup_platform).verify_profile_page_is_incomplete_after_login()
    assert Profile_Page_Incomplete, "Profile Page Is Not Incomplete After Login"


@when("I add the profile details")
@allure.step("When I add the profile details")
def add_the_profile_details(setup_platform):
    print("Adding Profile Details In Profile Page")
    ProfilePage(setup_platform).add_profile_details()


@then("I verify home page navigation")
@allure.step("Then I verify home page navigation")
def verify_home_page_navigation(setup_platform):
    print("Verifying Home Page")
    Home_page_reached = HomePage(setup_platform).verify_website_header_banner()
    assert Home_page_reached, "Home Page Is Not Reached After Adding Profile Details And Saving The Details"


@when("I click on add address in home page")
@allure.step("When I click on add address in home page")
def click_on_add_address_in_home_page(setup_platform):
    print("Clicking On Add Address In Home Page")
    HomePage(setup_platform).click_on_add_address()


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
    print("Verifying Address Is Addded And Selected")
    Address_Added = AddressPage(setup_platform).verify_address_is_added_and_selected()
    assert Address_Added, "Address Is Not Added And Selected From The List Of Address"


@when("I click on restaurants nearby in home page")
@allure.step("When I click on restaurants nearby in home page")
def click_on_restaurants_nearby_in_home_page(setup_platform):
    print("Clicking On Restaurants Nearby Button In Home Page")
    HomePage(setup_platform).click_on_restaurants_nearby()


@then("I verify nearby restaurants are diplayed")
@allure.step("Then I verify nearby restaurants are diplayed")
def verify_nearby_restaurants_are_displayed(setup_platform):
    print("Verifying Address Is Addded And Selected")
    Nearby_Restaurants = HomePage(setup_platform).verify_nearby_restaurants_are_displayed()
    assert Nearby_Restaurants, "Nearby Restaurants Are Not Displayed For Selected Address"


@when("I add multiple product with customization and coke convergence")
@allure.step("When I add multiple product with customization and coke convergence")
def add_multiple_product_with_customization_and_coke_convergence(setup_platform):
    print("Adding Multiple Product With Customization And Coke Convergence")
    HomePage(setup_platform).add_multiple_product_with_customization_and_coke_convergence()


@then("I verify the product added in cart")
@allure.step("Then I verify the product added in cart")
def verify_the_product_added_in_cart(setup_platform):
    print("Verifying Product Added In Cart")
    Product_Added = HomePage(setup_platform).verify_product_added_in_cart()
    assert Product_Added, "Product Is Not Added In Cart"


@when("I click on view cart button")
@allure.step("When I click on view cart button")
def click_on_view_cart_button(setup_platform):
    print("Clicking on View Cart Button")
    HomePage(setup_platform).click_on_view_cart()


@then('I verify product is visible on cart page with price without GST')
@allure.step("Then I verify product is visible on cart page with price without GST")
def verify_product_is_visible_on_cart_page_with_price_without_gst(setup_platform):
    print("Verifying Product Is Visible On Cart Page With Price Without GST")
    Product_Displayed = ViewCartPage(setup_platform).verify_product_displayed_in_cart_with_price_and_without_gst()
    assert Product_Displayed, "Product Is Not Displayed In Cart With Price And Without GST"


@when("I select offer from list of offer cards")
@allure.step("When I select offer from list of offer cards")
def select_offer_from_list_of_offer_cards(setup_platform):
    print("Selecting Offer")
    ViewCartPage(setup_platform).select_offer()


@then("I verify offer applied for the selected product")
@allure.step("Then I verify offer applied for the selected product")
def verify_offer_applied_for_the_selected_product(setup_platform):
    print("Verifying Offer Applied For The Selected Prodct")
    Offer_Applied = ViewCartPage(setup_platform).verify_offer_applied_for_the_selected_product()
    assert Offer_Applied, "Offer Not Applied For The Selected Product"


@then("I verify gross price and total price are same")
@allure.step("Then I verify gross price and total price are same")
def verify_gross_price_and_total_price_are_same(setup_platform):
    print("Verifying Gross Price And Total Price Are Same In View Cart Page")
    price_match = ViewCartPage(setup_platform).verify_gross_price_and_total_price_are_same()
    assert price_match, "Gross Price And Total Price Are Not Same"


@when("I click on pay button in view cart page")
@allure.step("When I click on pay button in view cart page")
def click_on_pay_button_in_view_cart_page(setup_platform):
    print("Clicking on pay button in view cart page")
    ViewCartPage(setup_platform).click_on_pay_button_in_view_cart_page()


@then("I verify juspay page is displayed")
@allure.step("Then I verify juspay page is displayed")
def verify_juspay_page_is_displayed(setup_platform):
    print("Verifying Juspay Page Is Displayed")
    juspay_page_reached = JuspayPage(setup_platform).verify_juspay_page_is_reached()
    assert juspay_page_reached, "Juspay Page Is Not Reached After Clicking On Pay Button"


@when("I select one payment method")
@allure.step("When I select one payment method")
def select_one_payment_method(setup_platform):
    print("Selecting One Payment Method")
    JuspayPage(setup_platform).select_payment_method()


@then("I verify selected payment method is displayed")
@allure.step("Then I verify selected payment method is displayed")
def verify_selected_payment_method_is_displayed(setup_platform):
    print("Verifying Selected Payment Method Is Displayed")
    payment_selected = JuspayPage(setup_platform).verify_selected_payment_method_is_displayed()
    assert payment_selected, "Selected Payment Method Is Not Displayed In Juspay Page"


@when("I click on proceed to pay")
@allure.step("When I click on proceed to pay")
def click_on_proceed_to_pay(setup_platform):
    print("Clicking On Proceed To Pay")
    JuspayPage(setup_platform).click_on_proceed_to_pay()


@then("I verify order placed successfully")
@allure.step("Then I verify order placed successfully")
def verify_order_placed_successfully(setup_platform):
    print("Verifying Order Placed Successfully")
    order_placed = JuspayPage(setup_platform).verify_order_placed_success_message()
    assert order_placed, "Order Is Not Placed Successfully"
