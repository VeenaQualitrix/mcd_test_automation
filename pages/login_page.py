from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

locators = {
    "LOGIN_PAGE_HEADER": (By.XPATH, "//h5[contains(@class, 'page__sub-heading') and contains(text(), 'Welcome to Mcdonalds')]"),
    "LABEL_ENTER_MOBILE_NUMBER": (By.XPATH, "//label[contains(text(), 'Enter your mobile number')]"),
    "MOBILE_NUMBER_INPUT_FIELD": (By.XPATH, "//input[@placeholder='10 Digit Mobile Number']"),
    "BUTTON_VERIFY_MOBILE": (By.XPATH, "//button[contains(text(), 'Verify Mobile')]"),
    "LABEL_ENTER_OTP": (By.XPATH, "//h5[contains(text(), 'Enter OTP')]"),
    "OTP_INPUT_FIELD": (By.XPATH, "(//div[@class='otp-field']/input[@type='tel'])[{}]"),
    "BUTTON_VERIFY_OTP": (By.XPATH, "//button[@mds-verifyotp-btn-verify]"),
    "PERSONAL_HEADER_DETAILS": (By.XPATH, "//div[contains(text(), 'Personal Details')]"),
    "EMPTY_MOBILE_TEXTFIELD_ERROR": (By.XPATH, "//label[@class='err-label']"),
    "REFERRAL_CODE_LINK": (By.XPATH, "//span[@class = 'page__raferFriendText']"),
    "REFERRAL_CODE_TEXT_FIELD": (By.XPATH, "//input[@placeholder = 'Have a referral code? (Optional)']"),
    "TERMS_AND_CONDITIONS_LINK": (By.XPATH, "//span[contains(text(), 'Terms and Conditions')]"),
    "TERMS_AND_CONDITIONS_HEADER": (By.XPATH, "//h1[contains(text(), 'Terms and conditions')]"),
    "REFERRAL_CODE_ERROR" : (By.XPATH, "//label[contains(text(), 'Please enter minimum 8 characters')]"),
    "Entered_MOBILE_NUMBER_FIELD": (By.XPATH, "//input[@maxlength ='10']"),
    }


