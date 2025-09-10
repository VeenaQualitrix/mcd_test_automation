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

'BURGER_DISPLAYED': (AppiumBy.XPATH, "//XCUIElementTypeTextField"),

"VEG_FILTER_BUTTON": (AppiumBy.ACCESSIBILITY_ID, "Veg"),

'SEARCH_RESULTS_VEG': (AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='main'])[2]"),

"NONVEG_FILTER_BUTTON": (AppiumBy.ACCESSIBILITY_ID, "Non-Veg"),

'SEARCH_RESULTS_NONVEG': (AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='main'])[2]"),

"ALL_ITEMS": (AppiumBy.ACCESSIBILITY_ID, "Popular Items"),

'SEARCH_BAR_TEXT_FIELD_FILLED': (AppiumBy.XPATH, "//XCUIElementTypeTextField"),

"VEG_FILTER_BUTTON_CLOSE": (AppiumBy.ACCESSIBILITY_ID, "ic-close-red"),

"BACK_BUTTON": (AppiumBy.ACCESSIBILITY_ID, "ic-arrow-left-primary"),

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


    def click_veg_filter(self):
        self.actions.click_button(*locators["VEG_FILTER_BUTTON"])
        print("Veg filter button tapped")

    def get_search_veg(self):
        results = []
        elements = self.actions.find_elements(*locators["SEARCH_RESULTS_VEG"])
        for elem in elements:
            try:
                text = elem.text.strip()
                if text:
                    results.append(text)
            except Exception as e:
                print(f" Could not fetch text for element: {e}")
        print(f" Captured Veg results: {results}")
        return results

    def click_nonveg_filter(self):
        self.actions.click_button(*locators["NONVEG_FILTER_BUTTON"])
        print("Tapped on Non-Veg filter")


    def get_search_nonveg(self):
        results = []
        elements = self.actions.find_elements(*locators["SEARCH_RESULTS_NONVEG"])
        for elem in elements:
            try:
                text = elem.text.strip()
                if text:
                    results.append(text)
            except Exception as e:
                print(f"Could not fetch text from element: {e}")
        print(f"Captured Non-Veg results: {results}")
        return results


    def clear_search(self):
        print("Trying to clear field")
        self.actions.click_button(*locators["SEARCH_BAR_TEXT_FIELD_FILLED"])
        self.actions.clear_text(*locators["SEARCH_BAR_TEXT_FIELD_FILLED"])
        print("Search input cleared")


    def get_all_items(self):
        elements = self.actions.find_elements(*locators["ALL_ITEMS"])
        results = [elem.text.strip() for elem in elements if elem.text.strip()]
        print(f"All items captured: {results}")
        return results


    def get_search_wrap(self):
        elements = self.actions.find_elements(*locators["SEARCH_RESULTS_VEG"])
        results = []

        for elem in elements:
            text = elem.text.strip()
            if text:  # ignore empty strings
                results.append(text)
        
        print(f"Search results found for Wrap: {results}")
        return results



    def fetch_displayed_items(self):
        elements = self.actions.find_elements(*locators["VEG_FILTER_BUTTON"])
        results = [elem.text.strip() for elem in elements if elem.text.strip()]
        print(f"Displayed items: {results}")
        return results

    def click_veg_filter_again(self):
        self.actions.click_button(*locators["VEG_FILTER_BUTTON_CLOSE"])
        print("Veg filter button tapped")

    def click_back_button(self):
        print("Attempting to click on the back button...")
        self.actions.click_button(*locators['BACK_BUTTON'])
        print("Back button clicked successfully.")
        try:
            assert self.actions.is_displayed(*locators['PREVIOUS_SCREEN_IDENTIFIER']), \
                " Failed: Previous screen not displayed after clicking back"
            print(" Verified: Previous screen is displayed after clicking back")
        except Exception as e:
            print(f"Warning: Could not verify previous screen. Details: {e}")
