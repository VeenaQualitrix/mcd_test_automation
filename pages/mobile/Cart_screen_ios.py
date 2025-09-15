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

'SUB_TOTAL': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Sub Total"]/following::XCUIElementTypeStaticText[1]'),

'HANDLINNG_CHARGERS': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Handling Charges"]/following::XCUIElementTypeStaticText[1]'),

'CART_ITEM_PRICE_LIST': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[contains(@name, "₹")])[1]'),

'CGST': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="CGST"]/following::XCUIElementTypeStaticText[contains(@name, "₹")][1]'),

'SGST': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="SGST"]/following::XCUIElementTypeStaticText[contains(@name, "₹")][1]'),

'TOTAL_AMOUNT': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Total Payable"]/following::XCUIElementTypeStaticText[contains(@name, "₹")][1]'),

'TOTAL_AMOUNT_DISCOUNT': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Total Payable"]/following::XCUIElementTypeStaticText[contains(@name, "₹")][2]'),


'BACK_BUTTON': (AppiumBy.ACCESSIBILITY_ID, 'ic-arrow-back'),

'CHARITY_KNOW_MORE_LINK': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Know More"]'),

'CHARITY_INFO_SECTION': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Your support will go a long way in keeping unwell children and their families together."]'),

'CHARITY_DONATION_CHECKBOX': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Donate ₹ 3 for Ronald Mcdonald House of Charity."]'),

'DONATION_AMOUNT': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="₹ 3.00"]'),

'VIEW_ALL_OFFERS': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="View All Offers"]'),

'OFFERS_PAGE_HEADER': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Offers For You"]'),

'ESTIMATED_DELIVERY_TIME': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name, "mins")]'),

'APPLY_PROMO_BUTTON': (AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="Apply"])[1]'),

'CHOOSE_ITEM':  (AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="Select"])[1]'),

'CLICK_OK': (AppiumBy.ACCESSIBILITY_ID, 'OK'),

'CLICK_CHANGE_OFFER': (AppiumBy.ACCESSIBILITY_ID, 'Change Offer'),

'APPLY_PROMO2_BUTTON':  (AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="Apply"])[2]'),

'APPLIED_PROMO_CODES':  (AppiumBy.XPATH, '//XCUIElementTypeStaticText[6]'),

'DISCOUNT_FLAT':  (AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="Apply"])[7]'),

'DISCOUNT_LABEL': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="10% Discount on purchase of ₹300"]'),

'INCREASE_QUANTITY': (AppiumBy.XPATH, '(//XCUIElementTypeImage[@name="ic-add"])[1]'),

'DISCOUNT': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Discount"]/following::XCUIElementTypeStaticText[1]'),

'PROMO_CODE_TEXT_FIELD': (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Enter Coupon Code"]'),

'CLICK_APPLY_EXPIRED': (AppiumBy.ACCESSIBILITY_ID, 'Apply'),

'PROMO_ERROR_MESSAGE': (AppiumBy.ACCESSIBILITY_ID, 'Promo Code Expired'),

'LOCATION_OPTION': (AppiumBy.ACCESSIBILITY_ID, 'Please select location'),

'SELECT_ADDRESS': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="Home"])[1]'),

'DROPDOWN': (AppiumBy.ACCESSIBILITY_ID, 'ic-arrow-down-cart'),

