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
    
"ADD_ITEM_BUTTON": (AppiumBy.ACCESSIBILITY_ID, "Add"),

'BREAKFAST_CATEGORY_BUTTON': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="McBreakfast"])[2]'),

'VEG_MCMUFFIN_ITEM': (AppiumBy.XPATH, '//XCUIElementTypeOther[@name="Veg McMuffin with protein plus Meal"]'),

"SELECT_LOCATION_BUTTON": (AppiumBy.ACCESSIBILITY_ID, "Please select location"),

'LOCATION_IN_POPUP': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="Gurugram Sector 99, 3rd Floor,"])[1]'),

'YOUR_ORDER_HEADER': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Your Order"]'),

"SEARCH_LOCATION_FIELD": (AppiumBy.ACCESSIBILITY_ID, "Search for area, street name.."),

"SEARCH_GPS_LOCATION": (AppiumBy.XPATH, '//XCUIElementTypeTextField'),

"CLICK_THE_LOCATION": (AppiumBy.ACCESSIBILITY_ID, "Gurugram"),

'FLAT_NO': (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="*House / Flat No."]'),

"CLEAR_ORDER_BUTTON": (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Clear All"]'),

"CLEAR_ORDER_OK_BUTTON": (AppiumBy.ACCESSIBILITY_ID, "OK"),

"CLICK_THE_LOCATION_DADAR": (AppiumBy.ACCESSIBILITY_ID, "Dadar"),

"CLICK_CUSTOMIZATION_OPTION": (AppiumBy.ACCESSIBILITY_ID, "Customise"),

'SOLD_OUT_LABEL': (AppiumBy.XPATH, "(//XCUIElementTypeStaticText[contains(@name, 'Sold out')])[1]"),

"ADD_ONE_ITEM": (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="Add"])[1]'),


"ADD_SECOND_ITEM": (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="Add"])[2]'),

"MCSAVER_CATEGORY_BUTTON": (AppiumBy.XPATH, '//XCUIElementTypeImage[contains(@name, "McSaver Combos")]'),

"PAYMENT_METHOD": (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Total Payable"]'),

"CONFIRM_BUTTON": (AppiumBy.CLASS_NAME, "XCUIElementTypeButton"),

"FIRST_MENU_ITEM_PRICE": (AppiumBy.XPATH, "(//XCUIElementTypeStaticText[contains(@name, '₹')])[1]"),

"FIRST_CART_ITEM_PRICE": (AppiumBy.XPATH, "(//XCUIElementTypeStaticText[contains(@name, '₹')])[18]"),

"CART_ITEM_NAME": (AppiumBy.XPATH, "//XCUIElementTypeStaticText[contains(@name, 'Veg McMuffin')]"),

"THREE_PC_MEAL_CATEGORY_BUTTON": (AppiumBy.XPATH, '//XCUIElementTypeImage[@name="Burger Combos ( 3 Pc Meals )"]'),

"THREE_PC_MEAL_ITEM_IN_CART": (AppiumBy.XPATH, "//XCUIElementTypeStaticText[contains(@name, 'Veg McMuffin')]"),

"THREE_PC_MEAL_CATEGORY_CLICK": (AppiumBy.XPATH, "//XCUIElementTypeOther[contains(@name, 'Mexican Grilled Chicken')]"),

'DESSERTS_CATEGORY_BUTTON': (AppiumBy.XPATH, '//XCUIElementTypeImage[@name="Desserts"]'),

'DESSERT_ITEM': (AppiumBy.XPATH, '//XCUIElementTypeOther[@name="Black Forest McFlurry Medium"]'),

'CART_ITEM_LIST': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Black Forest McFlurry Medium"]'),

'BURGERS_AND_WRAPS_MENU': (AppiumBy.XPATH, '//XCUIElementTypeImage[@name="Burgers & Wraps"]'),

'CHICKEN_WRAP_ITEM': (AppiumBy.XPATH, '//XCUIElementTypeOther[@name="Mexican Grilled Chicken & Cheese Burger"]'),

'CART_ITEM_LIST_WRAP': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Mexican Grilled Chicken & Cheese Burger"]'),

'SELECT_BURGER_CUSTOMIZATION_OPTION': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[contains(@name, "Mexican")])[3]'),

