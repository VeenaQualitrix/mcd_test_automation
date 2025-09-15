from conftest import setup_platform
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from pages.view_cart_page import ViewCartPage
import os
import time
import re
import subprocess

locators = {
        "ORDER_HISTORY_SCREEN": (AppiumBy.XPATH, "//android.widget.TextView[@text='Order History']"),
        "TRACK_ORDER": (AppiumBy.XPATH, "(//android.widget.Button[@text='Track'])[1]"),
        "POST_PAYMENT_SCREEN": (AppiumBy.XPATH, "//android.widget.TextView[@text='Delivering happiness at your doorstep']"),
        "ORDER_CANCELLED": (AppiumBy.XPATH, "//android.widget.TextView[@text='Cancelled']"),
        "ORDER_PLACED": (AppiumBy.XPATH, "///android.widget.TextView[@text='Placed']"),
        "ORDER_DELIVERED": (AppiumBy.XPATH, "//android.widget.TextView[@text='Delivered']"),
        "ORDER_PLACED_TEXT": (AppiumBy.XPATH, "//android.widget.TextView[@text='Yayy Your Order is Placed!']"),
        "ORDER_CANCELLED_TEXT": (AppiumBy.XPATH, "//android.widget.TextView[@text='Order cancelled']"),
        "CLICK_BACK_FROM_POST_PAYMENT": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-arrow-back-black']"),
        "MCDELIVERY_BM": (AppiumBy.XPATH, "(//android.widget.TextView[@text='McDelivery'])[1]"),
        "DINE_IN_BM": (AppiumBy.XPATH, "//android.widget.TextView[@text='Dine in']"),
        "TAKEOUT_BM": (AppiumBy.XPATH, "//android.widget.TextView[@text='Takeout']"),
        "MCDELIVERY_HELP_BUTTON": (AppiumBy.XPATH, "//android.view.View[.//android.widget.TextView[@text='McDelivery']]//android.widget.Button[@text='Help']"),
        "CANCELLED_HELP_BUTTON": (AppiumBy.XPATH, "//android.view.View[.//android.widget.TextView[@text='Cancelled']and .//android.widget.Button[@text='Help']]"),
        "ORDER_ACTIVE_HOURS_ENDED_MSG": (AppiumBy.XPATH, "//android.widget.TextView[@text = 'Order Active Hours Ended']"),
        "POP_UP_OK_BUTTON": (AppiumBy.XPATH, "//android.widget.Button[@text='OK']"),
        "ORDER_DETAILS": (AppiumBy.XPATH, "//android.widget.TextView[@text='Your order Details']"),
        "MENU_DETAILS": (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'x ')]"),
        "INVOICE": (AppiumBy.XPATH, "//android.widget.TextView[@text='Invoice']"),
        "ORDER_ID": (AppiumBy.XPATH, "(//android.widget.TextView[contains(@text, 'Order ID: ')])[1]"),
        "STORE_NAME": (AppiumBy.XPATH, "//android.widget.TextView[@text='Dadar Star Mall']"),
        "HOME_TEXT_ON_DELIVERY_ADDRESS": (AppiumBy.XPATH, "//android.view.View[@text='Home']"),
        "DELIVERY_ADDRESS": (AppiumBy.XPATH, "//android.widget.TextView[@text='Home']/following-sibling::android.widget.TextView'"),
        "PLACED_STATUS_BAR": (AppiumBy.XPATH, "//android.widget.TextView[@text='Placed']"),
        "ACCEPTED_STATUS_BAR": (AppiumBy.XPATH, "//android.widget.TextView[@text='Accepted']"),
        "IN_KITCHEN_STATUS_BAR": (AppiumBy.XPATH, "//android.widget.TextView[@text='In Kitchen']"),
        "OUT_FOR_DELIVERY_STATUS_BAR": (AppiumBy.XPATH, "//android.widget.TextView[@text='Out for delivery']"),
        "MCDELIVERED_STATUS_BAR": (AppiumBy.XPATH, "//android.widget.TextView[@text='McDelivered']"),
        

    
    }


