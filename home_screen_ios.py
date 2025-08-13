from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage
import time


class HomeScreen:

    locators = {
        "profile_button": (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"),
        "home_page_header": (AppiumBy.ACCESSIBILITY_ID, "home_page_header")  # Update with correct ID
    }


class MobileHomeScreen(BasePage):

    def verify_header_banner(self):
        time.sleep(3)
        return self.actions.is_element_displayed(*locators['HEADER_BANNER'])

    def tap_view_icon(self):
        self.actions.click_button(*locators['VIEW_ICON'])
        print("Tapped on View Icon on Mobile Home Screen")

    def tap_add_address_dropdown(self):
        self.actions.click_button(*locators['ADDRESS_DROPDOWN'])
        print("Tapped on Add Address Dropdown")

    def tap_restaurants_nearby(self):
        self.actions.click_button(*locators['NEARBY_RESTAURANTS'])
        print("Tapped on 'Restaurants Nearby'")

    def verify_nearby_restaurants_displayed(self):
        near_me_stores = self.actions.wait_for_elements(*locators['NEAR_ME_STORES'])
        if near_me_stores:
            print(f"Nearby Stores Found: {len(near_me_stores)}")
            return True
        print("No Nearby Stores Found")
        return False

    def select_item_from_meals_category(self):
        time.sleep(2)
        burger_name = " McChicken Burger "
        add_item_locator = locators['ADD_ITEM_TO_CART']
        formatted_xpath = add_item_locator[1].format(burger_name=burger_name)
        
        self.actions.click_button(add_item_locator[0], formatted_xpath)
        print("Tapped on 'Add Item' for:", burger_name)

        # Tap on Next
        if self.actions.is_element_displayed(*locators['CLICK_NEXT']):
            self.actions.click_button(*locators['CLICK_NEXT'])
            print("Tapped 'Next'")

        # Final Add to Cart
        if self.actions.is_element_displayed(*locators['CLICK_ADD_TO_CART']):
            self.actions.click_button(*locators['CLICK_ADD_TO_CART'])
            print("Tapped 'Add to Cart'")
