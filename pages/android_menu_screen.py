from pages.base_page import BasePage
from pages.android_view_screen import AndroidViewScreen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import time

locators = {
        "MENU_HEADER": (AppiumBy.XPATH, "//android.widget.TextView[@text='Our Menu']"),
        "BURGER_XPATH": (AppiumBy.XPATH, "//android.widget.TextView[@text='{}']"),
        "SINGLE_ADD_BUTTON": (AppiumBy.XPATH, "//android.widget.TextView[@text=Add']"),
        "ADD_BUTTON": (AppiumBy.XPATH, "(//android.widget.TextView[@text='Add'])[1]"),
        "CUSTOMISE_MEAL": (AppiumBy.XPATH, "//android.widget.TextView[@text='Customise Your Meal']"),
        "ADD_TO_CART_BUTTON": (AppiumBy.XPATH, "//android.widget.Button[@text='Add to Cart']"),
        "YOUR_ORDER": (AppiumBy.XPATH, "//android.widget.TextView[@text='Your Order']"),
        "CLEAR_ALL": (AppiumBy.XPATH, "//android.widget.TextView[@text='Clear All']"),
        "TOTAL_CHARGES": (AppiumBy.XPATH, "//android.widget.TextView[@text='Total Charges']"),
        "TOTAL_PAYABLE": (AppiumBy.XPATH, "//android.widget.TextView[@text='Total Payable']"),
        "SUB_TOTAL": (AppiumBy.XPATH, "//android.widget.TextView[@text='Sub Total']"),
        "HANDLING_CHARGE": (AppiumBy.XPATH, "//android.widget.TextView[@text='Handling Charges']"),
        "CGST": (AppiumBy.XPATH, "//android.widget.TextView[@text='CGST']"),
        "SGST": (AppiumBy.XPATH, "//android.widget.TextView[@text='SGST']"),
        "3PC_MEALS": (AppiumBy.XPATH, "//android.widget.TextView[@text='Burger Combos ( 3 Pc Meals )']"),
        "3PC_MEALS_HEADER": (AppiumBy.XPATH, "(//android.widget.TextView[@text='Burger Combos ( 3 Pc Meals )'])[2]"),
        "3PC_MEALS_BURGER": (AppiumBy.XPATH, "//android.widget.TextView[@text='McChicken Burger Happy Meal']"),
        "ITEM_QUANTITY": (AppiumBy.XPATH, "//android.widget.TextView[@text='01']"),
        "ADD_QUANTITY": (AppiumBy.XPATH, "(//android.widget.Image[@text='ic-add'])[1]"),
        "REMOVE_QUANTITY": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-subtract']"),
        "CUSTOMISE": (AppiumBy.XPATH, "//android.widget.TextView[@text='Customise']"),
        "DONE_BUTTON": (AppiumBy.XPATH, "//android.widget.Button[@text='Done']"),
        "FRIES_AND_SIDES": (AppiumBy.XPATH, "//android.widget.Image[@text='Fries & Sides']"),
        "FRIES_MEDIUM_PRODUCT": (AppiumBy.XPATH, "//android.widget.TextView[@text='Fries (Medium)']"),
        "NEXT_BUTTON": (AppiumBy.XPATH, "//android.widget.Button[@text='Next']"),
        "MEXICAN_RANGE": (AppiumBy.XPATH, "//android.widget.TextView[@text='Mexican Range & New Offerings']"),
        "PRODUCT_PRICE_IN_CART": (AppiumBy.XPATH, "//android.widget.TextView[@text='{}']/following-sibling::android.widget.TextView"),
        "PRODUCT_PRICE_IN_MENU": (AppiumBy.XPATH, "//android.widget.TextView[@text='{}']/..//android.widget.TextView[contains(@text,'₹')]"),
    

         }


