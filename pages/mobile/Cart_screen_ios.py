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

'ADD_INSTRUCTION_BUTTON': (AppiumBy.ACCESSIBILITY_ID, 'ic-address__add'),

'INSTRUCTION_TEXT_FIELD': (AppiumBy.XPATH, '//XCUIElementTypeTextView'),

'SUB_TOTAL': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[contains(@name, "₹")])[18]'),

'CART_ITEM_PRICE_LIST': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[contains(@name, "₹")])[1]'),

'CGST': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[contains(@name, "₹")])[21]'),

'SGST': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[contains(@name, "₹")])[22]'),

'BACK_BUTTON': (AppiumBy.ACCESSIBILITY_ID, 'ic-arrow-back'),

'CHARITY_KNOW_MORE_LINK': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Know More"]'),

'CHARITY_INFO_SECTION': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Your support will go a long way in keeping unwell children and their families together."]'),

'CHARITY_DONATION_CHECKBOX': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Donate ₹ 3 for Ronald Mcdonald House of Charity."]'),

'DONATION_AMOUNT': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="₹ 3.00"]'),

'VIEW_ALL_OFFERS': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="View All"]'),

'OFFERS_PAGE_HEADER': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Offers For You"]'),

'HANDLING_CHARGE': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[contains(@name, "₹")])[19]'),

