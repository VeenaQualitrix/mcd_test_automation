from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
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
        time.sleep(5)
        self.actions.is_element_displayed(*locators['ADD_NEW'])
        self.actions.click_button(*locators['ADD_NEW'])
        time.sleep(2)
        self.actions.is_element_displayed(*locators['CONFIRM_LOCATION'])
        self.actions.click_button(*locators["CONFIRM_LOCATION"])
        print("Clicked Confirm Location Button")

    def verify_redirect_to_address_filling_page(self):
        time.sleep(2)
        return self.actions.is_element_displayed(*locators['ADDRESS_SCREEN_HEADER'])
    
    def add_new_delivery_address(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['HOUSE_NUMBER'])
        self.actions.click_button(*locators["HOUSE_NUMBER"])
        print("Clicked on house textfield")
        time.sleep(2)
        self.actions.enter_text(*locators['HOUSE_NUMBER'], "Marathahalli village, HAL Airport road")
        time.sleep(2)
        self.driver.tap([(100, 100)]) 
        self.actions.click_button(*locators["SAVE_ADDRESS"])

    def verify_address_is_added_and_selected(self):
        time.sleep(2)
        locator_strategy, locator_pattern = locators['ADDRESS_SELECTED']
        dynamic_locator = (locator_strategy, locator_pattern.format("Marathahalli village, HAL Airport road"))
        return self.actions.is_element_displayed(*dynamic_locator)
        
    
    def verify_leave_address_mandatory_field_empty(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['HOUSE_NUMBER'])
        self.actions.click_button(*locators['HOUSE_NUMBER'])
        time.sleep(2)
        try:
            self.driver.hide_keyboard()
        except Exception:
            print("Keyboard was not present or could not be hidden.")
        self.actions.click_button(*locators['SAVE_ADDRESS'])
       
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

    

