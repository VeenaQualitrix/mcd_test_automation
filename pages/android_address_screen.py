from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

locators = {
        "SELECT_DELIVERY_ADDRESS_HEADER": (AppiumBy.XPATH, "//android.widget.TextView[@text='Select Delivery Address']"),
        "LOGIN_PROMPT": (AppiumBy.XPATH, "//android.widget.TextView[@text='Log In / Sign Up to Continue']"),
        "ADD_NEW": (AppiumBy.XPATH, "//android.widget.TextView[@text='Add new']"),
        "SEARCH_BUTTON": (AppiumBy.XPATH, "//android.widget.TextView[@text='Search for area, street name..']"),
        "SEARCH_INPUT_FIELD": (AppiumBy.CLASS_NAME, "android.widget.EditText"),
        "SELECT_ADDRESS": (AppiumBy.XPATH, "//android.view.View[@text='{}']"),
        "ADDRESS_SELECTED": (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '{}')]"),
        "FIRST_ADDRESS" : (AppiumBy.XPATH, "//android.widget.TextView[@text='Kasturba Road']"),
        "CONFIRM_LOCATION" : (AppiumBy.XPATH, "//android.widget.Button[@text='Confirm Location']"),
        "HOUSE_NUMBER" : (AppiumBy.XPATH, "//android.widget.EditText"),
        "SAVE_ADDRESS" : (AppiumBy.XPATH, "//android.widget.Button[@text='Save Address']"),
        "SAVE_AS_HOME_ADDRESS" : (AppiumBy.XPATH, "//android.widget.TextView[@text='Home']"),
        "SAVE_AS_WORK_ADDRESS" : (AppiumBy.XPATH, "//android.widget.TextView[@text='Work']"),
        "HOUSE_FIELD_EMPTY_ERROR":(AppiumBy.XPATH, "//android.widget.TextView[@text='Please enter valid House / Flat No.']"),
        "ADDRESS_SCREEN_HEADER" : (AppiumBy.XPATH, "//android.widget.TextView[@text='Building/Locality or nearby landmark']"),
        "ADDRESS_SAVED_WITH_SPECIAL_CHAR" : (AppiumBy.XPATH, "//android.widget.TextView[@text='%$^#@&*,']"),
        "ALL_ADDRESS" : (AppiumBy.XPATH, "//android.widget.TextView[@text='All Addresses']"),
        "CLICK_BACK_BUTTON" : (AppiumBy.XPATH, "(//android.widget.Image[@text='ic-arrow-left-primary'])[2]"),
        "CLICK_BACK_BUTTON_FROM_SELECT_LOCATION" : (AppiumBy.XPATH, "//android.widget.Image[@text='ic-arrow-left-primary']"),
        "ADDRESS_EDIT_ICON" : (AppiumBy.XPATH, "(//android.widget.Image[@text='ic-edit'])[1]"),
        "ADDRESS_DELETE_ICON" : (AppiumBy.XPATH, "(//android.widget.Image[@text='ic-delete'])[1]"),
        "DELETE_POP_UP" : (AppiumBy.XPATH, "//android.widget.TextView[@text='Delete Address']"),
        "CLICK_YES_BUTTON" : (AppiumBy.XPATH, "//android.widget.Button[@text='YES']"),
        "NEAR_LABEL" : (AppiumBy.XPATH, "//android.view.View[@text='Near :']"),
        "NEAR_LABEL_LAST_ADDRESS" : (AppiumBy.XPATH, "(//android.view.View[@text='Near : '])[2]"),
        "ADDRESS_SAVED_WITH_MAX_CHAR" : (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'AAAAAAA')]"),


}

