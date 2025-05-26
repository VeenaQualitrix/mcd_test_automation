from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

locators = {
    "PERSONAL_HEADER_DETAILS": (By.XPATH, "//div[contains(text(), 'Personal Details')]"),
    "USER_PROFILE_LOGO": (By.XPATH, "//h2[@class = 'avatar__logo-initial-txt']"),
    "PROFILE_PAGE_LOGO": (By.XPATH, "//img[@class = 'profile-page__logo']"),
    "USER_NAME": (By.XPATH, "//input[@placeholder='Enter your full name here']"),
    "MOBILE_NUMBER": (By.XPATH, "//input[@mds-profile-edit-input-mblno]"),
    "EMAIL_ID": (By.XPATH, "//input[@placeholder='Enter Your Email ID here']"),
    "DATE_OF_BIRTH": (By.XPATH, "//input[@placeholder='Click here to select']"),
    "SUBMIT_BUTTON": (By.XPATH, "//button[contains(text(), 'Save Changes')]"),
    "PROFILE_EDIT_ICON": (By.XPATH, "//img[@class = 'profile-page__link-btn']"),
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
