from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
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
        "MCCHICKEN_3PC_MEAL_ADDED": (AppiumBy.XPATH, "//android.widget.TextView[@text='Crispy Veggie Burger Meal (M)']"),
        "DESSERTS_PRODUCT_ADDED": (AppiumBy.XPATH, "//android.widget.TextView[@text='Hot Fudge Sundae']"),
        "WRAP_ITEM_ADDED": (AppiumBy.XPATH, "//android.widget.TextView[@text='Big Spicy Chicken Wrap']"),
        "CUSTOMISED_ITEM_ADDED": (AppiumBy.XPATH, "//android.widget.TextView[@text='Removed: Chipotle Sauce Added: Protein Slice']"),
        "COLD_COFFEE_ADDED": (AppiumBy.XPATH, "//android.widget.TextView[@text='Iced Coffee with French Vanilla']"),
        "HOT_COFFEE_ADDED": (AppiumBy.XPATH, "//android.widget.TextView[@text='Hot Chocolate (S)']"),
        "BROWNIE_PRODUCT_ADDED": (AppiumBy.XPATH, "//android.widget.TextView[@text='Chocochip Muffin']"),
        "MILLET_BUN_ADDED": (AppiumBy.XPATH, "//android.widget.TextView[@text='McSpicy Paneer Burger with Multi-Millet Bun']"),
        "TOTAL_PAYABLE": (AppiumBy.XPATH, "//android.widget.TextView[@text='Total Payable']/following-sibling::android.widget.TextView"),
        "DROP_DOWN_ICON": (AppiumBy.XPATH, "//android.widget.TextView[@text='Total Payable']/following-sibling::android.widget.TextView"),
        "REMOVE_ITEM_FROM_CART_PAGE" : (AppiumBy.XPATH, " (//android.widget.Image[@text='ic-subtract'])[1]"),
        "BURGER_XPATH": (AppiumBy.XPATH, "//android.widget.TextView[@text='{}']"),
        "MEXICAN_BURGER_ADDED": (AppiumBy.XPATH, "//android.widget.TextView[@text='Mexican Grilled Chicken & Cheese Burger + Fries (M)']"),
        "INCREASE_ITEM_QUANTITY_IN_CART" : (AppiumBy.XPATH, "(//android.widget.Image[@text='ic-add'])[1]"),
        "DECREASE_ITEM_QUANTITY_IN_CART" : (AppiumBy.XPATH, "//android.widget.Image[@text='ic-subtract']"),
        "ITEM_QUANTITY" : (AppiumBy.XPATH, "//android.widget.TextView[@text='02']"),
        "SUB_TOTAL" : (AppiumBy.XPATH, "//android.widget.TextView[@text='Sub Total']"),
        "HANDLING_CHARGES" : (AppiumBy.XPATH, "//android.widget.TextView[@text='Handling Charges']"),
        "CGST" : (AppiumBy.XPATH, "//android.widget.TextView[@text='CGST']"),
        "SGST" : (AppiumBy.XPATH, "//android.widget.TextView[@text='SGST']"),
        "ADD_DELIVERY_INSTRUCTIONS": (AppiumBy.XPATH, "//android.view.View[@text='Add Delivery Instructions ic-address__add']"),
        "NOTE_TEXT_AREA": (AppiumBy.XPATH, "//android.widget.EditText"),
        "RECOMMENDATION": (AppiumBy.XPATH, "//android.widget.TextView[@text='Recommendation']"),
        "RECOMMENDATION_ADD_BUTTON": (AppiumBy.XPATH, "(//android.widget.Image[@text='ic-add'])[1]"),
        "OFFERS_FOR_YOU": (AppiumBy.XPATH, "//android.widget.TextView[@text='Offers For You']"),
        "VIEW_ALL": (AppiumBy.XPATH, "//android.widget.TextView[@text='View All']"),
        "KNOW_MORE": (AppiumBy.XPATH, "//android.widget.TextView[@text='Know More']"),
        "DONATE_CHECKBOX_CHECKED": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-checkeddonate']"),
        "CHARITY_TEXT": (AppiumBy.XPATH, "//android.widget.TextView[@text='Donate ₹ 3 for Ronald Mcdonald House of Charity.']"),
        "CHARITY_INFO_HEADLINE": (AppiumBy.XPATH, "//android.widget.TextView[@text='Donate for Ronald Mcdonald House Charities']"),
        "CHARITY_INFO_DESCRIPTION": (AppiumBy.XPATH, "//android.widget.TextView[@text='Your support will go a long way in keeping unwell children and their families together.']"),
        "DONATION": (AppiumBy.XPATH, "//android.widget.TextView[@text='Donation']"),
        "DONATION_AMOUNT": (AppiumBy.XPATH, "//android.widget.TextView[@text='₹ 3.00']"),
        "DONATE_CHECKBOX_UNCHECKED": (AppiumBy.XPATH, "(//android.widget.TextView)[15]"),
        "ESTIMATED_DELIVERY_TIME_HEADLINE": (AppiumBy.XPATH, "//android.widget.TextView[@text='20 min delivery activated']"),
        "ESTIMATED_DELIVERY_TIME_TEXT": (AppiumBy.XPATH, "//android.widget.TextView[@text='Expect your order within 20 mins of ordering']"),
        "CLICK_BACK_BUTTON": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-arrow-back']"),
        "OFFER_APPLIED_TEXT": (AppiumBy.XPATH, "//android.widget.TextView[@text='Offer Applied!']"),
        "OFFER_CODE": (AppiumBy.XPATH, "//android.widget.TextView[@text='Offer Applied!']/following-sibling::android.widget.TextView[1]"),
        "CHANGE_OFFER": (AppiumBy.XPATH, "//android.widget.TextView[@text='Change Offer']"),
        "FIRST_OFFER_NAME": (AppiumBy.XPATH, "//android.widget.TextView[@text='SPD82AA49EE9040']"),
        "SECOND_OFFER_NAME": (AppiumBy.XPATH, "//android.widget.TextView[@text='SPDB28292DD88C1']"),


         }

class AndroidViewCartScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.initial_total = 0.0
        self.initial_prices = {}


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
    
    def verify_prices_breakdown_in_order_summary(self):
        time.sleep(2)

        # Step 1: Scroll to bottom where "Total Payable" is visible
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().textContains("Total Payable"));'
        )

        prices = {}
        labels = ['Sub Total', 'Handling Charges', 'CGST', 'SGST']

        for label in labels:
            # Create dynamic XPath using the label
            dynamic_xpath = (
                f"//android.widget.TextView[@text='{label}']/following-sibling::android.widget.TextView"
            )

            # Wait for element and fetch text
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, dynamic_xpath))
            )

            # Clean the price value and convert to float
            price_value = float(element.text.strip().replace('₹', '').strip())

            # Print label and price for debugging
            print(f"{label} price is: ₹{price_value}")

            # Store in dictionary with key as label in snake_case
            prices[label.lower().replace(' ', '_')] = price_value

        print("All prices fetched successfully:", prices)
        return prices
    
    def verify_display_of_charges_and_total_amount_in_order_summary(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['SUB_TOTAL'])
        print("Sub total is displayed")
        self.actions.is_element_displayed(*locators['HANDLING_CHARGES'])
        print("Handling charges is displayed")
        self.actions.is_element_displayed(*locators['CGST'])
        print("CGST is displayed")
        self.actions.is_element_displayed(*locators['SGST'])
        print("SGST is displayed")
        element = WebDriverWait(self.driver, 10).until(
             EC.visibility_of_element_located(locators['TOTAL_PAYABLE'])
        )
        # Extract and clean the amount text
        amount_text = element.text.strip().replace('₹', '').strip()
        total_amount = float(amount_text)
        print(f"Total Payable amount is: {total_amount}")

        self.driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true))'
        '.scrollIntoView(new UiSelector().text("Clear All"));'
    )

        return total_amount
    
    def scroll_to_add_delivery_instructions_and_click(self):
        time.sleep(2)

        # Step 1: Scroll to bottom where "Total Payable" is visible
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().textContains("SGST"));'
        )
        print("'Scrolled to Add Delivery Instructions' successfully.")

    def enter_notes_in_instructions_field(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['ADD_DELIVERY_INSTRUCTIONS'])
        print("Add sign is displayed")
        self.actions.click_button(*locators['ADD_DELIVERY_INSTRUCTIONS'])
        print("add sign button is clicked")
        time.sleep(3)
        self.actions.enter_text(*locators['NOTE_TEXT_AREA'], "Near Vipul Garden")
        print("Entered notes in instruction field")

    def verify_instructions_field_input(self):
        expected_text = "Near Vipul Garden"

        try:
            # Step 1: Fetch and verify the text in the instructions field
            actual_text = self.actions.get_element_attribute(*locators['NOTE_TEXT_AREA'], 'value')

            if actual_text and actual_text.strip() == expected_text:
                print("Instructions field accepted the input correctly.")
            else:
                print(f"Mismatch: Expected '{expected_text}', but found '{actual_text}'.")

            # Step 2: Scroll until "Clear All" is visible
            try:
                self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true))'
                    '.scrollIntoView(new UiSelector().text("Clear All"));'
                )
                print("Scrolled to 'Clear All' successfully.")
            except Exception as e:
                print(f"Could not scroll to 'Clear All': {str(e)}")

        except Exception as e:
            print(f"Exception while verifying input: {str(e)}")

    def verify_sub_total_for_single_added_item(self):
        time.sleep(2)

        # Step 1: Scroll to bottom where "Total Payable" is visible
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().textContains("Total Payable"));'
        )

        prices = {}
        labels = ['Sub Total']

        for label in labels:
            # Create dynamic XPath using the label
            dynamic_xpath = (
                f"//android.widget.TextView[@text='{label}']/following-sibling::android.widget.TextView"
            )

            # Wait for element and fetch text
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, dynamic_xpath))
            )

            # Clean the price value and convert to float
            price_value = float(element.text.strip().replace('₹', '').strip())

            # Print label and price for debugging
            print(f"{label} price is: ₹{price_value}")

            # Store in dictionary with key as label in snake_case
            prices[label.lower().replace(' ', '_')] = price_value

        print("All prices fetched successfully:", prices)
        return prices
    
    def add_item_from_recommendation(self):
        time.sleep(2)

        # Step 1: Scroll to bottom where "Total Payable" is visible
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().textContains("Recommendation"));'
        )
        print("Recommendation is displayed")
        self.actions.is_element_displayed(*locators['RECOMMENDATION_ADD_BUTTON'])
        self.actions.click_button(*locators['RECOMMENDATION_ADD_BUTTON'])
        print("'Add' button clicked.")
        time.sleep(2)
        # Final Add to Cart
        self.actions.is_element_displayed(*locators['ADD_TO_CART_BUTTON'])
        self.actions.click_button(*locators['ADD_TO_CART_BUTTON'])
        print("'ADD to Cart' is clicked")

    def verify_sub_total_for_all_added_item(self):
        prices = {}
        labels = ['Sub Total']

        for label in labels:
            # Create dynamic XPath using the label
            dynamic_xpath = (
                f"//android.widget.TextView[@text='{label}']/following-sibling::android.widget.TextView"
            )

            # Wait for element and fetch text
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, dynamic_xpath))
            )

            # Clean the price value and convert to float
            price_value = float(element.text.strip().replace('₹', '').strip())

            # Print label and price for debugging
            print(f"{label} price is: ₹{price_value}")

            # Store in dictionary with key as label in snake_case
            prices[label.lower().replace(' ', '_')] = price_value

        print("All prices fetched successfully:", prices)

        self.driver.back()  
        time.sleep(2)  
        return prices

    def Scroll_to_clear_all(self):
        time.sleep(2)
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().text("Clear All"));'
                )
        print("Scrolled to 'Clear All' successfully.")

    def verify_cgst_and_sgst_breakdown_in_order_summary(self):
        time.sleep(2)

        # Step 1: Scroll to bottom where "Total Payable" is visible
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().textContains("Total Payable"));'
        )

        prices = {}
        labels = ['CGST', 'SGST']

        for label in labels:
            # Create dynamic XPath using the label
            dynamic_xpath = (
                f"//android.widget.TextView[@text='{label}']/following-sibling::android.widget.TextView"
            )

            # Wait for element and fetch text
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, dynamic_xpath))
            )

            # Clean the price value and convert to float
            price_value = float(element.text.strip().replace('₹', '').strip())

            # Print label and price for debugging
            print(f"{label} price is: ₹{price_value}")

            # Store in dictionary with key as label in snake_case
            prices[label.lower().replace(' ', '_')] = price_value

        print("All prices fetched successfully:", prices)
        return prices
    
    def verify_tax_percentage_calculation(self):
        time.sleep(2)
        # Labels we need
        labels = ['Sub Total', 'CGST', 'SGST']
        prices = {}

        # Step 2: Dynamically fetch all required prices
        for label in labels:
            dynamic_xpath = (
                f"//android.widget.TextView[@text='{label}']/following-sibling::android.widget.TextView"
            )
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, dynamic_xpath))
            )

            # Convert to float after cleaning ₹ symbol
            price_value = float(element.text.strip().replace('₹', '').strip())
            prices[label.lower().replace(' ', '_')] = price_value
            print(f"{label} price fetched: ₹{price_value}")

        # Step 3: Calculate tax percentage
        subtotal = prices['sub_total']
        cgst = prices['cgst']
        sgst = prices['sgst']

        total_tax = cgst + sgst
        calculated_tax_percentage = (total_tax / subtotal) * 100

        print(f"\nSub Total: ₹{subtotal}")
        print(f"CGST: ₹{cgst}")
        print(f"SGST: ₹{sgst}")
        print(f"Total Tax: ₹{total_tax}")
        print(f"Calculated Tax Percentage: {calculated_tax_percentage:.2f}%")

        # Step 4: Validate tax percentage
        expected_tax_percentage = 6.0  # can be dynamic if needed
        tolerance = 0.1  # Allow a small margin for floating-point differences

        if abs(calculated_tax_percentage - expected_tax_percentage) <= tolerance:
            print(f" Tax percentage is correct: {calculated_tax_percentage:.2f}%")
        else:
            raise AssertionError(
                f" Tax percentage mismatch! "
                f"Expected: {expected_tax_percentage}%, "
                f"Calculated: {calculated_tax_percentage:.2f}%"
            )

        # Step 5: Go back to the previous screen
        print("Navigating back to the previous screen...")
        self.driver.back()
        time.sleep(1) 

    def click_know_more_link(self):
        time.sleep(2)

        # Step 1: Scroll to bottom where "Total Payable" is visible
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().textContains("Total Payable"));'
        )
        time.sleep(1)
        self.actions.is_element_displayed(*locators['KNOW_MORE'])
        self.actions.click_button(*locators['KNOW_MORE'])
        print("Know more link is clicked")

    def verify_charity_info_pop_up(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['CHARITY_INFO_HEADLINE'])
        self.actions.is_element_displayed(*locators['CHARITY_INFO_DESCRIPTION'])
        print("charity info description is displayed")
        self.driver.back()
        self.driver.back()
        time.sleep(1)

    def verify_charity_checkbox_is_selected(self):
        time.sleep(2)

        # Step 1: Scroll to bottom where "Total Payable" is visible
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().textContains("Total Payable"));'
        )
        time.sleep(1)
        self.actions.click_button(*locators['DONATE_CHECKBOX_UNCHECKED'])
        time.sleep(1)
        self.actions.is_element_displayed(*locators['DONATE_CHECKBOX_CHECKED'])
        print("Charity donate checkbox is checked")

    def verify_Donation_amount_added_in_payable_amount(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['DONATION'])
        print("Donation is displayed")
        self.actions.is_element_displayed(*locators['DONATION_AMOUNT'])
        print("Donation amount is displayed")
        time.sleep(1)
        self.driver.back()
        time.sleep(1)

    def uncheck_charity_checkbox(self):
        time.sleep(2)

        # Step 1: Scroll to bottom where "Total Payable" is visible
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().textContains("Total Payable"));'
        )
        time.sleep(1)
        self.actions.click_button(*locators['DONATE_CHECKBOX_UNCHECKED'])
        time.sleep(1)
        self.actions.is_element_displayed(*locators['DONATE_CHECKBOX_CHECKED'])
        print("Charity donate checkbox is checked")
        time.sleep(2)
        self.actions.click_button(*locators['DONATE_CHECKBOX_CHECKED'])
        print("Charity donate checkbox is clicked to uncheck it")
        time.sleep(1)
        self.actions.is_element_displayed(*locators['DONATE_CHECKBOX_UNCHECKED'])
        print("Charity donate checkbox is unchecked")

    def verify_donation_amount_removed_from_payable_amount(self):
        """
        Verifies that the donation label and donation amount
        are NOT visible on the screen.
        """
        time.sleep(5)  # Allow screen to load

        try:
            # Check if donation elements are visible
            is_donation_present = self.actions.is_element_displayed(*locators['DONATION'])
            is_donation_amount_present = self.actions.is_element_displayed(*locators['DONATION_AMOUNT'])
        except Exception:
            # If elements are not found at all, treat them as removed
            is_donation_present = False
            is_donation_amount_present = False

        # Assertions
        assert not is_donation_present, " Donation label is still displayed!"
        assert not is_donation_amount_present, " Donation amount is still displayed!"

        print("✅ Donation and donation amount are successfully removed from the payable section.")

        # Navigate back after verification
        self.driver.back()
        time.sleep(1)

    def click_view_all_link(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['VIEW_ALL'])
        print("View all link is displayed")
        time.sleep(1)
        self.actions.click_button(*locators['VIEW_ALL'])
        print("View all link is clicked")

    def verify_all_prices_prefixed_with_currency_symbol(self):
        """
        Verify that all dynamically fetched prices (Sub Total, CGST, SGST) 
        are prefixed with ₹, and navigate back after validation.
        """
        time.sleep(2)

        # Labels we need to check
        labels = ['Sub Total', 'Handling Charges', 'CGST', 'SGST']
        prices = {}

        try:
            for label in labels:
                # Step 1: Build dynamic XPath for each label
                dynamic_xpath = (
                    f"//android.widget.TextView[@text='{label}']/following-sibling::android.widget.TextView"
                )

                # Step 2: Wait for the element to be visible
                element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, dynamic_xpath))
                )

                # Fetch the raw text from the element
                text = element.text.strip()

                # Step 3: Verify the price is prefixed with ₹
                assert text.startswith('₹'), f" Price '{text}' for '{label}' is not prefixed with ₹"
                print(f" Verified: '{label}' price '{text}' is correctly prefixed with ₹")

                # Step 4: Convert text to float for further use
                price_value = float(text.replace('₹', '').strip())
                prices[label.lower().replace(' ', '_')] = price_value

            print(" All prices verified successfully.")

        except TimeoutException:
            raise AssertionError(f" Element with label '{label}' was not visible in time.")

        finally:
            # Step 5: Navigate back after validation
            print("Navigating back to the previous screen...")
            self.driver.back()
            time.sleep(1)

    def verify_estimated_delivery_time(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['ESTIMATED_DELIVERY_TIME_HEADLINE'])
        print("Estimated delivery time is displayed")
        time.sleep(1)
        self.actions.is_element_displayed(*locators['ESTIMATED_DELIVERY_TIME_TEXT'])
        print("Estimated delivery time along with text is displayed")

    def Click_back_button(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['CLICK_BACK_BUTTON'])
        self.actions.click_button(*locators['CLICK_BACK_BUTTON'])
        print("Back button clicked")

    def verify_applied_offer(self):
        try:
            time.sleep(5)
            
            # Verify "Offer Applied" section is visible
            self.actions.is_element_displayed(*locators['OFFER_APPLIED_TEXT'])

            # Wait for the dynamic offer code to be visible
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locators['OFFER_CODE'])
            )

            # Find the offer code element
            offer_element = self.driver.find_element(*locators['OFFER_CODE'])

            # Fetch the text dynamically
            offer_code = offer_element.text.strip()
            print(f"Fetched offer code: {offer_code}")

            return offer_code

        except Exception as e:
            print(f"Could not fetch or interact with the offer code: {e}")
            return None

    def verify_first_offer_is_removed_and_the_second_offer_is_displayed(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['OFFER_APPLIED'])
        print("offer applied text is displayed")
        if self.actions.is_element_displayed(*locators['APPLIED_OFFER_NAME']):
            print(" First offer is still displayed")
        else:
            print(" First offer is NOT displayed (as expected)")
        self.actions.is_element_displayed(*locators['APPLIED_SECOND_OFFER_NAME'])
        print("Second applied offer is displayed")
        time.sleep(1)
        self.driver.back()

    def increase_cart_item_multiple_times(self, times=4):
        time.sleep(5)
        if self.actions.is_element_displayed(*locators['INCREASE_ITEM_QUANTITY_IN_CART']):
            for i in range(times):
                self.actions.click_button(*locators['INCREASE_ITEM_QUANTITY_IN_CART'])
                print(f"Item increased in the cart: click {i+1}")
                time.sleep(1)

    def get_total_amount_from_order_summary(self):
        prices = self.verify_prices_breakdown_in_order_summary()
        self.initial_prices = prices
        self.initial_total = round(
            prices.get('sub_total', 0) +
            prices.get('handling_charges', 0) +
            prices.get('cgst', 0) +
            prices.get('sgst', 0), 2
        )
        print(f"Original total before discount: ₹{self.initial_total:.2f}")
        print(f"Breakdown: {self.initial_prices}")

        time.sleep(2)
        View_all = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().textContains("View All"));'
        )

        # Click it
        View_all.click()
        print("Clicked on view all")


    def verify_discount_is_applied_correctly(self):
        """Verify that discount has been applied after promo code"""
        if self.initial_total == 0.0:
            raise RuntimeError("Initial total not captured. Call capture_total_before_promo() first.")

        discounted_prices = self.verify_prices_breakdown_in_order_summary()
        discounted_total = round(
            discounted_prices.get('sub_total', 0) +
            discounted_prices.get('handling_charges', 0) +
            discounted_prices.get('cgst', 0) +
            discounted_prices.get('sgst', 0), 2
        )

        discount = round(self.initial_total - discounted_total, 2)

        print(f"Discounted breakdown: {discounted_prices}")
        print(f"Discounted total: ₹{discounted_total:.2f}")

        if discount > 0:
            print(f"✅ Discount applied successfully: ₹{discount:.2f}")
            handling_diff = round(self.initial_prices.get('handling_charges', 0) - discounted_prices.get('handling_charges', 0), 2)
            if handling_diff > 0:
                print(f"ℹ Handling charges reduced by: ₹{handling_diff:.2f}")
        else:
            raise AssertionError("❌ Discount not applied correctly. Total amount did not decrease.")

        time.sleep(1)
        self.driver.back()




        
        


        



    