class LoginPage(BasePage):

    def verify_login_page_reached(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['LOGIN_PAGE_HEADER'])
  
    def enter_mobile_number(self, mobile_number):
        self.actions.is_element_displayed(*locators['LABEL_ENTER_MOBILE_NUMBER'])
        self.actions.enter_text(*locators["MOBILE_NUMBER_INPUT_FIELD"], mobile_number)
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
   
    def leave_mobile_field_empty(self):
        self.actions.is_element_displayed(*locators['LABEL_ENTER_MOBILE_NUMBER'])
        self.actions.click_button(*locators["MOBILE_NUMBER_INPUT_FIELD"])
        self.actions.click_button(*locators["BUTTON_VERIFY_MOBILE"])
        self.actions.is_element_displayed(*locators['EMPTY_MOBILE_TEXTFIELD_ERROR'])
        time.sleep(5)
        print("Please enter valid Mobile number")

    def mobile_field_empty_error(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['EMPTY_MOBILE_TEXTFIELD_ERROR'])

    def enter_invalid_mobile_number(self, invalid_mobile_number):
        self.actions.is_element_displayed(*locators['LABEL_ENTER_MOBILE_NUMBER'])
        self.actions.enter_text(*locators["MOBILE_NUMBER_INPUT_FIELD"], invalid_mobile_number)
        self.actions.click_button(*locators["BUTTON_VERIFY_MOBILE"])
        self.actions.is_element_displayed(*locators['EMPTY_MOBILE_TEXTFIELD_ERROR'])
        time.sleep(5)
        print("Entered invalid Mobile Number And Clicked On Verify Mobile Button")

    def enter_alphabets_in_mobile_text_field(self, alphabets_in_mobile_number):
        self.actions.is_element_displayed(*locators['LABEL_ENTER_MOBILE_NUMBER'])
        self.actions.enter_text(*locators["MOBILE_NUMBER_INPUT_FIELD"], alphabets_in_mobile_number)
        self.actions.click_button(*locators["BUTTON_VERIFY_MOBILE"])
        self.actions.is_element_displayed(*locators['EMPTY_MOBILE_TEXTFIELD_ERROR'])
        time.sleep(5)
        print("Entered alphabets in mobile number And Clicked On Verify Mobile Button")

    def enter_mobile_number_with_space(self, mobile_number_with_space):
        self.actions.is_element_displayed(*locators['LABEL_ENTER_MOBILE_NUMBER'])
        self.actions.enter_text(*locators["MOBILE_NUMBER_INPUT_FIELD"], mobile_number_with_space)
        self.actions.click_button(*locators["BUTTON_VERIFY_MOBILE"])
        self.actions.is_element_displayed(*locators['EMPTY_MOBILE_TEXTFIELD_ERROR'])
        time.sleep(5)
        print("Entered mobile number with spaces And Clicked On Verify Mobile Button")

    def enter_mobile_number_with_special_char(self, special_characters_in_mobile_field):
        self.actions.is_element_displayed(*locators['LABEL_ENTER_MOBILE_NUMBER'])
        self.actions.enter_text(*locators["MOBILE_NUMBER_INPUT_FIELD"], special_characters_in_mobile_field)
        self.actions.click_button(*locators["BUTTON_VERIFY_MOBILE"])
        self.actions.is_element_displayed(*locators['EMPTY_MOBILE_TEXTFIELD_ERROR'])
        time.sleep(5)
        print("Entered mobile number with special characters And Clicked On Verify Mobile Button")

    def click_referral_code_link(self):
        self.actions.is_element_displayed(*locators['REFERRAL_CODE_LINK'])
        self.actions.click_button(*locators["REFERRAL_CODE_LINK"])
        time.sleep(5)
        print("Click here if you have a referral code text is displayed")

    def verify_referral_text_field_is_displayed(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['REFERRAL_CODE_TEXT_FIELD'])
    
    def enter_referral_code(self, Referral_code):
        self.actions.is_element_displayed(*locators['REFERRAL_CODE_TEXT_FIELD'])
        self.actions.enter_text(*locators["REFERRAL_CODE_TEXT_FIELD"], Referral_code)
        time.sleep(5)
        print("Entered referral code")

    def is_referral_code_accepted(self):
        try:
        # Wait for the error message to disappear or not be present at all
            WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(locators["REFERRAL_CODE_ERROR"])  
        )
            return True
        except TimeoutException:
            print("Referral code error is still visible or failed to disappear.")
            return False
        
    def enter_referral_code_click_verify(self, Referral_code):
        self.actions.is_element_displayed(*locators['REFERRAL_CODE_TEXT_FIELD'])
        self.actions.enter_text(*locators["REFERRAL_CODE_TEXT_FIELD"], Referral_code)
        self.actions.click_button(*locators["MOBILE_NUMBER_INPUT_FIELD"])
        self.actions.click_button(*locators["BUTTON_VERIFY_MOBILE"])
        time.sleep(5)
        print("Entered referral code and click verify")

    def click_verify_mobile_button_without_entering_mobile_number(self):
        self.actions.is_element_displayed(*locators['LABEL_ENTER_MOBILE_NUMBER'])
        self.actions.click_button(*locators["MOBILE_NUMBER_INPUT_FIELD"])
        self.actions.click_button(*locators["BUTTON_VERIFY_MOBILE"])
        self.actions.is_element_displayed(*locators['EMPTY_MOBILE_TEXTFIELD_ERROR'])
        time.sleep(5)
        print("Please enter valid Mobile number")

    def verify_otp_page_is_displayed(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['LABEL_ENTER_OTP'])
    
    def click_terms_and_conditions_link(self):
        self.actions.is_element_displayed(*locators['TERMS_AND_CONDITIONS_LINK'])
        self.actions.click_button(*locators["TERMS_AND_CONDITIONS_LINK"])
        time.sleep(5)
        print("Terms and conditions clicked and redirected to the page")

    def verify_terms_and_conditions_header(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['TERMS_AND_CONDITIONS_HEADER'])
    
    def enter_mobile_number_one_by_one(self, mobile_number_11_digits):
        self.actions.is_element_displayed(*locators["MOBILE_NUMBER_INPUT_FIELD"])
        input_field = self.driver.find_element(*locators["MOBILE_NUMBER_INPUT_FIELD"])
        input_field.clear()
        print("Entering mobile number one digit at a time:")
        for digit in mobile_number_11_digits:
            input_field.send_keys(digit)
            print(f"Typed digit: {digit}")
            time.sleep(0.2)
            if not mobile_number_11_digits:
              raise ValueError("Mobile number test data is missing or empty.")  
   
    def get_entered_mobile_number(self):
        locator = locators["Entered_MOBILE_NUMBER_FIELD"]
        print(f"DEBUG: Waiting for visibility of element: {locator}")
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        print(f"DEBUG: Element visible. Getting value from: {locator}")
        input_field = self.driver.find_element(*locator)
        current_value = input_field.get_attribute("value")
        print(f"DEBUG: Retrieved value: '{current_value}'")
        return current_value


    def copy_mobile_number_to_clipboard(self, mobile_number):
        pyperclip.copy(mobile_number)
        print(f"Copied Mobile Number '{mobile_number}' To Clipboard")

    def paste_mobile_number_using_ctrl_v(self):
        self.actions.is_element_displayed(*locators['LABEL_ENTER_MOBILE_NUMBER'])
        self.actions.click_button(*locators["MOBILE_NUMBER_INPUT_FIELD"])
        # Simulate Ctrl+V to paste clipboard content
        input_field = self.driver.find_element(*locators["Entered_MOBILE_NUMBER_FIELD"])
        input_field.send_keys(Keys.CONTROL, 'v')
        self.actions.click_button(*locators["BUTTON_VERIFY_MOBILE"])
        time.sleep(5)
        print("Pasted Mobile Number Using Ctrl+V And Clicked On Verify Mobile Button")
    
    def get_pasted_mobile_number(self):
        input_field = self.driver.find_element(*locators["MOBILE_NUMBER_INPUT_FIELD"])
        return input_field.get_attribute("value")
    
    def inspect_mobile_field(self):
        time.sleep(5)
        if self.actions.is_element_displayed(*locators['MOBILE_NUMBER_INPUT_FIELD']):
            return self.driver.find_element(*locators['MOBILE_NUMBER_INPUT_FIELD'])
        return None  # or raise an Exception

    def inspect_referral_link(self):
        if self.actions.is_element_displayed(*locators['REFERRAL_CODE_LINK']):
            return self.driver.find_element(*locators['REFERRAL_CODE_LINK'])
        return None

    def inspect_verify_button(self):
        if self.actions.is_element_displayed(*locators['BUTTON_VERIFY_MOBILE']):
            return self.driver.find_element(*locators['BUTTON_VERIFY_MOBILE'])
        return None

    def inspect_footer_link(self):
        if self.actions.is_element_displayed(*locators['TERMS_AND_CONDITIONS_LINK']):
            return self.driver.find_element(*locators['TERMS_AND_CONDITIONS_LINK'])
        return None

    
    
