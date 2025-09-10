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


locators = {
    
"SEARCH_BUTTON": (AppiumBy.ACCESSIBILITY_ID, "ic-search"),

'COUPON_INPUT_FIELD': (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Enter Coupon Code"]'),

"OFFER_CARD_LIST": (AppiumBy.ACCESSIBILITY_ID, "FLAT10"),

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
            self.driver.execute_script("mobile: scroll", {
                "direction": "down",
                "predicateString": "name == 'Sold out'"
            })

    def verify_offer_card_elements(self):
        offer_cards = self.actions.find_elements(*locators["OFFER_CARD_CONTAINER"])
        assert offer_cards, "No offer cards found on the screen."

        for index, card in enumerate(offer_cards):
            print(f"Verifying elements in offer card #{index + 1}")

            # Find all elements relative to the card
            code = self.actions.find_element(card, *locators["COUPON_CODE"])
            description = self.actions.find_element(card, *locators["COUPON_DESCRIPTION"])
            show_more = self.actions.find_element(card, *locators["SHOW_MORE_LINK"])
            apply_button = self.actions.find_element(card, *locators["APPLY_BUTTON"])

            # Assertions
            assert self.actions.is_element_displayed(code), f"Coupon code is not visible in card #{index + 1}"
            assert self.actions.is_element_displayed(description), f"Description is missing in card #{index + 1}"
            assert self.actions.is_element_displayed(show_more), f"'Show More' link is missing in card #{index + 1}"
            assert self.actions.is_element_displayed(apply_button), f"'Apply' button is missing in card #{index + 1}"
