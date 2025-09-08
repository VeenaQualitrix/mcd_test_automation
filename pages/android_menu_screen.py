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
        "CUSTOMISE": (AppiumBy.XPATH, "(//android.widget.TextView[@text='Customise'])[1]"),
        "DONE_BUTTON": (AppiumBy.XPATH, "//android.widget.Button[@text='Done']"),
        "FRIES_AND_SIDES": (AppiumBy.XPATH, "//android.widget.Image[@text='Fries & Sides']"),
        "FRIES_MEDIUM_PRODUCT": (AppiumBy.XPATH, "//android.widget.TextView[@text='Fries (Medium)']"),
        "NEXT_BUTTON": (AppiumBy.XPATH, "//android.widget.Button[@text='Next']"),
        "MEXICAN_RANGE": (AppiumBy.XPATH, "//android.widget.TextView[@text='Mexican Range & New Offerings']"),
        "PRODUCT_PRICE_IN_CART": (AppiumBy.XPATH, "//android.widget.TextView[@text='{}']/following-sibling::android.widget.TextView"),
        "PRODUCT_PRICE_IN_MENU": (AppiumBy.XPATH, "//android.widget.TextView[@text='{}']/..//android.widget.TextView[contains(@text,'₹')]"),
        "BACK_BUTTON": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-arrow-left-primary']"),
        "DESSERTS_ITEM": (AppiumBy.XPATH, "//android.widget.TextView[@text='Hot Fudge Sundae']"),
        "DESSERTS_THUMBNAIL_IMAGE": (AppiumBy.XPATH, "//android.widget.Image[@text='Desserts']"),
        "ALL_PRODUCT_PRICES_IN_MENU": (AppiumBy.XPATH, "//android.widget.TextView[@text='{0}']/following-sibling::android.widget.TextView"),
        "COLD_COFFEE_PRODUCT": (AppiumBy.XPATH, "//android.widget.TextView[@text='Iced Coffee with French Vanilla']"),
        "COFFEE_AND_BEVERAGES_MENU": (AppiumBy.XPATH, "(//android.widget.TextView[@text='Coffee & Beverages (Hot and Cold)'])[1]"),
        "MILLET_BUN_MENU": (AppiumBy.XPATH, "//android.widget.TextView[@text='Protein Plus and Burgers with Millet Bun']"),
        "MILLET_BUN_DESCRIPTION": (AppiumBy.XPATH, "//android.widget.TextView[@text='Spice up your meal with a healthier bite! Try your McSpicy Paneer Burger with the nutritious multi-millet bun.']]"),
        "SOLD_OUT": (AppiumBy.XPATH, "//android.view.View[@text='Sold out']"),
        "DESSERT_CATEGORY": (AppiumBy.XPATH, "(//android.widget.TextView[@text='Desserts'])[2]"),
        "FRIES_CATEGORY": (AppiumBy.XPATH, "(//android.widget.TextView[@text='Fries & Sides'])[2]"),
       
    

         }


