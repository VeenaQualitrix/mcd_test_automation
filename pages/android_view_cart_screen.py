from pages.base_page import BasePage
from actions.android_actions import AndroidActions
from pages.android_view_screen import AndroidViewScreen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import time

locators = {
        "YOUR_ORDER": (AppiumBy.XPATH, "//android.widget.TextView[@text='Your Order']"),
        "ADD_BUTTON": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-add']"),
        "ADD_TO_CART_BUTTON": (AppiumBy.XPATH, "//android.widget.Button[@text='Add to Cart']"),
        "VIEW_CART": (AppiumBy.XPATH, "//android.widget.TextView[@text='View Cart']"),
        "LOGIN_FROM_CHECKOUT_PAGE": (AppiumBy.XPATH, "//android.widget.Button[@text='Log In / Sign Up to Continue']"),
        "CANCEL_FROM_LOGIN_PROMPT": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-close']"),
        "PRODUCT_PRIZE_IN_CART": (AppiumBy.XPATH, "//android.widget.TextView[@text='{}']/following-sibling::android.widget.TextView"),
        "FRIES_ADDED": (AppiumBy.XPATH, "//android.widget.TextView[@text='Fries (Medium)']"),
        "BREAKFAST_ITEM_ADDED": (AppiumBy.XPATH, "//android.widget.TextView[@text='Veg McMuffin with protein plus Meal']"),
        "CLEAR_ALL": (AppiumBy.XPATH, "//android.widget.TextView[@text='Clear All']"),
        "DELETE_CART": (AppiumBy.XPATH, "//android.widget.TextView[@text='Delete Cart']"),
        "OK": (AppiumBy.XPATH, "//android.widget.Button[@text='OK']"),
        "MCCHICKEN_3PC_MEAL_ADDED": (AppiumBy.XPATH, "//android.widget.TextView[@text='McChicken Burger Happy Meal']"),
        "DESSERTS_PRODUCT_ADDED": (AppiumBy.XPATH, "//android.widget.TextView[@text='Hot Fudge Sundae']"),
        "WRAP_ITEM_ADDED": (AppiumBy.XPATH, "//android.widget.TextView[@text='Big Spicy Chicken Wrap']"),
        "CUSTOMISED_ITEM_ADDED": (AppiumBy.XPATH, "//android.widget.TextView[@text='Removed: Chipotle Sauce Added: Protein Slice']"),
        "COLD_COFFEE_ADDED": (AppiumBy.XPATH, "//android.widget.TextView[@text='Iced Coffee with French Vanilla']"),
        "HOT_COFFEE_ADDED": (AppiumBy.XPATH, "//android.widget.TextView[@text='Hot Chocolate (S)']"),
        "BROWNIE_PRODUCT_ADDED": (AppiumBy.XPATH, "//android.widget.TextView[@text='Chocochip Muffin']"),
        "MILLET_BUN_ADDED": (AppiumBy.XPATH, "//android.widget.TextView[@text='McSpicy Paneer Burger with Multi-Millet Bun']"),
        "TOTAL_PAYABLE": (AppiumBy.XPATH, "//android.widget.TextView[@text='Total Payable']/following-sibling::android.widget.TextView"),
        "REMOVE_ITEM_FROM_CART_PAGE" : (AppiumBy.XPATH, " (//android.widget.Image[@text='ic-subtract'])[1]"),
        "BURGER_XPATH": (AppiumBy.XPATH, "//android.widget.TextView[@text='{}']"),
        "MEXICAN_BURGER_ADDED": (AppiumBy.XPATH, "//android.widget.TextView[@text='Mexican Grilled Chicken & Cheese Burger + Fries (M)']"),
        "INCREASE_ITEM_QUANTITY_IN_CART" : (AppiumBy.XPATH, "(//android.widget.Image[@text='ic-add'])[1]"),
        "DECREASE_ITEM_QUANTITY_IN_CART" : (AppiumBy.XPATH, "//android.widget.Image[@text='ic-subtract']"),
        "ITEM_QUANTITY" : (AppiumBy.XPATH, "//android.widget.TextView[@text='02']"),


         }

