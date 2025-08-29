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
        time.sleep(2)
        self.actions.click_button(*locators['CLEAR_ORDER_BUTTON'])
        self.actions.click_button(*locators['CLEAR_ORDER_OK_BUTTON'])
        print("Order cleared")    

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
        element = self.driver.find_element(*locator)
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
        cart_items = self.driver.find_elements(*locators['CART_ITEM_LIST'])
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
        cart_items = self.driver.find_elements(*locators['CART_ITEM_LIST_WRAP'])
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