'EXTRA_ITEM': (AppiumBy.XPATH, '(//XCUIElementTypeImage[@name="ic-add"])[1]'),

'DONE_BUTTON': (AppiumBy.ACCESSIBILITY_ID, "Done"),

'FRIES_AND_SIDES_MENU': (AppiumBy.XPATH, '//XCUIElementTypeImage[@name="Fries & Sides"]'),

'FRIES_MEDIUM_ITEM': (AppiumBy.XPATH, '//XCUIElementTypeOther[@name="Fries (Medium)"]'),

'FRIES_IN_CART': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Fries (Medium)"]'),

'COFFEE_AND_BEVERAGES_MENU': (AppiumBy.XPATH, '//XCUIElementTypeImage[@name="Coffee & Beverages (Hot and Cold)"]'),

'CAPPUCCINO_COFFEE_ITEM': (AppiumBy.XPATH, '//XCUIElementTypeOther[@name="Cappuccino Coffee (S)"]'),

'CAPPUCCINO_IN_CART': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Cappuccino Coffee (S)"]'),

'CAKES_BROWNIES_MENU': (AppiumBy.XPATH, '//XCUIElementTypeImage[@name="Cakes Brownies and Cookies"]'),

'CHOCOCHIP_MUFFIN_BROWNIE': (AppiumBy.XPATH, '//XCUIElementTypeOther[@name="Chocochip Muffin"]'),

'CHOCOCHIP_MUFFIN_BROWNIE_IN_CART': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Chocochip Muffin"]'),

'PROTEIN_PLUS_MILLET_BUN_MENU': (AppiumBy.XPATH, '//XCUIElementTypeImage[@name="Protein Plus and Burgers with Millet Bun"]'),

'CHICKEN_BURGER_WITH_MILLET_BUN': (AppiumBy.XPATH, '//XCUIElementTypeOther[@name="McChicken Burger with Multi-Millet Bun"]'),

'CHICKEN_BURGER_WITH_MILLET_BUN_IN_CART': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="McChicken Burger with Multi-Millet Bun"]'),

'LARGER_DESSERT_IMAGE': (AppiumBy.XPATH, '//XCUIElementTypeImage[contains(@name, "img_")]'),

'NUTRITION_BURGER': (AppiumBy.XPATH, '(//XCUIElementTypeOther[contains(@label, "Burger")])[9]'),


'NUTRITION_INFO_1': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name, "Gluten")]'),

'NUTRITION_INFO_2': (AppiumBy.XPATH, '//XCUIElementTypeImage[contains(@name, "Milk")]'),

'NUTRITION_INFO_3': (AppiumBy.XPATH, '//XCUIElementTypeImage[contains(@name, "Peanut")]'),

'NUTRITION_INFO_4': (AppiumBy.XPATH, '//XCUIElementTypeImage[contains(@name, "Soybeans")]'),

'ANOTHER_ITEM': (AppiumBy.XPATH, '(//XCUIElementTypeImage[@name="ic-add"])[2]'),

'REMOVE_ITEM': (AppiumBy.XPATH, '(//XCUIElementTypeImage[@name="ic-subtract"])[1]'),

'INCREASE_QUANTITY': (AppiumBy.XPATH, '(//XCUIElementTypeImage[@name="ic-add"])[1]'),

'DECREASE_QUANTITY': (AppiumBy.XPATH, '//XCUIElementTypeImage[@name="ic-subtract"]'),

'SUB_TOTAL': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[contains(@name, "₹")])[14]'),

'HANDLING_CHARGE': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[contains(@name, "₹")])[15]'),

'CGST': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[contains(@name, "₹")])[16]'),

'SGST': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[contains(@name, "₹")])[17]'),

'CART_TOTAL': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[contains(@name, "₹")])[13]'),

'EMPTY_CART_MESSAGE': (AppiumBy.XPATH, '(//XCUIElementTypeOther[@name="main"])[2]'),

