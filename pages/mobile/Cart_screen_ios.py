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
    

'CART_ITEM_NAME': (AppiumBy.XPATH, '(//XCUIElementTypeImage)[5]'),

'CART_ITEM_PRICE': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[contains(@name, "₹")])[1]'),

'CART_ITEM_QUANTITY': (AppiumBy.ACCESSIBILITY_ID, '01'),

}
class CartScreenIos(BasePage):


    

    def validate_cart_items(self):
        time.sleep(2)
        print("Verifying cart item details (name, price, quantity)...")
        # Fetch all item elements
        item_names = self.actions.find_elements(*locators['CART_ITEM_NAME'])
        item_prices = self.actions.find_elements(*locators['CART_ITEM_PRICE'])
        item_quantities = self.actions.find_elements(*locators['CART_ITEM_QUANTITY'])
        # Make sure all lists are the same length
        total_items = min(len(item_names), len(item_prices), len(item_quantities))
        for index in range(total_items):
            name = item_names[index].text
            price = item_prices[index].text
            quantity = item_quantities[index].text
            print(f"Item {index + 1}: Name = {name}, Price = {price}, Quantity = {quantity}")


