from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import datetime
from datetime import datetime, timedelta
import time

locators = {
    "PERSONAL_HEADER_DETAILS": (By.XPATH, "//div[contains(text(), 'Personal Details')]"),
    "USER_PROFILE_ICON": (By.XPATH, "//h2[@class = 'avatar__logo-initial-txt']"),
    "PROFILE_ICON": (By.XPATH, "//div[@title = 'View Profile']"),
    "PROFILE_PAGE_LOGO": (By.XPATH, "//img[@class = 'profile-page__logo']"),
    "USER_NAME": (By.XPATH, "//input[@placeholder='Enter your full name here']"),
    "MOBILE_NUMBER": (By.XPATH, "//input[@mds-profile-edit-input-mblno]"),
    "EMAIL_ID": (By.XPATH, "//input[@placeholder='Enter Your Email ID here']"),
    "DATE_OF_BIRTH": (By.XPATH, " //label[contains(text(), 'Select Your Date of Birth')] "),
    "SUBMIT_BUTTON": (By.XPATH, "//button[contains(text(), 'Save Changes')]"),
    "PROFILE_EDIT_ICON": (By.XPATH, "//img[@class = 'profile-page__link-btn']"),
    "PROFILE_EDIT_PAGE": (By.XPATH, "//div[@class = 'profile-edit-page__header ion-hide-lg-down']"),
    "UPDATED_PROFILE_NAME": (By.XPATH, "//div[@class = 'bio__name']"),
    "EMPTY_PROFILE_NAME_FIELD_ERROR": (By.XPATH, "//label[contains(text(), 'Please enter valid full name')]"),
    "UPDATED_EMAIL_ADDRESS": (By.XPATH, "//div[@class = 'bio__email txt-ellipsis']"),
    "INCORRECT_EMAIL_FORMAT": (By.XPATH, "//label[contains(text(), 'Please enter valid Email ID')]"),
    "DATE_OF_BIRTH_TEXTFIELD": (By.XPATH, "//input[@placeholder='Click here to select']"),
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
    "COLOR_BLIND_FRIENDLY_TEXT_AFTER_MODE_ON": (By.XPATH, "//div[@class ='color-correction']"),
    "TOGGLE_BUTTON_IN_ON_MODE": (By.XPATH, "//label[@class='v1 v1--active']"),
    "PROFILE_NAME": (By.XPATH, "//div[@class = 'bio__name']"),
    "PROFILE_MOBILE": (By.XPATH, "//div[@class = 'bio__mobile']"),
    "PROFILE_EMAIL": (By.XPATH, "//div[@class = 'bio__email txt-ellipsis']"),
    "MCDELIVERY_ICON": (By.XPATH, "//img[@alt = 'logo']"),
    "LOG_OUT_BUTTON": (By.XPATH, "//div[contains(text(), 'Logout')]"),
    "CLOSE_CALENDAR_POPUP": (By.XPATH, "//ion-icon[@name ='close-outline']"),

    }


class ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)  # This calls BasePage.__init__ and sets up driver and actions
        self.expected_dob = None

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

    def clear_email_field(self):
        email_field = self.driver.find_element(*locators['EMAIL_ID'])
        email_field.send_keys(Keys.CONTROL + "a")   # Select all text
        email_field.send_keys(Keys.BACKSPACE)       # Delete selected text
        email_field.send_keys(Keys.TAB)
        time.sleep(2)

        submit_button = self.driver.find_element(*locators["SUBMIT_BUTTON"])
        # Scroll into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        time.sleep(1)
        submit_button.click()
        print("✅ Submit button clicked after scrolling.")


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
        time.sleep(2)
        
        # Scroll to Date of Birth section
        date_of_birth = self.driver.find_element(*locators["DATE_OF_BIRTH"])
        self.driver.execute_script("arguments[0].scrollIntoView();", date_of_birth)
        self.actions.is_element_displayed(*locators['DATE_OF_BIRTH'])
        print("[INFO] Date of birth section is displayed")

        # Open the calendar/date picker
        self.actions.click_button(*locators['DATE_OF_BIRTH_TEXTFIELD'])
        self.actions.is_element_displayed(*locators['DATE_PICKER'])
        print("[INFO] Calendar modal appeared")
        
        # Wait for ion-datetime to be visible
        try:
            ion_datetime = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "ion-datetime"))
            )
        except TimeoutException:
            raise Exception("[ERROR] ion-datetime component not found within the modal.")

        # Format today's date as 'YYYY-MM-DD'
        today = datetime.now()
        formatted_date = today.strftime("%Y-%m-%d")
        formatted_dob = today.strftime("%d/%m/%Y")  # For assertion use later
        print(f"[DEBUG] Setting ion-datetime value to {formatted_date}")

        # Set value via JavaScript and trigger ionChange
        self.driver.execute_script("""
            arguments[0].value = arguments[1];
            arguments[0].dispatchEvent(new Event('ionChange'));
        """, ion_datetime, formatted_date)

        time.sleep(1)  # Allow UI to react

        # Click the "Select" button
        self.actions.click_button(*locators["SELECT_BUTTON"])
        print("[INFO] Date selected and confirmed")

        # -------- SCROLL UPWARD AND CLICK SUBMIT --------
        try:
            submit_button = self.driver.find_element(*locators["SUBMIT_BUTTON"])

            # Scroll the page upward until the submit button is visible
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)
            print("[INFO] Scrolled upward to the Submit button")

            # Wait until the button is clickable
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locators["SUBMIT_BUTTON"])
            )

            # Click the Submit button
            self.actions.click_button(*locators["SUBMIT_BUTTON"])
            print("[INFO] Submit button clicked successfully")

        except Exception as e:
            raise Exception(f"[ERROR] Failed to scroll and click Submit button: {str(e)}")

        time.sleep(2)
        return formatted_dob

        
    def verify_updated_date_of_birth(self):
        time.sleep(5)
        # get actual DOB from UI
        dob_element = self.driver.find_element(*locators['DATE_OF_BIRTH_TEXTFIELD'])

        # Try to get 'value' attribute (common for inputs)
        actual_dob = dob_element.get_attribute("value")

        # If still empty, fallback to text()
        if not actual_dob:
            actual_dob = dob_element.text.strip()

        print(f"[DEBUG] Actual DOB on profile (value or text): {actual_dob}")
        return actual_dob
        
    def is_date_selectable(self, day, month, year):
        try:
            date_locator = (By.XPATH, f"//td[@data-day='{day}' and @data-month='{month}' and @data-year='{year}']")
            print(f"[DEBUG] Trying to locate date element: {date_locator}")
            
            date_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(date_locator)
            )
            print("[DEBUG] Date element found")

            # Check if it's disabled
            is_disabled = "disabled" in date_element.get_attribute("class")
            return not is_disabled
        except TimeoutException:
            print("[DEBUG] Future date element not found - probably disabled.")
            return False

    def verify_future_dob_disabled(self):
        time.sleep(5)
        date_of_birth = self.driver.find_element(*locators["DATE_OF_BIRTH"])
        self.driver.execute_script("arguments[0].scrollIntoView();", date_of_birth)
        self.actions.is_element_displayed(*locators['DATE_OF_BIRTH'])
        print("Date of birth section is displayed")

        # Open the calendar/date picker
        self.actions.click_button(*locators['DATE_OF_BIRTH_TEXTFIELD'])
        self.actions.is_element_displayed(*locators['DATE_PICKER'])
        print("Calendar modal appeared")
        time.sleep(5)

        # Calculate tomorrow's date
        tomorrow = datetime.now() + timedelta(days=1)
        future_day = tomorrow.day
        future_month = tomorrow.month
        future_year = tomorrow.year

        # Check if future date is selectable
        is_selectable = self.actions.is_date_selectable(future_day, future_month, future_year)
        print(f"[DEBUG] Is future date selectable? {is_selectable}")

        # If future date is NOT selectable, close the calendar popup
        if not is_selectable:
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(locators['CLOSE_CALENDAR_POPUP'])
                ).click()
                print("[INFO] Calendar popup closed as future date is not selectable")
            except TimeoutException:
                print("[ERROR] Unable to close the calendar popup")

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
        time.sleep(5)

        # Confirm text shows up
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        self.actions.is_element_displayed(*locators['COLOR_BLIND_FRIENDLY_TEXT'])
        assert self.actions.is_element_displayed(*locators['COLOR_BLIND_FRIENDLY_TEXT']), "Color blind mode ON text not visible"
        print("Color blind mode is ON.")
        time.sleep(5)
        toggle_button = self.driver.find_element(*locators['TOGGLE_BUTTON'])
        ActionChains(self.driver).move_to_element(toggle_button).click().perform()
        time.sleep(5)
        self.actions.is_element_displayed(*locators['COLOR_SCHEME'])
        toggle_button = self.driver.find_element(*locators['TOGGLE_BUTTON_COLOR_SCHEME_PAGE'])
        ActionChains(self.driver).move_to_element(toggle_button).click().perform()
        time.sleep(5)
    
        # Verify toggle is off
        is_off = not self.actions.is_element_displayed(*locators['TOGGLE_BUTTON'])
        assert is_off, "Toggle button is still ON"
        print("Toggle button is OFF")
        time.sleep(5)


    def color_scheme(self):
        time.sleep(2)
        return self.actions.is_element_displayed(*locators['COLOR_SCHEME'])
        
        
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
        try:
            # Wait for the log out button to be present
            log_out_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(locators["LOG_OUT_BUTTON"])
            )

            # Scroll into view (works for Web)
            try:
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", log_out_button)
                print("Scrolled to log out button using JavaScript.")
            except Exception:
                print(" scrollIntoView failed, attempting manual swipe for mobile.")
                # Fallback: swipe for mobile native apps
                self.driver.swipe(500, 1500, 500, 300, 800)

            # Wait until the button is clickable
            log_out_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(locators["LOG_OUT_BUTTON"])
            )

            # Click the button
            log_out_button.click()
            print(" Log out button clicked")

        except Exception as e:
            print(f" Failed to click log out button: {e}")
            raise

