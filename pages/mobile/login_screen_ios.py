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
    "BOTTOM_TAB_MY_MCD_IMAGE": (
        AppiumBy.XPATH,
        '//XCUIElementTypeImage[@name="ic-bottom-tab-mymcd"]'
    ),
    "LOGIN_SIGNUP_TEXT": (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Login/Sign Up"]'
    ),
    "MOBILE_NUMBER_INPUT_FIELD": (
        AppiumBy.XPATH,
        '//XCUIElementTypeTextField[@value="10 Digit Mobile Number"]'
    ),
    "MOBILE_NUMBER_INPUT_FIELDS": (
        AppiumBy.XPATH,
        '//XCUIElementTypeTextField[@value="11 Digit Mobile Number"]'
    ),
    "VERIFY_MOBILE_BUTTON": (
        AppiumBy.ACCESSIBILITY_ID,
        'Verify Mobile'
    ),
    "REFERRAL_CODE_LINK": (AppiumBy.ACCESSIBILITY_ID, 'Click here if you have a referral code.'),
    
    "REFERRAL_CODE_HINT_TEXT": (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Click here if you have a referral code."]'
    ),
    "REFERRAL_CODE_TEXT_FIELD": (
        AppiumBy.XPATH,
        '//XCUIElementTypeTextField[contains(@value,"Have a referral")]' 

    ),

    "BACK_TO_LOGIN_TEXT": (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Back to login page"]'
    ),
    "LABEL_ENTER_OTP": (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Enter OTP"]'),


    "LABEL_ENTER_MOBILE_NUMBER": (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='Please enter mobile number']"),


    "REFERRAL_CODE_ERROR": (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='Please enter minimum 8 characters']"),

    'EMPTY_MOBILE_TEXTFIELD_ERROR': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='Please enter valid mobile number']"),

    'TERMS_AND_CONDITIONS_LINK': (AppiumBy.ACCESSIBILITY_ID, "Terms and Conditions"),

    'TERMS_AND_CONDITIONS_AGE_LABEL': (AppiumBy.XPATH,
    '//XCUIElementTypeApplication[@name="McDelivery"]/XCUIElementTypeWindow[2]/XCUIElementTypeOther/XCUIElementTypeOther'),

    "Entered_MOBILE_NUMBER_FIELD": (By.XPATH, "//XCUIElementTypeTextField[@name='mobileNumber']"),
    'OTP_INPUT_FIELD': (AppiumBy.XPATH,'//XCUIElementTypeTextField'),
    'BUTTON_VERIFY_OTP': ( AppiumBy.ACCESSIBILITY_ID,"Verify")


}