class AndroidViewCartScreen(BasePage):
    
    def Click_login_prompt_from_checkout(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['LOGIN_FROM_CHECKOUT_PAGE'])
        self.actions.click_button(*locators['LOGIN_FROM_CHECKOUT_PAGE'])
        time.sleep(2)
    
    def click_cancel_to_login_or_signup_page(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['CANCEL_FROM_LOGIN_PROMPT'])
        self.actions.click_button(*locators['CANCEL_FROM_LOGIN_PROMPT'])
        time.sleep(2)

    def verify_login_page_navigation_from_checkout(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['LOGIN_PAGE_HEADER_FROM_CHECKOUT'])
    
    def verify_redirect_to_checkout_page(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['YOUR_ORDER'])
    
    def verify_product_price_is_displayed_correct_in_cart(self, product_name="Mexican Grilled Chicken & Cheese Burger + Fries (M)"):
        time.sleep(2)
        by, value = locators['PRODUCT_PRIZE_IN_CART']
        cart_price_locator = (by, value.format(product_name))
        cart_price_element = self.driver.find_element(*cart_price_locator)
        cart_price = cart_price_element.text.strip().replace(" ", "")
        print(f" Cart price for '{product_name}' is: {cart_price}")

    def verify_fries_added_to_cart(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['FRIES_ADDED'])

    def verify_breakfast_item_added_to_cart(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['BREAKFAST_ITEM_ADDED'])

    def Clear_all_cart(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['CLEAR_ALL'])
        self.actions.click_button(*locators['CLEAR_ALL'])
        print("Clear all is clicked")
        self.actions.is_element_displayed(*locators['DELETE_CART'])
        print("Delete cart pop up is displayed")
        time.sleep(2)
        self.actions.click_button(*locators['OK'])
        print("Ok button is clicked")
        self.driver.quit()

    def verify_3pc_meal_item_added_to_cart(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['MCCHICKEN_3PC_MEAL_ADDED'])

    def verify_Desserts_item_added_to_cart(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['DESSERTS_PRODUCT_ADDED'])

    def verify_Wrap_item_added_to_cart(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['WRAP_ITEM_ADDED'])

    def verify_customised_item_is_displayed_to_cart(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['CUSTOMISED_ITEM_ADDED'])
        print("Removed: Chipotle Sauce Added: Protein Slice is displayed")

    def verify_cold_coffee_added_to_cart(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['COLD_COFFEE_ADDED'])
        print("Cold coffee added to cart")

    def verify_cold_coffee_and_hot_coffee_added_to_cart(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['COLD_COFFEE_ADDED'])
        print("Cold coffee added to cart")
        self.actions.is_element_displayed(*locators['HOT_COFFEE_ADDED'])
        print("Hot coffee added to cart")

    def verify_brownie_added_to_cart(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['BROWNIE_PRODUCT_ADDED'])
        print("Chocochip Muffin is added to cart")

    def verify_millet_bun_added_to_cart(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['MILLET_BUN_ADDED'])
        print("'McSpicy Paneer Burger with Multi-Millet Bun' is added to cart")
    

    def get_all_cart_items(self):
        time.sleep(2)  # wait for cart to load

        names = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Burger')]")
        prices = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '₹')]")
        quantities = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[contains(@resource-id, 'quantity') or @text='01']")

        cart_items = []
        for i in range(len(names)):
            name = names[i].text.strip()
            price = prices[i].text.strip() if i < len(prices) else "N/A"
            quantity = quantities[i].text.strip() if i < len(quantities) else "N/A"

            cart_items.append({"name": name, "price": price, "quantity": quantity})
            print(f"Item {i+1}: {name}, Price: {price}, Quantity: {quantity}")

        return cart_items
    
    def remove_cart_item(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['REMOVE_ITEM_FROM_CART_PAGE'])
        self.actions.click_button(*locators['REMOVE_ITEM_FROM_CART_PAGE'])
        print("Item removed from cart page")

    def Verify_selected_items_removed_from_cart(self, product_name="Mexican Corn & Cheese Burger"):
        time.sleep(2) 

        by, value = locators['BURGER_XPATH']
        formatted_locator = (by, value.format(product_name))

        # Try to find matching elements
        elements = self.driver.find_elements(*formatted_locator)

        if len(elements) == 0:
            print(f" Product '{product_name}' successfully removed from cart.")
            return True
        else:
            print(f" Product '{product_name}' is still present in cart.")
            return False

    def increase_cart_item(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['INCREASE_ITEM_QUANTITY_IN_CART'])
        self.actions.click_button(*locators['INCREASE_ITEM_QUANTITY_IN_CART'])
        print("Item increased in the cart after clicking add sign")

    def verify_item_quantity(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['ITEM_QUANTITY'])
        print("Item quantity updated from 1 to 2")

    def Verify_single_item_in_cart(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['MEXICAN_BURGER_ADDED'])
        print("'Mexican Grilled Chicken & Cheese Burger + Fries (M)' is added to cart")

    def Verify_total_payable_amount_is_displayed_in_cart_page(self):
        time.sleep(2)

        # Step 1: Scroll to bottom where "Total Payable" is visible
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().textContains("Total Payable"));'
        )

        # Step 2: Fetch the amount
        by, value = locators['TOTAL_PAYABLE']
        amount_element = self.driver.find_element(by, value)

        if amount_element.is_displayed():
            amount_text = amount_element.text.strip()
            print(f" Total payable amount is displayed: {amount_text}")
        else:
            print(" Total payable amount not found")
            amount_text = None

        # Step 3: Swipe back to top to click "View Cart"
        self.driver.back()
        return amount_text



    