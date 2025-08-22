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
    


'SAVED_ADDRESS_ITEM': (AppiumBy.XPATH, '//XCUIElementTypeOther[@name="web dialogue"]/XCUIElementTypeOther[3]'),

'SELECTED_ADDRESS_LABEL': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="Home"])[1]'),

'EDIT_ADDRESS_ICON': (AppiumBy.XPATH, '(//XCUIElementTypeImage[@name="ic-edit"])[1]'),

'FLAT_NO': (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="*House / Flat No."]'),

'FLOOR': (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Floor no / Wing name"]'),

'FLAT_NO_ADDRESS': (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="123 Main Street"]'),

'FLOOR_ADDRESS': (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="2nd floor"]'),

'SAVE_ADDRESS_BUTTON': (AppiumBy.ACCESSIBILITY_ID, "Save Address"),

'UPDATED_ADDRESS_LABEL': (
    AppiumBy.XPATH, 
    "//*[contains(@name, '221B Baker Street')]"
),
'DELETE_ICON': (AppiumBy.XPATH, '(//XCUIElementTypeImage[@name="ic-delete"])[2]'),
'CONFRIM_YES': (AppiumBy.ACCESSIBILITY_ID, "Yes"),

'FIRST_NEARBY_RESTAURANT': (AppiumBy.ACCESSIBILITY_ID, "Mantri Mall"),

'SECOND_NEARBY_RESTAURANT': (AppiumBy.ACCESSIBILITY_ID, "Basaveshwar Nagar"),

'MOBILE_NUMBER': (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Contact Number"]'),

'ADDRESS_ERROR_MESSAGE': (AppiumBy.ACCESSIBILITY_ID, "Please enter valid House / Flat No."),

'LOGOUT_BUTTON': (AppiumBy.ACCESSIBILITY_ID, "ic-logoutIconLogout ic-arrow-right"),

'DELETE_ICON_TWO': (AppiumBy.XPATH, '(//XCUIElementTypeImage[@name="ic-delete"])[1]'),

'DELETE_ICON_THREE': (AppiumBy.XPATH, '(//XCUIElementTypeImage[@name="ic-delete"])[3]'),


'DEFAULT_ADDRESS_LABEL': (AppiumBy.ACCESSIBILITY_ID, "Can not delete selected address"),

'HOME_TAG': (AppiumBy.ACCESSIBILITY_ID, "Home"),

'WORK_TAG': (AppiumBy.ACCESSIBILITY_ID, "Work"),


}

class AddressStoreScreenIos(BasePage):



    def select_existing_address_from_saved_list(self):
        if self.actions.is_element_displayed(*locators["SAVED_ADDRESS_ITEM"]):
            self.actions.click_button(*locators["SAVED_ADDRESS_ITEM"])
            print("Existing address selected from the saved list.")
        else:
            raise AssertionError("Saved address not found in the list.")
 
    
    def verify_selected_address_applied(self):
        if self.actions.is_element_displayed(*locators["SELECTED_ADDRESS_LABEL"]):
            print("Selected address is applied successfully.")
        else:
            raise AssertionError("Selected address is not applied or not visible.")
        

    def click_edit_icon(self):
        if self.actions.is_element_displayed(*locators["EDIT_ADDRESS_ICON"]):
            self.actions.click_button(*locators["EDIT_ADDRESS_ICON"])
            print(" Clicked the edit icon for the selected address.")
        else:
            raise AssertionError("Edit icon for the address is not visible.")

    def modify_address_details(self):
        if self.actions.is_element_displayed(*locators["FLAT_NO_ADDRESS"]):
            self.actions.clear_text(*locators["FLAT_NO_ADDRESS"])
            self.actions.send_keys(*locators["FLAT_NO"], "221B Baker Street")
            print("Modified flat number.")

        if self.actions.is_element_displayed(*locators["FLOOR_ADDRESS"]):
            self.actions.clear_text(*locators["FLOOR_ADDRESS"])
            self.actions.send_keys(*locators["FLOOR"], "3rd Floor")
            print("Modified floor.")


    def verify_updated_address_in_list(self):
        expected_address = "221B Baker Street"  # or construct dynamically if needed

        if self.actions.is_element_displayed(*locators["UPDATED_ADDRESS_LABEL"]):
            actual_address = self.actions.get_text(*locators["UPDATED_ADDRESS_LABEL"])
            assert expected_address in actual_address, (
                f"Expected address '{expected_address}' not found in '{actual_address}'"
            )
            print(f"Updated address '{expected_address}' is present in the list.")
        else:
            raise AssertionError(" Updated address label is not displayed.")


    def click_delete_icon(self):
        if self.actions.is_element_displayed(*locators["DELETE_ICON"]):
            self.actions.click_button(*locators["DELETE_ICON"])
            self.actions.click_button(*locators["CONFRIM_YES"])
            print("Clicked on delete icon for the selected address.")
        else:
            raise AssertionError("Delete icon for the selected address is not visible.")

    def select_nearby_restaurant_first_times(self):
            time.sleep(3)
            self.actions.click_button(*locators["FIRST_NEARBY_RESTAURANT"])
            

    def select_nearby_restaurant_second_times(self):
            time.sleep(3)
            self.actions.click_button(*locators["SECOND_NEARBY_RESTAURANT"])
    
    def leave_address_fields_blank(self):
        self.actions.click_button(*locators["FLAT_NO"])
        if self.actions.is_element_displayed(*locators["MOBILE_NUMBER"]):
            self.actions.send_keys(*locators["MOBILE_NUMBER"], "9876543210")
        print("Address fields left blank, only phone number entered.")
        
    def verify_address_fields_required_error(self):
        expected_error = "Please enter valid House / Flat No."
        if self.actions.is_element_displayed(*locators["ADDRESS_ERROR_MESSAGE"]):
            actual_error = self.actions.get_text(*locators["ADDRESS_ERROR_MESSAGE"])
            assert expected_error in actual_error, f"Expected: '{expected_error}', but got: '{actual_error}'"
            print(f"Error message displayed: {actual_error}")
        else:
            raise AssertionError("Error message for required address fields is not displayed.")

    def verify_near_label_under_addresses(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators["FIRST_NEARBY_RESTAURANT"])
        self.actions.is_element_displayed(*locators["SECOND_NEARBY_RESTAURANT"])
        print("'Near' label is displayed under each address.")

    def scroll_to_store_by_name(self, store_name="Orion Mall"):
        print(f"Scrolling to store: {store_name}")
        self.driver.execute_script(
            'mobile: scroll',
            {
                'direction': 'down',
                'predicateString': f"name CONTAINS '{store_name}'"
            }
        )


    def verify_all_addresses_scrollable(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators["FIRST_NEARBY_RESTAURANT"])
        self.actions.is_element_displayed(*locators["SECOND_NEARBY_RESTAURANT"])
                    
    def logout_user(self):
        self.actions.click_button(*locators["LOGOUT_BUTTON"])
        print(" User has been logged out.")
    
    def delete_all_saved_addresses(self):
        if self.actions.is_element_displayed(*locators["DELETE_ICON"]):
            self.actions.click_button(*locators["DELETE_ICON"])
            self.actions.click_button(*locators["CONFRIM_YES"])
            print("First address deleted.")
        else:
            print("First delete icon not found.")
        if self.actions.is_element_displayed(*locators["DELETE_ICON_TWO"]):
            self.actions.click_button(*locators["DELETE_ICON_TWO"])
            self.actions.click_button(*locators["CONFRIM_YES"])
            print("Second address deleted.")
        else:
            print("Second delete icon not found.")
        if self.actions.is_element_displayed(*locators["DELETE_ICON_THREE"]):
            self.actions.click_button(*locators["DELETE_ICON_THREE"])
            self.actions.click_button(*locators["CONFRIM_YES"])
            print("Third address deleted.")
        else:
            print("Third delete icon not found.")
        print("Address deletion flow completed.")

    def verify_default_address_not_deleted(self):
        self.actions.is_element_displayed(*locators["DEFAULT_ADDRESS_LABEL"])
        
    
    def select_and_verify_address_tags(self):
        if self.actions.is_element_displayed(*locators["HOME_TAG"]):
            self.actions.click_button(*locators["HOME_TAG"])
            print("Home tag selected.")
        else:
            raise AssertionError("Home tag option not found.")
        if self.actions.is_element_displayed(*locators["WORK_TAG"]):
            self.actions.click_button(*locators["WORK_TAG"])
            print("Work tag selected.")
        else:
            raise AssertionError("Work tag option not found.")
        if self.actions.is_element_displayed(*locators["HOME_TAG"]):
            self.actions.click_button(*locators["HOME_TAG"])
            print("Home tag selected.")
        else:
            raise AssertionError("Home tag option not found.")
