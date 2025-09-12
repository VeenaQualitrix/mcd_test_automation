from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from actions.ios_actions import iOSActions
from selenium.webdriver.common.keys import Keys
import time
import allure
import pytest
import pyperclip
import re
import pytest


locators = {
    
"SEARCH_BUTTON": (AppiumBy.ACCESSIBILITY_ID, "ic-search"),

'COUPON_INPUT_FIELD': (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Enter Coupon Code"]'),

"OFFER_CARD_LIST": (AppiumBy.ACCESSIBILITY_ID, "FLAT10"),

"COUPON_CODE": (AppiumBy.ACCESSIBILITY_ID, "FLAT10"),

'COUPON_DESCRIPTION': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="10% Discount on purchase of ₹300"]'),

'SHOW_MORE_LINK': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="Show More"])[9]'),

'APPLY_BUTTON': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name, "FLAT10")]/following::XCUIElementTypeButton[@name="Apply"][1]'),

'COUPON_SUCCESS_MESSAGE': (AppiumBy.XPATH, '//XCUIElementTypeOther[@name="Discount Coupon, web alert dialogue"]/XCUIElementTypeOther[2]'),

'CLICK_OK': (AppiumBy.ACCESSIBILITY_ID, 'OK'),

'MIN_CART_WARNING': (AppiumBy.XPATH, '//XCUIElementTypeOther[@name="Promo Not Applied, web alert dialogue"]/XCUIElementTypeOther[2]'),

'CHANGE_OFFER_BUTTON': (AppiumBy.ACCESSIBILITY_ID, 'Change Offer'),

'SECOND_COUPON_APPLY_BUTTON': (AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="Apply"])[4]'),

'APPLIED_COUPON_CODE': (AppiumBy.ACCESSIBILITY_ID, 'Gofree'),

}
class OffersScreenIos(BasePage):

    def enter_coupon_code(self, menu_item):
        time.sleep(5)
        self.actions.enter_text(*locators["COUPON_INPUT_FIELD"], menu_item)
        print(f"Entered menu item: {menu_item}")


    

    def tap_search_button(self):
        try:
            self.actions.click_button(*locators['SEARCH_BUTTON'])
            print("Search button clicked successfully")
        except Exception as e:
            print(f"Failed to tap on the search button: {e}")
            raise


    def get_offer_cards(self):
        try:
            elements = self.actions.get_text(*locators['OFFER_CARD_LIST'])
            return elements if elements else []
        except Exception as e:
            print(f"Error while fetching offer cards: {e}")
            return []

    def scroll_through_offer_cards(self):
        for i in range(2):
            print(f"Scrolling through offer cards - pass {i + 1}")
            self.driver.execute_script(
                "mobile: scroll", {
                    "direction": "down",
                    "predicateString": "name == 'Freedelivery+Free product'"
                }
            )


    def verify_offer_card_elements(self):
        print("Verifying elements in the currently visible offer card")
        code = self.actions.find_element(*locators["COUPON_CODE"])
        description = self.actions.find_element(*locators["COUPON_DESCRIPTION"])
        show_more = self.actions.find_element(*locators["SHOW_MORE_LINK"])
        apply_button = self.actions.find_element(*locators["APPLY_BUTTON"])
        # Assertions
        assert self.actions.is_element_displayed(code), "Coupon code is not visible"
        assert self.actions.is_element_displayed(description), "Description is missing"
        assert self.actions.is_element_displayed(show_more), "'Show More' link is missing"
        assert self.actions.is_element_displayed(apply_button), "'Apply' button is missing"

    def tap_apply_button(self):
        time.sleep(3)
        self.actions.click_button(*locators["APPLY_BUTTON"])
        print("Tapped on the Apply button under a valid offer")


    def verify_coupon_applied(self):
        time.sleep(3)
        success_msg = self.actions.find_element(*locators["COUPON_SUCCESS_MESSAGE"])
        assert self.actions.is_element_displayed(success_msg), "Coupon was not applied or eligibility not met"
        self.actions.click_button(*locators["CLICK_OK"])
        print("Coupon applied successfully to the cart")


    def verify_min_cart_warning(self):
        time.sleep(3)
        self.actions.find_element(*locators["MIN_CART_WARNING"])
        self.actions.click_button(*locators["CLICK_OK"])




    def click_change_offer(self):
        self.actions.click_button(*locators["CHANGE_OFFER_BUTTON"])
        print("Clicked on Change Offer button")

    def apply_another_coupon(self):
        self.driver.execute_script(
            "mobile: scroll",
            {"direction": "down", "predicateString": "label CONTAINS 'McDelivery999'"}
        )
        print("Scrolled to 'McDelivery999' coupon")
        self.actions.click_button(*locators["SECOND_COUPON_APPLY_BUTTON"])
        print("Applied 'McDelivery999' coupon")
        self.actions.click_button(*locators["CLICK_OK"])

        

    def verify_updated_coupon_applied(self, updated_coupon_code):
        time.sleep(2)
        applied_coupon_element = self.actions.find_element(*locators["APPLIED_COUPON_CODE"])
        assert self.actions.is_element_displayed(applied_coupon_element), "Applied coupon code is not displayed"
        actual_applied_code = applied_coupon_element.text.strip()
        print(f"Currently applied coupon code: '{actual_applied_code}'")
        assert updated_coupon_code.lower() in actual_applied_code.lower(), (
            f"Expected applied coupon: '{updated_coupon_code}', but found: '{actual_applied_code}'"
        )
        print("Updated coupon is applied to the order successfully.")
