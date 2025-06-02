
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import datetime
from datetime import datetime, timedelta
import time

locators = {
    "PERSONAL_HEADER_DETAILS": (By.XPATH, "//div[contains(text(), 'Personal Details')]"),
    "USER_PROFILE_ICON": (By.XPATH, "//h2[@class = 'avatar__logo-initial-txt']"),
    "PROFILE_PAGE_LOGO": (By.XPATH, "//img[@class = 'profile-page__logo']"),
    "USER_NAME": (By.XPATH, "//input[@placeholder='Enter your full name here']"),
    "MOBILE_NUMBER": (By.XPATH, "//input[@mds-profile-edit-input-mblno]"),
    "EMAIL_ID": (By.XPATH, "//input[@placeholder='Enter Your Email ID here']"),
    "DATE_OF_BIRTH": (By.XPATH, "//input[@placeholder='Click here to select']"),
    "SUBMIT_BUTTON": (By.XPATH, "//button[contains(text(), 'Save Changes')]"),
    "PROFILE_EDIT_ICON": (By.XPATH, "//img[@class = 'profile-page__link-btn']"),
    "PROFILE_EDIT_PAGE": (By.XPATH, "//div[@class = 'profile-edit-page__header ion-hide-lg-down']"),
    "UPDATED_PROFILE_NAME": (By.XPATH, "//div[@class = 'bio__name']"),
    "EMPTY_PROFILE_NAME_FIELD_ERROR": (By.XPATH, "//label[contains(text(), 'Please enter valid full name')]"),
    "UPDATED_EMAIL_ADDRESS": (By.XPATH, "//div[@class = 'bio__email txt-ellipsis']"),
    "INCORRECT_EMAIL_FORMAT": (By.XPATH, "//label[contains(text(), 'Please enter valid Email ID')]"),
    "UPDATED_DATE_OF_BIRTH": (By.XPATH, "//input[@type='text']"),
    "DATE_PICKER": (By.XPATH, "//span[contains(text(), 'Choose DOB')]"),
    "SELECT_BUTTON": (By.XPATH, "//button[contains(text(), 'Select')]"),
    "CHANGE_PICTURE_LINK": (By.XPATH, "//div[contains(text(), ' Change Picture ')]"),
    "FILE_UPLOAD_POP_UP": (By.XPATH, "//ion-list[@role = 'list']"),
    "NAME_FIELD_ICON": (By.XPATH, "//img[@title = 'ic-user']"),
    "MOBILE_FIELD_ICON": (By.XPATH, "//img[@title = 'ic-mobile']"),
    "EMAIl_FIELD_ICON": (By.XPATH, "//img[@title = 'ic-message']"),
    "DOB_FIELD_ICON": (By.XPATH, "//img[@title = 'ic-calender']"),
    "COLOR_BLIND_FRIENDLY_TEXT": (By.XPATH, "//div[contains(text(), ' Use Colour Blind Friendly ')]"),
    "TOGGLE_BUTTON": (By.XPATH, "(//input[@type = 'checkbox'])[1]"),
     "TOGGLE_BUTTON_COLOR_SCHEME_PAGE": (By.XPATH, "(//input[@type = 'checkbox'])[2]"),
    "COLOR_SCHEME": (By.XPATH, "//div[@class = 'bottom-sheet']"),
    "COLOR_BLIND_BACK_BUTTON": (By.XPATH, "//img[@class = 'address-header__back-btn']"),
    "SELECT_COLOR_BLIND_RADIO_BUTTON": (By.XPATH, "//div[@class = 'bottom-sheet__radio']"),
     "COLOR_BLIND_FRIENDLY_TEXT_AFTER_MODE_ON": (By.XPATH, "//div[@class ='color-correction__para']"),
    }


