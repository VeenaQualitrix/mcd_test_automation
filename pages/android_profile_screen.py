from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.webdriver import WebDriver as AppiumDriver
import datetime
from datetime import datetime, timedelta
import time

locators = {
    "PERSONAL_HEADER_DETAILS": (AppiumBy.XPATH, "//android.widget.TextView[@text='Personal Details']"),
    "SAVE_BUTTON": (AppiumBy.XPATH, "//android.widget.Button[@text='Save']"),
    "HAMBURGER_ICON": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-bottom-tab-mymcd']"),
    "USER_NAME": (AppiumBy.XPATH, "(//android.widget.EditText)[1]"),
    "MOBILE_NUMBER": (AppiumBy.XPATH, "(//android.widget.EditText)[2]"),
    "EMAIL_ID": (AppiumBy.XPATH, "(//android.widget.EditText)[3]"),
    "DATE_OF_BIRTH": (AppiumBy.XPATH, "//android.view.View[@text='Select Your Date of Birth']"),
    "UPDATED_PROFILE_NAME": (AppiumBy.XPATH, "(//android.widget.TextView)[5]"),
    "EMPTY_PROFILE_NAME_FIELD_ERROR": (AppiumBy.XPATH, "//android.view.View[@text='Please enter valid full name']"),
    "UPDATED_EMAIL_ADDRESS": (AppiumBy.XPATH, "//android.widget.TextView[@text='testuser11@gmail.com']"),
    "INCORRECT_EMAIL_FORMAT": (AppiumBy.XPATH, "//android.view.View[@text='Please enter valid Email ID']"),
    "DATE_OF_BIRTH_TEXTFIELD": (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.EditText").instance(3)'),
    "CALENDAR_ICON": (AppiumBy.XPATH, '//android.widget.Image[@text="ic-calender"]'),
    "DATE_PICKER": (AppiumBy.XPATH, "//android.widget.TextView[@text='Choose DOB']"),
    "SELECT_BUTTON": (AppiumBy.XPATH, "//android.widget.Button[@text='Select']"),
    "CHANGE_PICTURE_LINK": (AppiumBy.XPATH, "//android.widget.TextView[@text='Change Picture']"),
    "FILE_UPLOAD_POP_UP": (AppiumBy.XPATH, "//android.widget.TextView[@text='From Photos']"),
    "NAME_FIELD_ICON": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-user']"),
    "MOBILE_FIELD_ICON": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-mobile']"),
    "EMAIL_FIELD_ICON": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-message']"),
    "DOB_FIELD_ICON": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-calender']"),
    "COLOR_BLIND_FRIENDLY_TEXT": (AppiumBy.XPATH, "//android.widget.TextView[@text='Use Colour Blind Friendly']"),
    "TOGGLE_BUTTON": (AppiumBy.XPATH, "//android.view.View[@text='_']"),
    "COLOR_SCHEME_PAGE": (AppiumBy.XPATH, "//android.widget.TextView[@text='Colour Blind Friendly]"),
    "SELECT_COLOR_SCHEME_MODE": (AppiumBy.XPATH, "//android.widget.TextView[@text='Select Colour Blind Friendly Mode']"),
    "COLOR_BLIND_BACK_BUTTON": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-arrow-left-primary']"),
    "SELECT_COLOR_BLIND_RADIO_BUTTON": (AppiumBy.XPATH, "//android.app.Dialog/android.view.View/android.view.View[2]"),
    "COLOR_BLIND_FRIENDLY_TEXT_AFTER_MODE_ON": (By.XPATH, "//div[@class ='color-correction']"),
    "TOGGLE_BUTTON_IN_ON_MODE": (By.XPATH, "//label[@class='v1 v1--active']"),

    }


class AndroidProfileScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)  # This calls BasePage.__init__ and sets up driver and actions
        self.expected_dob = None

    def verify_profile_screen_reached(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['PERSONAL_HEADER_DETAILS'])
    
    def Click_save_button_on_profile_details_screen(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['PERSONAL_HEADER_DETAILS'])
        # Scroll until Save button is visible
        save_button = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView(new UiSelector().text("Save").instance(0));'
        )

        # Click Save button
        save_button.click()    

    def add_profile_details(self):
        self.actions.enter_text(*locators['USER_NAME'], "User01")
        self.actions.enter_text(*locators["EMAIL_ID"], "user01@gmail.com")
        time.sleep(10)
        self.actions.click_button(*locators["SUBMIT_BUTTON"])

    def click_user_profile_icon(self):
        self.actions.is_element_displayed(*locators['USER_PROFILE_ICON'])
        time.sleep(5)
        self.actions.click_button(*locators['USER_PROFILE_ICON'])

    def verify_profile_page_navigation(self):
        time.sleep(3)
        return self.actions.is_element_displayed(*locators['PROFILE_PAGE_LOGO'])        

    def click_edit_profile_icon(self):
        self.actions.is_element_displayed(*locators['PROFILE_EDIT_ICON'])
        time.sleep(5)
        self.actions.click_button(*locators['PROFILE_EDIT_ICON'])

    def verify_profile_edit_page(self):
        time.sleep(3)
        return self.actions.is_element_displayed(*locators['PROFILE_EDIT_PAGE'])
        
    def edit_profile_name(self):
        username_field = self.driver.find_element(*locators['USER_NAME'])
        username_field.clear()
        self.actions.enter_text(*locators['USER_NAME'], "Test User01")

        # Scroll until Save button is visible
        save_button = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView(new UiSelector().text("Save").instance(0));'
        )

        # Click Save button
        save_button.click()

    def updated_profile_name(self):
        self.actions.is_element_displayed(*locators['HAMBURGER_ICON'])
        time.sleep(10)
        self.actions.click_button(*locators['HAMBURGER_ICON'])

        if self.actions.is_element_displayed(*locators['UPDATED_PROFILE_NAME']):
            return self.driver.find_element(*locators['UPDATED_PROFILE_NAME']).text
        else:
            return None

    def clear_profile_name_field(self):
        username_field = self.driver.find_element(*locators['USER_NAME'])
        username_field.clear()  # This works for most Android text fields


    def profile_name_field_empty_error(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['EMPTY_PROFILE_NAME_FIELD_ERROR'])
    
    def enter_invalid_char_in_name_field(self):
        username_field = self.driver.find_element(*locators['USER_NAME'])
        username_field.clear()
        self.actions.enter_text(*locators['USER_NAME'], "John@123")
        time.sleep(3)

    def edit_email_address(self):
        email_field = self.driver.find_element(*locators['EMAIL_ID'])
        email_field.clear()
        self.actions.enter_text(*locators['EMAIL_ID'], "testuser11@gmail.com")
        # Scroll until Save button is visible
        save_button = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView(new UiSelector().text("Save").instance(0));'
        )

        # Click Save button
        save_button.click()

    def updated_email_address(self):
        self.actions.is_element_displayed(*locators['HAMBURGER_ICON'])
        time.sleep(10)
        self.actions.click_button(*locators['HAMBURGER_ICON'])

        if self.actions.is_element_displayed(*locators['UPDATED_EMAIL_ADDRESS']):
            return self.driver.find_element(*locators['UPDATED_EMAIL_ADDRESS']).text
        else:
            return None
        
    def enter_incorrect_email_format_in_email_field(self):
        email_field = self.driver.find_element(*locators['EMAIL_ID'])
        email_field.clear()
        self.actions.enter_text(*locators['EMAIL_ID'], "user@.com")
        time.sleep(3)

    def incorrect_email_error(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['INCORRECT_EMAIL_FORMAT'])

    def edit_date_of_birth(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['DATE_OF_BIRTH'])
        self.actions.click_button(*locators['CALENDAR_ICON'])
        print("Date picker opened")

        # Get today's date and format the expected label text
        today = datetime.now()
        day_name = today.strftime('%A')         # e.g. "Friday"
        month_name = today.strftime('%B')       # e.g. "August"
        day_number = today.day                  # e.g. 8

        expected_text = f"Today, {day_name}, {month_name} {day_number}"
        print(f"Looking for text: {expected_text}")

        # Wait for the date element to appear
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiSelector().text("{expected_text}")'
                ))
            ).click()
            print("Date element clicked")
        except Exception as e:
            print(f"Failed to find or click date element: {expected_text}")
            raise e

        self.actions.click_button(*locators["SELECT_BUTTON"])
        print("Date selected")
        time.sleep(1)
        formatted_dob = today.strftime("%d/%m/%Y")
        return formatted_dob
        
    def verify_updated_date_of_birth(self):
        dob_element = self.driver.find_element(*locators['DATE_OF_BIRTH_TEXTFIELD'])

        # Safely retrieve the DOB text
        actual_dob = dob_element.text.strip()

        print(f"[DEBUG] Actual DOB on profile: {actual_dob}")
        return actual_dob
        

    def verify_future_dob_disabled(self):
        time.sleep(5)
        time.sleep(2)
        self.actions.is_element_displayed(*locators['DATE_OF_BIRTH'])
        self.actions.click_button(*locators['CALENDAR_ICON'])
        print("Date picker opened")

        tomorrow = datetime.now() + timedelta(days=1)
        future_day = tomorrow.day
        future_month = tomorrow.month
        future_year = tomorrow.year

        is_selectable = self.actions.is_date_selectable(future_day, future_month, future_year)
        print(f"[DEBUG] Is future date selectable? {is_selectable}")

        # Return True if date is selectable, else False
        return is_selectable

    def click_change_picture_link(self):
        self.actions.is_element_displayed(*locators['CHANGE_PICTURE_LINK'])
        time.sleep(10)
        self.actions.click_button(*locators['CHANGE_PICTURE_LINK'])

    def verify_file_upload_pop_up(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['FILE_UPLOAD_POP_UP'])

    def check_save_changes_button_disabled(self):
        time.sleep(3)
        save_button = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView(new UiSelector().text("Save").instance(0));'
        )
        return not save_button.is_enabled()

    def check_icon_presence_near_each_field(self):
        time.sleep(2)
        fields = ['NAME_FIELD_ICON', 'MOBILE_FIELD_ICON', 'EMAIL_FIELD_ICON', 'DOB_FIELD_ICON'] 

        for field in fields:  
            print(f"Checking icon for: {field}")
            try:
                is_displayed = self.actions.is_element_displayed(*locators[field])
                print(f"Displayed: {is_displayed}")
                assert is_displayed, f"Icon for {field} is not displayed"
            except Exception as e:
                self.driver.save_screenshot(f"screenshots/{field}_icon_error.png")
                raise

    def verify_correct_icons(self):
        expected_icons = ['NAME_FIELD_ICON', 'MOBILE_FIELD_ICON', 'EMAIL_FIELD_ICON', 'DOB_FIELD_ICON']
        for field_key in expected_icons:
            print(f"Checking visibility of icon: {field_key}")
            assert self.actions.is_element_displayed(*locators[field_key]), f"Icon for {field_key} is not displayed"


    def switch_toggle_button(self):
        # Scroll to the toggle text
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView(new UiSelector().text("Save").instance(0));'
        )
        self.actions.is_element_displayed(*locators['COLOR_BLIND_FRIENDLY_TEXT'])
        # Tap toggle button
        self.driver.find_element(*locators['TOGGLE_BUTTON']).click()
        # Verify color scheme popup
        self.actions.is_element_displayed(*locators['COLOR_SCHEME_PAGE'])
        time.sleep(2)
        self.driver.find_element(*locators['TOGGLE_BUTTON']).click()
        self.actions.is_element_displayed(*locators['SELECT_COLOR_SCHEME_MODE'])

        # Select radio button
        self.driver.find_element(*locators['SELECT_COLOR_BLIND_RADIO_BUTTON']).click()
        time.sleep(2)

        # Verify text after turning ON color scheme mode
        self.actions.is_element_displayed(*locators['COLOR_BLIND_FRIENDLY_TEXT'])
        print("Color blind mode is ON.")

        # Turn OFF toggle
        self.driver.find_element(*locators['TOGGLE_BUTTON']).click()
        time.sleep(2)
        self.actions.is_element_displayed(*locators['COLOR_SCHEME_PAGE'])
        self.driver.find_element(*locators['TOGGLE_BUTTON']).click()

        # Verify it's OFF (can also check attribute/state)
        is_off = not self.actions.is_element_displayed(*locators['TOGGLE_BUTTON'])
        assert is_off, "Toggle button is still ON"
        print("Color blind mode is OFF.")


    def color_scheme(self):
        time.sleep(2)
        return self.actions.is_element_displayed(*locators['COLOR_BLIND_FRIENDLY_TEXT'])
        
        
    def color_blind_mode_On_and_reload_page(self):
        element = self.driver.find_element(*locators['COLOR_BLIND_FRIENDLY_TEXT'])
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        self.actions.is_element_displayed(*locators['COLOR_BLIND_FRIENDLY_TEXT'])
        toggle_button = self.driver.find_element(*locators['TOGGLE_BUTTON'])
        ActionChains(self.driver).move_to_element(toggle_button).click().perform()
        color_scheme = self.actions.is_element_displayed(*locators['COLOR_SCHEME'])
        print(color_scheme)
        toggle_button = self.driver.find_element(*locators['TOGGLE_BUTTON_COLOR_SCHEME_PAGE'])
        ActionChains(self.driver).move_to_element(toggle_button).click().perform()
        select_radio = self.driver.find_element(*locators['SELECT_COLOR_BLIND_RADIO_BUTTON'])
        ActionChains(self.driver).move_to_element(select_radio).click().perform()
        time.sleep(5)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        self.actions.is_element_displayed(*locators['COLOR_BLIND_FRIENDLY_TEXT'])
        assert self.actions.is_element_displayed(*locators['COLOR_BLIND_FRIENDLY_TEXT']), "Color blind mode ON text not visible"
        print("Color blind mode is ON.")
        self.driver.refresh()
        time.sleep(10)
         # Wait for page to reload and element to reappear
        element_after_reload = self.driver.find_element(*locators['DATE_OF_BIRTH'])
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element_after_reload)
        self.actions.is_element_displayed(*locators['COLOR_BLIND_FRIENDLY_TEXT_AFTER_MODE_ON'])
        # Check if toggle is still ON
        is_on = self.actions.is_element_displayed(*locators['TOGGLE_BUTTON_IN_ON_MODE'])
        assert is_on, "Toggle button is OFF"
        print("Toggle button is ON")
    

    def verify_color_blind_preference_retained(self):
        time.sleep(2)
        return self.actions.is_element_displayed(*locators['TOGGLE_BUTTON_IN_ON_MODE'])


    def Verify_current_profile_info(self, user_data_store):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['PROFILE_ICON'])
        self.actions.click_button(*locators['PROFILE_ICON'])
        time.sleep(2)
        user_data_store["original_name"] = self.driver.find_element(*locators['PROFILE_NAME']).get_attribute("value")
        user_data_store["original_mobile"] = self.driver.find_element(*locators['PROFILE_MOBILE']).get_attribute("value")
        user_data_store["original_email"] = self.driver.find_element(*locators['PROFILE_EMAIL']).get_attribute("value")
        print("Captured profile info: ")
        print(user_data_store)
        time.sleep(2)
        self.actions.is_element_displayed(*locators['MCDELIVERY_ICON'])
        self.actions.click_button(*locators['MCDELIVERY_ICON'])

    def Verify_profile_info_remian_unchanged(self, user_data_store):
        time.sleep(2)
        current_name = self.driver.find_element(*locators['PROFILE_NAME']).get_attribute("value")
        current_mobile = self.driver.find_element(*locators['PROFILE_MOBILE']).get_attribute("value")
        current_email = self.driver.find_element(*locators['PROFILE_EMAIL']).get_attribute("value")

        assert current_name == user_data_store["original_name"], f"Expected name: {user_data_store['original_name']}, but got: {current_name}"
        assert current_mobile == user_data_store["original_name"], f"Expected name: {user_data_store['original_mobile']}, but got: {current_name}"
        assert current_email == user_data_store["original_email"], f"Expected email: {user_data_store['original_email']}, but got: {current_email}"
        print(" Profile info remains unchanged after switching business model.")

    def verify_profile_page_navigation_after_switching_model(self):
        self.actions.is_element_displayed(*locators['PROFILE_ICON'])
        self.actions.click_button(*locators['PROFILE_ICON'])
        time.sleep(3)
        return self.actions.is_element_displayed(*locators['PROFILE_PAGE_LOGO'])
    
    def Click_save_changes_on_profile_details_page(self):
        self.actions.is_element_displayed(*locators['SUBMIT_BUTTON'])
        time.sleep(2)
        self.actions.click_button(*locators["SUBMIT_BUTTON"])

    def Click_log_out_on_profile_details_page(self):
        log_out_button = self.driver.find_element(*locators["LOG_OUT_BUTTON"])
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", log_out_button)
        time.sleep(10)
        log_out_button.click()
        print("Log out button clicked")