class AndroidMenuScreen(BasePage):

    def add_breakfast_item(self, item_name):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['MENU_HEADER'])
        print("Our Menu header is displayed")
        time.sleep(1)
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
        print("'ADD to Cart' is clicked")
    
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
        time.sleep(1)
        self.actions.click_button(*locators['BACK_BUTTON'])
        print("Back button is clicked from customise screen")

    def click_customise_option(self):
        time.sleep(1)
        self.actions.is_element_displayed(*locators['CUSTOMISE'])
        self.actions.click_button(*locators['CUSTOMISE'])
        print(" Customise button is clicked")

    def click_add_and_remove_sign_to_customised_item(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['ADD_QUANTITY'])
        self.actions.click_button(*locators['ADD_QUANTITY'])
        print(" add quantity button is clicked")
        time.sleep(3)
        self.actions.is_element_displayed(*locators['REMOVE_QUANTITY'])
        self.actions.click_button(*locators['REMOVE_QUANTITY'])
        print(" Remove quantity button is clicked")
        time.sleep(1)
        self.actions.click_button(*locators['DONE_BUTTON'])
        time.sleep(1)
        self.actions.click_button(*locators['ADD_TO_CART_BUTTON'])
        print("'ADD to Cart' is clicked")

    def add_multiple_items_to_cart(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['MENU_HEADER'])
        print("Our Menu header is displayed")
        time.sleep(1)

        self.actions.is_element_displayed(*locators['MEXICAN_RANGE'])
        self.actions.click_button(*locators['MEXICAN_RANGE'])

        # List of items to add
        item_names = [
            "Mexican Grilled Chicken & Cheese Burger",
            "Mexican Corn & Cheese Burger"
        ]

        for burger_name in item_names:
            by, value = locators['BURGER_XPATH']
            formatted_locator = (by, value.format(burger_name))
            self.actions.click_button(*formatted_locator)
            print(f"Clicked on item: {burger_name}")

            # Click on Add and Add to Cart for each item
            self.actions.click_button(*locators['ADD_BUTTON'])
            print("'Add' button is clicked")
            time.sleep(1)
            self.actions.click_button(*locators['NEXT_BUTTON'])
            time.sleep(1)
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

    def add_item_in_cart(self, item_name):
        """Click on menu item and add it to the cart."""
        time.sleep(2)
        self.actions.is_element_displayed(*locators['MENU_HEADER'])
        print("Our Menu header is displayed")

        # Click on Mexican Range
        self.actions.is_element_displayed(*locators['MEXICAN_RANGE'])
        self.actions.click_button(*locators['MEXICAN_RANGE'])
        print("Clicked on Mexican Range")

        # --- Ensure product is visible 
        by, value = locators['BURGER_XPATH']
        formatted_locator = (by, value.format(item_name))
        self.actions.is_element_displayed(*formatted_locator)

        # --- Fetch Menu Price ---
        by, value = locators['ALL_PRODUCT_PRICES_IN_MENU']
        price_locator = (by, value.format(item_name))
        menu_price_elements = self.driver.find_elements(*price_locator)

        menu_prices = [
            el.text.strip().replace(" ", "")
            for el in menu_price_elements
            if el.text.strip() and "₹" in el.text
        ]

        if not menu_prices:
            raise AssertionError(f"No valid price found for {item_name}, got: {[el.text for el in menu_price_elements]}")

        self.menu_price = menu_prices[-1]  # store menu price in the object
        print(f"[DEBUG] Final menu price considered for '{item_name}': {self.menu_price}")

        # --- Add item to cart ---
        self.actions.click_button(*formatted_locator)
        print(f"Clicked on item: {item_name}")
        self.actions.click_button(*locators['ADD_BUTTON'])
        self.actions.click_button(*locators['ADD_TO_CART_BUTTON'])
        print(f"'{item_name}' added to cart")

        return self.menu_price   # Return menu price for later comparison


    def verify_price_in_cart_matches_menu_price(self, product_name, menu_price):
        """Verify that cart price matches menu price passed as argument."""
        time.sleep(3)

        by, value = locators['PRODUCT_PRICE_IN_CART']
        cart_price_locator = (by, value.format(product_name))
        cart_price_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(cart_price_locator)
        )
        cart_price = cart_price_element.text.strip().replace(" ", "")
        print(f"[DEBUG] Cart price for '{product_name}': {cart_price}")
        print(f"[DEBUG] Expected menu price: {menu_price}")

        assert cart_price == menu_price, f"Price mismatch: Menu({menu_price}) != Cart({cart_price})"
        print("Price in cart matches the menu price!")


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

    def add_fries_in_cart(self):
        time.sleep(5)
        scrollable = 'new UiScrollable(new UiSelector().resourceId("background-content"))'
        item_text = "Fries (Medium)"
        max_scrolls = 5 
        item = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().resourceId("background-content"))'
            '.scrollIntoView(new UiSelector().textContains("Fries (Medium)"));'
        )
        item.click()
        print(" Clicked on Fries (Medium)")

        for i in range(max_scrolls):
            try:
                # Try to scroll to and find the item
                McChicken_3pc_meal = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'{scrollable}.scrollIntoView(new UiSelector().text("{item_text}"));'
                )
                McChicken_3pc_meal.click()
                print(f" Clicked on {item_text}")
                break
            except Exception:
                # If not found, scroll forward and retry
                self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'{scrollable}.scrollForward()'
                )
        else:
            raise Exception(f" Could not find {item_text} after {max_scrolls} scrolls")

        # Now click on Add button
        add_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators['ADD_BUTTON'])
        )
        add_btn.click()
        print(" 'Add' button is clicked")
        time.sleep(1)
        self.actions.click_button(*locators['NEXT_BUTTON'])
        time.sleep(1)
        self.actions.click_button(*locators['ADD_TO_CART_BUTTON'])
        print(" 'Add to cart' button is clicked")

    def Select_3PC_meals_menu(self):
        time.sleep(5)
        Select_3pc_meals = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollForward()'
            '.scrollIntoView(new UiSelector().textContains("Burger Combos ( 3 Pc Meals )"));'
        )

        Select_3pc_meals.click()
        print("Clicked on Burger Combos ( 3 Pc Meals )")

    def add_McChicken_meal_in_cart(self):
        time.sleep(3)  # Give time for the page to load fully

        scrollable = 'new UiScrollable(new UiSelector().resourceId("background-content"))'
        item_text = "Crispy Veggie Burger Meal (M)"
        max_scrolls = 10

        for i in range(max_scrolls):
            try:
                # Try to locate the element without scrolling first
                item = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiSelector().text("{item_text}")'
                )
                print(f"Found '{item_text}' on attempt {i+1}")
                item.click()
                print(f"Clicked on '{item_text}'")
                break
            except:
                print(f"Scroll attempt {i + 1}... Element not found yet, scrolling forward.")
                self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'{scrollable}.scrollForward()'
                )
        else:
            raise Exception(f"Could not find '{item_text}' after {max_scrolls} scrolls")

        # Wait for and click Add button
        add_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators['ADD_BUTTON'])
        )
        add_btn.click()
        print("'Add' button clicked")

        time.sleep(1)
        self.actions.click_button(*locators['ADD_TO_CART_BUTTON'])
        print("'Add to cart' button clicked")

    def Select_Desserts_menu(self):
            time.sleep(5)
            Select_Desserts = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true))'
                '.scrollIntoView(new UiSelector().textContains("Desserts"));'
            )

            Select_Desserts.click()
            print("Clicked on Desserts menu")

    def add_Desserts_product_in_cart(self):
        time.sleep(1)
        self.actions.is_element_displayed(*locators['DESSERTS_ITEM'])
        self.actions.click_button(*locators['DESSERTS_ITEM'])
        # Now click on Add button
        add_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators['ADD_BUTTON'])
        )
        add_btn.click()
        print(" 'Add' button is clicked")
        time.sleep(1)
        self.actions.click_button(*locators['NEXT_BUTTON'])
        time.sleep(1)
        self.actions.click_button(*locators['ADD_TO_CART_BUTTON'])
        print(" 'Add to cart' button is clicked")

    def verify_Desserts_thumnbnails_image_is_clearly_displayed(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['DESSERTS_THUMBNAIL_IMAGE'])
        print("The desserts thumbnails image is loded and clearly displayed under menu section")

    def Select_Burgers_and_wrap_menu(self):
        time.sleep(5)
        Select_Burgers_and_Wraps = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().textContains("Burgers & Wraps"));'
        )

        Select_Burgers_and_Wraps.click()
        print("Clicked on Burgers & Wraps menu")

    def add_Chicken_wrap_to_cart(self):
        time.sleep(5)
        scrollable = 'new UiScrollable(new UiSelector().resourceId("background-content"))'
        item_text = "Big Spicy Chicken Wrap"
        max_scrolls = 5   

        for i in range(max_scrolls):
            try:
                # Try to scroll to and find the item
                Big_Spicy_Chicken_Wrap = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'{scrollable}.scrollIntoView(new UiSelector().text("{item_text}"));'
                )
                Big_Spicy_Chicken_Wrap.click()
                print(f" Clicked on {item_text}")
                break
            except Exception:
                # If not found, scroll forward and retry
                self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'{scrollable}.scrollForward()'
                )
        else:
            raise Exception(f" Could not find {item_text} after {max_scrolls} scrolls")

        # Now click on Add button
        add_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators['ADD_BUTTON'])
        )
        add_btn.click()
        print(" 'Add' button is clicked")
        time.sleep(1)
        self.actions.click_button(*locators['NEXT_BUTTON'])
        time.sleep(1)
        self.actions.click_button(*locators['ADD_TO_CART_BUTTON'])
        print(" 'Add to cart' button is clicked")

    def Select_Coffee_and_beverages_menu(self):
        time.sleep(5)
        Select_Coffee_and_beverages = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().textContains("Coffee & Beverages (Hot and Cold)"));'
        )

        Select_Coffee_and_beverages.click()
        print("Clicked on Coffee & beverages menu")

    def add_cold_coffee_to_cart(self):
        time.sleep(1)
        self.actions.is_element_displayed(*locators['COLD_COFFEE_PRODUCT'])
        self.actions.click_button(*locators['COLD_COFFEE_PRODUCT'])
        time.sleep(1)
        self.actions.click_button(*locators['ADD_BUTTON'])
        print(" 'Add' button is clicked")

    def add_hot_coffee_to_cart(self):
        time.sleep(5)
        scrollable = 'new UiScrollable(new UiSelector().resourceId("background-content"))'
        item_text = "Hot Chocolate (S)"
        max_scrolls = 5  

        for i in range(max_scrolls):
            try:
                # Try to scroll to and find the item
                Hot_Chocolate = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'{scrollable}.scrollIntoView(new UiSelector().text("{item_text}"));'
                )
                Hot_Chocolate.click()
                print(f" Clicked on {item_text}")
                break
            except Exception:
                # If not found, scroll forward and retry
                self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'{scrollable}.scrollForward()'
                )
        else:
            raise Exception(f" Could not find {item_text} after {max_scrolls} scrolls")

        # Now click on Add button
        add_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators['ADD_BUTTON'])
        )
        add_btn.click()
        print(" 'Add' button is clicked")
        time.sleep(1)
        self.actions.click_button(*locators['ADD_TO_CART_BUTTON'])
        print(" 'Add to cart' button is clicked")
        time.sleep(1)
        self.actions.click_button(*locators['COFFEE_AND_BEVERAGES_MENU'])
        print(" 'Coffee & beverages' menu is clicked")

    def Select_Cakes_brownies_and_cookies_menu(self):
        time.sleep(5)
        Select_Cakes_brownies_and_cookies = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().textContains("Cakes Brownies and Cookies"));'
        )

        Select_Cakes_brownies_and_cookies.click()
        print("Clicked on Cakes Brownies and Cookies menu")


    def add_brownie_to_cart(self):
        time.sleep(5)
        scrollable = 'new UiScrollable(new UiSelector().resourceId("background-content"))'
        item_text = "Chocochip Muffin"
        max_scrolls = 10   # safety limit to avoid infinite scrolling

        for i in range(max_scrolls):
            try:
                # Try to scroll to and find the item
                muffin = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'{scrollable}.scrollIntoView(new UiSelector().text("{item_text}"));'
                )
                muffin.click()
                print(f" Clicked on {item_text}")
                break
            except Exception:
                # If not found, scroll forward and retry
                self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'{scrollable}.scrollForward()'
                )
        else:
            raise Exception(f" Could not find {item_text} after {max_scrolls} scrolls")

        # Now click on Add button
        add_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators['ADD_BUTTON'])
        )
        add_btn.click()
        print(" 'Add' button is clicked")

    def select_millet_bun_menu(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['MENU_HEADER'])
        print("Our Menu header is displayed")
        time.sleep(1)
        self.actions.is_element_displayed(*locators['MILLET_BUN_MENU'])
        self.actions.click_button(*locators['MILLET_BUN_MENU'])
        print("'Protein Plus and Burgers with Millet Bun' is clicked")

    def add_millet_bun_to_cart(self):
        time.sleep(5)
        scrollable = 'new UiScrollable(new UiSelector().resourceId("background-content"))'
        item_text = "McSpicy Paneer Burger with Multi-Millet Bun"
        max_scrolls = 10   # safety limit to avoid infinite scrolling

        for i in range(max_scrolls):
            try:
                # Try to scroll to and find the item
                Millet_bun = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'{scrollable}.scrollIntoView(new UiSelector().text("{item_text}"));'
                )
                Millet_bun.click()
                print(f" Clicked on {item_text}")
                break
            except Exception:
                # If not found, scroll forward and retry
                self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'{scrollable}.scrollForward()'
                )
        else:
            raise Exception(f" Could not find {item_text} after {max_scrolls} scrolls")

        # Now click on Add button
        add_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators['ADD_BUTTON'])
        )
        add_btn.click()
        print(" 'Add' button is clicked")
        time.sleep(1)
        self.actions.click_button(*locators['ADD_TO_CART_BUTTON'])
        print(" 'Add to cart' button is clicked")


    def click_on_millet_bun_burger(self):
        time.sleep(5)
        scrollable = 'new UiScrollable(new UiSelector().resourceId("background-content"))'
        item_text = "McSpicy Paneer Burger with Multi-Millet Bun"
        max_scrolls = 10   # safety limit to avoid infinite scrolling

        for i in range(max_scrolls):
            try:
                # Try to scroll to and find the item
                Millet_bun = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'{scrollable}.scrollIntoView(new UiSelector().text("{item_text}"));'
                )
                Millet_bun.click()
                print(f" Clicked on {item_text}")
                break
            except Exception:
                # If not found, scroll forward and retry
                self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'{scrollable}.scrollForward()'
                )
        else:
            raise Exception(f" Could not find {item_text} after {max_scrolls} scrolls")
        
    def verify_millet_bun_description_is_displayed(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['MILLET_BUN_DESCRIPTION'])
        print("Millet bun descrption is displayed")

    def add_sold_out_breakfast_item(self, item_name):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['MENU_HEADER'])
        print("Our Menu header is displayed")
        time.sleep(1)
        # Format burger/item locator dynamically
        by, value = locators['BURGER_XPATH']
        formatted_locator = (by, value.format(item_name))
        self.actions.click_button(*formatted_locator)
        print(f" Clicked on item: {item_name}")

    def verify_sold_out_option_is_displayed(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['SOLD_OUT'])
        print("The 'Sold out' is displayed and user unable to add item")
        self.driver.back()

    def verify_Desserts_category_is_accessble_via_scrolling(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['DESSERT_CATEGORY'])
        print("The desserts items is displayed after clicking the category")

    def verify_Fries_category_is_accessble_via_scrolling(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['FRIES_CATEGORY'])
        print("The Fries items is displayed after clicking the category")
       
       