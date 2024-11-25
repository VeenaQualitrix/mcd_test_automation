from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

locators = {
    "PERSONAL_HEADER_DETAILS": (By.XPATH, "//div[contains(text(), 'Personal Details')]"),
    "USER_NAME": (By.XPATH, "//input[@placeholder='Enter your full name here']"),
    "MOBILE_NUMBER": (By.XPATH, "//input[@mds-profile-edit-input-mblno]"),
    "EMAIL_ID": (By.XPATH, "//input[@placeholder='Enter Your Email ID here']"),
    "DATE_OF_BIRTH": (By.XPATH, "//input[@placeholder='Click here to select']"),
    "SUBMIT_BUTTON": (By.XPATH, "//button[contains(text(), 'Save Changes')]")
    }


class ProfilePage(BasePage):

    def verify_profile_page_reached(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['PERSONAL_HEADER_DETAILS'])

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

    def add_profile_details(self):
        self.actions.enter_text(*locators['USER_NAME'], "User01")
        self.actions.enter_text(*locators["EMAIL_ID"], "user01@gmail.com")
        time.sleep(10)
        self.actions.click_button(*locators["SUBMIT_BUTTON"])