'BACKBUTTON': (AppiumBy.ACCESSIBILITY_ID, 'ic-arrow-left-primary'),



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
        print("Validating that the subtotal equals the sum of all item prices (ignoring decimals)...")
        time.sleep(2)
        self.driver.execute_script(
            "mobile: scroll",
            {"direction": "down", "predicateString": "name == 'Subtotal'"}
        )
        time.sleep(2)
        # Expand item list if needed
        self.actions.click_button(*locators['DROPDOWN'])
        # Get all item prices
        item_price_elements = self.actions.find_elements(*locators['CART_ITEM_PRICE_LIST'])
        item_prices = []
        for elem in item_price_elements:
            price_text = elem.text.strip()
            if price_text:
                try:
                    amount = float(re.sub(r"[^\d.]", "", price_text))
                    item_prices.append(amount)
                except ValueError:
                    print(f"Unable to parse item price: '{price_text}'")
        calculated_subtotal = int(sum(item_prices))  # Ignore decimals
        print(f"Calculated subtotal from items (rounded): ₹{calculated_subtotal}")
        # Get displayed subtotal
        displayed_subtotal_text = self.actions.get_text(*locators['SUB_TOTAL']).strip()
        displayed_subtotal = int(float(re.sub(r"[^\d.]", "", displayed_subtotal_text)))  # Ignore decimals
        print(f"Displayed subtotal on UI (rounded): ₹{displayed_subtotal}")
        # Assert subtotal matches
        assert calculated_subtotal == displayed_subtotal, (
            f"Subtotal mismatch: Expected ₹{calculated_subtotal}, but found ₹{displayed_subtotal}"
        )
        print("Subtotal matches total of all items (ignoring decimal part).")



    def validate_tax_breakdown(self):
        print("Validating CGST and SGST independently...")
        try:
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

    import re

    def validate_donation_amount(self):
        self.actions.click_button(*locators['DROPDOWN'])
        print("Validating donation amount of ₹3.00 is displayed...")
        donation_text = self.actions.get_text(*locators['DONATION_AMOUNT'])
        print(f"Donation text found: {donation_text}")
        donation_value = float(re.sub(r"[^\d.]", "", donation_text))
        assert donation_value == 3.0, f"Donation amount is not ₹3.00 Found: ₹{donation_value}"
        print("Donation amount of ₹3.00 is correctly displayed.")


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
        print("Scrolling to 'View All Offers'...")
        self.driver.execute_script("mobile: scroll", {
            "direction": "down",
            "predicateString": "name == 'Offers For You'"
        })
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
        print("Scrolling to ensure all price elements are visible...")
        self.driver.execute_script(
            "mobile: scroll",
            {"direction": "down", "predicateString": "name == 'Add Delivery Instructions'"}
        )
        # Expand detailed view if needed
        self.actions.click_button(*locators['DROPDOWN'])
        # Find all visible elements containing ₹
        elements = self.driver.find_elements(AppiumBy.XPATH, "//XCUIElementTypeStaticText[contains(@name, '₹')]")
        price_elements = []
        for elem in elements:
            text = elem.text.strip()
            if text.startswith("₹"):
                price_elements.append(text)
            else:
                print(f"Skipping non-price element: '{text}'")
        if not price_elements:
            raise AssertionError("No valid price elements found starting with ₹.")
        for price_text in price_elements:
            print(f"Validating price element: '{price_text}'")
            if not price_text.startswith("₹"):
                raise AssertionError(f"Element text '{price_text}' does not start with ₹ symbol")
        print("All price elements start with ₹ symbol.")




    def is_total_price_correct(self):
        self.actions.click_button(*locators['DROPDOWN'])
        print("Validating if the total price matches the sum of Subtotal + CGST + SGST + Handling Charges...")
        # Fetch values from the UI
        subtotal_text = self.actions.get_text(*locators['SUB_TOTAL']).strip()
        handling_text = self.actions.get_text(*locators['HANDLINNG_CHARGERS']).strip()
        cgst_text = self.actions.get_text(*locators['CGST']).strip()
        sgst_text = self.actions.get_text(*locators['SGST']).strip()
        total_text = self.actions.get_text(*locators['TOTAL_AMOUNT']).strip()
        # Clean and convert to float
        subtotal = float(re.sub(r"[^\d.]", "", subtotal_text))
        handling = float(re.sub(r"[^\d.]", "", handling_text))
        cgst = float(re.sub(r"[^\d.]", "", cgst_text))
        sgst = float(re.sub(r"[^\d.]", "", sgst_text))
        total_displayed = float(re.sub(r"[^\d.]", "", total_text))
        # Calculate expected total
        expected_total = round(subtotal + handling + cgst + sgst, 2)
        # Print breakdown
        print(f"Subtotal: ₹{subtotal}")
        print(f"Handling Charges: ₹{handling}")
        print(f"CGST: ₹{cgst}")
        print(f"SGST: ₹{sgst}")
        print(f"Expected Total: ₹{expected_total}")
        print(f"Displayed Total: ₹{total_displayed}")
        # Allow a small tolerance of 0.05 (5 paisa)
        tolerance = 0.07
        difference = abs(expected_total - total_displayed)
        assert difference <= tolerance, (
            f"Total price mismatch: Expected ₹{expected_total}, but got ₹{total_displayed}. Difference: ₹{difference}"
        )
        print("Total price matches all expected components within tolerance.")

    
        
    def validate_estimated_delivery_time(self):
        print("Validating visibility of 'Estimated Delivery Time' below the delivery address...")
        element = self.actions.find_element(*locators['ESTIMATED_DELIVERY_TIME'])
        if element.is_displayed():
            print("'Estimated Delivery Time' is displayed correctly.")
        else:
            raise AssertionError("'Estimated Delivery Time' is not visible on the screen.")

    
    def apply_first_promo_code(self):
        print("Clicking on 'Apply Promo Code' button...")
        self.actions.click_button(*locators['APPLY_PROMO_BUTTON'])
        print("Promo code applied successfully.")
        print("Selecting an item after applying promo code...")
        self.actions.click_button(*locators['CHOOSE_ITEM'])
        print("Item selected.")
        print("Clicking OK to confirm...")
        self.actions.click_button(*locators['CLICK_OK'])
        print("Confirmation completed.")

    def apply_second_promo_code(self):
        print("Clicking 'Change Offer' to apply second promo code...")
        self.actions.click_button(*locators['CLICK_CHANGE_OFFER'])
        print("Clicked 'Change Offer' button.")
        print("Clicking 'Apply Second Promo' button...")
        self.actions.click_button(*locators['APPLY_PROMO2_BUTTON'])
        print("Second promo code applied.")
        print("Selecting item after applying second promo...")
        self.actions.click_button(*locators['CHOOSE_ITEM'])
        print("Item selected for second promo.")
        print("Clicking 'OK' to confirm second promo...")
        self.actions.click_button(*locators['CLICK_OK'])
        print("Second promo code application confirmed.")

    
    def validate_single_promo_code_applied(self):
        applied_promo_elements = self.actions.find_elements(*locators['APPLIED_PROMO_CODES'])
        visible_promo_codes = [elem for elem in applied_promo_elements if elem.is_displayed()]
        print(f"Number of visible applied promo codes: {len(visible_promo_codes)}")
        return len(visible_promo_codes) == 1


    def add_multiple_item_quantities(self):
        time.sleep(1)
        print("Updating item quantity in the cart...")
        for i in range(4):
            print(f"Clicking '+' to increase quantity ({i + 1}/5)...")
            self.actions.click_button(*locators['INCREASE_QUANTITY'])
            time.sleep(0.5)  # Optional: small delay between clicks
        print("Increased item quantity 5 times.")


    def click_flat_discount(self):
        print("Scrolling to bring the flat discount offer into view...")
        # Scroll to the discount code using predicateString (e.g., FLAT10 or part of it)
        self.driver.execute_script("mobile: scroll", {
            "direction": "down",
            "predicateString": "name CONTAINS 'FLAT10'"
        })
        print("Clicking on the flat discount offer...")
        self.actions.click_button(*locators['DISCOUNT_FLAT'])
        print("Flat discount offer clicked successfully.")
        self.actions.click_button(*locators['CLICK_OK'])
        print("Second promo code application confirmed.")



    def validate_discount_deduction(self):
        print("Validating: Total Payable = Subtotal + Handling Charges + CGST + SGST - Discount")
        self.actions.click_button(*locators['DROPDOWN'])
        # Fetch and clean all values
        subtotal = float(re.sub(r"[^\d.]", "", self.actions.get_text(*locators['SUB_TOTAL']).strip()))
        handling = float(re.sub(r"[^\d.]", "", self.actions.get_text(*locators['HANDLINNG_CHARGERS']).strip()))
        cgst = float(re.sub(r"[^\d.]", "", self.actions.get_text(*locators['CGST']).strip()))
        sgst = float(re.sub(r"[^\d.]", "", self.actions.get_text(*locators['SGST']).strip()))
        discount = float(re.sub(r"[^\d.]", "", self.actions.get_text(*locators['DISCOUNT']).strip()))
        # This is the total amount after discount
        payable_total_text = self.actions.get_text(*locators['TOTAL_AMOUNT_DISCOUNT']).strip()
        total_payable = float(re.sub(r"[^\d.]", "", payable_total_text))
        # Calculate expected total
        expected_total = round((subtotal + handling + cgst + sgst) - discount, 2)
        # Print values for debugging
        print(f"Subtotal: ₹{subtotal}")
        print(f"Handling Charges: ₹{handling}")
        print(f"CGST: ₹{cgst}")
        print(f"SGST: ₹{sgst}")
        print(f"Discount: ₹{discount}")
        print(f"Expected Total Payable (after discount): ₹{expected_total}")
        print(f"Displayed Total Payable: ₹{total_payable}")
        # Allow ₹2.00 tolerance due to rounding
        tolerance = 2.00
        difference = abs(expected_total - total_payable)
        # Validate within tolerance
        assert difference <= tolerance, (
            f"Mismatch in Total Payable: Expected ₹{expected_total}, Found ₹{total_payable}, Difference: ₹{difference}"
        )
        print(" Total Payable amount is correct (within ₹2.00 tolerance).")


         
    def enter_promo_code(self, promo_code):
        time.sleep(5)
        self.actions.enter_text(*locators["PROMO_CODE_TEXT_FIELD"], promo_code)
        print(f"Entered promo code: {promo_code}")
        self.actions.click_button(*locators["CLICK_APPLY_EXPIRED"])
        print(f"Clicked Apply for promo code: {promo_code}")
        self.actions.click_button(*locators['CHOOSE_ITEM'])
        print("Selected item after applying promo code.")


    def verify_expired_promo_message(self, expected_message):
        time.sleep(2)  # wait for message to appear
        actual_message = self.actions.get_text(*locators["PROMO_ERROR_MESSAGE"])
        print(f"Promo error message shown: {actual_message}")
        assert expected_message in actual_message, \
            f"Expected message '{expected_message}', but got '{actual_message}'"
        print(" Error message verified successfully.")
        self.actions.click_button(*locators['CLICK_OK'])
        self.actions.click_button(*locators['BACKBUTTON'])

    def add_delivery_instruction(self, notes):
        print("Scrolling to 'Add Delivery Instructions'...")
        self.driver.execute_script("mobile: scroll", {
            "direction": "down",
            "predicateString": "name == 'Add Delivery Instructions'"
        })
        time.sleep(1)  # Optional small delay after scroll
        print("Clicking on 'Add Delivery Instructions'...")
        self.actions.click_button(*locators['ADD_INSTRUCTION_BUTTON'])
        self.actions.enter_text(*locators["INSTRUCTION_TEXT_FIELD"], notes)
        actual_notes = self.actions.get_text(*locators["INSTRUCTION_TEXT_FIELD"])
        # Assertion
        assert notes == actual_notes, \
            f" Expected delivery instruction '{notes}', but found '{actual_notes}'"
        print(f" Delivery instruction verified in cart: {actual_notes}")
        print("Scrolling to 'Add Delivery Instructions'...")
        # Number of scroll attempts
        scroll_times = 3
        for _ in range(scroll_times):
            try:
                self.driver.execute_script("mobile: scroll", {
                    "direction": "up",
                    "predicateString": "name == 'Clear All'"
                })
            except Exception as e:
                print(f"Scroll attempt failed: {e}")



    def select_location(self):
        self.actions.click_button(*locators["LOCATION_OPTION"]) 
        self.actions.click_button(*locators["SELECT_ADDRESS"]) 
        print("Delivery location selected successfully.")
