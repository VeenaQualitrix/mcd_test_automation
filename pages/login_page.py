from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

locators = {
    "LOGIN_PAGE_HEADER": (By.XPATH, "//h5[contains(@class, 'page__sub-heading') and contains(text(), 'Welcome to Mcdonalds')]"),
    "LABEL_ENTER_MOBILE_NUMBER": (By.XPATH, "//label[contains(text(), 'Enter your mobile number')]"),
    "MOBILE_NUMBER_INUPUT_FIELD": (By.XPATH, "//input[@placeholder='10 Digit Mobile Number']"),
    "BUTTON_VERIFY_MOBILE": (By.XPATH, "//button[contains(text(), 'Verify Mobile')]"),
    "LABEL_ENTER_OTP": (By.XPATH, "//h5[contains(text(), 'Enter OTP')]"),
    "OTP_INPUT_FIELD": (By.XPATH, "(//div[@class='otp-field']/input[@type='tel'])[{}]"),
    "BUTTON_VERIFY_OTP": (By.XPATH, "//button[@mds-verifyotp-btn-verify]"),
    "PERSONAL_HEADER_DETAILS": (By.XPATH, "//div[contains(text(), 'Personal Details')]")
    }


class LoginPage(BasePage):

    def verify_login_page_reached(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['LOGIN_PAGE_HEADER'])
  
    def enter_mobile_number(self, mobile_number):
        self.actions.is_element_displayed(*locators['LABEL_ENTER_MOBILE_NUMBER'])
        self.actions.enter_text(*locators["MOBILE_NUMBER_INUPUT_FIELD"], mobile_number)
        self.actions.click_button(*locators["BUTTON_VERIFY_MOBILE"])
        time.sleep(5)
        print("Entered Mobile Number And Clicked On Verify Mobile Button")

    def enter_otp(self, otp):
        self.actions.is_element_displayed(*locators['LABEL_ENTER_OTP'])
        by, value = locators["OTP_INPUT_FIELD"]
        for index, digit in enumerate(otp):
            format_value = value.format(index+1)
            self.actions.enter_text(by, format_value, digit)
        self.actions.click_button(*locators["BUTTON_VERIFY_OTP"])
        time.sleep(5)
        print("Entered OTP And Clicked On Verify Button")
