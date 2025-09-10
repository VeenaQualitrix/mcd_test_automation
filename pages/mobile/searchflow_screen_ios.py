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
    
"SEARCH_ICON_HOME": (AppiumBy.ACCESSIBILITY_ID, "Search"),

'SEARCH_BAR_TEXT_FIELD': (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Search here"]'),

'SEARCH_ICON_INSIDE': (AppiumBy.XPATH, '(//XCUIElementTypeImage[@name="ic-search"])[1]'),

'SEARCH_RESULT_ITEMS': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Fries (Large)"]'),

"NO_ITEMS_MESSAGE": (AppiumBy.ACCESSIBILITY_ID, "No matching item found"),

"EMPTY_ITEMS_MESSAGE": (AppiumBy.ACCESSIBILITY_ID, "Search menu item"),

'CART_ITEM_NAME': (AppiumBy.XPATH, "(//XCUIElementTypeImage[contains(@name, 'Fries')])[1]"),

'BURGER_DISPLAYED': (AppiumBy.XPATH, "//XCUIElementTypeTextField")

}
class SearchScreenIos(BasePage):



    def click_search_icon(self):
        print("Attempting to click the Search icon")
        time.sleep(2) 
        self.actions.is_element_displayed(*locators['SEARCH_ICON_HOME'])
        self.actions.click_button(*locators['SEARCH_ICON_HOME'])
        print("Clicked the Search icon")


    def enter_search_text(self, menu_item):
        time.sleep(5) 
        self.actions.enter_text(*locators["SEARCH_BAR_TEXT_FIELD"], menu_item)
        print(f"Entered menu item: {menu_item}")

    def click_search_icon_inside(self):
        time.sleep(2) 
        self.actions.click_button(*locators["SEARCH_ICON_INSIDE"])
        print("Clicked on the search icon inside the search bar")


    def get_search_results(self):
        results = []
        elements = self.actions.find_elements(*locators["SEARCH_RESULT_ITEMS"])
        for elem in elements:
            text = elem.text 
            results.append(text)
        print(f"Search results found: {results}")
        return results    
    
    def get_no_items_message(self):
        return self.actions.get_text(*locators["NO_ITEMS_MESSAGE"])
    
    def get_no_items_empty_message(self):
        return self.actions.get_text(*locators["EMPTY_ITEMS_MESSAGE"])


    def get_cart_item_name(self):
        return self.actions.get_text(*locators["CART_ITEM_NAME"])

    
    def burger_display_in_search(self):
        time.sleep(2) 
        results = []
        elements = self.actions.find_elements(*locators["BURGER_DISPLAYED"])
        for elem in elements:
            text = elem.text.strip()
            if text:  # avoid empty strings
                results.append(text)
        print(f"Search results found: {results}")
        return results


    def get_search_placeholder_text(self):
        elements = self.actions.find_elements(*locators["SEARCH_BAR_TEXT_FIELD"])
        if not elements:
            raise Exception("Search bar element not found")
        placeholder = elements[0].get_attribute("value")  # first element
        return placeholder.strip() if placeholder else ""