class AndroidMenuScreen(BasePage):
    
    def click_add_for_customise_item(self, item_name):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['MENU_HEADER'])
        print("Our Menu header is displayed")
        time.sleep(1)
        self.actions.is_element_displayed(*locators['MEXICAN_RANGE'])
        self.actions.click_button(*locators['MEXICAN_RANGE'])

        # Format burger/item locator dynamically
        by, value = locators['BURGER_XPATH']
        formatted_locator = (by, value.format(item_name))
        self.actions.click_button(*formatted_locator)
        print(f" Clicked on item: {item_name}")
        # Finally, click on Add button
        self.actions.click_button(*locators['ADD_BUTTON'])
        print(" 'Add' button is clicked")


    def verify_customise_option_appear(self):
        time.sleep(1)
        self.actions.is_element_displayed(*locators['CUSTOMISE_MEAL'])
        print("Customise your meal is displayed")

    def add_multiple_items_to_cart(self):
        time.sleep(2)
        # List of items to add
        item_names = [
            "Sausage McMuffin + Hashbrown",
            "Veg McMuffin + Hashbrown"
        ]
        for burger_name in item_names:
            self.click_add_for_customise_item(burger_name)
        time.sleep(2)
        self.actions.click_button(*locators['ADD_TO_CART_BUTTON'])
        print("'ADD to Cart' is clicked")

    def add_single_item_in_cart(self, item_name):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['MENU_HEADER'])
        print("Our Menu header is displayed")
        time.sleep(1)
        self.actions.is_element_displayed(*locators['MEXICAN_RANGE'])
        self.actions.click_button(*locators['MEXICAN_RANGE'])

        # Format burger/item locator dynamically
        by, value = locators['BURGER_XPATH']
        formatted_locator = (by, value.format(item_name))
        self.actions.click_button(*formatted_locator)
        print(f" Clicked on item: {item_name}")
        # Finally, click on Add button
        self.actions.click_button(*locators['ADD_BUTTON'])
        print(" 'Add' button is clicked")
        time.sleep(1)
        self.actions.click_button(*locators['ADD_TO_CART_BUTTON'])
        print(" 'Add to cart' button is clicked")

    def verify_price_in_cart_matches_menu_price(self, product_name="Mexican Grilled Chicken & Cheese Burger + Fries (M)"):
        time.sleep(2)

        # --- Get price from Cart ---
        by, value = locators['PRODUCT_PRICE_IN_CART']
        cart_price_locator = (by, value.format(product_name))
        cart_price_element = self.driver.find_element(*cart_price_locator)
        cart_price = cart_price_element.text.strip().replace(" ", "")
        print(f" Cart price for '{product_name}' is: {cart_price}")
        self.driver.back()
        time.sleep(1)
        self.actions.is_element_displayed(*locators['MEXICAN_RANGE'])
        self.actions.click_button(*locators['MEXICAN_RANGE'])

        # --- Get price from Menu ---
        by, value = locators['PRODUCT_PRICE_IN_MENU']
        menu_price_locator = (by, value.format(product_name))
        menu_price_element = self.driver.find_element(*menu_price_locator)
        menu_price = menu_price_element.text.strip().replace(" ", "")
        print(f"📋 Menu price for '{product_name}' is: {menu_price}")

        # --- Compare Prices ---
        assert cart_price == menu_price, f" Price mismatch: Menu({menu_price}) != Cart({cart_price})"
        print(" Price in cart matches the menu price.")

    def click_fries_and_sides_menu(self):
        time.sleep(5)
        Fries_and_slides = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().textContains("Fries & Sides"));'
        )

        # Click it
        Fries_and_slides.click()
        print("Clicked on fries & slides")
        #time.sleep(1)
        #self.actions.is_element_displayed(*locators['FRIES_AND_SIDES'])
        #self.actions.click_button(*locators['FRIES_AND_SIDES'])

    def add_fries_in_cart(self):
        time.sleep(2)
        Fries_medium = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().textContains("Fries (Medium)"));'
        )
        Fries_medium.click()
        print("Clicked on fries & slides")
        self.actions.click_button(*locators['ADD_BUTTON'])
        print(" 'Add' button is clicked")
        time.sleep(1)
        self.actions.click_button(*locators['NEXT_BUTTON'])
        time.sleep(1)
        self.actions.click_button(*locators['ADD_TO_CART_BUTTON'])
        print(" 'Add to cart' button is clicked")