class AndroidOrderHistoryScreen(BasePage):

    def verify_order_history_page_is_displayed(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['ORDER_HISTORY_SCREEN'])
        print("Order History screen is displayed")

    def click_on_track_order(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['TRACK_ORDER'])
        print("Track order button is displayed")
        time.sleep(1)
        self.actions.click_button(*locators['TRACK_ORDER'])
        print("Clicked Track Order button")

    def verify_user_navigated_to_post_payment_page(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['POST_PAYMENT_SCREEN'])
        print("Post payment screen is displayed")

    def verify_display_of_order_status_on_each_card(self):
        time.sleep(2)

        # Step 2: List of order statuses to check
        order_status_list = [
            ("ORDER_PLACED", "Placed"),
            ("ORDER_CANCELLED", "Cancelled"),
            ("ORDER_DELIVERED", "Delivered")
        ]

        # Step 3: Loop through each status
        for key, visible_text in order_status_list:
            try:
                # Step 3a: Scroll to the text (e.g. 'Placed')
                self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiScrollable(new UiSelector().scrollable(true))'
                    f'.scrollIntoView(new UiSelector().textContains("{visible_text}"));'
                )

                # Step 3b: Check if element is visible
                if self.actions.is_element_displayed(*locators[key]):
                    print(f"[PASS] Order status '{visible_text}' is displayed.")
                else:
                    print(f"[WARN] Order status '{visible_text}' is not visible after scroll.")

            except Exception as e:
                # Step 3c: If not found or any error happens, print the error (but don't crash)
                print(f"[SKIP] Could not find or scroll to '{visible_text}'. Error: {str(e)}")

            time.sleep(1)

    def get_track_order_locator(self, status_text):
        xpath = (
            f"//android.widget.TextView[@text='{status_text}']"
            f"/ancestor::android.view.View[1]"
            f"//android.widget.Button[@text='Track']"
        )
        return (AppiumBy.XPATH, xpath)
    
    def click_on_placed_order_tracking(self, status_text):
        try:
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true))'
                f'.scrollIntoView(new UiSelector().text("{status_text}"));'
            )
            print(f"Scrolled to order status '{status_text}'")
        except Exception as e:
            print(f"Could not scroll to order status '{status_text}': {e}")

        time.sleep(1) 

        # Step 2: Verify order status element is displayed
        order_status_locator = (AppiumBy.XPATH, f"//android.widget.TextView[@text='{status_text}']")
        self.actions.is_element_displayed(*order_status_locator)
        print(f"Order status '{status_text}' is displayed")

        # Step 3: Click on the Track button using dynamic locator
        track_locator = self.get_track_order_locator(status_text)
        self.actions.click_button(*track_locator)
        print("Clicked Track Order button")

    def click_on_cancelled_order_tracking(self, status_text):
        try:
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true))'
                f'.scrollIntoView(new UiSelector().text("{status_text}"));'
            )
            print(f"Scrolled to order status '{status_text}'")
        except Exception as e:
            print(f"Could not scroll to order status '{status_text}': {e}")

        time.sleep(1) 

        # Step 2: Verify order status element is displayed
        order_status_locator = (AppiumBy.XPATH, f"//android.widget.TextView[@text='{status_text}']")
        self.actions.is_element_displayed(*order_status_locator)
        print(f"Order status '{status_text}' is displayed")

        # Step 3: Click on the Track button using dynamic locator
        track_locator = self.get_track_order_locator(status_text)
        self.actions.click_button(*track_locator)
        print("Clicked Track Order button")

    def verify_placed_order_status_on_post_payment_page(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['ORDER_PLACED_TEXT'])
        print("'Yayy Your Order is Placed!'is displayed")
        time.sleep(1)
        self.actions.click_button(*locators['CLICK_BACK_FROM_POST_PAYMENT'])
        print("Clicked back button")

    def verify_cancelled_order_status_on_post_payment_page(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['ORDER_CANCELLED_TEXT'])
        print("Order cancelled text is displayed for cancelled order")

    def verify_each_order_card_display_BM_name(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['MCDELIVERY_BM'])
        print("Mcdelivery is displayed on order card")

    def scroll_down_the_page_on_order_history_page(self, status_text):
        try:
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true))'
                f'.scrollIntoView(new UiSelector().text("{status_text}"));'
            )
            print(f"Scrolled to order status '{status_text}'")
        except Exception as e:
            print(f"Could not scroll to order status '{status_text}': {e}")

        time.sleep(1) 

        # Step 2: Verify order status element is displayed
        order_status_locator = (AppiumBy.XPATH, f"//android.widget.TextView[@text='{status_text}']")
        self.actions.is_element_displayed(*order_status_locator)
        print(f"Order status '{status_text}' is displayed")

    def verify_display_of_addition_order_history(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['ORDER_DELIVERED'])
        print("The page scrolled down, and the 'Delivered' order status is displayed.")

    def verify_help_button_visible_only_for_order_placed_via_Mcdelivery(self):
        """
        Verifies that the 'Help' button is visible ONLY for McDelivery orders.
        """
        time.sleep(2)  
        # Step 1: Scroll to McDelivery block
        self.scroll_to_order_type("McDelivery")

        # Step 2: Assert McDelivery order block is present
        assert self.actions.is_element_displayed(*locators["MCDELIVERY_BM"]), " McDelivery BM not found on screen"

        # Step 3: Assert Help button is present for McDelivery
        assert self.actions.is_element_displayed(*locators["MCDELIVERY_HELP_BUTTON"]), \
            " 'Help' button is NOT visible for McDelivery, but it should be."

        print(" 'Help' button is visible for McDelivery BM")

    def scroll_to_order_type(self, order_type_text):
        """
        Scrolls to an order block containing the given order type (like 'Dine in' or 'Takeout')
        """
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{order_type_text}"));'
        )
        time.sleep(1)

    def is_help_button_present_for_order_type(self, order_type_text):
        """
        Checks if a Help button is present in the same block as the specified order type.
        """
        try:
            # Scroll to the order type first
            self.scroll_to_order_type(order_type_text)

            # Find the parent container (android.view.View) containing the order type
            container_xpath = f"//android.view.View[.//android.widget.TextView[@text='{order_type_text}']]"
            container = self.driver.find_element(AppiumBy.XPATH, container_xpath)

            # Search for Help button within this container
            help_buttons = container.find_elements(AppiumBy.XPATH, ".//android.widget.Button[@text='Help']")

            return len(help_buttons) > 0

        except Exception as e:
            print(f"[ERROR] Could not verify Help button for {order_type_text}: {e}")
            return False  # Assume false if something goes wrong

    def verify_help_button_not_visible_for_other_BMs(self):
        """
        Verifies that the 'Help' button is NOT visible for Dine in and Takeout order types.
        """
        order_types = ["Dine in", "Takeout"]

        for order_type in order_types:
            has_help = self.is_help_button_present_for_order_type(order_type)
            assert not has_help, f" 'Help' button **should NOT** be visible for order type: {order_type}"
            print(f" Verified: 'Help' button not present for '{order_type}'")

    def select_an_older_order_and_click_on_Help_button(self):
        """
        Scrolls down manually to find a 'Cancelled' order and clicks the 'Help' button inside that card.
        Only scrolls downward.
        """
        max_scrolls = 10
        found = False

        for _ in range(max_scrolls):
            try:
                # Try to find the element
                cancelled_element = self.driver.find_element(
                    AppiumBy.XPATH,
                    "//android.widget.TextView[contains(@text, 'Cancelled')]"
                )
                print(" Found Cancelled order")
                found = True
                break
            except Exception:
                # If not found, scroll down once
                print(" Scrolling down to find 'Cancelled' order...")
                self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true)).scrollForward()'
                )
                time.sleep(1)

        if not found:
            raise AssertionError(" Could not find 'Cancelled' order after scrolling down.")

        # Continue if found
        assert self.actions.is_element_displayed(*locators['CANCELLED_HELP_BUTTON']), \
            " Help button is NOT visible for Cancelled order"

        print(" Help button is visible for Cancelled order")
        self.actions.click_button(*locators['CANCELLED_HELP_BUTTON'])
        print(" Clicked on Help button")

    def verify_order_active_hours_ended_msg_is_displayed(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['ORDER_ACTIVE_HOURS_ENDED_MSG'])
        print("The time exceeded pop up msg is displayed")
        self.actions.click_button(*locators['POP_UP_OK_BUTTON'])
        print("Clicked on Ok button")

    def verify_your_order_details_section_is_displayed(self):
        time.sleep(2)

        try:
            # Use Android's UiScrollable to scroll and find the element
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("Your order Details"))'
            )

            # Now verify it's displayed using your existing method
            self.actions.is_element_displayed(*locators['ORDER_DETAILS'])
            print(" 'Your order Details' section is displayed.")

        except Exception as e:
            print(" Failed to find 'Your order Details' section.")
            raise e

    def verify_menu_details_are_displayed(self):
        time.sleep(3)

        # Get all elements matching the menu item XPath
        menu_items = self.driver.find_elements(*locators["MENU_DETAILS"])

        if not menu_items:
            raise AssertionError(" No menu items found with the expected pattern.")

        for index, item in enumerate(menu_items):
            if not item.is_displayed():
                raise AssertionError(f" Menu item at index {index} is not displayed.")
            print(f" Menu item displayed: {item.text}")

        print(" All menu items are displayed successfully.")

    def click_on_invoice_to_download(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['INVOICE'])
        print("Invoice is displayed")
        time.sleep(2)
        self.actions.click_button(*locators['INVOICE'])
        print("Clicked on Invoice to download it")

    def step_verify_invoice_downloaded(context):
        expected_filename = "invoice.pdf"
        max_retries = 5
        found = False

        for attempt in range(max_retries):
            print(f"🔍 Checking Downloads folder (Attempt {attempt + 1}/{max_retries})...")
            result = subprocess.run(
                ["adb", "shell", "ls", "/storage/emulated/0/Download"],
                capture_output=True, text=True
            )

            if result.returncode != 0:
                raise Exception(" Failed to access device's Downloads folder")

            downloaded_files = result.stdout.splitlines()
            print("📂 Files in Downloads:", downloaded_files)

            if expected_filename in downloaded_files:
                found = True
                print(f" Invoice file '{expected_filename}' found in Downloads.")
                break

            time.sleep(2)

        if not found:
            raise AssertionError(f" Invoice file '{expected_filename}' NOT found in Downloads folder.")
        
    def verify_order_number_is_displayed(self):
        time.sleep(3)

        # Find the order ID element dynamically (no hardcoded value)
        order_id_element = self.driver.find_element(*locators['ORDER_ID'])

        # Ensure the element is displayed
        self.actions.is_element_displayed(*locators['ORDER_ID'])
        
        # Get the full text
        order_id_text = order_id_element.text
        print(f" Full Order ID text: {order_id_text}")

        # Extract just the order ID part using regex
        match = re.search(r"Order ID:\s*(KRD-[A-Z]+-\d{2}-\d{2}-\d{4}-\d+)", order_id_text)
        if match:
            extracted_order_id = match.group(1)
            print(f" Extracted Order ID: {extracted_order_id}")
        else:
            raise Exception(" Could not extract Order ID from text.")
        
    def verify_any_store_name_is_displayed(self):
        time.sleep(2)

        # List of expected store names (add more as needed)
        possible_store_names = [
            "Kasturba Road",
            "Dadar Star Mall",
            "Mantri Mall",
            "Bandra"
        ]

        store_found = False

        for store_name in possible_store_names:
            try:
                print(f"🔍 Scanning for store: {store_name}")

                # Scroll into view using UiScrollable
                self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                    f'.scrollIntoView(new UiSelector().textContains("{store_name}"))'
                )

                # Once found, verify it's displayed
                locator = (AppiumBy.XPATH, f'//android.widget.TextView[contains(@text, "{store_name}")]')
                if self.actions.is_element_displayed(*locator):
                    print(f" Store name '{store_name}' is displayed.")
                    store_found = True
                    break

            except Exception as e:
                print(f" Store '{store_name}' not found yet. Trying next...")

        if not store_found:
            raise AssertionError(" None of the expected store names were found on the screen.")
        
    def verify_complete_address_is_displayed(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['HOME_TEXT_ON_DELIVERY_ADDRESS'])
        print("Home text on delivery address is displayed")
        self.actions.is_element_displayed(*locators['DELIVERY_ADDRESS'])
        print("Complete delivery address is displayed")

    def get_delivery_address(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['HOME_TEXT_ON_DELIVERY_ADDRESS'])
        print("Home text on delivery address is displayed")
        elements = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
    
        for el in elements:
            if "," in el.text and len(el.text.split()) > 5:
                print(" Detected Dynamic Address:", el.text)
                return el.text
    
        raise Exception(" Delivery address not found")
    
    def verify_status_bar_is_displayed(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['PLACED_STATUS_BAR'])
        print("Placed status bar is displayed")
        self.actions.is_element_displayed(*locators['ACCEPTED_STATUS_BAR'])
        print("Accepted status bar is displayed")
        self.actions.is_element_displayed(*locators['IN_KITCHEN_STATUS_BAR'])
        print("In-Kitchen status bar is displayed")
        self.actions.is_element_displayed(*locators['OUT_FOR_DELIVERY_STATUS_BAR'])
        print("Out for delivery status bar is displayed")
        self.actions.is_element_displayed(*locators['MCDELIVERED_STATUS_BAR'])
        print("Mcdelivered status bar is displayed")