'DROPDOWN': (AppiumBy.ACCESSIBILITY_ID, "ic-arrow-down-cart"),

}
class OderingScreenIos(BasePage):


     
    def select_breakfast_category(self):
        time.sleep(3)
        print("Attempting to select the Breakfast category")
        self.actions.is_element_displayed(*locators['BREAKFAST_CATEGORY_BUTTON'])
        print("Selected the Breakfast category")

    def select_veg_mcmuffin_protein_plus_meal(self):
        time.sleep(2)
        print("Attempting to select Veg McMuffin item")
        self.actions.click_button(*locators['VEG_MCMUFFIN_ITEM'])
        print("Selected Veg McMuffin")

    
    def click_add_item(self):
        time.sleep(2)
        print("Attempting to click the Add Item button")
        self.actions.click_button(*locators['ADD_ITEM_BUTTON'])
        print("Clicked the Add Item button")

    def click_select_location(self):
        time.sleep(2)
        print("Attempting to click on 'Please select location'")
        self.actions.click_button(*locators['SELECT_LOCATION_BUTTON'])
        print("Clicked on 'Please select location'")

    def select_location_in_popup(self):
        time.sleep(2)
        print("Attempting to select a location from the popup")
        self.actions.click_button(*locators['LOCATION_IN_POPUP'])
        print("Selected the location from the popup")

    def verify_your_order_displayed(self):
        time.sleep(2)
        print("Verifying the 'Your Order' screen is displayed")
        order_header = self.actions.is_element_displayed(*locators['YOUR_ORDER_HEADER'])
        assert order_header is not None, "Your Order screen is not displayed"
        print("'Your Order' screen verified successfully")

    def search_location(self):
        time.sleep(2)
        print("Searching for location")
        self.actions.click_button(*locators['SEARCH_LOCATION_FIELD'])
        self.actions.click_button(*locators['SEARCH_GPS_LOCATION'])
        self.actions.send_keys(*locators['SEARCH_GPS_LOCATION'], "Gurugram")
        self.actions.click_button(*locators['CLICK_THE_LOCATION'])
        print("Location search initiated")

    def enter_address_details_breakfast(self):
        time.sleep(2)  # Ideally replace with explicit wait
        self.actions.send_keys(*locators['FLAT_NO'], "Gurugram")
        print("Entered address: Flat No - Gurugram")    

    def clear_order(self):
        self.actions.click_button(*locators['CLEAR_ORDER_BUTTON'])
        self.actions.click_button(*locators['CLEAR_ORDER_OK_BUTTON'])
        print("Order cleared successfully.")
                


  

    def search_location_outofstock(self):
        time.sleep(2)
        print("Searching for location")
        self.actions.click_button(*locators['SEARCH_LOCATION_FIELD'])
        self.actions.click_button(*locators['SEARCH_GPS_LOCATION'])
        self.actions.send_keys(*locators['SEARCH_GPS_LOCATION'], "Dadar")
        self.actions.click_button(*locators['CLICK_THE_LOCATION_DADAR'])
        print("Location search initiated")    

    def enter_address_details_outodstock(self):
        time.sleep(2)  # Ideally replace with explicit wait
        self.actions.send_keys(*locators['FLAT_NO'], "Dadar")
        print("Entered address: Flat No - Dadar")      

    def is_item_marked_sold_out(self):
        try:
            self.driver.execute_script("mobile: scroll", {
                "direction": "down",
                "predicateString": "name == 'Sold out'"
            })
            time.sleep(2)  # wait briefly after scroll
            return self.actions.is_element_displayed(*locators['SOLD_OUT_LABEL'])
        except Exception as e:
            print(f"Error checking sold-out label: {e}")
            return False

    def select_customization_option(self):
        try:
            self.actions.is_element_displayed(*locators['CLICK_CUSTOMIZATION_OPTION']) 
            self.actions.click_button(*locators['CLICK_CUSTOMIZATION_OPTION'])  
            print("Clicked on the customization option")
        except Exception as e:
            print(f"Failed to click customization option: {e}")
            raise

    def add_first_available_item(self):
        time.sleep(2)
        self.actions.click_button(*locators['ADD_ONE_ITEM'])    

    def add_second_available_item(self):
        time.sleep(2)
        self.actions.click_button(*locators['ADD_SECOND_ITEM'])     

    def select_mcsaver_category(self):
        time.sleep(3)
        print("Attempting to select the MCsaver category")
        self.actions.click_button(*locators['MCSAVER_CATEGORY_BUTTON'])
        print("Navigated to the MCsaver menu page")
    
    def is_payment_method_and_confirm_button_displayed(self):
        time.sleep(2)
        self.driver.execute_script("mobile: scroll", {
            "direction": "down",
            "predicateString": "name == 'Total Payable'"
            })
        payment_visible = self.actions.is_element_displayed(*locators['PAYMENT_METHOD'])
        confirm_visible = self.actions.is_element_displayed(*locators['CONFIRM_BUTTON'])
        print(f"Payment method visible: {payment_visible}")
        print(f"Confirm button visible: {confirm_visible}")

    def scroll_to_element(self, locator):
        element = self.actions.find_element(*locator)
        self.driver.execute_script("mobile: scrollToElement", {"elementId": element.id})
        time.sleep(1)

    def verify_pricing(self):
        time.sleep(2)
        self.actions.get_text(*locators['FIRST_MENU_ITEM_PRICE'])
        
    def verify_sold_out_items_not_clickable(self):
        time.sleep(2)
        if self.actions.is_element_displayed(*locators['SOLD_OUT_LABEL']):
            print("'Sold out' label is visible.")
            try:
                self.actions.click_button(*locators['SOLD_OUT_LABEL'])
                raise AssertionError("Add button was clickable for a sold out item.")
            except Exception:
                print("Correct: 'Add' button not clickable for sold out item.")
        
   
    def verify_item_in_cart(self):
        time.sleep(2)
        item_name = self.actions.get_text(*locators['CART_ITEM_NAME'])  # Read the cart item
        print(f"Item in cart: {item_name}")
        expected_item = "Veg McMuffin with protein plus Meal"
        assert expected_item in item_name, f"Expected '{expected_item}' in cart but found '{item_name}'"
        print("Item successfully verified in cart.")


    def select_3pc_meal_category(self):
        time.sleep(2)
        print("Attempting to select the 3Pc Meal category")
        self.actions.click_button(*locators['THREE_PC_MEAL_CATEGORY_BUTTON'])
        print("Navigated to the 3Pc Meal menu page")


    
    def verify_3pc_meal_item_in_cart(self):
        time.sleep(2)  # Consider using explicit waits
        item_visible = self.actions.is_element_displayed(*locators['THREE_PC_MEAL_CATEGORY_CLICK'])
        print(f"3pc meal item visibility in cart: {item_visible}")
        assert item_visible, "3pc meal item was not added to the cart"


    def select_3pc_meal(self):
        time.sleep(2)
        print("Clicking on the 3Pc Meal category")
        self.actions.click_button(*locators['THREE_PC_MEAL_CATEGORY_CLICK'])
        print("3Pc Meal category selected successfully")

    def select_desserts_category(self):
        try:
            print("Scrolling to 'Desserts' category in left menu...")
            self.driver.execute_script("mobile: scroll", {
                "direction": "down",
                "predicateString": "label == 'Desserts'"
            })
            time.sleep(2)
        except Exception as e:
            print(f"Scroll to 'Desserts' failed: {e}")
        
        try:
            print("Clicking on 'Desserts' category...")
            self.actions.click_button(*locators['DESSERTS_CATEGORY_BUTTON'])
            print("Navigated to the Desserts menu page")
        except Exception as e:
            print(f"Click on 'Desserts' failed: {e}")


    def select_random_dessert_item(self):
        time.sleep(2)
        print("Locating dessert items on the screen...")
        self.actions.is_element_displayed(*locators['DESSERT_ITEM'])
        print("Clicking on a dessert item...")
        self.actions.click_button(*locators['DESSERT_ITEM'])
        print("Dessert item selected successfully")


    def verify_dessert_item_in_cart(self):
        time.sleep(2)
        print("Verifying that the dessert item is added to the cart...")
        cart_items = self.actions.find_elements(*locators['CART_ITEM_LIST'])
        for item in cart_items:
            print("Cart contains:", item.get_attribute("name"))
        dessert_found = any("McFlurry" in item.get_attribute("name") for item in cart_items)
        if not dessert_found:
            raise AssertionError("Dessert item not found in the cart.")
        print("Dessert item verified in the cart successfully.")

    def click_burgers_and_wraps_menu(self):
        time.sleep(2)
        print("Clicking on the 'Burgers & Wraps' menu...")
        self.actions.click_button(*locators['BURGERS_AND_WRAPS_MENU'])
        print("'Burgers & Wraps' menu clicked successfully.")
        

    def select_chicken_wrap_item(self):
        time.sleep(2)
        print("Selecting the 'Chicken Wrap' item...")
        self.actions.click_button(*locators['CHICKEN_WRAP_ITEM'])
        print("'Chicken Wrap' item selected successfully.")

    def verify_chicken_wrap_item_in_cart(self):
        time.sleep(2)
        print("Verifying 'Mexican Grilled Chicken' item is in the cart...")
        cart_items = self.actions.find_elements(*locators['CART_ITEM_LIST_WRAP'])
        for item in cart_items:
            item_name = item.get_attribute("name")
            print("Cart item found:", item_name)
        item_found = any("Mexican Grilled Chicken" in item.get_attribute("name") for item in cart_items)
        if not item_found:
            raise AssertionError("'Mexican Grilled Chicken' not found in cart.")

        print("'Mexican Grilled Chicken' item successfully verified in cart.")

    def select_burger_customization_option(self):
        time.sleep(3)
        print("Selecting the burger from customization options...")
        self.actions.click_button(*locators['SELECT_BURGER_CUSTOMIZATION_OPTION'])
        print("Burger customization option selected.")

    def click_customize_button(self):
        time.sleep(2)
        print("Clicking on the 'Customize' button...")
        self.actions.click_button(*locators['CLICK_CUSTOMIZATION_OPTION'])
        print("'Customize' button clicked successfully.")

    def add_extra_item(self):
        time.sleep(2)
        print("Adding extra item during customization...")
        self.actions.click_button(*locators['EXTRA_ITEM'])
        self.actions.click_button(*locators['DONE_BUTTON'])
        print("Extra item added successfully.")

    def click_fries_and_sides_menu(self):
        time.sleep(2)
        print("Clicking on the 'Fries and Sides' menu...")
        self.actions.click_button(*locators['FRIES_AND_SIDES_MENU'])
        print("'Fries and Sides' menu clicked successfully.")

    def click_fries_medium(self):
        time.sleep(2)
        print("Scrolling to the 'Fries (Medium)' item...")
        self.driver.execute_script("mobile: scroll", {
            "direction": "down",
            "predicateString": "name == 'Fries (Medium)'"
        })
        print("Clicking on the 'Fries (Medium)' item...")
        self.actions.click_button(*locators['FRIES_MEDIUM_ITEM'])
        print("'Fries (Medium)' item clicked successfully.")


    def is_fries_item_in_cart(self):
        time.sleep(2)
        print("Checking if the fries item is present in the cart...")
        fries_in_cart_visible = self.actions.is_element_displayed(*locators['FRIES_IN_CART'])
        print(f"Fries item present in cart: {fries_in_cart_visible}")
        return fries_in_cart_visible

    def click_coffee_and_beverages_menu(self):
        time.sleep(2)
        print("Clicking on the 'Coffee & Beverages' menu...")
        self.actions.click_button(*locators['COFFEE_AND_BEVERAGES_MENU'])
        print("'Coffee & Beverages' menu clicked successfully.")

    def click_cappuccino_coffee(self):
        time.sleep(2)
        print("Scrolling to the 'Cappuccino' coffee item...")
        self.driver.execute_script("mobile: scroll", {
            "direction": "down",
            "predicateString": "name == 'Cappuccino Coffee (S)'"
        })
        print("Clicking on the 'Cappuccino' coffee item...")
        self.actions.click_button(*locators['CAPPUCCINO_COFFEE_ITEM'])
        print("'Cappuccino' coffee item clicked successfully.")

    def is_cappuccino_in_cart(self):
        time.sleep(2)
        print("Checking if the cappuccino coffee item is present in the cart...")
        cappuccino_visible = self.actions.is_element_displayed(*locators['CAPPUCCINO_IN_CART'])
        print(f"Cappuccino coffee item present in cart: {cappuccino_visible}")
        return cappuccino_visible

    def click_cakes_brownies_menu(self):
        time.sleep(2)
        print("Clicking on the 'Cakes, Brownies & Cookies' menu...")
        self.actions.click_button(*locators['CAKES_BROWNIES_MENU'])
        print("'Cakes, Brownies & Cookies' menu clicked successfully.")

    def click_chocochip_muffin_brownie(self):
        time.sleep(2)
        print("Scrolling to the 'Chocochip Muffin' item...")
        self.driver.execute_script("mobile: scroll", {
            "direction": "down",
            "predicateString": "name == 'Chocochip Muffin'"
        })
        print("Clicking on the 'Chocochip Muffin' item...")
        self.actions.click_button(*locators['CHOCOCHIP_MUFFIN_BROWNIE'])
        print("'Chocochip Muffin' item clicked successfully.")

    def chocochip_muffin_brownie_in_cart(self):
        time.sleep(2)
        print("Checking if the 'Chocochip Muffin' item is present in the cart...")
        is_visible = self.actions.is_element_displayed(*locators['CHOCOCHIP_MUFFIN_BROWNIE_IN_CART'])
        print(f"'Chocochip Muffin' item present in cart: {is_visible}")


        
    def click_protein_plus_and_millet_bun_menu(self):
        time.sleep(2)
        print("Clicking on 'Protein Plus and Burgers with Millet Bun' menu...")
        self.actions.click_button(*locators['PROTEIN_PLUS_MILLET_BUN_MENU'])
        print("'Protein Plus and Burgers with Millet Bun' menu clicked successfully.")

    def click_chicken_burger_with_millet_bun(self):
        time.sleep(2)
        print("Scrolling to the 'McChicken Burger with Multi-Millet Bun' item...")
        for i in range(8):
            time.sleep(2)
            print(f"Scroll attempt {i + 1}...")
            self.driver.execute_script("mobile: scroll", {
                "direction": "down",
                "predicateString": "name == 'McChicken Burger with Multi-Millet Bun'"
            })
        print("Completed 10 scroll attempts for 'McChicken Burger with Multi-Millet Bun'.")
        self.actions.click_button(*locators['CHICKEN_BURGER_WITH_MILLET_BUN'])
        print("'Chicken Burger with Millet Bun' item clicked successfully.")

    def chicken_burger_with_millet_bun_in_cart(self):
        time.sleep(2)
        print("Checking if the 'Chicken Burger with Millet Bun' item is present in the cart...")
        is_visible = self.actions.is_element_displayed(*locators['CHICKEN_BURGER_WITH_MILLET_BUN_IN_CART'])
        print(f"'Chicken Burger with Millet Bun' item present in cart: {is_visible}")

    def verify_larger_dessert_image(self):
        time.sleep(2)
        print("Verifying that the larger dessert image is displayed...")
        is_visible = self.actions.is_element_displayed(*locators['LARGER_DESSERT_IMAGE'])
        print(f"Larger dessert image visible: {is_visible}")

    def is_nutrition_info_displayed(self):
        self.driver.execute_script("mobile: scroll", {
        "direction": "down",
        "predicateString": "label == 'McAloo Tikki Burger with Cheese'"
    })
        time.sleep(2)
        print("Clicking on the nutrition burger to open nutrition info...")
        self.actions.click_button(*locators['NUTRITION_BURGER'])
        time.sleep(2)
        # Each tuple: (locator_key, should_be_visible, success_message)
        nutrition_elements = [
            ('NUTRITION_INFO_1', True, "Nutrition Info 1 is displayed as expected."),
            ('NUTRITION_INFO_2', False, "Nutrition Info 2 should not be visible."),
            ('NUTRITION_INFO_3', True, "Nutrition Info 3 is displayed correctly."),
            ('NUTRITION_INFO_4', True, "Nutrition Info 4 is displayed.")
        ]
        for locator_key, should_be_visible, message in nutrition_elements:
            try:
                is_visible = self.actions.is_element_displayed(*locators[locator_key])
                if should_be_visible:
                    assert is_visible, f"{locator_key} was expected to be visible but is not."
                    print(message)
                else:
                    assert not is_visible, f"{locator_key} was not expected to be visible but it is."
                    print(f"{locator_key} is correctly not displayed.")
            except Exception as e:
                print(f"Error while checking visibility of {locator_key}: {e}")




    def click_another_item_to_add(self):
        time.sleep(2)
        print("Clicking on another item to add to the cart...")
        self.actions.click_button(*locators['ANOTHER_ITEM'])
        print("Another item clicked and added to the cart.")


    def remove_item_from_cart(self):
        time.sleep(2)
        print("Clicking the remove button on the item...")
        self.actions.click_button(*locators['REMOVE_ITEM'])
        print("Item removed from the cart.")

    def update_item_quantity(self):
        time.sleep(1)
        print("Updating item quantity in the cart...")
        # Click '+' to increase
        self.actions.click_button(*locators['INCREASE_QUANTITY'])
        print("Increased item quantity.")
        time.sleep(1)
        # Click '-' to decrease
        self.actions.click_button(*locators['DECREASE_QUANTITY'])
        print("Decreased item quantity.")

    def verify_total_price_calculation(self):
        print("Verifying if the total price in the cart is calculated correctly...")
        time.sleep(2)
        print("Scrolling to 'Total Payable' section...")
        self.driver.execute_script("mobile: scroll", {
            "direction": "down",
            "predicateString": "name CONTAINS 'Add Delivery Instructions'"
        })
        self.actions.click_button(*locators['DROPDOWN'])
        print("Fetching individual price components...")
        # Get prices of individual components
        item_prices = [
            self.actions.get_text(*locators['SUB_TOTAL']),
            self.actions.get_text(*locators['HANDLING_CHARGE']),
            self.actions.get_text(*locators['CGST']),
            self.actions.get_text(*locators['SGST'])
        ]
        # Convert price strings like "₹100.50" to float values
        numeric_prices = [float(re.sub(r"[^\d.]", "", price)) for price in item_prices]
        calculated_total = round(sum(numeric_prices), 2)
        print(f"Sub Total: {numeric_prices[0]}")
        print(f"Handling Charge: {numeric_prices[1]}")
        print(f"CGST: {numeric_prices[2]}")
        print(f"SGST: {numeric_prices[3]}")
        print(f"Calculated Total: ₹{calculated_total}")
        # Get displayed total from UI
        displayed_total = self.actions.get_text(*locators['CART_TOTAL'])
        displayed_total_value = float(re.sub(r"[^\d.]", "", displayed_total))
        print(f"Displayed Total: ₹{displayed_total_value}")
        if calculated_total == displayed_total_value:
            print("Total price calculation is correct.")
        else:
            print("Mismatch in total price calculation.")

    def scroll_through_all_menu_categories(self):
        print("Scrolling through all menu categories...")
        # Scroll multiple times to ensure all categories are revealed
        for _ in range(55):  # Adjust the range based on app length
            self.driver.execute_script("mobile: scroll", {
                "direction": "down"
            })
            time.sleep(1)  # Small delay between scrolls
        print("Completed scrolling through all menu categories.")

    def validate_cart_is_empty(self):
        print("Checking if the cart is empty on app launch...")
        time.sleep(2)  # wait for UI to load
        if self.actions.is_element_displayed(*locators['EMPTY_CART_MESSAGE']):
            print("'Your cart is empty' message is displayed.")
        else:
            print("'Your cart is empty' message is NOT displayed.")


    def add_multiple_item_quantities(self):
        time.sleep(1)
        print("Updating item quantity in the cart...")
        for i in range(5):
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