'CART_TOTAL': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[contains(@name, "₹")])[18]')
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


    def add_delivery_instructions(self, note_text):
        print("Scrolling to 'Add Delivery Instructions'...")
        self.driver.execute_script("mobile: scroll", {
            "direction": "down",
            "predicateString": "name == 'Add Delivery Instructions'"
        })
        time.sleep(1)  # Optional small delay after scroll
        print("Clicking on 'Add Delivery Instructions'...")
        self.actions.click_button(*locators['ADD_INSTRUCTION_BUTTON'])
        print(f"Entering delivery instructions: {note_text}")
        self.actions.enter_text(*locators['INSTRUCTION_TEXT_FIELD'], note_text)
        print("Delivery instructions added successfully.")

    def verify_subtotal_reflects_all_items(self):
        print("Verifying that the subtotal reflects all additions accurately...")
        time.sleep(2)
        print("Scrolling to 'Subtotal' section...")
        self.driver.execute_script("mobile: scroll", {
            "direction": "down",
            "predicateString": "name == 'Subtotal'"
        })
        time.sleep(2)
        print("Fetching individual item prices from the cart...")
        # Get all item price elements in the cart (e.g., "₹179")
        item_price_elements = self.driver.find_elements(*locators['CART_ITEM_PRICE_LIST'])
        item_prices = []
        for elem in item_price_elements:
            price_text = elem.text.strip()
            if price_text:
                price_value = float(re.sub(r"[^\d.]", "", price_text))
                item_prices.append(price_value)
        calculated_subtotal = round(sum(item_prices), 2)
        print(f"Calculated subtotal from all items: ₹{calculated_subtotal}")
        # Get displayed subtotal from UI (e.g., "Subtotal: ₹358.08")
        displayed_subtotal_text = self.actions.get_text(*locators['SUB_TOTAL'])
        displayed_subtotal = float(re.sub(r"[^\d.]", "", displayed_subtotal_text))
        print(f"Displayed Subtotal on UI: ₹{displayed_subtotal}")
        if calculated_subtotal == displayed_subtotal:
            print("Subtotal reflects all added items accurately.")
        else:
            print("Subtotal mismatch.")
            print(f"Expected: ₹{calculated_subtotal}, Found: ₹{displayed_subtotal}")

    def validate_tax_breakdown(self):
        print("Validating CGST and SGST independently...")

        try:
            # Scroll to 'Total Payable'
            self.driver.execute_script("mobile: scroll", {
                "direction": "down",
                "predicateString": "name CONTAINS 'Total Payable'"
            })
            time.sleep(2)

            # Wait for CGST and SGST to appear
            cgst_text = self.actions.get_text(*locators['CGST'])
            sgst_text = self.actions.get_text(*locators['SGST'])

            cgst = float(re.sub(r"[^\d.]", "", cgst_text))
            sgst = float(re.sub(r"[^\d.]", "", sgst_text))

            gst_rate = 2.5  # Assuming 2.5% each

            implied_subtotal_cgst = round((cgst / gst_rate) * 100, 2)
            implied_subtotal_sgst = round((sgst / gst_rate) * 100, 2)

            print(f"CGST: ₹{cgst} → Implied Subtotal: ₹{implied_subtotal_cgst}")
            print(f"SGST: ₹{sgst} → Implied Subtotal: ₹{implied_subtotal_sgst}")

            if abs(implied_subtotal_cgst - implied_subtotal_sgst) < 0.1:
                print(" CGST and SGST are consistent and appear correct.")
            else:
                print(" CGST and SGST calculation mismatch.")
        except TimeoutException as e:
            print(" Failed to locate CGST/SGST in time. Details:")
            print(str(e))


    def click_back_button(self):
        print("Attempting to click on the back button...")
        self.actions.click_button(*locators['BACK_BUTTON'])
        print("Back button clicked successfully.")
        

    def click_know_more_charity(self):
        print("Attempting to scroll to 'Know More' link in the charity donation section...")
        self.driver.execute_script("mobile: scroll", {
            "direction": "down",
            "predicateString": "name CONTAINS 'Know More'"
        })
        time.sleep(1)  # Give a moment for scroll to complete
        print("Clicking on 'Know More' link...")
        self.actions.click_button(*locators['CHARITY_KNOW_MORE_LINK'])
        print("'Know More' link clicked successfully.")

    def is_charity_info_visible(self):
        print("Checking if the charity donation information is displayed...")
        is_visible = self.actions.is_element_displayed(*locators['CHARITY_INFO_SECTION'])
        if is_visible:
            print("Charity donation information is displayed in the cart.")
        else:
            print("Charity donation information is NOT displayed in the cart.")

    def charity_checkbox(self):
        print("Attempting to scroll to 'Know More' link in the charity donation section...")
        self.driver.execute_script("mobile: scroll", {
            "direction": "down",
            "predicateString": "name CONTAINS 'Know More'"
        })
        time.sleep(1) 
        self.actions.click_button(*locators['CHARITY_DONATION_CHECKBOX'])
        print("Charity donation checkbox selected")

    def validate_donation_amount(self):
        print("Validating donation amount of ₹3 is displayed...")
        donation_text = self.actions.get_text(*locators['DONATION_AMOUNT'])
        donation_value = float(re.sub(r"[^\d.]", "", donation_text))
        assert donation_value == 3.0, "Donation amount is not ₹3 as expected."
        print("Donation amount of ₹3 is correctly displayed.")

    def uncheck_charity_donation(self):
        print("Scrolling to 'Donation' section...")
        try:
            # Scroll to the 'Know More' text to ensure the donation checkbox is in view
            self.driver.execute_script("mobile: scroll", {
                "direction": "down",
                "predicateString": "name == 'Know More'"
            })
            time.sleep(1)  # Preferably use an explicit wait instead
            # Attempt to click the charity donation checkbox
            if self.actions.click_button(*locators['CHARITY_DONATION_CHECKBOX']):
                print("Charity donation checkbox is unchecked successfully.")
            else:
                print("Charity donation checkbox was not clickable or already unchecked.")
        except Exception as e:
            print(f"Error while unchecking charity donation checkbox: {e}")



    def verify_donation_removed(self):
        try:
            donation_text = self.actions.get_text(*locators['DONATION_AMOUNT'])
            donation_amount = float(donation_text.replace("₹", "").strip())
            if donation_amount == 3.0:
                print("Donation amount ₹3 is still present in cart.")
            else:
                print("Donation amount is not ₹3. Possibly already removed.")
        except Exception:
            print("Donation amount element not found, assuming it's removed.")

    def click_view_all_offers(self):
        print("Clicking on 'View All Offers' link...")
        self.actions.click_button(*locators['VIEW_ALL_OFFERS'])
        print("'View All Offers' clicked successfully.")


    def verify_offers_page_is_visible(self):
        print("Verifying that the offers page is displayed...")
        is_displayed = self.actions.is_element_displayed(*locators['OFFERS_PAGE_HEADER'])
        if is_displayed:
            print("Offers page is successfully displayed.")
        else:
            raise AssertionError("Offers page is not displayed.")

    

    def validate_currency_symbols(self):
        wait = WebDriverWait(self.driver, 15)  # 15 seconds timeout
        
        print("Waiting for ₹ symbol in Subtotal element...")
        try:
            wait.until(EC.visibility_of_element_located(locators['SUB_TOTAL']))
        except TimeoutException:
            raise AssertionError("Subtotal element not visible or ₹ symbol missing.")

        print("Validating ₹ symbol presence in all price components...")
        price_elements = [
            locators['SUB_TOTAL'],
            locators['HANDLING_CHARGE'],
            locators['CGST'],
            locators['SGST'],
            locators['CART_TOTAL']
        ]
        
        missing_symbols = []
        for locator in price_elements:
            # Wait for element visibility before interaction
            try:
                elem = wait.until(EC.visibility_of_element_located(locator))
                price_text = elem.text
                if "₹" not in price_text:
                    missing_symbols.append(f"{locator} with text '{price_text}'")
            except TimeoutException:
                missing_symbols.append(f"{locator} not found or not visible")
                
        if missing_symbols:
            raise AssertionError(f"₹ symbol missing or elements not found: {missing_symbols}")
        print("All price components have ₹ symbol.")


                