class ProfilePage(BasePage):

    def verify_profile_page_reached(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['PERSONAL_HEADER_DETAILS'])
    
    def get_element_value(self, locator_key):
        element = self.actions.wait_for_element(*locators[locator_key])
        if element is None:
          raise Exception(f"{locator_key} element not found.")
        return element.get_attribute("value")

    
    '''
    def verify_profile_page_is_incomplete_after_login(self):
        profile_details = []
        user_name = self.actions.wait_for_element(*locators['USER_NAME'])
        user_name = user_name.get_attribute("value")
        mobile_number = self.actions.wait_for_element(*locators['MOBILE_NUMBER'])
        mobile_number = mobile_number.get_attribute("value")
        email_id = self.actions.wait_for_element(*locators["EMAIL_ID"])
        email_id = email_id.get_attribute("value")
        date_of_birth = self.actions.wait_for_element(*locators["DATE_OF_BIRTH"])
        date_of_birth = date_of_birth.get_attribute("value")
        profile_details.extend([user_name, mobile_number, email_id, date_of_birth])
        print(profile_details)
        if any(value == "" or value is None for value in profile_details):
            return True
        else:
            return False
    '''

    def verify_profile_page_is_incomplete_after_login(self):
       def get_element_value(field_name):
        """Fetch the value of an element safely, or raise if not found."""
        element = self.actions.wait_for_element(*locators[field_name])
        if element is None:
            raise Exception(f"{field_name} element not found on the page.")
        return element.get_attribute("value")

    # Fetch all profile values using the helper
       profile_details = [
        get_element_value('USER_NAME'),
        get_element_value('MOBILE_NUMBER'),
        get_element_value('EMAIL_ID'),
        get_element_value('DATE_OF_BIRTH')
    ]

       print("Profile details:", profile_details)

    # Return True if any field is empty or None (i.e., profile is incomplete)
       return any(value in ("", None) for value in profile_details)


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
        time.sleep(10)
        self.actions.click_button(*locators["SUBMIT_BUTTON"])

    def updated_profile_name(self):
        self.actions.is_element_displayed(*locators['USER_PROFILE_ICON'])
        time.sleep(10)
        self.actions.click_button(*locators['USER_PROFILE_ICON'])

        if self.actions.is_element_displayed(*locators['UPDATED_PROFILE_NAME']):
            return self.driver.find_element(*locators['UPDATED_PROFILE_NAME']).text
        else:
            return None

    def clear_profile_name_field(self):
        username_field = self.driver.find_element(*locators['USER_NAME'])
        username_field.send_keys(Keys.CONTROL + "a")   # Select all text
        username_field.send_keys(Keys.BACKSPACE)       # Delete selected text
        username_field.send_keys(Keys.TAB)
        time.sleep(10)


    def profile_name_field_empty_error(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['EMPTY_PROFILE_NAME_FIELD_ERROR']), "Validation error not displayed after clearing name field"
    
    def enter_invalid_char_in_name_field(self):
        username_field = self.driver.find_element(*locators['USER_NAME'])
        username_field.clear()
        self.actions.enter_text(*locators['USER_NAME'], "John@123")
        time.sleep(5)
        self.actions.click_button(*locators["SUBMIT_BUTTON"])

    def edit_email_address(self):
        email_field = self.driver.find_element(*locators['EMAIL_ID'])
        email_field.clear()
        self.actions.enter_text(*locators['EMAIL_ID'], "testuser11@gmail.com")
        time.sleep(5)
        self.actions.click_button(*locators["SUBMIT_BUTTON"])

    def updated_email_address(self):
        self.actions.is_element_displayed(*locators['USER_PROFILE_ICON'])
        time.sleep(10)
        self.actions.click_button(*locators['USER_PROFILE_ICON'])

        if self.actions.is_element_displayed(*locators['UPDATED_EMAIL_ADDRESS']):
            return self.driver.find_element(*locators['UPDATED_EMAIL_ADDRESS']).text
        else:
            return None
        
    def enter_incorrect_email_format_in_email_field(self):
        email_field = self.driver.find_element(*locators['EMAIL_ID'])
        email_field.clear()
        self.actions.enter_text(*locators['EMAIL_ID'], "user@.com")
        time.sleep(5)
        self.actions.click_button(*locators["SUBMIT_BUTTON"])

    def incorrect_email_error(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['INCORRECT_EMAIL_FORMAT'])
    
    def edit_date_of_birth(self):
        element = self.driver.find_element(*locators['DATE_OF_BIRTH'])
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        time.sleep(2)
        self.actions.click_button(*locators['DATE_OF_BIRTH'])
        # Locate the frame element first, then switch to it
        self.actions.is_element_displayed(*locators['DATE_PICKER'])
        print("Calendar appeared")

        handles = self.driver.window_handles
        size = len(handles)
        parent_handle = self.driver.current_window_handle
        for x in range(size):
            if handles[x] != parent_handle:
                self.driver.switch_to.window(handles[x])
                print(self.driver.title)

        # Get today's date
        today = datetime.now()
        day_str = str(today.day)

        # Select today's date by visible text
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//*[text()='{day_str}']"))
)

        # Now find and click it
        date_cell = self.driver.find_element(By.XPATH, f"//*[text()='{day_str}']")
        date_cell.click()
        self.actions.click_button(*locators["SELECT_BUTTON"])
        time.sleep(2)
        


    def updated_date_of_birth(self):
        self.actions.is_element_displayed(*locators['USER_PROFILE_ICON'])
        time.sleep(10)
        self.actions.click_button(*locators['USER_PROFILE_ICON'])
        element = self.driver.find_element(*locators['DATE_OF_BIRTH'])
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        time.sleep(2)

        if self.actions.is_element_displayed(*locators['UPDATED_DATE_OF_BIRTH']):
            return self.driver.find_element(*locators['UPDATED_DATE_OF_BIRTH']).text
        else:
            return None
        
    def enter_future_date_of_birth(self):
        element = self.driver.find_element(*locators['DATE_OF_BIRTH'])
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        time.sleep(2)
        self.actions.click_button(*locators['DATE_OF_BIRTH'])
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(*locators['DATE_PICKER'])
    )
        # Define the target future date
        target_day = 20
        target_month = "July"
        target_year = 2025

        # Get current date
        today = datetime.datetime.today()

        # Create datetime object for the target date
        target_date_str = f"{target_day} {target_month} {target_year}"
        target_date = datetime.datetime.strptime(target_date_str, "%d %B %Y")

        # Check if the target date is in the future
        if target_date > today:
            print(f"ERROR: Attempt to select a future date ({target_date.date()}) is not allowed.")
            return

        # Proceed to select the date if it's valid (not in the future)
        self.actions.select_date_from_calendar(str(target_day), target_month, str(target_year))
        time.sleep(2)
        self.actions.click_button(*locators["SUBMIT_BUTTON"])

    def verify_future_dob_disabled(self):
        self.actions.click_button(*locators['DATE_OF_BIRTH'])

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['DATE_PICKER'])
    )

        # Define a known future date (e.g., tomorrow)
        tomorrow = datetime.now() + timedelta(days=1)
        future_day = str(tomorrow.day)
        future_month = tomorrow.strftime("%B")
        future_year = str(tomorrow.year)

    # Try to select the future date using custom method
        is_selectable = self.actions.is_date_selectable(future_day, future_month, future_year)

    # Validate that future date is not selectable
        assert not is_selectable, f"Future date {tomorrow.strftime('%Y-%m-%d')} should not be selectable"

    def click_change_picture_link(self):
        self.actions.is_element_displayed(*locators['CHANGE_PICTURE_LINK'])
        time.sleep(10)
        self.actions.click_button(*locators['CHANGE_PICTURE_LINK'])

    def verify_file_upload_pop_up(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['FILE_UPLOAD_POP_UP'])


    def check_save_changes_button_disabled(self):
        self.actions.is_element_displayed(*locators['USER_NAME'])
        save_button = self.driver.find_element(*locators['SUBMIT_BUTTON'])
        return not save_button.is_enabled()

    def check_icon_presence_near_each_field(self):
        element = self.driver.find_element(*locators['DOB_FIELD_ICON'])  
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        time.sleep(2)
        fields = ['NAME_FIELD_ICON', 'MOBILE_FIELD_ICON', 'EMAIl_FIELD_ICON', 'DOB_FIELD_ICON'] 

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
        expected_icons = ['NAME_FIELD_ICON', 'MOBILE_FIELD_ICON', 'EMAIl_FIELD_ICON', 'DOB_FIELD_ICON']
        for field_key in expected_icons:
            print(f"Checking visibility of icon: {field_key}")
            assert self.actions.is_element_displayed(*locators[field_key]), f"Icon for {field_key} is not displayed"


    def switch_toggle_button(self):
    # Scroll to and click the first toggle
        element = self.driver.find_element(*locators['COLOR_BLIND_FRIENDLY_TEXT'])
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        self.actions.is_element_displayed(*locators['COLOR_BLIND_FRIENDLY_TEXT'])
        toggle_button = self.driver.find_element(*locators['TOGGLE_BUTTON'])
        ActionChains(self.driver).move_to_element(toggle_button).click().perform()
        color_scheme = self.actions.is_element_displayed(*locators['COLOR_SCHEME'])
        print(color_scheme)
        # Click the toggle inside the popup
        toggle_button = self.driver.find_element(*locators['TOGGLE_BUTTON_COLOR_SCHEME_PAGE'])
        ActionChains(self.driver).move_to_element(toggle_button).click().perform()

        # Select radio button
        select_radio = self.driver.find_element(*locators['SELECT_COLOR_BLIND_RADIO_BUTTON'])
        ActionChains(self.driver).move_to_element(select_radio).click().perform()

        # Confirm text shows up
        self.actions.is_element_displayed(*locators['COLOR_BLIND_FRIENDLY_TEXT'])
        assert self.actions.is_element_displayed(*locators['COLOR_BLIND_FRIENDLY_TEXT']), "Color blind mode ON text not visible"
        print("Color blind mode is ON.")
        toggle_button = self.driver.find_element(*locators['TOGGLE_BUTTON'])
        ActionChains(self.driver).move_to_element(toggle_button).click().perform()
        time.sleep(2)
    
        # Verify toggle is off
        is_off = not self.actions.is_element_displayed(*locators['TOGGLE_BUTTON'])
        assert is_off, "Toggle button is still ON"
        print("Toggle button is OFF")


    def color_scheme(self):
        self.actions.is_element_displayed(*locators['COLOR_BLIND_FRIENDLY_TEXT'])
        toggle_button = self.driver.find_element(*locators['TOGGLE_BUTTON'])
        ActionChains(self.driver).move_to_element(toggle_button).click().perform()
        element = self.driver.find_element(*locators['COLOR_BLIND_FRIENDLY_TEXT'])
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        self.actions.is_element_displayed(*locators['COLOR_SCHEME'])
        time.sleep(2)
        
    def color_blind_mode_On_and_reload_page(self):
        element = self.driver.find_element(*locators['COLOR_BLIND_FRIENDLY_TEXT'])
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        self.actions.is_element_displayed(*locators['COLOR_BLIND_FRIENDLY_TEXT'])
        toggle_button = self.driver.find_element(*locators['TOGGLE_BUTTON'])
        ActionChains(self.driver).move_to_element(toggle_button).click().perform()
        self.actions.is_element_displayed(*locators['COLOR_SCHEME'])
        self.actions.click_button(*locators['TOGGLE_BUTTON'])
        self.actions.click_button(*locators['SELECT_COLOR_BLIND_RADIO_BUTTON'])
        time.sleep(2)
        self.actions.is_element_displayed(*locators['COLOR_BLIND_FRIENDLY_TEXT'])
        print("Color blind mode is ON.")
        self.driver.refresh()
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(locators['COLOR_BLIND_FRIENDLY_TEXT'])
    )
        print("Page reloaded. Element still present — preference may be retained.")
    

    def verify_color_blind_preference_retained(self):
        time.sleep(2)
        return self.actions.is_element_displayed(*locators['COLOR_BLIND_FRIENDLY_TEXT_AFTER_MODE_ON'])

    def make_changes_and_refresh_page(self, user_data_store):
        # Save current values before changing
        user_data_store["original_name"] = self.driver.find_element(*locators['USER_NAME']).get_attribute("value")
        user_data_store["original_email"] = self.driver.find_element(*locators['EMAIL_ID']).get_attribute("value")
        username_field = self.driver.find_element(*locators['USER_NAME'])
        username_field.clear()
        self.actions.enter_text(*locators['USER_NAME'], "Namrata user")
        time.sleep(2)
        email_field = self.driver.find_element(*locators['EMAIL_ID'])
        email_field.clear()
        self.actions.enter_text(*locators['EMAIL_ID'], "namratauser@gmail.com")
        time.sleep(3)
        self.driver.refresh()

    def verify_data_is_not_saved_after_refresh(self, user_data_store):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locators['USER_NAME'])
    )
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locators['EMAIL_ID'])
    )

        current_name = self.driver.find_element(*locators['USER_NAME']).get_attribute("value")
        current_email = self.driver.find_element(*locators['EMAIL_ID']).get_attribute("value")

        assert current_name == user_data_store["original_name"], f"Expected name: {user_data_store['original_name']}, but got: {current_name}"
        assert current_email == user_data_store["original_email"], f"Expected email: {user_data_store['original_email']}, but got: {current_email}"