class LoginScreenIos(BasePage):

    def click_bottom_tab_my_mcd(self):
        time.sleep(5)
        self.actions.click_button(*locators["BOTTOM_TAB_MY_MCD_IMAGE"])
        print("Clicked on 'My McD' bottom tab.")

    def verify_bottom_tab_my_mcd_is_displayed(self):
        time.sleep(5)
        is_displayed = self.actions.is_element_displayed(*locators["BOTTOM_TAB_MY_MCD_IMAGE"])
        print("'My McD' bottom tab is displayed." if is_displayed else "'My McD' bottom tab is NOT displayed.")
        return is_displayed

    def verify_login_signup_text(self):
        time.sleep(5)
        is_displayed = self.actions.is_element_displayed(*locators["LOGIN_SIGNUP_TEXT"])
        print("'Login/Sign Up' text is displayed." if is_displayed else "'Login/Sign Up' text is NOT displayed.")
        return is_displayed

    def click_login_signup_button(self):
        time.sleep(5)
        self.actions.click_button(*locators["LOGIN_SIGNUP_TEXT"])
        print("Clicked on 'Login/Sign Up' button.")

    def enter_mobile_number(self, mobile_number):
        self.actions.fluentWaitNew(locators["MOBILE_NUMBER_INPUT_FIELD"])
        self.actions.enter_text(*locators["MOBILE_NUMBER_INPUT_FIELD"], mobile_number)
        print(f"Entered mobile number: {mobile_number}")

      

        # # try:
        # #     # iOS-specific hide keyboard
        # #     self.driver.hide_keyboard()
        # # except Exception as e:
        # #     print(f"[Warning] Failed to hide keyboard: {e}")
        # #     # Try tapping outside or on another element
        # #     self.actions.tap_coordinates(10, 10)  # Safe coordinate on screen

        # time.sleep(2)

    def click_verify_mobile(self):
        time.sleep(5)
        self.actions.click_button(*locators["VERIFY_MOBILE_BUTTON"])
        # print(verify_button)
        # verify_button.click()
        print("Clicked on 'Verify Mobile' button.")

    def click_referral_code_link(self):
        self.actions.is_element_displayed(*locators['REFERRAL_CODE_LINK'])
        self.actions.click_button(*locators["REFERRAL_CODE_LINK"])
        time.sleep(10)
        print("Click here if you have a referral code text is displayed")

    def click_referral_code_hint_text(self):
        time.sleep(5)
        self.actions.click_button(*locators["REFERRAL_CODE_HINT_TEXT"])
        print("Referral code hint is displayed.")

    def enter_referral_code(self, referral_code):
        time.sleep(5)
        self.actions.enter_text(*locators["REFERRAL_CODE_TEXT_FIELD"], referral_code)
        print(f"Entered referral code: {referral_code}")

    def enter_otp(self, otp):
        self.actions.is_element_displayed(*locators['LABEL_ENTER_OTP'])
        by, value = locators["OTP_INPUT_FIELD"]

        for index, digit in enumerate(otp):
            field_locator = (by, value.format(index + 1))
            field = self.driver.find_element(*field_locator)
            field.click()
            field.send_keys(digit)
            time.sleep(0.5)

        # Optional: Tap outside to force blur and trigger UI updates
        self.actions.tap_on_coordinates(100, 100)
        time.sleep(1)

        verify_by, verify_value = locators["BUTTON_VERIFY_OTP"]

        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((verify_by, verify_value))
            )
            print("Verify button is now enabled.")
        except TimeoutException:
            self.driver.save_screenshot("verify_button_timeout.png")
            raise Exception("Verify button not enabled after entering OTP.")

        self.actions.click_button(verify_by, verify_value)
        print("Entered OTP and clicked Verify.")

    def enter_alphabets_in_mobile_text_field(self, text):
        time.sleep(2)
        self.actions.enter_text(*locators["MOBILE_NUMBER_INPUT_FIELD"], text)
        print(f"Entered alphabets '{text}' in the mobile number field.")

    def leave_mobile_field_empty(self):
        self.actions.click_button(*locators["MOBILE_NUMBER_INPUT_FIELD"])
        time.sleep(2)

        try:
            self.driver.hide_keyboard()
            print("Hide keyboard")
        except Exception as e:
            print(f"Keyboard might already be hidden: {e}")

    def verify_mobile_button_is_disabled(self):
            time.sleep(3)
            element = self.driver.find_element(By.ACCESSIBILITY_ID, "Verify Mobile")
            assert not element.is_enabled(), "Verify button should be disabled for empty or invalid input"
            print("Verified: Button is disabled as expected")

    def enter_invalid_mobile_number(self, invalid_mobile_number):
            self.actions.is_element_displayed(*locators['LABEL_ENTER_MOBILE_NUMBER'])
            self.actions.enter_text(*locators["MOBILE_NUMBER_INPUT_FIELD"], invalid_mobile_number)
            print("Entered invalid Mobile Number")

    def copy_mobile_number_to_clipboard(self, mobile_number):
        pyperclip.copy(mobile_number)
        print(f"Copied Mobile Number '{mobile_number}' To Clipboard")


    
    def get_pasted_mobile_number(self):
        input_field = self.driver.find_element(*locators["MOBILE_NUMBER_INPUT_FIELD"])
        return input_field.get_attribute("value")

    

    def enter_alphabets_in_mobile_text_field(self, alphabets_in_mobile_number):
            self.actions.is_element_displayed(*locators['LABEL_ENTER_MOBILE_NUMBER'])
            self.actions.enter_text(*locators["MOBILE_NUMBER_INPUT_FIELD"], alphabets_in_mobile_number)
            print("Entered alphabets in mobile number")

    def enter_mobile_number_with_space(self, mobile_number_with_space):
            self.actions.is_element_displayed(*locators['LABEL_ENTER_MOBILE_NUMBER'])
            self.actions.enter_text(*locators["MOBILE_NUMBER_INPUT_FIELD"], mobile_number_with_space)
            print("Entered mobile number with spaces And Clicked On Verify Mobile Button")

    def enter_mobile_number_with_special_char(self, special_characters_in_mobile_field):
            self.actions.is_element_displayed(*locators['LABEL_ENTER_MOBILE_NUMBER'])
            self.actions.enter_text(*locators["MOBILE_NUMBER_INPUT_FIELD"], special_characters_in_mobile_field)
            print("Entered mobile number with special characters And Clicked On Verify Mobile Button")
    
    def tap_terms_and_conditions_link(self):
        time.sleep(2)
        self.actions.click_button(*locators["TERMS_AND_CONDITIONS_LINK"])
        print("Tapped on Terms and Conditions link")

    def verify_referral_text_field_is_displayed(self):
            time.sleep(5)
            return self.actions.is_element_displayed(*locators['REFERRAL_CODE_TEXT_FIELD'])
        
    def copy_mobile_number_to_clipboard(self, mobile_number):
        self.driver.set_clipboard_text(mobile_number)
        print(f"Set Mobile Number '{mobile_number}' to device clipboard")

    def paste_mobile_number_using_clipboard(self):
        input_field = self.driver.find_element(*locators["MOBILE_NUMBER_INPUT_FIELD"])
        input_field.click()
        time.sleep(1)

        # 🔁 Skip long press / paste tap — directly paste from clipboard
        clipboard_text = self.driver.get_clipboard_text()
        print(f"Clipboard Text Retrieved: {clipboard_text}")

        input_field.send_keys(clipboard_text)
        print("Sent clipboard text to input field using send_keys")
        time.sleep(2)    

    def verify_referral_code_accepted_without_error(self):
            try:
            # Wait for the error message to disappear or not be present at all
                WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located(locators["REFERRAL_CODE_ERROR"])  
            )
                return True
            except TimeoutException:
                print("Referral code error is still visible or failed to disappear.")
                return False
            
    def hide_keyboard_by_tapping_outside(self):
            try:
                self.driver.hide_keyboard()
            except Exception:
                print("Native hide_keyboard failed, falling back to tap.")

            mobile_field = self.driver.find_element(*locators['MOBILE_NUMBER_INPUT_FIELD'])
            rect = mobile_field.rect

            tap_x = rect['x'] + rect['width'] // 2
            tap_y = rect['y'] + rect['height'] + 10  # just below the input

            self.actions.tap_on_coordinates(tap_x, tap_y)
            
    def enter_referral_code_click_verify(self, referral_code):
            if self.actions.is_element_displayed(*locators['REFERRAL_CODE_TEXT_FIELD']):
                self.actions.enter_text(*locators["REFERRAL_CODE_TEXT_FIELD"], referral_code)
                time.sleep(2)
                self.actions.click_button(*locators["MOBILE_NUMBER_INPUT_FIELD"])
                self.click_verify_mobile()
                # ✅ Since we're in the same class, this works
                # self.hide_keyboard_by_tapping_outside()

                print("Entered referral code and clicked verify")
            else:
                print("Referral code field not displayed")

    def mobile_field_empty_error(self):
            time.sleep(5)
            is_displayed = self.actions.is_element_displayed(*locators['EMPTY_MOBILE_TEXTFIELD_ERROR'])
            if is_displayed:
                print("Error displayed: 'Please enter the mobile number'")
            else:
                print("No error message for empty mobile field")
            return is_displayed

    def verify_otp_screen_is_displayed(self):
            time.sleep(5)
            return self.actions.is_element_displayed(*locators['LABEL_ENTER_OTP'])   
    
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

def inspect_referral_link(self):
    time.sleep(2)
    return self.actions.get_element(*locators["REFERRAL_CODE_LINK"])


def inspect_verify_button(self):
    time.sleep(2)
    return self.actions.get_element(*locators["VERIFY_MOBILE_BUTTON"])


def inspect_footer_link(self):
    time.sleep(2)
    return self.actions.get_element(*locators["FOOTER_LINK"])


def inspect_mobile_field(self):
    time.sleep(2)
    return self.actions.get_element(*locators["MOBILE_NUMBER_INPUT_FIELD"])

        
    

def verify_terms_and_conditions_page_displayed(self):
    time.sleep(2)
    assert self.actions.is_element_displayed(*locators["TERMS_AND_CONDITIONS_PAGE_LABEL"]), \
        "Terms and Conditions page is not displayed"
    print("Verified: Terms and Conditions page is displayed")
        
        