class AndroidAddressScreen(BasePage):

    def hide_keyboard_by_tapping_outside(self):
        try:
            self.driver.hide_keyboard()
        except Exception:
            print("Native hide_keyboard failed, falling back to tap.")

        mobile_field = self.driver.find_element(*locators['HOUSE_NUMBER'])
        rect = mobile_field.rect

        tap_x = rect['x'] + rect['width'] // 2
        tap_y = rect['y'] + rect['height'] + 10  # just below the input

        self.actions.tap_on_coordinates(tap_x, tap_y)
    
    def verify_redirect_to_login_or_signup_page(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['LOGIN_PROMPT'])
    
    def click_login_prompt(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['LOGIN_PROMPT'])
        self.actions.click_button(*locators["LOGIN_PROMPT"])
        print("Clicked on Log In/ Sign up button")

    def verify_add_new_button_to_add_address(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['SELECT_DELIVERY_ADDRESS_HEADER'])
        self.actions.is_element_displayed(*locators['ADD_NEW'])
        print("Add new button is displayed to add new address")

    def search_for_address_after_selecting_business_model(self):
        time.sleep(2)
        self.actions.click_button(*locators['SEARCH_BUTTON'])
        time.sleep(2)
        self.actions.click_button(*locators['SEARCH_INPUT_FIELD'])
        self.actions.enter_text(*locators["SEARCH_INPUT_FIELD"], "Bengaluru")
        self.driver.press_keycode(66)  # KEYCODE_ENTER
        time.sleep(5)
        # Click the suggested address
        select_address_locator = (
            locators['SELECT_ADDRESS'][0],
            locators['SELECT_ADDRESS'][1].format("Bengaluru")
        )
        self.actions.is_element_displayed(*select_address_locator)
        self.actions.click_button(*select_address_locator)
        print("Suggested address clicked.")

        # Click the first address (confirmation or next step)
        self.actions.is_element_displayed(*locators['FIRST_ADDRESS'])
        self.actions.click_button(*locators['FIRST_ADDRESS'])
        print("First address clicked.")

    def search_for_address_after_selecting_Dine_In_model(self):
        time.sleep(2)
        self.actions.click_button(*locators['SEARCH_BUTTON'])
        time.sleep(2)
        self.actions.click_button(*locators['SEARCH_INPUT_FIELD'])
        self.actions.enter_text(*locators["SEARCH_INPUT_FIELD"], "Gurugram")
        self.driver.press_keycode(66)  # KEYCODE_ENTER
        time.sleep(5)
        # Click the suggested address
        select_address_locator = (
            locators['SELECT_ADDRESS'][0],
            locators['SELECT_ADDRESS'][1].format("Gurugram")
        )
        self.actions.is_element_displayed(*select_address_locator)
        self.actions.click_button(*select_address_locator)
        print("Suggested address clicked.")
        

    def verify_selected_address_is_displayed(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['FIRST_ADDRESS'])
        print("Kasturba Road address is displayed")

    def click_add_address_from_checkout(self):
        print("Checking and clicking address arrow.")
        self.actions.is_element_displayed(*locators['ADDRESS_ARROW'])
        self.actions.click_button(*locators['ADDRESS_ARROW'])
        print("Address arrow clicked.")
        time.sleep(2)


    def verify_address_appear_as_selected_delivery_address(self):
        try:
            WebDriverWait(self.driver, 10).until(
             EC.visibility_of_element_located(locators['SELECTED_DELIVERY_ADDRESS'])
        )
            is_displayed = self.actions.is_element_displayed(*locators['SELECTED_DELIVERY_ADDRESS'])
            assert is_displayed, "Selected delivery address is not displayed"
            return True
        except Exception as e:
            raise AssertionError(f"Validation failed: Selected delivery address did not appear. Details: {e}")
        
    def Click_add_new_button_and_confirm_location(self):
        time.sleep(1)
        self.actions.is_element_displayed(*locators['ADD_NEW'])
        self.actions.click_button(*locators['ADD_NEW'])
        time.sleep(2)
        self.actions.is_element_displayed(*locators['CONFIRM_LOCATION'])
        self.actions.click_button(*locators["CONFIRM_LOCATION"])
        print("Clicked Confirm Location Button")

    def verify_redirect_to_address_filling_page(self):
        time.sleep(2)
        return self.actions.is_element_displayed(*locators['ADDRESS_SCREEN_HEADER'])
    
    def _scroll_bottom_sheet_until_text(self, text, max_scrolls=8):
        """
        Scrolls *inside the bottom-sheet/inner ScrollView* until an element
        containing the given text is visible, then returns it.
        """
        # Try to grab the first scrollable container (the inner ScrollView/RecyclerView)
        container = None
        try:
            container = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().scrollable(true).instance(0)'
            )
        except Exception:
            pass

        for _ in range(max_scrolls):
            # Is the target visible now?
            try:
                el = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiSelector().textContains("{text}")'
                )
                if el.is_displayed():
                    return el
            except Exception:
                pass

            # Scroll *inside* the container if we found one, else do a screen swipe
            if container:
                self.driver.execute_script("mobile: scrollGesture", {
                    "elementId": container.id,
                    "direction": "down",
                    "percent": 0.9
                })
            else:
                size = self.driver.get_window_size()
                self.driver.swipe(
                    size['width'] * 0.5, size['height'] * 0.8,
                    size['width'] * 0.5, size['height'] * 0.3, 400
                )

        raise NoSuchElementException(f'Could not find "{text}" after scrolling.')
          
    def add_new_delivery_address(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['HOUSE_NUMBER'])
        self.actions.click_button(*locators["HOUSE_NUMBER"])
        print("Clicked on house textfield")
        time.sleep(1)
        self.actions.enter_text(*locators['HOUSE_NUMBER'], "Marathahalli village, HAL Airport road")
        time.sleep(1)
        # Use the scroll helper from AndroidActions
        save_btn = self._scroll_bottom_sheet_until_text("Save Address")
        save_btn.click()
        print("Clicked on Save Address")

    def verify_address_is_added_and_selected(self):
        time.sleep(2)
        locator_strategy, locator_pattern = locators['ADDRESS_SELECTED']
        dynamic_locator = (locator_strategy, locator_pattern.format("Marathahalli village, HAL Airport road"))
        return self.actions.is_element_displayed(*dynamic_locator)
          
    def verify_leave_address_mandatory_field_empty(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['HOUSE_NUMBER'])
        self.actions.click_button(*locators['HOUSE_NUMBER'])
        time.sleep(1)
        # Use the scroll helper from AndroidActions
        save_btn = self._scroll_bottom_sheet_until_text("Save Address")
        save_btn.click()
        print("Clicked on Save Address")
       
    def verify_address_mandatory_field_empty_error(self):
        time.sleep(2)
        return self.actions.is_element_displayed(*locators['HOUSE_FIELD_EMPTY_ERROR'])
    
    def enter_special_char_in_house_field(self):
        self.actions.is_element_displayed(*locators['HOUSE_NUMBER'])
        self.actions.enter_text(*locators["HOUSE_NUMBER"], "%$^#@&*")
        time.sleep(2)
        try:
            self.driver.hide_keyboard()
        except Exception:
            print("Keyboard was not present or could not be hidden.")
        self.actions.click_button(*locators['SAVE_ADDRESS'])
        print("Entered special characters in house/flat field")

    def verify_field_accept_special_char_and_address_saved(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['ADDRESS_SAVED_WITH_SPECIAL_CHAR'])
    
    def verify_saved_delivery_address(self, user_data_store):
        # Save current values before changing
        try:
            selected_address = self.driver.find_element(*locators['SELECTED_DELIVERY_ADDRESS'])
            saved_address = selected_address.text
            user_data_store["saved address"] = saved_address
        except Exception as e:
            raise AssertionError(f"Could not retrieve selected delivery address. Error: {e}")
        
    def enter_text_in_house_field_and_cancel_before_saving(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['HOUSE_NUMBER'])
        self.actions.enter_text(*locators["HOUSE_NUMBER"], "vipul greens")
        self.actions.click_button(*locators["CLICK_BACK_BUTTON"])
        time.sleep(2)
        self.actions.click_button(*locators["CLICK_BACK_BUTTON_FROM_SELECT_LOCATION"])
        print("Entered text in house/flat field and click back button without saving")
        

    def verify_address_is_not_saved_when_click_back_button_without_saving(self):
        time.sleep(2)  
        all_address_elements = self.driver.find_elements(*locators["ALL_ADDRESS"])
        all_addresses = [addr.text.strip().lower() for addr in all_address_elements]

        assert "vipul greens" not in all_addresses, \
            "Address 'vipul greens' is unexpectedly present in the All Address section."
        print("Verified: 'vipul greens' is not present in All Address section.")
        self.driver.back()


    def verify_duplicate_address_saved(self):
        time.sleep(2)  
        # Get all address elements from the "All Address" section
        address_elements = self.driver.find_elements(*locators["ALL_ADDRESS"])

        # Extract the text of each address
        addresses = [el.text.strip() for el in address_elements]

        # Check for duplicates
        seen = set()
        duplicates = []

        for addr in addresses:
            if addr in seen:
                duplicates.append(addr)
            else:
                seen.add(addr)

        # Print results
        if duplicates:
            print("Duplicate addresses found:")
            for dup in set(duplicates):
                print("-", dup)
        else:
            print("No duplicate addresses found.")
        self.driver.back()

    def search_for_address_after_selecting_business_model(self):
        time.sleep(2)
        self.actions.click_button(*locators['SEARCH_BUTTON'])
        time.sleep(5)
        self.actions.enter_text(*locators["SEARCH_INPUT_FIELD"], "Bengaluru")
        time.sleep(5)
        self.actions.click_button(locators['SELECT_ADDRESS'][0], locators['SELECT_ADDRESS'][1].format("Bengaluru"))
        time.sleep(10)
        self.actions.is_element_displayed(*locators['FIRST_ADDRESS'])
        self.actions.click_button(*locators['FIRST_ADDRESS'])
        print("First address clicked.")

    def Click_from_listed_address(self):
        WebDriverWait(self.driver, 10).until(
             EC.visibility_of_element_located(locators['SELECT_DELIVERY_ADDRESS_HEADER'])
        )
        self.actions.click_button(locators['SELECT_ADDRESS'][0], locators['SELECT_ADDRESS'][1].format("Marathahalli village, HAL Airport road"))
        print("Address from list clicked")

       
    def click_address_edit_icon(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['ADDRESS_EDIT_ICON'])
        self.actions.click_button(*locators['ADDRESS_EDIT_ICON'])
        print("Edit icon clicked")

    def modify_existing_address_and_click_save(self, updated_house_name):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['HOUSE_NUMBER'])
        self.actions.enter_text(*locators["HOUSE_NUMBER"], updated_house_name)
        time.sleep(2)
        save_btn = self._scroll_bottom_sheet_until_text("Save Address")
        save_btn.click()
        print("Clicked on Save Address")
        time.sleep(1)
        print(f"Entered updated house/flat value: '{updated_house_name}' and clicked save button")

    def verify_updated_address_display_in_address_list(self, expected_partial_text):
        time.sleep(2)
        # Fetch all address elements
        all_address_elements = self.driver.find_elements(*locators["ALL_ADDRESS"])
        # Extract text and normalize for comparison
        all_addresses = [addr.text.strip().lower() for addr in all_address_elements]
        print("Addresses found on screen:", all_addresses)
        # Check if expected text is present in any address
        is_present = any(expected_partial_text.lower() in address for address in all_addresses)

        assert is_present, f"Expected address '{expected_partial_text}' not found in the All Address section."
        print(f"Verified: '{expected_partial_text}' is present in All Address section.")

    def enter_text_exceeding_max_limit(self):
        time.sleep(2)
        long_text = "A" * 301
        element = self.driver.find_element(*locators['HOUSE_NUMBER'])
        element.clear()
        element.send_keys(long_text)
        print("Entered 301 characters into address field.")
        time.sleep(2)
        save_btn = self._scroll_bottom_sheet_until_text("Save Address")
        save_btn.click()
        print("Clicked on Save Address")

    def verify_field_accept_maximum_char_and_address_saved(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['ADDRESS_SAVED_WITH_MAX_CHAR'])

    def Verify_address_shown_in_list_before_deletion(self, user_data_store):
        time.sleep(2)
        address_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    locators['ADDRESS_SELECTED'][0],
                    locators['ADDRESS_SELECTED'][1].format("Marathahalli village, HAL Airport road"))))
        address_title = address_element.text.strip()
        user_data_store["original_address"] = address_title
        print("Captured address name before deletion:", address_title)
        return address_title

    def click_address_delete_icon(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['ADDRESS_DELETE_ICON'])
        self.actions.click_button(*locators['ADDRESS_DELETE_ICON'])
        print("Delete icon clicked")
        time.sleep(2)
        self.actions.is_element_displayed(*locators['DELETE_POP_UP'])
        self.actions.click_button(*locators['CLICK_YES_BUTTON'])
        print("Clicked on YES option on address delete pop up")

    def Verify_address_removed_from_list_after_deletion(self, user_data_store):
        time.sleep(2)
        deleted_address_name = user_data_store.get("original_address") 
        print(f"Validating deleted address: '{deleted_address_name}'")

        all_address_elements = self.driver.find_elements(*locators["ALL_ADDRESS"])
        all_titles = [el.text.strip() for el in all_address_elements]
        print("Remaining address titles after deletion:", all_titles)

        assert deleted_address_name not in all_titles, f"'{deleted_address_name}' is still visible after deletion!"
        self.driver.back()

    def verify_address_list(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['ALL_ADDRESS'])
    
    def verify_near_label_visible_in_address_description(self):
        time.sleep(2)
        near_elements = self.driver.find_elements(*locators['NEAR_LABEL'])
        for el in near_elements:
            print(el.text)
        self.driver.back()

    def All_addresses_accessible_via_scrolling(self):
        try:
            # Use UiScrollable to bring last address into view
            last_address_element = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView('
                'new UiSelector().textContains("Marathahalli"))'
            )
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of(last_address_element)
            )
            print(" Scrolled to access the last address")
            return last_address_element

        except Exception as e:
            print(" Failed to scroll to last address:", str(e))
            raise
    

    

