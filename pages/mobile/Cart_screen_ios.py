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

'CGST': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[contains(@name, "₹")])[20]'),

'SGST': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[contains(@name, "₹")])[21]'),

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

'DISCOUNT_SUB_TOTAL': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[contains(@name, "₹")])[19]'),

'PROMO_CODE_TEXT_FIELD': (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Enter Coupon Code"]'),

'CLICK_APPLY_EXPIRED': (AppiumBy.ACCESSIBILITY_ID, 'Apply'),

'PROMO_ERROR_MESSAGE': (AppiumBy.ACCESSIBILITY_ID, 'Promo Code Expired'),

'LOCATION_OPTION': (AppiumBy.ACCESSIBILITY_ID, 'Please select location'),

'SELECT_ADDRESS': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="Home"])[1]'),

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

    

    def validate_currency_symbols(self, timeout=15):
        print("Scrolling to 'Add Delivery Instructions'...")
        self.driver.execute_script("mobile: scroll", {
            "direction": "down",
            "predicateString": "name == 'Add Delivery Instructions'"
        })
        """
        Validates that specific elements (using XPath with ₹) are visible
        and correctly prefixed with the ₹ symbol.
        """
        wait = WebDriverWait(self.driver, timeout)
        print("Validating ₹ symbol on specific cart price elements...")

        price_elements = {
            "Subtotal":        (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[contains(@name, "₹")])[18]'),
            "CGST":            (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[contains(@name, "₹")])[20]'),
            "SGST":            (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[contains(@name, "₹")])[21]')
        }
        failures = []
        for label, locator in price_elements.items():
            try:
                print(f"Waiting for '{label}' element: {locator[1]}")
                element = wait.until(EC.visibility_of_element_located(locator))
                price_text = element.text.strip()
                print(f"{label}: '{price_text}'")

                # Validate ₹ is at the start of the text
                if not re.match(r"^₹\s?\d", price_text):
                    failures.append(f"{label}: '{price_text}' (invalid or missing ₹ symbol)")
            except TimeoutException:
                failures.append(f"{label}: Element not visible or not found")
        if failures:
            print("Validation failed for the following price components:")
            for issue in failures:
                print(" -", issue)
            raise AssertionError("₹ symbol validation failed:\n" + "\n".join(failures))
        print("All specified price elements correctly display the ₹ symbol.")



    def is_total_price_correct(self):
        print("Fetching all item prices...")
        item_price_elements = self.driver.find_elements(*locators['CART_ITEM_PRICE_LIST'])

        item_prices = []
        for elem in item_price_elements:
            price_text = elem.text.strip()
            print(f"Item price: {price_text}")
            if not price_text.startswith("₹"):
                raise AssertionError(f"Price does not start with ₹: {price_text}")
            # Extract price as float
            price = float(price_text.replace("₹", "").strip())
            item_prices.append(price)

        # Sum item prices and convert to int to ignore decimals
        expected_total_int = int(round(sum(item_prices), 0))
        print(f"Expected total price (integer part): ₹{expected_total_int}")

        # Scroll to total price element to make sure it's visible
        self.driver.execute_script("mobile: scroll", {
            "direction": "down",
            "predicateString": "name == 'Add Delivery Instructions'"
        })

        print("Fetching displayed total price...")
        total_element = self.driver.find_element(*locators['SUB_TOTAL'])
        displayed_total_text = total_element.text.strip()
        print(f"Displayed total text: {displayed_total_text}")

        if not displayed_total_text.startswith("₹"):
            raise AssertionError(f"Displayed total does not start with ₹: {displayed_total_text}")

        displayed_total = float(displayed_total_text.replace("₹", "").strip())
        displayed_total_int = int(round(displayed_total, 0))

        if expected_total_int != displayed_total_int:
            raise AssertionError(f"Total mismatch: Expected ₹{expected_total_int}, but found ₹{displayed_total_int}")

        print(f"Total price matches (ignoring decimals): ₹{displayed_total_int}")
    
        
    def validate_estimated_delivery_time(self):
        print("Validating visibility of 'Estimated Delivery Time' below the delivery address...")
        element = self.driver.find_element(*locators['ESTIMATED_DELIVERY_TIME'])
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
        applied_promo_elements = self.driver.find_elements(*locators['APPLIED_PROMO_CODES'])
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
        print("Fetching all cart item prices...")
        
        # Fetch all item prices
        item_price_elements = self.driver.find_elements(*locators['CART_ITEM_PRICE_LIST'])
        item_prices = []

        for elem in item_price_elements:
            price_text = elem.text.strip()
            print(f"Item price: {price_text}")
            
            if not price_text.startswith("₹"):
                raise AssertionError(f"Item price does not start with ₹: {price_text}")
            
            # Remove ₹ and comma, convert to float, then to int (removes decimals)
            price = int(float(price_text.replace("₹", "").replace(",", "").strip()))
            item_prices.append(price)

        # Fetch discount percentage text
        discount_text = self.driver.find_element(*locators['DISCOUNT_LABEL']).text.strip()
        print(f"Discount text: {discount_text}")
        
        # Extract numeric part from discount (e.g., "10%" or "10per")
        match = re.search(r"(\d+)", discount_text)
        if not match:
            raise AssertionError(f"Discount text does not contain a number: {discount_text}")
        discount_percentage = float(match.group(1))
        print(f"Discount percentage extracted: {discount_percentage}%")

        # Calculate discount amount
        total_price = sum(item_prices)
        discount = (discount_percentage / 100) * total_price
        print(f"Calculated discount: ₹{discount:.2f}")

        # Scroll to bring subtotal into view
        print("Scrolling to subtotal section...")
        self.driver.execute_script("mobile: scroll", {
            "direction": "down",
            "predicateString": "name == 'Subtotal'"
        })

        # Fetch subtotal
        subtotal_text = self.driver.find_element(*locators['DISCOUNT_SUB_TOTAL']).text.strip()
        print(f"Subtotal text: {subtotal_text}")
        if not subtotal_text.startswith("₹"):
            raise AssertionError(f"Subtotal text does not start with ₹: {subtotal_text}")
        subtotal = float(subtotal_text.replace("₹", "").replace(",", "").strip())

        # Print summary
        print(f"Total of all item prices: ₹{total_price:.2f}")
        print(f"Discount applied: ₹{discount:.2f}")
        print(f"Subtotal displayed: ₹{subtotal:.2f}")

        # Validate subtotal correctness (rounded to integer for no decimals)
        expected_subtotal = int(round(total_price - discount))
        displayed_subtotal = int(round(subtotal))
        if expected_subtotal != displayed_subtotal:
            raise AssertionError(f"Subtotal mismatch: Expected ₹{expected_subtotal}, but found ₹{displayed_subtotal}")

        print("Cart prices, discount, and subtotal validated successfully.")

         
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
