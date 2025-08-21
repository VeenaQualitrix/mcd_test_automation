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


locators = {
    


'SAVED_ADDRESS_ITEM': (AppiumBy.XPATH, '//XCUIElementTypeOther[@name="web dialogue"]/XCUIElementTypeOther[3]'),

'SELECTED_ADDRESS_LABEL': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="Home"])[1]'),


}
class AddressStoreScreenIos(BasePage):



    def select_existing_address_from_saved_list(self):
        if self.actions.is_element_displayed(*locators["SAVED_ADDRESS_ITEM"]):
            self.actions.click_button(*locators["SAVED_ADDRESS_ITEM"])
            print("Existing address selected from the saved list.")
        else:
            raise AssertionError("Saved address not found in the list.")
 
    
    def verify_selected_address_applied(self):
        if self.actions.is_element_displayed(*locators["SELECTED_ADDRESS_LABEL"]):
            print("Selected address is applied successfully.")
        else:
            raise AssertionError("Selected address is not applied or not visible.")
        

